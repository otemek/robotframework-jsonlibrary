from typing import Optional, Union

# from robot.utils.asserts import fail
from jmespath import Options, compile, search
from jmespath.exceptions import ParseError
from jmespath.parser import ParsedResult

from JSONLibrary.parsers.definitions import JsonQuery


class JmesPath(JsonQuery):
    def parse(self, expression: str) -> ParsedResult:
        try:
            return compile(expression=expression)
        except ParseError as ex:
            raise AssertionError(
                f"""Parser failed to understand syntax '{expression}'.\nerror message: "
                {ex}\n
                """
            )

    def query(self, expression: str, document: dict, options: Optional[Options] = None) -> Union[dict, list]:
        return search(expression=expression, data=document, options = options)
