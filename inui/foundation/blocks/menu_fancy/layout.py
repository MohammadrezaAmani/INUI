from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""menu menu-fancy align-center""",
                    data=(
                        Li(
                            classs="""menu-fancy-option1 is-selected""",
                            data=(A(href="""#""", data=("""About Me""",)),),
                        ),
                        Li(
                            classs="""menu-fancy-option2""",
                            data=(A(href="""#""", data=("""Work""",)),),
                        ),
                        Li(
                            classs="""menu-fancy-option3""",
                            data=(A(href="""#""", data=("""Resume""",)),),
                        ),
                        Li(
                            classs="""menu-fancy-option4""",
                            data=(A(href="""#""", data=("""Contact""",)),),
                        ),
                    ),
                ),
            )
        ),
    )
)
