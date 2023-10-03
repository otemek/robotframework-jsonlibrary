import json
import pytest
from JSONLibrary.parsers.jmespath import JmesPath
from pathlib import Path

TEST_DIR = Path(__file__).parent


def json_file():
    return TEST_DIR.read_text()


@pytest.fixture(scope="module")
def lib_jmespath() -> JmesPath:
    return JmesPath()


@pytest.fixture(scope="module")
def json_sample(json_file) -> dict:
    return json.load(json_file)


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
    assert lib_jmespath.parse(expression)

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