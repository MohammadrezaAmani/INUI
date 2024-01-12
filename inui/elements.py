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


class BaseElement:
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


class BaseVoidElement(BaseElement):
    def render(self, prettify: bool = False):
        return f"""<{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)}>"""


class Doctype(BaseVoidElement):
    pass


class Abbr(BaseElement):
    pass


class Acronym(BaseElement):
    pass


class Address(BaseElement):
    pass


class A(BaseElement):
    pass


class Applet(BaseElement):
    pass


class Area(BaseVoidElement):
    pass


class Article(BaseElement):
    pass


class Aside(BaseElement):
    pass


class Audio(BaseElement):
    pass


class Base(BaseVoidElement):
    pass


class Basefont(BaseVoidElement):
    pass


class Bdi(BaseElement):
    pass


class Bdo(BaseElement):
    pass


class Bgsound(BaseVoidElement):
    pass


class Big(BaseElement):
    pass


class Blockquote(BaseElement):
    pass


class Body(BaseElement):
    pass


class B(BaseElement):
    pass


class Br(BaseVoidElement):
    pass


class Button(BaseElement):
    pass


class Caption(BaseElement):
    pass


class Canvas(BaseElement):
    pass


class Center(BaseElement):
    pass


class Cite(BaseElement):
    pass


class Code(BaseElement):
    pass


class Colgroup(BaseElement):
    pass


class Col(BaseVoidElement):
    pass


class Comment(BaseElement):
    class Meta:
        start_tag = "!--"
        end_tag = "--"

    def render(self, prettify: bool = False) -> str:
        return f"<{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)} {str(self.data)}{self.end_tag}>"


class Data(BaseElement):
    pass


class Datalist(BaseElement):
    pass


class Dd(BaseElement):
    pass


class Dfn(BaseElement):
    pass


class Del(BaseElement):
    pass


class Details(BaseElement):
    pass


class Dialog(BaseElement):
    pass


class Dir(BaseElement):
    pass


class Div(BaseElement):
    pass


class Dl(BaseElement):
    pass


class Embed(BaseVoidElement):
    pass


class Fieldset(BaseElement):
    pass


class Figcaption(BaseElement):
    pass


class Figure(BaseElement):
    pass


class Font(BaseElement):
    pass


class Footer(BaseElement):
    pass


class Form(BaseElement):
    pass


class Frame(BaseVoidElement):
    pass


class Frameset(BaseElement):
    pass


class Head(BaseElement):
    pass


class Header(BaseElement):
    pass


class H1(BaseElement):
    pass


class H2(BaseElement):
    pass


class H3(BaseElement):
    pass


class H4(BaseElement):
    pass


class H5(BaseElement):
    pass


class H6(BaseElement):
    pass


class Hgroup(BaseElement):
    pass


class Hr(BaseVoidElement):
    pass


class Html(BaseElement):
    pass


class Iframe(BaseElement):
    pass


class Img(BaseElement):
    pass


class Input(BaseVoidElement):
    pass


class Ins(BaseElement):
    pass


class Isindex(BaseVoidElement):
    pass


class I(BaseElement):
    pass


class Kbd(BaseElement):
    pass


class Keygen(BaseVoidElement):
    pass


class Label(BaseElement):
    pass


class Legend(BaseElement):
    pass


class Li(BaseElement):
    pass


class Main(BaseElement):
    pass


class Mark(BaseElement):
    pass


class Marquee(BaseElement):
    pass


class Menuitem(BaseElement):
    pass


class Meta(BaseVoidElement):
    pass


class Meter(BaseElement):
    pass


class Nav(BaseElement):
    pass


class Nobr(BaseElement):
    pass


class Noembed(BaseElement):
    pass


class Noscript(BaseElement):
    pass


class Object(BaseElement):
    pass


class Ol(BaseElement):
    pass


class Optgroup(BaseElement):
    pass


class Option(BaseElement):
    pass


class Output(BaseElement):
    pass


class P(BaseElement):
    pass


class Pre(BaseElement):
    pass


class Progress(BaseElement):
    pass


class Q(BaseElement):
    pass


class Rp(BaseElement):
    pass


class Rt(BaseElement):
    pass


class Ruby(BaseElement):
    pass


class S(BaseElement):
    pass


class Samp(BaseElement):
    pass


class Script(BaseElement):
    pass


class Section(BaseElement):
    pass


class Small(BaseElement):
    pass


class Source(BaseElement):
    pass


class Spacer(BaseVoidElement):
    pass


class Span(BaseElement):
    pass


class Strike(BaseElement):
    pass


class Strong(BaseElement):
    pass


class Style(BaseElement):
    pass


class Sub(BaseElement):
    pass


class Sup(BaseElement):
    pass


class Summary(BaseElement):
    pass


class Svg(BaseElement):
    pass


class Table(BaseElement):
    pass


class Tbody(BaseElement):
    pass


class Td(BaseElement):
    pass


class Template(BaseElement):
    pass


class Tfoot(BaseElement):
    pass


class Th(BaseElement):
    pass


class Thead(BaseElement):
    pass


class Time(BaseElement):
    pass


class Title(BaseElement):
    pass


class Tr(BaseElement):
    pass


class Track(BaseElement):
    pass


class Tt(BaseElement):
    pass


class U(BaseElement):
    pass


class Var(BaseElement):
    pass


class Video(BaseElement):
    pass


class Wbr(BaseElement):
    pass


class Xmp(BaseElement):
    pass


if __name__ == "__main__":
    print(
        Html(
            Head(Title("Hello World")),
            Body(
                "salam",
                Hr(),
                "INUI",
            ),
            Footer("Goodbye World"),
        )
    )
