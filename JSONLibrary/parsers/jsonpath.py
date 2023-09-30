from jsonpath_ng import Index, Fields
from jsonpath_ng.ext import parse as parse_ng
from jsonpath_ng.exceptions import JsonPathParserError
from robot.utils.asserts import fail


class JsonPathNg:
    ...


class JsonPathNgExt:
    def parse(self, expression: str):
        try:
            return parse_ng(expression)
        except JsonPathParserError as ex:
            fail(
                "Parser failed to understand syntax '{}'. error message: "
                "\n{}\n\nYou may raise an issue on https://github.com/h2non/jsonpath-ng".format(
                    expression, ex
                )
            )
