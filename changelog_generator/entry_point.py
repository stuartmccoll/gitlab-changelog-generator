from argparse import ArgumentParser

from changelog_generator.generator import generate_changelog


def process_arguments() -> dict:
    parser = ArgumentParser(prog="changegen")
    parser.add_argument(
        "-i",
        "--ip",
        dest="ip",
        help="specify IP address of GitLab repository",
        required=True,
    )
    parser.add_argument(
        "-a",
        "--api",
        dest="api",
        help="specify GitLab API version",
        choices=["1", "2", "3", "4"],
        default="4",
    )
    parser.add_argument(
        "-g", "--group", dest="group", help="specify GitLab group", required=True
    )
    parser.add_argument(
        "-p", "--project", dest="project", help="specify GitLab project", required=True
    )
    parser.add_argument(
        "-b",
        "--branches",
        nargs=2,
        dest="branches",
        help="specify GitLab branches to compare",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--changelog",
        dest="changelog",
        help="specify whether an existing CHANGELOG.md exists",
        choices=["Y", "N"],
        default="N",
    )
    parser.add_argument(
        "-v", "--version", dest="version", help="specify version number", required=True
    )

    args = parser.parse_args()

    return {
        "ip_address": args.ip,
        "api_version": args.api,
        "project_group": args.group,
        "project": args.project,
        "branch_one": args.branches[0],
        "branch_two": args.branches[1],
        "version": args.version,
        "changelog": args.changelog,
    }


def main():
    generate_changelog(process_arguments())


if __name__ == "__main__":
    main()
