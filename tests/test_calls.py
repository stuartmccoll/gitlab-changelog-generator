import mock
import unittest

from .changelog_generator.calls import (
    get_last_commit_date,
    get_commits_since_date,
)


class TestCalls(unittest.TestCase):
    @mock.patch("changelog_generator.calls.requests.get")
    def test_get_last_commit_date(self, mock_get):
        mock_get.return_value.json.return_value = {
            "committed_date": "2018-06-10T14:01:44.000+00:00"
        }

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

        commit_date = get_last_commit_date(cli_args)
        self.assertEqual(commit_date, "2018-06-10T14:01:45.000000+00:00")

    @mock.patch("changelog_generator.calls.requests.get")
    def test_commits_since_date(self, mock_get):
        mock_get.return_value.json.return_value = [
            {
                "parent_ids": ["06f7e730ff5edcc5a955d939c1e39ac363ad3e41"],
                "committed_date": "2018-06-10T14:01:44.000+00:00",
            },
            {
                "parent_ids": ["06f7e730ff5edcc5a955d939c1e39ac363ad3e41"],
                "committed_date": "2018-06-10T14:01:44.000+00:00",
            },
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

        commits = get_commits_since_date("2018-06-10T14:01:45.000000+00:00", cli_args)
        [
            self.assertEqual(
                commit,
                {
                    "parent_ids": ["06f7e730ff5edcc5a955d939c1e39ac363ad3e41"],
                    "committed_date": "2018-06-10T14:01:44.000+00:00",
                },
            )
            for commit in commits
        ]
