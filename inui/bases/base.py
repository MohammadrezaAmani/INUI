from typing import Any, Dict, NamedTuple, Type, TypeVar, Union

from inui.bases.attributes import BaseAttributes
from inui.bases.data import BaseData


class _Meta(NamedTuple):
    start_tag: str = None
    end_tag: str = None
    start_sign: str = "<"
    end_sign: str = ">"
    close_sign: str = "</"
    void_sign: str = "/>"


empty = _Meta("", "", "", "", "", "")


class Base:
    _Meta: Type["_Meta"] = _Meta()
    _data = BaseData()
    _attributes = BaseAttributes()
    is_deleted = False
    attributes_class = BaseAttributes
    _data_class = BaseData

    def __init__(
        self, *data: Any, _meta: Type["_Meta"] | None = None, **attributes: Any
    ) -> None:
        self.data = data
        self.attributes = attributes
        self._Meta = _meta or self._Meta

    @property
    def data(self) -> BaseData:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = self._data_class(*value)

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
    def attributes(self) -> BaseAttributes:
        return self._attributes

    @attributes.setter
    def attributes(self, value: Union[BaseAttributes, Dict[str, Any]]) -> None:
        if not isinstance(value, (self.attributes_class, dict)):
            raise TypeError("attributes must be an instance of Attributes or dict")
        self._attributes = (
            self.attributes_class(**value) if isinstance(value, dict) else value.copy()
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

    def _compare(self, other, op) -> "Base":
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

    def render(self, template_name, context=None, request=None, base_path: str = ""):
        with open(base_path + template_name) as f:
            text = f.read()
        return self.from_string(text, context, request)

    def describe(self):
        return []

    def delete(self):
        self._Meta = none._Meta
        self._data = self._data_class()
        self._attributes = self.attributes_class()
        self.is_deleted = True

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self.select(name)

    def select(
        self,
        *field,
        case_senstive: bool = True,
        number: int | None = None,
        as_list=False,
    ):
        return []

    def filter(
        self,
        *args,
        case_senstive: bool = True,
        number: int | None = None,
        as_list=False,
        **queries,
    ):
        return []


class none(Base):
    _Meta = empty


T = TypeVar("T")
