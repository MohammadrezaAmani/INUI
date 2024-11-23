from __future__ import annotations

from typing import Any, Dict, List, NamedTuple, Type, TypeVar

from inui.bases.attributes import BaseAttributes
from inui.bases.base import Base
from inui.bases.data import BaseData
from inui.config.replaces import replace
from inui.query import (
    AttributeDescribe,
    Describe,
    NoneQueryset,
    Q,
    Queryset,
    filter,
    select,
)


class Attributes(BaseAttributes):
    def __init__(self, **kwargs: Any) -> None:
        self.attrs: Dict[str, Any] = {
            replace(key): value for key, value in kwargs.items()
        }

    def describe(self):
        return [AttributeDescribe(key, value) for key, value in self.attrs.items()]

    def __str__(self) -> str:
        return " ".join(
            f'{replace(name)}="{self._str(value)}"'
            for name, value in self.attrs.items()
            if value is not None
        )

    def append(self, key: str = "class", *values):
        key = replace(key).lower()
        return super().append(key, *values)

    def _str(self, data, seperator=" ", fill=""):
        try:
            if isinstance(data, type):
                if isinstance(data(), Base):
                    data = data()
        except Exception as _:
            pass
        return super()._str(data, seperator, fill)

    def select(
        self,
        field: str,
        case_senstive: bool = True,
        number: int | None = None,
        as_list: bool = False,
    ):
        result = []
        if number == 0:
            if as_list:
                return []
            else:
                return NoneQueryset()

        if isinstance(field, str):
            field = field if case_senstive else field.lower()
            field = Q.process_field(field)
        try:
            if field[0].startswith(tuple("0123456789")):
                ...
        except Exception as _:
            ...

        return result


class _Data(BaseData):
    def __init__(self, *args) -> None:
        self._data: List[Any] = args

    def _str(self, data):
        try:
            if isinstance(data, type):
                if isinstance(data(), Base):
                    data = data()
        except Exception as _:
            pass
        return super()._str(data)

    def describe(self, data: list | None = None):
        results = []
        if data is None:
            data = self._data
        self._fix_calls()
        for d in data:
            if isinstance(d, Base):
                results.append(d.describe())
            elif isinstance(d, (set, list, tuple)):
                results.append(
                    Describe(attributes=[], data=self.describe(d)), type=type(d)
                )
            else:
                results.append(Describe(attributes=[], data=d, type=type(d)))
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
        result = []
        number = len(self._data) if number is None else number
        if number == 0:
            if as_list:
                return []
            else:
                return NoneQueryset()
        self._fix_calls()
        if isinstance(field, str):
            field = field if case_senstive else field.lower()
            field = Q.process_field(field)
        try:
            if field[0].startswith(tuple("0123456789")):
                if len(field) == 1:
                    res = [self._data[int(field[0])]]
                else:
                    res = select(
                        self._data[int(field[0])],
                        field[1:],
                        case_senstive=case_senstive,
                        number=number,
                        as_list=True,
                    )
                if as_list:
                    return res
                else:
                    return Queryset(*res)
        except Exception as _:
            pass

        for i in self._data:
            name = ""
            if isinstance(i, Base):
                name = i.__class__.__name__
            if not case_senstive:
                name = name.lower()

            if name == field[0]:
                if len(field) == 1:
                    result.append(i)
                else:
                    res = select(
                        i,
                        field[1:],
                        case_senstive=case_senstive,
                        number=number,
                        as_list=True,
                    )
                    if res != NoneQueryset() and res is not None and res != []:
                        result = [*result, *res]
                number != 1
                if number <= 0:
                    break
        if as_list:
            return result
        else:
            return Queryset(*result) if result else NoneQueryset()

    def filter(): ...


class _Meta(NamedTuple):
    start_tag: str = None
    end_tag: str = None
    start_sign: str = "<"
    end_sign: str = ">"
    close_sign: str = "</"
    void_sign: str = "/>"


empty = _Meta("", "", "", "", "", "")


class BaseElement(Base):
    _Meta: Type[_Meta] = _Meta()
    _data = _Data()
    _attributes = Attributes()
    is_deleted = False
    _data_class = _Data
    attributes_class = Attributes

    def select(
        self,
        *field,
        case_senstive: bool = True,
        number: int | None = None,
        as_list=False,
    ):
        return select(
            self, *field, case_senstive=case_senstive, number=number, as_list=as_list
        )

    def filter(
        self,
        *args,
        case_senstive: bool = True,
        number: int | None = None,
        as_list=False,
        **queries,
    ):
        return filter(
            self,
            self,
            *args,
            case_senstive=case_senstive,
            number=number,
            as_list=as_list,
            **queries,
        )


class BaseVoidElement(BaseElement):
    def render_to_string(self, prettify: bool = False):
        return f"""{self._Meta.start_sign}{self.start_tag}\
{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}{self._Meta.void_sign} """


class BaseSvgElement(BaseElement): ...


class Class(BaseElement):
    def __init__(self, *args) -> None:
        self.args = args

    def render_to_string(self, prettify: bool = False) -> str:
        return " ".join(list(map(self._str, self.args)))


class none(BaseElement):
    _Meta = empty


T = TypeVar("T")


def __from_context__(key: str, *defualt: T) -> T:
    return (*defualt,)


def __out__(*args: T) -> T:
    return (*args,)


def __request__(*defualt: T) -> T:
    return (*defualt,)
