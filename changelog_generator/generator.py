import datetime
import os.path

from changelog_generator.log_handlers import logger
from changelog_generator.calls import get_last_commit_date, get_commits_since_date


def generate_changelog(cli_args: dict) -> str:
    # Get the date of the last commit
    last_commit = get_last_commit_date(cli_args)

    # Get any commits since that date
    new_commits = get_commits_since_date(last_commit, cli_args)

    # Get the current date so that we can add it to the CHANGELOG.md document
    date = datetime.datetime.now()
    current_date = date.strftime("%Y-%m-%d")

    # Determine whether a CHANGELOG.md file already exists
    if os.path.isfile("CHANGELOG.md"):
        if cli_args["changelog"] == "Y":
            with open("CHANGELOG.md", "r") as original_changelog:
                original_changelog_data = original_changelog.read()
                with open("CHANGELOG.md", "w") as modified_changelog:
                    modified_changelog.write(
                        f"## v{cli_args['version']} ({current_date})\n"
                    )
                    [
                        modified_changelog.write(
                            f"* {commit['committed_date'][:10]} - {y} \n"
                        )
                        for commit in new_commits
                        for y in commit["message"].split("\n")
                    ]
                    modified_changelog.write(f"\n")
                    modified_changelog.write(original_changelog_data)
                    return "CHANGELOG.md updated successfully" 
        else:
            logger.info("Existing CHANGELOG.md found but not specified")
            logger.info("Writing CHANGELOG_generated.md as a result...")
            with open("CHANGELOG_generated.md", "w") as changelog:
                changelog.write(f"## v{cli_args['version']} ({current_date})\n")
                [
                    changelog.write(f"* {commit['committed_date'][:10]} - {y} \n")
                    for commit in new_commits
                    for y in commit["message"].split("\n")
                ]
            return "CHANGELOG_generated.md written successfully"
    else:
        logger.info(
            "No CHANGELOG.md found and no CHANGELOG.md specified..."
        )
        logger.info("Writing CHANGELOG.md as a result...")
        with open("CHANGELOG.md", "w") as changelog:
            changelog.write(f"## v{cli_args['version']} ({current_date})\n")
            [
                changelog.write(f"* {commit['committed_date'][:10]} - {y} \n")
                for commit in new_commits
                for y in commit["message"].split("\n")
            ]

        return "New CHANGELOG.md file written successfully"
