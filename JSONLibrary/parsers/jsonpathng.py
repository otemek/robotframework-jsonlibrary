from typing import Union
from jsonpath_ng import Index, Fields
from jsonpath_ng.ext import parse
from jsonpath_ng.exceptions import JsonPathParserError
from robot.utils.asserts import fail

from JSONLibrary.parsers.definitions import JsonQuery


class JsonPathNgExt(JsonQuery):
    def parse(self, expression: str):
        try:
            return parse(path=expression)
        except JsonPathParserError as ex:
            fail(
                "Parser failed to understand syntax '{}'. error message: "
                "\n{}\n\nYou may raise an issue on https://github.com/h2non/jsonpath-ng".format(
                    expression, ex
                )
            )


    def query(self, expression: str, document) -> list:
        return self.parse(expression=expression).find(document)  # type: ignore

