import json
import pytest
from JSONLibrary.parsers.definitions import JsonQuery
from JSONLibrary.parsers.jmespath import JmesPath
from pathlib import Path
from jmespath.parser import ParsedResult

TEST_FILE = Path(__file__).parent / ".." / "json" / "example.json"

# @pytest.fixture(scope="module")
# def json_file():
#     return TEST_DIR.read_text()


@pytest.fixture(scope="module")
def lib_jmespath() -> JsonQuery:
    return JmesPath()


@pytest.fixture(scope="module")
def json_sample() -> dict:
    with open(TEST_FILE, "r") as fl:
        return json.load(fl)


def test_can_create_Jmespath_implementation(lib_jmespath) -> None:
    assert type(lib_jmespath) is JmesPath


@pytest.mark.parametrize(
    ["expression"],
    [
        ["firstName"],
        ["phoneNumbers[?@.type=='car'].number"],
        ["nonexist[]"]
    ],
)
def test_can_parse_jmespath_syntax_correctly(lib_jmespath, expression):
    parsed_expression = lib_jmespath.parse(expression)
    assert type(parsed_expression) == ParsedResult


@pytest.mark.parametrize(
    ["expression"],
    [
        ["$.firstName"],
        ["phoneNumbers[*].*]"],
        ["nonexist[$]"]
    ],
)
def test_raise_error_on_wrong_synstax_expression(lib_jmespath, expression):
    with pytest.raises(AssertionError) as ex:
        lib_jmespath.parse(expression)
    assert ex.match(f"Parser failed to understand syntax")


@pytest.mark.parametrize(
    ["expression", "expected"],
    [
        ["firstName", "John"]
    ]
)
def test_can_query_expected_data(lib_jmespath: JsonQuery, json_sample: dict, expression, expected):
    actual = lib_jmespath.query(expression=expression, document=json_sample)
    assert actual == expected