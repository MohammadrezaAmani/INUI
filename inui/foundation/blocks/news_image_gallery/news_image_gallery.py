from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""news-image-gallery-container""",
                    data=(
                        Div(
                            classs="""row""",
                            data=(
                                Div(
                                    classs="""small-12 medium-12 large-8 columns""",
                                    data=(
                                        Div(
                                            classs="""orbit""",
                                            role="""region""",
                                            aria_lable="""Favorite Space Pictures""",
                                            data_orbit="",
                                            data_options="""animInFromLeft:fade-in; animInFromRight:fade-in; animOutToLeft:fade-out; animOutToRight:fade-out;""",
                                            data=(
                                                Ul(
                                                    classs="""orbit-container""",
                                                    data=(
                                                        Button(
                                                            classs="""orbit-previous""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Previous Slide""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            classs="""orbit-next""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Next Slide""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""is-active orbit-slide""",
                                                            data=(
                                                                Img(
                                                                    classs="""orbit-image""",
                                                                    src="""https://i.imgur.com/4K3hXoZ.jpg""",
                                                                    alt="""Space""",
                                                                ),
                                                                Figcaption(
                                                                    classs="""orbit-caption""",
                                                                    data=(
                                                                        """Space, the final frontier.""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""orbit-slide""",
                                                            data=(
                                                                Img(
                                                                    classs="""orbit-image""",
                                                                    src="""https://i.imgur.com/V7zk0Y3.jpg""",
                                                                    alt="""Space""",
                                                                ),
                                                                Figcaption(
                                                                    classs="""orbit-caption""",
                                                                    data=(
                                                                        """Lets Rocket!""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""orbit-slide""",
                                                            data=(
                                                                Img(
                                                                    classs="""orbit-image""",
                                                                    src="""https://i.imgur.com/vivEvd0.jpg""",
                                                                    alt="""Space""",
                                                                ),
                                                                Figcaption(
                                                                    classs="""orbit-caption""",
                                                                    data=(
                                                                        """Encapsulating""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""orbit-slide""",
                                                            data=(
                                                                Img(
                                                                    classs="""orbit-image""",
                                                                    src="""https://i.imgur.com/VKdPzTp.jpg""",
                                                                    alt="""Space""",
                                                                ),
                                                                Figcaption(
                                                                    classs="""orbit-caption""",
                                                                    data=(
                                                                        """Outta This World""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Nav(
                                                    classs="""orbit-bullets""",
                                                    data=(
                                                        Button(
                                                            classs="""is-active""",
                                                            data_slide="""0""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """First slide details.""",
                                                                    ),
                                                                ),
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Current Slide""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            data_slide="""1""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Second slide details.""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            data_slide="""2""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Third slide details.""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            data_slide="""3""",
                                                            data=(
                                                                Span(
                                                                    classs="""show-for-sr""",
                                                                    data=(
                                                                        """Fourth slide details.""",
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
                                Div(
                                    classs="""small-12 medium-12 large-4 columns""",
                                    data=(
                                        Div(
                                            classs="""rounded-social-buttons""",
                                            data=(
                                                A(
                                                    classs="""social-button facebook""",
                                                    href="""#""",
                                                ),
                                                A(
                                                    classs="""social-button twitter""",
                                                    href="""#""",
                                                ),
                                                A(
                                                    classs="""social-button linkedin""",
                                                    href="""#""",
                                                ),
                                                A(
                                                    classs="""social-button google-plus""",
                                                    href="""#""",
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""clearfix""",
                                        ),
                                        H4(
                                            classs="""news-image-gallery-title""",
                                            data=(
                                                """Extraterrestrial culture: How we express ourselves through space exploration""",
                                            ),
                                        ),
                                        P(
                                            data=(
                                                """
        This is not a new thing. Terrestrial cultures have (always) had a degree of extraterrestrial-ity in them. Cultural astronomers and archeoastronomers...
        """,
                                                A(
                                                    href="""#""",
                                                    classs="""read-more""",
                                                    data=(
                                                        """
          Read More
        """,
                                                    ),
                                                ),
                                            )
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
