from typing import Optional

from inui.base import Base


class Size(Base):
    metric: Optional[str] = None

    def __init__(self, value=0) -> None:
        self.value = value

    def render_to_string(self, prettify: bool = False) -> str:
        metric = self.metric or self.__class__.__name__.lower()
        return f"{self.value}{metric}"


class Px(Size): ...


class Rem(Size): ...


class Em(Size): ...


class Percent(Size):
    metric = "%"


class VW(Size): ...


class VH(Size): ...


class VMIN(Size): ...


class VMin(Size): ...


class VMax(Size): ...


class EX(Size): ...


class CH(Size): ...


class PT(Size): ...


class CM(Size): ...


class PC(Size): ...


class MM(Size): ...


class IN(Size): ...
