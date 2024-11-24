from typing import Any

from inui.base import BaseVoidElement
from inui.bootstrap.utils import bs_class_to_lower
from inui.conf import FOUNDATION_CSS_URL
from inui.elements import Button, Html, Link


class FoundationEmail(BaseVoidElement):
    def __init__(
        self, *data: Any, url: str = FOUNDATION_CSS_URL, **attributes: Any
    ) -> None:
        self.url = url
        super().__init__(*data, **attributes)

    def render_to_string(self, prettify: bool = False):
        return Link(href=self.url).render_to_string()


class BaseFoundation(BaseVoidElement):
    def __init__(self, *values) -> None:
        self.values = values

    def render_to_string(self, prettify: bool = False) -> str:
        values = ""
        if self.values:
            values += "-"
            values += "-".join(list(map(str, self.values)))
        return bs_class_to_lower(self.__class__.__name__) + values


class button(BaseFoundation): ...


class tiny(BaseFoundation): ...


class small(BaseFoundation): ...


class large(BaseFoundation): ...


class small_expanded(BaseFoundation): ...


class tiny_expanded(BaseFoundation): ...


class large_expanded(BaseFoundation): ...


class colors(BaseFoundation): ...


class secondary: ...


class success(BaseFoundation): ...


class warning(BaseFoundation): ...


class alert(BaseFoundation): ...


Html(
    FoundationEmail,
    Button(
        "salam",
    )
    @ button
    @ tiny,
)
