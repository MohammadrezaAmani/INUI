from typing import Any

from inui.base import BaseElement, BaseVoidElement
from inui.base import _Meta as meta_base


class e(BaseElement):
    Meta = meta_base("", "", "", "", "", "")


class Doctype(BaseVoidElement): ...


class Abbr(BaseElement): ...


class Acronym(BaseElement): ...


class Address(BaseElement): ...


class A(BaseElement): ...


class Applet(BaseElement): ...


class Area(BaseVoidElement): ...


class Article(BaseElement): ...


class Aside(BaseElement): ...


class Audio(BaseElement): ...


class Base(BaseVoidElement): ...


class Basefont(BaseVoidElement): ...


class Bdi(BaseElement): ...


class Bdo(BaseElement): ...


class Bgsound(BaseVoidElement): ...


class Big(BaseElement): ...


class Blockquote(BaseElement): ...


class Body(BaseElement): ...


class B(BaseElement): ...


class Br(BaseVoidElement): ...


class Button(BaseElement): ...


class Caption(BaseElement): ...


class Canvas(BaseElement): ...


class Center(BaseElement): ...


class Cite(BaseElement): ...


class Code(BaseElement): ...


class Colgroup(BaseElement): ...


class Col(BaseVoidElement): ...


class Comment(BaseElement):
    class Meta:
        start_tag = "!--"
        end_tag = "--"

    def render_to_string(self, prettify: bool = False) -> str:
        return f"<{self.start_tag}{' ' if len(self.attributes) > 0 else ''}{str(self.attributes)} {str(self.data)}{self.end_tag}>"


class Data(BaseElement): ...


class Datalist(BaseElement): ...


class Dd(BaseElement): ...


class Dfn(BaseElement): ...


class Del(BaseElement): ...


class Details(BaseElement): ...


class Dialog(BaseElement): ...


class Dir(BaseElement): ...


class Div(BaseElement): ...


class Dl(BaseElement): ...


class Embed(BaseVoidElement): ...


class Fieldset(BaseElement): ...


class Figcaption(BaseElement): ...


class Figure(BaseElement): ...


class Font(BaseElement): ...


class Footer(BaseElement): ...


class Form(BaseElement): ...


class Frame(BaseVoidElement): ...


class Frameset(BaseElement): ...


class Head(BaseElement): ...


class Header(BaseElement): ...


class H1(BaseElement): ...


class H2(BaseElement): ...


class H3(BaseElement): ...


class H4(BaseElement): ...


class H5(BaseElement): ...


class H6(BaseElement): ...


class Hgroup(BaseElement): ...


class Hr(BaseVoidElement): ...


class Html(BaseElement): ...


class Iframe(BaseElement): ...


class Img(BaseElement): ...


class Input(BaseVoidElement): ...


class Ins(BaseElement): ...


class Isindex(BaseVoidElement): ...


class I(BaseElement):  # noqa: E742
    ...


class Kbd(BaseElement): ...


class Keygen(BaseVoidElement): ...


class Label(BaseElement): ...


class Legend(BaseElement): ...


class Li(BaseElement): ...


class Link(BaseElement): ...


class Main(BaseElement): ...


class Mark(BaseElement): ...


class Marquee(BaseElement): ...


class Menuitem(BaseElement): ...


class Meta(BaseVoidElement): ...


class Meter(BaseElement): ...


class Nav(BaseElement): ...


class Nobr(BaseElement): ...


class Noembed(BaseElement): ...


class Noscript(BaseElement): ...


class Object(BaseElement): ...


class Ol(BaseElement): ...


class Ul(BaseElement): ...


class Optgroup(BaseElement): ...


class Option(BaseElement): ...


class Output(BaseElement): ...


class P(BaseElement): ...


class Pre(BaseElement): ...


class Progress(BaseElement): ...


class Q(BaseElement): ...


class Rp(BaseElement): ...


class Rt(BaseElement): ...


class Ruby(BaseElement): ...


class S(BaseElement): ...


class Samp(BaseElement): ...


class Script(BaseElement): ...


class Section(BaseElement): ...


class Small(BaseElement): ...


class Source(BaseElement): ...


class Spacer(BaseVoidElement): ...


class Span(BaseElement): ...


class Strike(BaseElement): ...


class Strong(BaseElement): ...


class Style(BaseElement): ...


class Sub(BaseElement): ...


class Sup(BaseElement): ...


class Summary(BaseElement): ...


class Svg(BaseElement): ...


class Table(BaseElement): ...


class Tbody(BaseElement): ...


class Td(BaseElement): ...


class Template(BaseElement): ...


class Tfoot(BaseElement): ...


class Th(BaseElement): ...


class Thead(BaseElement): ...


class Time(BaseElement): ...


class Title(BaseElement): ...


class Tr(BaseElement): ...


class Track(BaseElement): ...


class Tt(BaseElement): ...


class U(BaseElement): ...


class Var(BaseElement): ...


class Video(BaseElement): ...


class Wbr(BaseElement): ...


class Xmp(BaseElement): ...
"""
<html>
    <head>
        <title>Hot Reload Example</title>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                document.body.innerHTML = event.data;
            };
        </script>
    </head>
    <body>
        <h1>Hot Reload</h1>
    </body>
</html>
"""


class HotReload(BaseVoidElement):
    def __init__(
        self, *data: Any, host: str = "localhost", port: int = 8000, **attributes: Any
    ) -> None:
        self.host = host
        self.port = port
        super().__init__(*data, **attributes)

    def render_to_string(self, prettify: bool = False):
        return Script(
            """
            var ws = new WebSocket("ws://%s:%s/ws");
            ws.onopen = function() {
                console.log("Connected to WebSocket");
            };
            ws.onmessage = function(event) {
                console.log("Message received:", event.data);
                document.body.innerHTML = event.data;
            };
            ws.onclose = function() {
                console.log("Disconnected from WebSocket");
            };
            """
            % (self.host, str(self.port))
        ).render_to_string()


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
