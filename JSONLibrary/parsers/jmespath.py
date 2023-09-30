from typing import Callable, Optional, Union

from robot.utils.asserts import fail
from jmespath import Options, compile, search
from jmespath.exceptions import ParseError


class JmesPath:
    def parse(self, expression: str):
        try:
            return compile(expression=expression)
        except ParseError as ex:
            fail(
                f"""Parser failed to understand syntax '{expression}'.\nerror message: "
                {ex}\n
                """
            )

    def query(self, expression: str, document: dict, options: Optional[Options] = None) -> Union[dict, list]:
        return search(expression=expression, data=document, options = options)
