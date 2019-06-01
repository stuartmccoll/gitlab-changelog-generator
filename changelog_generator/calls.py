import datetime
import logging
import requests
import sys

from dateutil import parser


logger = logging.getLogger(__name__)


def get_last_commit_date(cli_args: dict) -> str:
    """
    Queries a specified GitLab API and returns the date of the most
    recent commit.
    """
    request_url = f"{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/" f"{cli_args['project_group']}%2F{cli_args['project']}/repository/commits/{cli_args['branch_one']}"
    logger.info(f"Requesting last commit date with URL: {request_url}")
    try:
        response = requests.get(
            request_url,
            headers={
                "PRIVATE-TOKEN": cli_args["token"]
                if "token" in cli_args
                else None
            },
        )
        logger.info(response.status_code)
        response.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        logger.error(
            f"{get_last_commit_date.__name__} call to GitLab API failed with HTTPError: {ex}"
        )
        sys.exit(1)
    except requests.exceptions.ConnectionError as ex:
        logger.error(
            f"{get_last_commit_date.__name__} call to GitLab API failed with ConnectionError: {ex}"
        )
        sys.exit(1)

    logger.debug(response.status_code)
    logger.debug(response.json())

    response_json = response.json()

    commit_date = datetime.datetime.strptime(
        response_json["committed_date"][:-6], "%Y-%m-%dT%H:%M:%S.%f"
    ) + datetime.timedelta(seconds=1)

    commit_date = parser.parse(
        response_json["committed_date"]
    ) + datetime.timedelta(microseconds=1)

    return datetime.datetime.strftime(commit_date, "%Y-%m-%dT%H:%M:%S.%f")


def get_closed_issues_for_project(cli_args: dict) -> dict:
    """
    Queries a specified GitLab API and returns a list containing
    the titles and URLs of closed issues since a given date.
    """
    request_url = f"{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/{cli_args['project_group']}%2F{cli_args['project']}/issues?state=closed"
    logger.info(
        f"Requesting tags for project {cli_args['project']} with URL: {request_url}"
    )
    try:
        response = requests.get(
            request_url,
            headers={"PRIVATE-TOKEN": cli_args["token"]}
            if "token" in cli_args
            else None,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with HTTPError: {ex}"
        )
        sys.exit(1)
    except requests.exceptions.ConnectionError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with ConnectionError: {ex}"
        )
        sys.exit(1)

    logger.debug(response.status_code)
    logger.debug(response.json())

    return response.json()


def get_last_tagged_release_date(cli_args: dict) -> str:
    """
    Queries a specified GitLab API and returns a string containing
    the created_at date of the last tagged release.
    """
    request_url = f"{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/{cli_args['project_group']}%2F{cli_args['project']}/repository/tags"
    logger.info(
        f"Requesting tags for project {cli_args['project']} with URL: {request_url}"
    )
    try:
        response = requests.get(
            request_url,
            headers={"PRIVATE-TOKEN": cli_args["token"]}
            if "token" in cli_args
            else None,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with HTTPError: {ex}"
        )
        sys.exit(1)
    except requests.exceptions.ConnectionError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with ConnectionError: {ex}"
        )
        sys.exit(1)

    logger.debug(response.status_code)
    logger.debug(response.json())

    return response.json()[0]["commit"]["created_at"]


def get_commits_since_date(date: str, cli_args: dict) -> list:
    """
    Queries a specified GitLab API and returns a JSON response containing
    all commits since a given date.
    """

    request_url = f"{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/{cli_args['project_group']}%2F{cli_args['project']}/repository/commits/?ref_name={cli_args['branch_two']}&since={date}"
    logger.info(
        f"Requesting commits on branch '{cli_args['branch_two']}' in repository '{cli_args['project']}' since date '{date}' with URL: {request_url}"
    )
    try:
        response = requests.get(
            request_url,
            headers={"PRIVATE-TOKEN": cli_args["token"]}
            if "token" in cli_args
            else None,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with HTTPError: {ex}"
        )
        sys.exit(1)
    except requests.exceptions.ConnectionError as ex:
        logger.error(
            f"{get_commits_since_date.__name__} call to GitLab API failed with ConnectionError: {ex}"
        )
        sys.exit(1)

    logger.debug(response.status_code)
    logger.debug(response.json())

    response_json = response.json()
    clean_response = [
        item for item in response_json if len(list(item["parent_ids"])) == 1
    ]

    return sorted(
        clean_response,
        key=lambda x: datetime.datetime.strftime(
            parser.parse(x["committed_date"]), "%Y-%m-%dT%H:%M:%S.%f"
        ),
    )
