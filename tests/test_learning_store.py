import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ielts-buddy" / "scripts" / "learning_store.py"


class LearningStoreTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = Path(self.temp.name) / "learning.db"

    def tearDown(self):
        self.temp.cleanup()

    def run_cli(self, *arguments):
        result = subprocess.run(
            ["python3", str(SCRIPT), "--db", str(self.db), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout)

    def test_attempt_mastery_review_and_outbox(self):
        self.run_cli("init")
        failed = self.run_cli(
            "record-attempt",
            "--subject", "reading",
            "--object-type", "question",
            "--object-id", "q-1",
            "--skill", "reading.paraphrase",
            "--correct", "false",
        )
        recommendation = self.run_cli("next", "--subject", "reading")
        self.assertEqual(recommendation["activityType"], "review")
        self.assertEqual(recommendation["review"]["objectId"], "q-1")

        self.run_cli(
            "record-attempt",
            "--subject", "reading",
            "--object-type", "question",
            "--object-id", "q-1",
            "--skill", "reading.paraphrase",
            "--correct", "true",
        )
        state = self.run_cli("snapshot", "--subject", "reading")
        self.assertEqual(state["eventCount"], 2)
        self.assertEqual(state["mastery"][0]["mastery"], 0.5128)
        self.assertEqual(state["upcomingReviews"][0]["intervalDays"], 1)

        outbox = self.run_cli("outbox")
        self.assertEqual(len(outbox["events"]), 2)
        acknowledged = self.run_cli("ack", "--event-id", failed["event"]["eventId"])
        self.assertEqual(acknowledged["acknowledged"], 1)
        self.assertEqual(len(self.run_cli("outbox")["events"]), 1)

    def test_remote_import_is_idempotent(self):
        self.run_cli("init")
        event = {
            "cursor": 9,
            "eventId": "7b1da35e-b89f-4f69-a010-4716dce3ecb6",
            "deviceId": "web-agent",
            "eventType": "practice.attempted",
            "subjectCode": "listening",
            "objectType": "question",
            "objectId": "q-remote",
            "skillCodes": ["listening.detail"],
            "payload": {"correct": True},
            "schemaVersion": 1,
            "occurredAt": "2026-07-12T10:00:00Z",
        }
        payload = Path(self.temp.name) / "events.json"
        payload.write_text(json.dumps({"data": {"events": [event], "nextCursor": 9}}))
        first = self.run_cli("import", "--input", str(payload))
        second = self.run_cli("import", "--input", str(payload))
        self.assertEqual(first["imported"], 1)
        self.assertEqual(second["duplicates"], 1)
        state = self.run_cli("snapshot")
        self.assertEqual(state["cloudCursor"], 9)
        self.assertEqual(state["eventCount"], 1)

    def test_cloud_cursor_order_wins_over_client_timestamps(self):
        self.run_cli("init")
        events = [
            {
                "cursor": 4,
                "eventId": "d6e78f54-5910-44a1-a7cd-abba7c808f4c",
                "deviceId": "agent-a",
                "eventType": "practice.attempted",
                "objectType": "question",
                "objectId": "q-1",
                "skillCodes": ["reading.detail"],
                "payload": {"correct": False},
                "schemaVersion": 1,
                "occurredAt": "2026-07-12T12:00:00Z",
            },
            {
                "cursor": 5,
                "eventId": "7af19fd1-3b82-454d-a262-f6df89a02d08",
                "deviceId": "agent-b",
                "eventType": "practice.attempted",
                "objectType": "question",
                "objectId": "q-1",
                "skillCodes": ["reading.detail"],
                "payload": {"correct": True},
                "schemaVersion": 1,
                "occurredAt": "2026-07-12T10:00:00Z",
            },
        ]
        payload = Path(self.temp.name) / "ordered-events.json"
        payload.write_text(json.dumps({"data": {"events": events, "nextCursor": 5}}))
        self.run_cli("import", "--input", str(payload))
        state = self.run_cli("snapshot")
        self.assertEqual(state["mastery"][0]["evidenceCount"], 2)


if __name__ == "__main__":
    unittest.main()
