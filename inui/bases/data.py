from typing import Any, List


class BaseData:
    def __init__(self, *args) -> None:
        self._data: List[Any] = args

    def __str__(self) -> str:
        return "".join(map(self._str, self._data))

    def _str(self, data):
        return str(data)

    def append(self, *args):
        self._data = (*self._data, *args)

    def copy(self):
        return self._data.copy()

    def describe(self, data: list | None = None):
        results = []
        return results

    def _fix_calls(self):
        for i, d in enumerate(self._data):
            try:
                if isinstance(d, type):
                    self._data[i] = d()
            except Exception as _:
                pass

    def select(
        self,
        field: str,
        case_senstive: bool = True,
        number: int | None = None,
        as_list: bool = False,
    ):
        return []

    def filter():
        return []

    def __len__(self):
        return len(self._data)

    def delete(self, data: list[Any] | Any):
        if not isinstance(data, (list, tuple, set)):
            data = (data,)
        for value in data:
            while value in self._data:
                self._data.remove(value)
