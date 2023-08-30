from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Nav(
                    classs="""hover-underline-menu""",
                    data_menu_underline_from_center="",
                    data=(
                        Ul(
                            classs="""menu align-center""",
                            data=(
                                Li(data=(A(href="""#""", data=("""One""",)),)),
                                Li(data=(A(href="""#""", data=("""Two""",)),)),
                                Li(data=(A(href="""#""", data=("""Three""",)),)),
                                Li(data=(A(href="""#""", data=("""Four""",)),)),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
