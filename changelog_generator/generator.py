import datetime
import dateutil.parser
import os.path
import re

from changelog_generator.calls import (
    get_closed_issues_for_project,
    get_commits_since_date,
    get_last_commit_date,
    get_last_tagged_release_date,
)
from changelog_generator.log_handlers import logger

include_projs = ["zpm"]
type_map = {
    "fix": "Fixed",
    "feat": "Added",
    "chg": "Changes",
    "chore": "Additions",
    "test": "Tests",
    "": "Others",
}

type_order = ["feat", "chg", "fix", "chore", "test", "", ]


def generate_changelog(cli_args: dict) -> str:
    # Get the date of the last commit
    last_commit = get_last_commit_date(cli_args)

    closed_issues_since_last_tag = get_closed_issues_since_last_tag(cli_args)

    # Get any commits since that date
    new_commits = get_commits_since_date(last_commit, cli_args)

    # Get the current date so that we can add it to the CHANGELOG.md document
    date = datetime.datetime.now()
    current_date = date.strftime("%Y-%m-%d")

    allowed_projs = include_projs
    allowed_projs.append(cli_args["sub_project"])
    logger.debug("allow_projs")
    logger.debug(allowed_projs)

    commits_type_dict = {
        type: [] for type in type_map
    }
    commits_type_dict[""] = []
    for commit in new_commits:
        lines = commit["message"].split("\n")
        first_line = lines[0]
        match_obj = re.match(r'^(.+)\((.+)\):', first_line)
        change_type = match_obj.group(1)
        proj = match_obj.group(2)
        if proj not in allowed_projs:
            continue
        if change_type in type_map:
            commits_type_dict[change_type].append(commit)
        else:
            commits_type_dict[""].append(commit)

    # Determine whether a CHANGELOG.md file already exists
    file_path = f"{cli_args['sub_project']}/CHANGELOG.md"
    if not os.path.isfile(file_path):
        open(file_path, 'a').close()
    with open(file_path, "r") as original_changelog:
        original_changelog_data = original_changelog.read()
        with open(file_path, "w") as modified_changelog:
            modified_changelog.write(f"## v{cli_args['version']} ({current_date})\n")
            for type in type_order:
                commits = commits_type_dict[type]
                if not commits:
                    continue
                modified_changelog.write(
                    f"\n### {type_map[type]} \n"
                )
                for commit in commits:
                    modified_changelog.write("\n")
                    logger.debug("commit ")
                    logger.debug(commit)
                    lines = commit["message"].split("\n")
                    modified_changelog.write(
                        f"  * {commit['committed_date'][:10]} - {lines[0]} \n"
                    )
                    modified_changelog.write("\n".join("    " + line for line in lines[1:] if line))
                    modified_changelog.write("\n")

            if closed_issues_since_last_tag:
                modified_changelog.write(f"\n### Closed Issues\n")
                [
                    modified_changelog.write(f"* {closed_issue['title']}")
                    for closed_issue in closed_issues_since_last_tag
                ]
            modified_changelog.write(f"\n")
            modified_changelog.write(original_changelog_data)
            return f"{file_path} updated successfully"


def get_closed_issues_since_last_tag(cli_args: dict) -> list:
    last_tagged_release_date = get_last_tagged_release_date(cli_args)

    closed_issues = get_closed_issues_for_project(cli_args)

    closed_issues_since_tag = []
    for issue in closed_issues:
        logger.info(issue)
        if dateutil.parser.parse(issue["closed_at"]) > dateutil.parser.parse(
                last_tagged_release_date
        ):
            closed_issues_since_tag.append(
                {"closed_at": issue["closed_at"], "title": issue["title"]}
            )

    return closed_issues_since_tag
