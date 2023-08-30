from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""orbit clean-hero-slider""",
                    role="""region""",
                    aria_lable="""Favorite Space Pictures""",
                    data_orbit="",
                    data=(
                        Div(
                            classs="""orbit-wrapper""",
                            data=(
                                Div(
                                    classs="""orbit-controls""",
                                    data=(
                                        Button(
                                            classs="""orbit-previous""",
                                            data=(
                                                Span(
                                                    classs="""show-for-sr""",
                                                    data=("""Previous Slide""",),
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
                                            ),
                                        ),
                                    ),
                                ),
                                Ul(
                                    classs="""orbit-container""",
                                    data=(
                                        Li(
                                            classs="""orbit-slide""",
                                            data=(
                                                Figure(
                                                    classs="""orbit-figure""",
                                                    data=(
                                                        Img(
                                                            classs="""orbit-image""",
                                                            src="""https://lorempixel.com/800/350/""",
                                                            alt="""image alt text""",
                                                        ),
                                                        Figcaption(
                                                            classs="""orbit-caption""",
                                                            data=(
                                                                H3(
                                                                    data=(
                                                                        """Lorem Ipsum Etiam""",
                                                                    )
                                                                ),
                                                                P(
                                                                    data=(
                                                                        """Etiam porta sem malesuada magna mollis euismod. Vestibulum id ligula porta felis euismod semper.""",
                                                                    )
                                                                ),
                                                                A(
                                                                    href="""#""",
                                                                    classs="""button yellow""",
                                                                    data=(
                                                                        """Mattis Elit""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""orbit-slide""",
                                            data=(
                                                Figure(
                                                    classs="""orbit-figure""",
                                                    data=(
                                                        Img(
                                                            classs="""orbit-image""",
                                                            src="""https://lorempixel.com/800/350/""",
                                                            alt="""image alt text""",
                                                        ),
                                                        Figcaption(
                                                            classs="""orbit-caption""",
                                                            data=(
                                                                H3(
                                                                    data=(
                                                                        """Ipsum Ornare Ultricies""",
                                                                    )
                                                                ),
                                                                P(
                                                                    data=(
                                                                        """Nullam quis risus eget urna mollis ornare vel eu leo. Donec ullamcorper nulla non metus auctor fringilla. Lorem ipsum dolor sit amet, consectetur adipiscing elit.""",
                                                                    )
                                                                ),
                                                                A(
                                                                    href="""#""",
                                                                    classs="""button yellow""",
                                                                    data=(
                                                                        """Egestas Amet""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""orbit-slide""",
                                            data=(
                                                Figure(
                                                    classs="""orbit-figure""",
                                                    data=(
                                                        Img(
                                                            classs="""orbit-image""",
                                                            src="""https://lorempixel.com/800/350/""",
                                                            alt="""image alt text""",
                                                        ),
                                                        Figcaption(
                                                            classs="""orbit-caption""",
                                                            data=(
                                                                H3(
                                                                    data=(
                                                                        """Malesuada Parturient""",
                                                                    )
                                                                ),
                                                                P(
                                                                    data=(
                                                                        """Fusce dapibus, tellus ac cursus commodo, sit amet risus. Cras mattis consectetur purus sit amet fermentum. Maecenas sed diam sit amet non magna.""",
                                                                    )
                                                                ),
                                                                A(
                                                                    href="""#""",
                                                                    classs="""button yellow""",
                                                                    data=(
                                                                        """Sollicitudin""",
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
                        ),
                        Nav(
                            classs="""orbit-bullets""",
                            data=(
                                Button(
                                    classs="""is-active""",
                                    data_slide="""1""",
                                    data=(
                                        Span(
                                            classs="""show-for-sr""",
                                            data=("""Lorem Ipsum Etiam""",),
                                        ),
                                    ),
                                ),
                                Button(
                                    data_slide="""2""",
                                    data=(
                                        Span(
                                            classs="""show-for-sr""",
                                            data=("""Lorem Ipsum Etiam""",),
                                        ),
                                    ),
                                ),
                                Button(
                                    data_slide="""3""",
                                    data=(
                                        Span(
                                            classs="""show-for-sr""",
                                            data=("""Lorem Ipsum Etiam""",),
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
