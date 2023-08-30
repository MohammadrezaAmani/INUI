from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""mobile-bottom-bar""",
                    data=(
                        A(
                            href="""#""",
                            classs="""footer-link""",
                            data=(
                                I(
                                    classs="""fa fa-cog""",
                                ),
                                Span(classs="""footer-text""", data=("""Settings""",)),
                            ),
                        ),
                        A(
                            href="""#""",
                            classs="""footer-link""",
                            data=(
                                I(
                                    classs="""fa fa-sign-out""",
                                ),
                                Span(classs="""footer-text""", data=("""Log out""",)),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
