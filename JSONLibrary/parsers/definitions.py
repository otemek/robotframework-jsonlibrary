from typing import Any, Protocol


class JsonQuery(Protocol):
    def query(self, expression: str, document: dict) -> Any:
        ...
