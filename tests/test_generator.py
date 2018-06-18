import mock
import unittest

from .changelog_generator.generator import generate_changelog


class TestGenerator(unittest.TestCase):
    @mock.patch("os.path.isfile")
    @mock.patch("changelog_generator.generator.get_commits_since_date")
    @mock.patch("changelog_generator.generator.get_last_commit_date")
    def test_generator(self, mock_get_commit_date, mock_get_commits, mock_is_file):

        mock_get_commit_date.return_value = "2018-06-10T14:01:45.000000+00:00"
        mock_get_commits.return_value = [
            {
                "parent_ids": ["06f7e730ff5edcc5a955d939c1e39ac363ad3e41"],
                "committed_date": "2018-06-10T14:01:44.000+00:00",
                "message": "Test commit message"
            }
        ]

        cli_args = {
            "ip_address": "localhost",
            "api_version": "4",
            "project_group": "test-group",
            "project": "test-project",
            "branch_one": "release",
            "branch_two": "master",
            "version": "1",
            "changelog": "N",
        }

        result = generate_changelog(cli_args)
        self.assertEqual(result, "CHANGELOG_generated.md written successfully")
