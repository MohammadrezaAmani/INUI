from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""fullscreen-image-slider""",
                    data=(
                        Div(
                            classs="""orbit""",
                            role="""region""",
                            aria_lable="""FullScreen Pictures""",
                            data_orbit="",
                            data=(
                                Ul(
                                    classs="""orbit-container""",
                                    data=(
                                        Button(
                                            classs="""orbit-previous""",
                                            data=(
                                                Span(
                                                    classs="""show-for-sr""",
                                                    data=("""Previous Slide""",),
                                                ),
                                                Span(
                                                    classs="""nav fa fa-chevron-left fa-3x""",
                                                ),
                                            ),
                                        ),
                                        Button(
                                            classs="""orbit-next""",
                                            data=(
                                                Span(
                                                    classs="""show-for-sr""",
                                                    data=("""Next Slide""",),
                                                ),
                                                Span(
                                                    classs="""nav fa fa-chevron-right fa-3x""",
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""is-active orbit-slide""",
                                            data=(
                                                Img(
                                                    classs="""orbit-image""",
                                                    src="""https://i.imgur.com/16z9ObN.jpg""",
                                                    alt="""Space""",
                                                ),
                                                Figcaption(
                                                    classs="""orbit-caption""",
                                                    data=(
                                                        H1(
                                                            data=(
                                                                """Lorem ipsum dolor sit amet, """,
                                                                Br(),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""orbit-slide""",
                                            data=(
                                                Img(
                                                    classs="""orbit-image""",
                                                    src="""https://i.imgur.com/JD4Caxa.jpg""",
                                                    alt="""Space""",
                                                ),
                                                Figcaption(
                                                    classs="""orbit-caption""",
                                                    data=(
                                                        H1(
                                                            data=(
                                                                """Lorem ipsum dolor sit amet, """,
                                                                Br(),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""orbit-slide""",
                                            data=(
                                                Img(
                                                    classs="""orbit-image""",
                                                    src="""https://i.imgur.com/rsTQbNV.jpg""",
                                                    alt="""Space""",
                                                ),
                                                Figcaption(
                                                    classs="""orbit-caption""",
                                                    data=(
                                                        H1(
                                                            data=(
                                                                """Lorem ipsum dolor sit amet, """,
                                                                Br(),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
