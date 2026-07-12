import hashlib
import importlib.util
import json
import os
import shutil
import sqlite3
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "ielts-buddy"
UPDATER_PATH = SOURCE / "scripts" / "update_skill.py"
SPEC = importlib.util.spec_from_file_location("ielts_buddy_updater", UPDATER_PATH)
UPDATER = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(UPDATER)


class SkillUpdaterTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.target = self.root / "agent-skills" / "ielts-buddy"
        self.state = self.root / "ielts-home" / "skill-install.json"
        self.learning_db = self.root / "ielts-home" / "learning.db"
        self.environment = patch.dict(os.environ, {"IELTS_BUDDY_HOME": str(self.root / "ielts-home")})
        self.environment.start()

    def tearDown(self):
        self.environment.stop()
        self.temp.cleanup()

    def test_install_records_version_and_keeps_data_outside_skill(self):
        self.learning_db.parent.mkdir(parents=True)
        with sqlite3.connect(self.learning_db) as connection:
            connection.execute("CREATE TABLE sentinel (value TEXT NOT NULL)")
            connection.execute("INSERT INTO sentinel VALUES ('existing-learning-data')")
        result = UPDATER.install_from_directory(SOURCE, self.target, self.state)
        self.assertEqual(result["version"], "0.2.0")
        self.assertTrue((self.target / "scripts" / "update_skill.py").is_file())
        with sqlite3.connect(self.learning_db) as connection:
            value = connection.execute("SELECT value FROM sentinel").fetchone()[0]
        self.assertEqual(value, "existing-learning-data")
        self.assertEqual(json.loads(self.state.read_text())["installPath"], str(self.target.resolve()))

    def test_cli_install_and_status(self):
        environment = {**os.environ, "IELTS_BUDDY_HOME": str(self.root / "ielts-home")}
        install = subprocess.run(
            [
                "python3", str(UPDATER_PATH), "install",
                "--source", str(SOURCE), "--target", str(self.target), "--state", str(self.state),
            ],
            check=True,
            capture_output=True,
            text=True,
            env=environment,
        )
        self.assertEqual(json.loads(install.stdout)["version"], "0.2.0")
        status = subprocess.run(
            [
                "python3", str(self.target / "scripts" / "update_skill.py"), "status",
                "--target", str(self.target), "--state", str(self.state),
            ],
            check=True,
            capture_output=True,
            text=True,
            env=environment,
        )
        self.assertEqual(json.loads(status.stdout)["version"], "0.2.0")

    def test_update_replaces_skill_after_package_validation(self):
        UPDATER.install_from_directory(SOURCE, self.target, self.state)
        archive, checksum = self.make_release("0.3.0", marker="release-0.3.0")
        result = UPDATER.apply_update(
            self.target,
            self.state,
            self.service_manifest("0.3.0", archive, checksum),
            allow_file_url=True,
        )
        self.assertTrue(result["updated"])
        self.assertEqual(json.loads((self.target / "manifest.json").read_text())["version"], "0.3.0")
        self.assertIn("release-0.3.0", (self.target / "SKILL.md").read_text())

    def test_failed_post_install_restores_previous_skill(self):
        UPDATER.install_from_directory(SOURCE, self.target, self.state)
        archive, checksum = self.make_release("0.3.0", broken_learning_store=True)
        with self.assertRaises(RuntimeError):
            UPDATER.apply_update(
                self.target,
                self.state,
                self.service_manifest("0.3.0", archive, checksum),
                allow_file_url=True,
            )
        self.assertEqual(json.loads((self.target / "manifest.json").read_text())["version"], "0.2.0")
        self.assertEqual(json.loads(self.state.read_text())["version"], "0.2.0")

    def test_update_contract_marks_unsupported_install(self):
        UPDATER.install_from_directory(SOURCE, self.target, self.state)
        result = UPDATER.evaluate_update(
            self.target,
            {
                "update": {
                    "channel": "stable",
                    "latestVersion": "0.4.0",
                    "minimumSupportedVersion": "0.3.0",
                    "eventSchemaVersion": 1,
                    "package": None,
                }
            },
        )
        self.assertTrue(result["updateAvailable"])
        self.assertFalse(result["supported"])
        self.assertFalse(result["packageReady"])

    def test_check_uses_24_hour_cache(self):
        UPDATER.install_from_directory(SOURCE, self.target, self.state)
        remote = {
            "update": {
                "channel": "stable",
                "latestVersion": "0.2.0",
                "minimumSupportedVersion": "0.2.0",
                "eventSchemaVersion": 1,
                "package": None,
            }
        }
        with patch.object(UPDATER, "fetch_service_manifest", return_value=remote) as fetch:
            first = UPDATER.check_for_update(self.target, self.state, "https://example.test", force=True)
            second = UPDATER.check_for_update(self.target, self.state, "https://example.test")
        self.assertFalse(first["cached"])
        self.assertTrue(second["cached"])
        self.assertEqual(fetch.call_count, 1)

    def test_checksum_failure_does_not_replace_skill(self):
        UPDATER.install_from_directory(SOURCE, self.target, self.state)
        archive, _ = self.make_release("0.3.0")
        with self.assertRaises(ValueError):
            UPDATER.apply_update(
                self.target,
                self.state,
                self.service_manifest("0.3.0", archive, "0" * 64),
                allow_file_url=True,
            )
        self.assertEqual(json.loads((self.target / "manifest.json").read_text())["version"], "0.2.0")

    def make_release(self, version, marker=None, broken_learning_store=False):
        release_root = self.root / f"release-{version}"
        skill = release_root / "ielts-buddy"
        shutil.copytree(SOURCE, skill)
        manifest_path = skill / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["version"] = version
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        if marker:
            with (skill / "SKILL.md").open("a") as handle:
                handle.write(f"\n<!-- {marker} -->\n")
        if broken_learning_store:
            (skill / "scripts" / "learning_store.py").write_text("raise SystemExit(2)\n")
        archive = self.root / f"ielts-buddy-skill-v{version}.tar.gz"
        with tarfile.open(archive, "w:gz") as package:
            package.add(skill, arcname="ielts-buddy")
        return archive, hashlib.sha256(archive.read_bytes()).hexdigest()

    @staticmethod
    def service_manifest(version, archive, checksum):
        return {
            "update": {
                "channel": "stable",
                "latestVersion": version,
                "minimumSupportedVersion": "0.2.0",
                "eventSchemaVersion": 1,
                "package": {"url": archive.as_uri(), "sha256": checksum},
            }
        }


if __name__ == "__main__":
    unittest.main()
