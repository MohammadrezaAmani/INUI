from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                H2(
                    classs="""type-sidelines double""",
                    data=(Span(data=("""$4,000""",)),),
                ),
                H2(classs="""type-sidelines""", data=(Span(data=("""OR""",)),)),
                H2(
                    classs="""type-sidelines custom""",
                    data=(Span(data=("""$10,000""",)),),
                ),
                H2(
                    classs="""type-sidelines custom-2""",
                    data=(Span(data=("""DIVIDE""",)),),
                ),
            )
        ),
    )
)
