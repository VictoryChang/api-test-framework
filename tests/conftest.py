import json

import pytest

from clients.reqres_client import ReqResClient


def pytest_html_report_title(report):
    report.title = "API"


def load_schema(path: str) -> dict:
    with open(path) as reader:
        return json.loads(reader.read())


@pytest.fixture(scope="session")
def client():
    return ReqResClient()
