from dataclasses import dataclass
from typing import Any, List, Union

from inui.bases.base import Base


class Queryset:
    def __init__(self, *data) -> None:
        self.data = data

    def add_data(self, data):
        self.data = (*self.data, data)

    def select(
        self,
        *fields,
        depth: int | None = None,
        **queries,
    ):
        return [i.select(*fields) for i in self.filter(depth=depth, **queries)]

    def filter(
        self,
        *qs,
        depth: int | None = None,
        **queries,
    ) -> "Queryset":
        result = []
        for i in self.data:
            if result[i].filter(*qs, depth, **queries):
                result.append(i)
        return Queryset(result)

    def first(self, value=0):
        try:
            return self.data[value]
        except Exception as _:
            return None

    def last(self, value=-1):
        try:
            return self.data[value]
        except Exception as _:
            return None

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self.select(name)


class NoneQueryset(Queryset):
    def __init__(self, *data) -> None:
        self.data = []

    def add_data(self, data): ...


class Q:
    replace_with = (("in", "in_"),)

    def __init__(self, *fields, **queries) -> None:
        self.fields = [Q.process_field(i) for i in fields]
        self.queries = {Q.process_field(key): value for key, value in queries.items()}

    @staticmethod
    def replaces(data: list[str] | None = None):
        data = data or []
        for key, value in enumerate(data):
            for replace, with_ in Q.replace_with:
                if value == replace:
                    data[key] = with_
        return tuple(data)

    @staticmethod
    def process_field(field):
        if isinstance(field, (list, set, tuple)):
            return field
        return Q.replaces(str(field).split("__"))

    @staticmethod
    def process(element, *qs):
        for q in qs:
            if not isinstance(q, Q):
                raise "error"


class Tree:
    def __init__(self, element) -> None:
        self.element = element

    def show(self):
        print(self.element.data)


class query: ...


class Funcs:
    contains = "contains"
    icontains = "icontains"
    exact = "exact"
    iexact = "iexact"
    endswith = "endswith"
    iendswith = "iendswith"
    in_ = "in"
    isempty = "isempty"
    regex = "regex"
    iregex = "iregex"
    startwith = "startwith"
    istartwith = "istartwith"
    startswith = "startswith"
    gt = "gt"
    gte = "gte"
    lt = "lt"
    lte = "lte"
    len = "len"
    type = "type"
    attr = "attr"
    first = "first"
    last = "last"

    @staticmethod
    def apply_function(
        result,
        field: str,
        case_senstive: bool = True,
        number: int | None = None,
        as_list=False,
    ):
        if field[0] == Ut.type:
            result = [type(i) for i in result]
        elif field[0] == Ut.first:
            result = [result[0]] if len(result) > 0 else []
        elif field[0] == Ut.length:
            result = [len(i) for i in result]
        elif field[0] == Ut.class_name:
            result = [
                (i.__class__.__name__ if not isinstance(i, int) else int)
                for i in result
            ]
        elif field[0] == Ut.len:
            result = [len(i) for i in result]
        elif field[0] == Ut.lower:
            for i in range(len(result)):
                if isinstance(result[i], str):
                    result[i] = result[i].lower()
        elif field[0] == Ut.upper:
            for i in range(len(result)):
                if isinstance(result[i], str):
                    result[i] = result[i].upper()
        elif field[0] == Ut.title:
            for i in range(len(result)):
                if isinstance(result[i], str):
                    result[i] = result[i].title()
        elif field[0] == Ut.value:
            for i in range(len(result)):
                if hasattr(result[i], "data"):
                    result[i] = getattr(result[i], "data")

        return result if as_list else Queryset(*result)


class Ut:
    type = "_type"
    first = "_first"
    last = "_last"
    class_name = "_class_name"
    lower = "_lower"
    upper = "_upper"
    title = "_title"
    length = "_length"
    len = "_len"
    value = "_value"


def select(
    element,
    *fields: str,
    case_senstive: bool = True,
    number: int | None = None,
    as_list=False,
):
    result = []
    if isinstance(element, (list, tuple, set)):
        for elm in element:
            result = [
                *result,
                *_select(
                    elm,
                    *fields,
                    case_senstive=case_senstive,
                    number=number,
                    as_list=True,
                ),
            ]
    else:
        result = _select(
            element,
            *fields,
            case_senstive=case_senstive,
            number=number,
            as_list=True,
        )

    return result if as_list else Queryset(*result)


def _select(
    element,
    *fields: str,
    case_senstive: bool = True,
    number: int | None = None,
    as_list=False,
):
    result = []
    for field in fields:
        res = []
        if isinstance(field, str):
            field = field if case_senstive else field.lower()
            field = Q.process_field(field)
        if field[0].startswith("_"):
            res = Funcs.apply_function(
                [element],
                field,
                case_senstive=case_senstive,
                number=number,
                as_list=True,
            )
            field = field[1:]
        while len(field) > 0 and field[0].startswith("_"):
            if field[0].startswith("_"):
                res = Funcs.apply_function(
                    res,
                    field,
                    case_senstive=case_senstive,
                    number=number,
                    as_list=True,
                )
                field = field[1:]
            if len(field) <= 0:
                break

        if len(field) > 0 and field[0] == "attr":
            out = element.attributes.select(
                field,
                case_senstive=case_senstive,
                number=number,
                as_list=True,
            )
            res = [
                *res,
                *out,
            ]
        elif len(field) > 0:
            out = element.data.select(
                field,
                case_senstive=case_senstive,
                number=number,
                as_list=True,
            )
            res = [
                *res,
                *out,
            ]
        result = [*result, *res]
    return result if as_list else Queryset(*result)


class Function:
    def __init__(self) -> None:
        pass

    def equals(self, key: str, value: Any, data) -> bool:
        return value == data

    def contains(self, key: str, value: Any, data) -> bool:
        if value in data:
            return True
        return False

    def icontains(self, key: str, value: Any, data) -> bool:
        if self.to_i(value) in self.to_i(data):
            return True
        return False

    def exact(self, key: str, value: Any, data) -> bool:
        if data == value:
            return True
        return False

    def iexact(self, key: str, value: Any, data) -> bool:
        if self.to_i(data) == self.to_i(value):
            return True
        return False

    def endswith(self, key: str, value: Any, data) -> bool:
        if isinstance(data, (set, tuple, dict, list, Queryset)):
            try:
                if data[-1] == value:
                    return True
            except Exception as _:
                return False
        if str(data).endswith(value):
            return True
        return False

    def iendswith(self, key: str, value: Any, data) -> bool:
        if isinstance(data, (set, tuple, dict, list, Queryset)):
            try:
                if self.to_i(data[-1]) == self.to_i(value):
                    return True
            except Exception as _:
                return False
        if self.to_i(data).endswith(self.to_i(value)):
            return True
        return False

    def in_(self, key: str, value: Any, data) -> bool:
        try:
            if value in data:
                return True
        except Exception as _:
            ...
        try:
            if data in value:
                return True
        except Exception as _:
            ...
        return False

    def iin(self, key: str, value: Any, data) -> bool:
        data = self.to_i(data)
        value = self.to_i(value)
        if value in data or data in value:
            return True
        return False

    def isempty(self, key: str, value: bool, data) -> bool:
        empty = False
        if len(data) == 0:
            empty = True

        return empty == value

    def regex(self, key: str, value: Any, data) -> bool:
        #! must be completed.
        if data == value:
            return True
        return False

    def iregex(self, key: str, value: Any, data) -> bool:
        #! must be completed.
        if data == value:
            return True
        return False

    def startwith(self, key: str, value: Any, data) -> bool:
        if isinstance(data, (set, tuple, dict, list, Queryset)):
            try:
                if data[0] == value:
                    return True
            except Exception as _:
                return False
        if str(data).startswith(str(value)):
            return True
        return False

    def istartwith(self, key: str, value: Any, data) -> bool:
        if isinstance(data, (set, tuple, dict, list, Queryset)):
            try:
                if self.to_i(data[0]) == self.to_i(value):
                    return True
            except Exception as _:
                return False
        if self.to_i(data).startswith(self.to_i(value)):
            return True
        return False

    def gt(self, key: str, value: Any, data) -> bool:
        if data > value:
            return True
        return False

    def gte(self, key: str, value: Any, data) -> bool:
        if data >= value:
            return True
        return False

    def lt(self, key: str, value: Any, data) -> bool:
        if data < value:
            return True
        return False

    def lte(self, key: str, value: Any, data) -> bool:
        if data <= value:
            return True
        return False

    def to_i(self, value):
        return str(value).lower()

    def apply(self, key: str, value: Any, data):
        return self.equals(key, value, data)

    def guess_func(self, key: str):
        replaces = {"in_": "in"}
        reverse_replace = {value: key for key, value in replaces.items()}
        for i in self.__dir__():
            i = replaces.get(i, i)
            if not i.startswith("__") and key.endswith(f"___{i}"):
                key = key.replace(f"___{i}", "")
                i = reverse_replace.get(i, i)
                return True, getattr(self, i), key
        return False, self.equals, key


def filter(
    *elements,
    # *fields: str,
    case_senstive: bool = True,
    number: int | None = None,
    as_list=False,
    **queries,
):
    results = []
    func = Function()
    for element in elements:
        its_in = False
        for key, value in queries.items():
            _, f, key = func.guess_func(key)
            for i in select(
                element, key, case_senstive=case_senstive, number=number, as_list=True
            ):
                print(
                    {
                        "key": key,
                        "value": value,
                        "f": f,
                        "i": i,
                        "result": f(key, value, i),
                    }
                )
                if f(key, value, i):
                    its_in = True
                break
        if its_in:
            results.append(element)
    return results if as_list else Queryset(*results)


def insert(
    *elements,
    data: list[Base] = None,
    # *fields: str,
    case_senstive: bool = True,
    number: int | None = None,
    as_list=False,
    **queries,
):
    results = filter(
        *elements, case_senstive=case_senstive, number=number, as_list=True, **queries
    )
    for i in results:
        i: Base
        if isinstance(i, Base):
            i.add_child(data)

    return results if as_list else Queryset(*results)


def delete(
    *elements,
    data: list[Base] | None = None,
    # *fields: str,
    case_senstive: bool = True,
    number: int | None = None,
    as_list=False,
    **queries,
):
    results = filter(
        *elements, case_senstive=case_senstive, number=number, as_list=True, **queries
    )
    if data:
        for i in results:
            if isinstance(i, Base):
                i.data.delete(data)
    else:
        for i in results:
            if isinstance(i, Base):
                i.delete()
    return results if as_list else Queryset(*results)


@dataclass
class AttributeDescribe:
    key: str
    value: Any


@dataclass
class Describe:
    attributes: List[AttributeDescribe] | None = None
    data: List["Describe"] | None = None
    type: Union["type", None] = None
