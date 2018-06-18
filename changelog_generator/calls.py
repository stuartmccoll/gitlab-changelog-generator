import datetime
import logging
import requests


logger = logging.getLogger(__name__)


def get_last_commit_date(cli_args: dict) -> str:
    """
    Queries a specified GitLab API and returns the date of the most
    recent commit.
    """
    request_url = f"http://{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/" f"{cli_args['project_group']}%2F{cli_args['project']}/repository/commits/{cli_args['branch_one']}"
    logger.info(f"Requesting last commit date with URL: {request_url}")
    response = requests.get(request_url)

    logger.debug(response.status_code)
    logger.debug(response.json())

    response_json = response.json()

    commit_date = datetime.datetime.strptime(
        response_json["committed_date"][:-6], "%Y-%m-%dT%H:%M:%S.%f"
    ) + datetime.timedelta(seconds=1)

    return datetime.datetime.strftime(
        commit_date, f"%Y-%m-%dT%H:%M:%S.%f{response_json['committed_date'][-6:]}"
    )


def get_commits_since_date(date: str, cli_args: dict) -> list:
    """
    Queries a specified GitLab API and returns a JSON response containing
    all commits since a given date.
    """

    request_url = f"http://{cli_args['ip_address']}/api/v{cli_args['api_version']}/projects/{cli_args['project_group']}%2F{cli_args['project']}/repository/commits/?ref_name={cli_args['branch_two']}&since={date}"
    logger.info(
        f"Requesting commits on branch '{cli_args['branch_two']}' in repository '{cli_args['project']}' since date '{date}' with URL: {request_url}"
    )
    response = requests.get(request_url)

    logger.debug(response.status_code)
    logger.debug(response.json())

    response_json = response.json()
    clean_response = [
        item for item in response_json if len(list(item["parent_ids"])) == 1
    ]

    return sorted(
        clean_response,
        key=lambda x: datetime.datetime.strptime(
            x["committed_date"][:-6], "%Y-%m-%dT%H:%M:%S.%f"
        ),
    )
