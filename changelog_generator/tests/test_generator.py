import datetime
import mock
import unittest

from changelog_generator.generator import generate_changelog


class TestGenerator(unittest.TestCase):
    @mock.patch("os.path.isfile")
    @mock.patch("changelog_generator.generator.get_commits_since_date")
    @mock.patch("changelog_generator.generator.get_last_commit_date")
    def test_generate_changelog_existing(self, mock_get_commit_date, mock_get_commits, mock_is_file):
        mock_is_file.return_value = True
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

        with mock.patch("builtins.open", mock.mock_open()) as mock_file:
            result = generate_changelog(cli_args)
            mock_file.assert_called_once_with(mock.ANY, "w")
            mock_file().write.assert_called_with("* 2018-06-10 - Test commit message \n")
            self.assertEqual(result, "CHANGELOG_generated.md written successfully")

    @mock.patch("changelog_generator.generator.datetime")
    @mock.patch("os.path.isfile")
    @mock.patch("changelog_generator.generator.get_commits_since_date")
    @mock.patch("changelog_generator.generator.get_last_commit_date")
    def test_generate_changelog_update(self, mock_get_commit_date, mock_get_commits, mock_is_file, mock_datetime):
        mock_datetime.datetime.now.return_value = datetime.date(2018, 6, 18)
        mock_is_file.return_value = True
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
            "changelog": "Y",
        }

        with mock.patch("builtins.open", mock.mock_open(read_data="Existing data")) as mock_file:
            result = generate_changelog(cli_args)
            mock_file.assert_called_with(mock.ANY, "w")
            mock_file().write.assert_has_calls([
                mock.call("## v1 (2018-06-18)\n"),
                mock.call("* 2018-06-10 - Test commit message \n"),
                mock.call("\n"),
                mock.call("Existing data")
            ])
            self.assertEqual(result, "CHANGELOG.md updated successfully")

    @mock.patch("os.path.isfile")
    @mock.patch("changelog_generator.generator.get_commits_since_date")
    @mock.patch("changelog_generator.generator.get_last_commit_date")
    def test_generate_changelog_new(self, mock_get_commit_date, mock_get_commits, mock_is_file):
        mock_is_file.return_value = False
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

        with mock.patch("builtins.open", mock.mock_open()) as mock_file:
            result = generate_changelog(cli_args)
            mock_file.assert_called_once_with(mock.ANY, "w")
            mock_file().write.assert_called_with("* 2018-06-10 - Test commit message \n")
            self.assertEqual(result, "New CHANGELOG.md file written successfully")
