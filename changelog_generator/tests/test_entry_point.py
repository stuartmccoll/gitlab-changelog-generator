import sys
import unittest

from changelog_generator.entry_point import process_arguments


class TestGenerator(unittest.TestCase):
    def test_process_arguments(self):
        sys.argv = [
            "script",
            "--ip",
            "localhost",
            "--group",
            "test-group",
            "--project",
            "test-project",
            "--branches",
            "release",
            "master",
            "--version",
            "1.2.3",
            "--token",
            "test-token",
        ]
        expected_result = {
            "ip_address": "localhost",
            "api_version": "4",
            "project_group": "test-group",
            "project": "test-project",
            "branch_one": "release",
            "branch_two": "master",
            "version": "1.2.3",
            "changelog": "N",
            "token": "test-token",
            "ssl": True,
        }

        result = process_arguments()
        self.assertEqual(result, expected_result)
