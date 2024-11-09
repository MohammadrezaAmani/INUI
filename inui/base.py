from __future__ import annotations

from typing import Any, Dict, List, NamedTuple, Tuple, Type, Union

from inui.config.replaces import replace


class Attributes:
    def __init__(self, **kwargs: Any) -> None:
        self.attrs: Dict[str, Any] = {key: value for key, value in kwargs.items()}

    # def __getattribute__(self, __name: str) -> Any:
    #     if __name == "attrs":
    #         return super().__getattribute__("attrs")
    #     return self.attrs.get(__name, None)

    def __str__(self) -> str:
        return " ".join(
            f'{replace(name)}="{self._str(value)}"'
            for name, value in self.attrs.items()
            if value is not None
        )

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
        try:
            if isinstance(data, type):
                if isinstance(data(), Base):
                    data = data()
        except Exception as _:
            pass

        if isinstance(data, (set, tuple, list)):
            result = seperator.join([str(i) for i in data])
            return f"{fill}{result}{fill}"
        return str(data)

    def copy(self):
        return self.attrs.copy()


class _Data:
    def __init__(self, *args) -> None:
        self._data: List[Any] = args

    def __str__(self) -> str:
        return "".join(map(self._str, self._data))

    def _str(self, data):
        try:
            if isinstance(data, type):
                if isinstance(data(), Base):
                    data = data()
        except Exception as _:
            pass
        return str(data)

    def append(self, *args):
        self._data = (*self._data, *args)

    def copy(self):
        return self._data.copy()


class Meta(NamedTuple):
    start_tag: str = None
    end_tag: str = None
    start_sign: str = "<"
    end_sign: str = ">"
    close_sign: str = "</"
    void_sign: str = "/>"


empty = Meta("", "", "", "", "", "")


class Base:
    Meta: Type[Meta] = Meta()
    _data = _Data()
    _attributes = Attributes()

    def __init__(
        self, *data: Any, _meta: Type[Meta] | None = None, **attributes: Any
    ) -> None:
        self.data = data
        self.attributes = attributes
        self.Meta = _meta or self.Meta

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
            if self.Meta.start_tag is not None
            else self.__class__.__name__.lower()
        )

    @start_tag.setter
    def start_tag(self, value: str) -> None:
        self.Meta.start_tag = value

    @property
    def end_tag(self) -> str:
        return (
            self.Meta.end_tag
            if self.Meta.end_tag is not None
            else self.__class__.__name__.lower()
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

        return f"{self.Meta.start_sign}{self.start_tag}{' ' if len(self.attributes) > 0 else ''}\
{str(self.attributes)}{self.Meta.end_sign}{str(self.data)}{self.Meta.close_sign}{self.end_tag}{self.Meta.end_sign}"

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()

    def __add__(self, other) -> str:
        return Base(self.__str__() + " " + self._str(other), _meta=empty)

    def __radd__(self, other) -> str:
        return self._str(other) + " " + self.__str__()

    def __len__(self):
        return len(self.__str__())

    def __getitem__(self, item):
        return self.__str__()[item]

    def _str(self, data):
        try:
            if isinstance(data, type):
                if isinstance(data(), Base):
                    data = data()
        except Exception as _:
            pass
        return str(data)

    def __lt__(self, other):
        return Base(f"{self._str(other)} > {self.__str__()}", _meta=empty)

    def __gt__(self, other):
        return Base(f"{self.__str__()} > {self._str(other)}", _meta=empty)

    def __le__(self, other):
        return Base(f"{self.__str__()} <= {self._str(other)}", _meta=empty)

    def __ge__(self, other):
        return Base(f"{self.__str__()} >= {self._str(other)}", _meta=empty)

    def __mul__(self, value: int) -> str:
        return Base(self.__str__() * int(value), _meta=empty)

    def __rmul__(self, value: int) -> str:
        return self.__mul__(value)

    def __imul__(self, value: int) -> str:
        return self.__mul__(value)

    def css(self, tag: str = ""):
        return tag + self.start_tag

    def __matmul__(self, other):
        return self._temp(other)

        # return self._data.append(other)

    def __and__(self, other):
        return self._temp(other)

    def __or__(self, other):
        return self._temp(other)

    def __mod__(self, other):
        return self._temp(other)

    def __truediv__(self, other):
        if not isinstance(other, (list, set, tuple)):
            other = (other,)
        return self._attributes.append(*other)

    def __imatmul__(self, other):
        return self._itemp(other)

    def __iand__(self, other):
        return self._itemp(other)

    def __ior__(self, other):
        return self._itemp(other)

    def __imod__(self, other):
        return self._itemp(other)

    def __itruediv__(self, other):
        return self._itemp(other)

    def copy(self):
        return self.__class__(*self._data._data, **self._attributes.copy())

    def _temp(self, other):
        if not isinstance(other, (list, set, tuple)):
            other = (other,)
        copy = self.copy()
        copy._attributes.append(
            "class",
            *other,
        )
        return copy

    def _itemp(self, other):
        if not isinstance(other, (list, set, tuple)):
            other = (other,)
        self._attributes.append(
            "class",
            *other,
        )
        return self


class BaseElement(Base): ...


class BaseVoidElement(BaseElement):
    def render(self, prettify: bool = False):
        return f"""{self.Meta.start_sign}{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}{self.Meta.close_sign} """


class BaseSvgElement(Base): ...


class Class(Base):
    def __init__(self, *args) -> None:
        self.args = args

    def render(self, prettify: bool = False) -> str:
        return " ".join(list(map(self._str, self.args)))
