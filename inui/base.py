from __future__ import annotations

from typing import Any, Dict, List, NamedTuple, Tuple, Type, Union


class Attributes:
    def __init__(self, **kwargs: Any) -> None:
        self.attrs: Dict[str, Any] = {key: value for key, value in kwargs.items()}

    def __getattribute__(self, __name: str) -> Any:
        if __name == "attrs":
            return super().__getattribute__("attrs")
        return self.attrs.get(__name, None)

    def __str__(self) -> str:
        return " ".join(
            f'{name}="{value}"'
            for name, value in self.attrs.items()
            if value is not None
        )

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

    def copy(self) -> Attributes:
        return Attributes(**self.attrs)

    def clear(self) -> None:
        self.attrs.clear()

    def pop(self, index: str, default: Any = None) -> Any:
        return self.attrs.pop(index, default)

    def popitem(self) -> Tuple[str, Any]:
        return self.attrs.popitem()


class _Data:
    def __init__(self, *args) -> None:
        self._data: List[Any] = args

    def __str__(self) -> str:
        return "".join(map(str, self._data))


class Meta(NamedTuple):
    start_tag: str = None
    end_tag: str = None


class Base:
    Meta: Type[Meta] = Meta()

    def __init__(self, *data: Any, **attributes: Any) -> None:
        self.data = data
        self.attributes = attributes

    @property
    def data(self) -> list:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = _Data(*value)

    @property
    def start_tag(self) -> str:
        return (
            self.Meta.start_tag
            if self.Meta.start_tag
            else self.__class__.__name__.lower()
        )

    @start_tag.setter
    def start_tag(self, value: str) -> None:
        self.Meta.start_tag = value

    @property
    def end_tag(self) -> str:
        return (
            self.Meta.end_tag if self.Meta.end_tag else self.__class__.__name__.lower()
        )

    @end_tag.setter
    def end_tag(self, value: str) -> None:
        self.Meta.end_tag = value

    @property
    def attributes(self) -> Attributes:
        return self._attributes

    @attributes.setter
    def attributes(self, value: Union[Attributes, Dict[str, Any]]) -> None:
        if not isinstance(value, (Attributes, dict)):
            raise TypeError("attributes must be an instance of Attributes or dict")
        self._attributes = (
            Attributes(**value) if isinstance(value, dict) else value.copy()
        )

    def render(self, prettify: bool = False) -> str:
        return f"<{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}>{str(self.data)}</{self.end_tag}>"

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()


class BaseElement(Base):
    ...


class BaseVoidElement(BaseElement):
    def render(self, prettify: bool = False):
        return f"""<{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}>"""


class BaseSvgElement(Base):
    ...
