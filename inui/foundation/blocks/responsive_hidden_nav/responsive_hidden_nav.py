from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""responsive-hidden-nav-container""",
                    data=(
                        Nav(
                            classs="""top-bar responsive-hidden-nav""",
                            data_responsive_hidden_nav="",
                            data=(
                                Button(
                                    classs="""responsive-hidden-button""",
                                    data=(
                                        Div(
                                            classs="""hamburger""",
                                        ),
                                    ),
                                ),
                                Ul(
                                    classs="""visible-links""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""Responsive""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""navigation""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(A(href="""#""", data=("""whose""",)),)
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""overflowing""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""elements""",)),
                                            )
                                        ),
                                        Li(data=(A(href="""#""", data=("""get""",)),)),
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""stacked""",)),
                                            )
                                        ),
                                        Li(data=(A(href="""#""", data=("""into""",)),)),
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""hamburger""",),
                                                ),
                                            )
                                        ),
                                        Li(data=(A(href="""#""", data=("""menu""",)),)),
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""effortlessly""",),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Ul(
                                    classs="""hidden-links hidden""",
                                ),
                            ),
                        ),
                        H4(
                            classs="""demo-title""",
                            data=("""resize the window please..""",),
                        ),
                    ),
                ),
            )
        ),
    )
)
