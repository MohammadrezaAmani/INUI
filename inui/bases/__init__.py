from typing import Any, Dict, List, Tuple


class Attributes:
    def __init__(self, **kwargs: Any) -> None:
        self.attrs: Dict[str, Any] = kwargs

    def describe(self):
        return []

    def __str__(self) -> str:
        return str(self.attrs)

    def fix_values(self, value: str | list = ""):
        if isinstance(value, str):
            return value

    def __getitem__(self, index: str) -> Any:
        return self.attrs.get(index, None)

    def __setitem__(self, index: str, value: Any) -> None:
        self.attrs[index] = value

    def __delitem__(self, index: str) -> None:
        del self.attrs[index]

    def __iter__(self) -> Any:
        return iter(self.attrs)

    def __len__(self) -> int:
        return len(self.attrs)

    def keys(self) -> List[str]:
        return list(self.attrs.keys())

    def values(self) -> List[Any]:
        return list(self.attrs.values())

    def items(self) -> List[Tuple[str, Any]]:
        return list(self.attrs.items())

    def get(self, index: str, default: Any = None) -> Any:
        return self.attrs.get(index, default)

    def update(self, **kwargs: Any) -> None:
        self.attrs.update(kwargs)

    def clear(self) -> None:
        self.attrs.clear()

    def pop(self, index: str, default: Any = None) -> Any:
        return self.attrs.pop(index, default)

    def popitem(self) -> Tuple[str, Any]:
        return self.attrs.popitem()

    def append(self, key: str = "class", *values):
        if key not in self.attrs.keys():
            self.attrs[key] = values
        else:
            if isinstance(self.attrs[key], (list, tuple, set)):
                self.attrs[key] = (*self.attrs[key], *values)
            else:
                self.attrs[key] = (self.attrs[key], *values)

    def _str(self, data, seperator=" ", fill=""):
        if isinstance(data, (set, tuple, list)):
            result = seperator.join([self._str(i) for i in data])
            return f"{fill}{result}{fill}"

        if isinstance(data, dict):
            result = ""
            for key, value in data.items():
                result += f"{self._str(key)}: {self._str(value)};"
            return f"{fill}{result}{fill}"
        return str(data)

    def copy(self):
        return self.attrs.copy()

    def select(
        self,
        field: str,
        case_senstive: bool = True,
        number: int | None = None,
        as_list: bool = False,
    ):
        return ...
