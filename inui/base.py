from __future__ import annotations

import re
from typing import Any, Dict, List, NamedTuple, Tuple, Type, TypeVar, Union

from inui.config.replaces import replace


def _fix_quoute(string: str):
    string = string.replace("\\", "\\\\")
    if "'" in string and '"' in string:
        string = string.replace('"', '\\"')
        string = string.replace("'", "\\'")
    elif '"' in string:
        string = string.replace('"', "'")
    elif "'" in string:
        string = string.replace("'", '"')
    return string


def _find_quote(string: str):
    if '"' in string and '"' in string:
        string = string.replace('"', '\\"')
        string = string.replace("'", "\\'")
        return f'"{string}"'
    elif "'" in string:
        return f'"{string}"'

    elif '"' in string:
        return f"'{string}'"
    else:
        return f'"{string}"'


class Attributes:
    def __init__(self, **kwargs: Any) -> None:
        self.attrs: Dict[str, Any] = {
            replace(key): value for key, value in kwargs.items()
        }

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
        key = replace(key).lower()
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


class _Meta(NamedTuple):
    start_tag: str = None
    end_tag: str = None
    start_sign: str = "<"
    end_sign: str = ">"
    close_sign: str = "</"
    void_sign: str = "/>"


empty = _Meta("", "", "", "", "", "")


class Base:
    _Meta: Type[_Meta] = _Meta()
    _data = _Data()
    _attributes = Attributes()

    def __init__(
        self, *data: Any, _meta: Type[_Meta] | None = None, **attributes: Any
    ) -> None:
        self.data = data
        self.attributes = attributes
        self._Meta = _meta or self._Meta

    @property
    def data(self) -> list:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = _Data(*value)

    @property
    def start_tag(self) -> str:
        return (
            self._Meta.start_tag
            if self._Meta.start_tag is not None
            else self.__class__.__name__.lower()
        )

    @start_tag.setter
    def start_tag(self, value: str) -> None:
        self._Meta.start_tag = value

    @property
    def end_tag(self) -> str:
        return (
            self._Meta.end_tag
            if self._Meta.end_tag is not None
            else self.__class__.__name__.lower()
        )

    @end_tag.setter
    def end_tag(self, value: str) -> None:
        self._Meta.end_tag = value

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

    def render_to_string(self, prettify: bool = False) -> str:

        return f"{self._Meta.start_sign}{self.start_tag}{' ' if len(self.attributes) > 0 else ''}\
{str(self.attributes)}{self._Meta.end_sign}{str(self.data)}{self._Meta.close_sign}{self.end_tag}{self._Meta.end_sign}"

    def __str__(self) -> str:
        return self.render_to_string()

    def __repr__(self) -> str:
        return self.render_to_string()

    def __add__(self, other):
        return none(self.copy(), other)

    def __radd__(self, other) -> str:
        return none(other, self.copy())

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

    def _compare(self, other, op) -> Base:
        return none(self.copy(), op, other)

    def __lt__(self, other):
        return self._compare(other, "<")

    def __gt__(self, other):
        return self._compare(other, ">")

    def __le__(self, other):
        return self._compare(other, "<=")

    def __ge__(self, other):
        return self._compare(other, ">=")

    def __mul__(self, value: int):
        return none(*[self.copy() for _ in range(int(value))])

    def __rmul__(self, value: int):
        return self.__mul__(value)

    def __imul__(self, value: int):
        return self.__mul__(value)

    def css(self, tag: str = ""):
        return tag + self.start_tag

    def __matmul__(self, other):
        return self.add_attribute(other, key="style")

    def __and__(self, other):
        return self.add_attribute(other, key="id")

    def __or__(self, other):
        return self.add_child(other)

    def __mod__(self, other):
        return self.add_attribute(other, key="class")

    def __truediv__(self, other):
        return self.add_attribute(other, key="type")

    def __floordiv__(self, other):
        return self.add_attribute(other, key="name")

    def __ifloordiv__(self, other):
        return self.add_attribute(other, key="name")

    def __imatmul__(self, other):
        return self.__matmul__(other)

    def __iand__(self, other):
        return self.__and__(other)

    def __ior__(self, other):
        return self.__or__(other)

    def __imod__(self, other):
        return self.__mod__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def copy(self):
        return self.__class__(*self._data._data, **self._attributes.copy())

    def add_attribute(self, other, key="class"):
        if not isinstance(other, (list, set, tuple)):
            other = (other,)
        self._attributes.append(
            key,
            *other,
        )
        return self

    def add_child(self, other):
        if not isinstance(other, (list, set, tuple)):
            other = (other,)
        self._data.append(
            *other,
        )
        return self

    def from_string(
        self,
        template_name: str = "",
        context: dict[str, Any] | None = None,
        request=None,
    ):
        context = context or {}

        def replace_from_context(match: re.Match):
            var_name = match.group(1)
            default_value = eval(match.group(2))
            r = context.get(var_name, default_value)
            if isinstance(r, str):
                r = _find_quote(r)
            return str(r)

        def replace_request(match: re.Match):
            default_value = eval(match.group(1))
            r = request or default_value
            if isinstance(r, str):
                r = _find_quote(r)
            return str(r)

        template_name = re.sub(
            r"__from_context__\(\s*['\"](\w+)['\"]\s*,\s*(.*?)\s*\)",
            replace_from_context,
            template_name,
        )
        template_name = re.sub(r"__request__\((.*?)\)", replace_request, template_name)

        template_name = re.sub(r"__out__\((.*?)\)", r"output = \1", template_name)
        local_vars = {}
        exec(template_name, {}, local_vars)

        return local_vars.get("output")

    def render(self, template_name, context=None, request=None, base_path: str = ""):
        with open(base_path + template_name) as f:
            text = f.read()
        return self.from_string(text, context, request)


class BaseElement(Base): ...


class BaseVoidElement(BaseElement):
    def render_to_string(self, prettify: bool = False):
        return f"""{self._Meta.start_sign}{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}{self._Meta.close_sign} """


class BaseSvgElement(Base): ...


class Class(Base):
    def __init__(self, *args) -> None:
        self.args = args

    def render_to_string(self, prettify: bool = False) -> str:
        return " ".join(list(map(self._str, self.args)))


class none(Base):
    _Meta = empty


T = TypeVar("T")


def __from_context__(key: str, *defualt: T) -> T:
    return (*defualt,)


def __out__(*args: T) -> T:
    return (*args,)


def __request__(*defualt: T) -> T:
    return (*defualt,)


# if "\n" not in
