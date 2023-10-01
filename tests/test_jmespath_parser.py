import pytest
import json
from pathlib import Path
from JSONLibrary.jsonlibrary import JSONLibrary

from JSONLibrary.parsers.jmespath import JmesPath


json_library = JSONLibrary("jmespath")
test_json_file = Path(__file__).parent / "json" / "example.json"


@pytest.fixture
def json_file():
    return json.load(test_json_file.open())


def test_can_read_json_file(json_file):
    assert  json_library.load_json_from_file(test_json_file) == json_file


def test_add_object_to_json(json_file) -> None:
    ...
