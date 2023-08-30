from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""breadcrumb-counter-nav""",
                    data=(
                        Li(
                            classs="""breadcrumb-counter-nav-item""",
                            data=(A(href="""#""", data=("""Setup""",)),),
                        ),
                        Li(
                            classs="""breadcrumb-counter-nav-item current""",
                            data=(A(href="""#""", data=("""Sample Analysis""",)),),
                        ),
                        Li(
                            classs="""breadcrumb-counter-nav-item""",
                            data=(A(href="""#""", data=("""Sort Layout""",)),),
                        ),
                        Li(
                            classs="""breadcrumb-counter-nav-item""",
                            data=(A(href="""#""", data=("""Sort""",)),),
                        ),
                        Li(
                            classs="""breadcrumb-counter-nav-item""",
                            data=(A(href="""#""", data=("""Reporting""",)),),
                        ),
                    ),
                ),
            )
        ),
    )
)
