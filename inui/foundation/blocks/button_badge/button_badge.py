from inui.elements import *
from inui.svg import *

Html(
    data=(
        Head(
            data=(
                Link(
                    href="""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css""",
                    rel="""stylesheet""",
                ),
            )
        ),
        Body(
            data=(
                A(
                    href="""#""",
                    classs="""button-badge""",
                    data=(
                        I(
                            classs="""fa fa-envelope""",
                        ),
                        Span(classs="""badge alert""", data=("""1""",)),
                    ),
                ),
            )
        ),
    )
)
