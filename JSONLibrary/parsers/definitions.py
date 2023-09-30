from typing import Protocol, Union


class JsonQuery(Protocol):
    def query(self, expression: str, document: dict) -> Union[dict, list]:
        ...