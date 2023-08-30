from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""off-canvas ecommerce-header-off-canvas position-left""",
                    id="""ecommerce-header""",
                    data_off_canvas="",
                    data=(
                        Button(
                            classs="""close-button""",
                            aria_lable="""Close menu""",
                            typee="""button""",
                            data_close="",
                            data=(Span(aria_hidden="""true""", data=("""×""",)),),
                        ),
                        Ul(
                            classs="""vertical menu""",
                            data=(
                                Li(
                                    classs="""main-nav-link""",
                                    data=(
                                        A(
                                            href="""categories.html""",
                                            data=("""Category 1""",),
                                        ),
                                    ),
                                ),
                                Li(
                                    classs="""main-nav-link""",
                                    data=(A(href="""#""", data=("""Category 2""",)),),
                                ),
                                Li(
                                    classs="""main-nav-link""",
                                    data=(
                                        A(
                                            href="""why.html""",
                                            data=("""Category 3""",),
                                        ),
                                    ),
                                ),
                                Li(
                                    classs="""main-nav-link""",
                                    data=(
                                        A(
                                            href="""build.html""",
                                            data=("""Category 4""",),
                                        ),
                                    ),
                                ),
                                Li(
                                    classs="""main-nav-link""",
                                    data=(A(href="""#""", data=("""Category 5""",)),),
                                ),
                            ),
                        ),
                        Hr(),
                        Ul(
                            classs="""menu vertical""",
                            data=(
                                Li(data=(A(href="""#""", data=("""Help""",)),)),
                                Li(data=(A(href="""#""", data=("""Order Status""",)),)),
                                Li(data=(A(href="""#""", data=("""Contact""",)),)),
                                Li(data=(A(href="""#""", data=("""My Account""",)),)),
                            ),
                        ),
                    ),
                ),
                Div(
                    classs="""off-canvas-content""",
                    data_off_canvas_content="",
                    data=(
                        Div(
                            classs="""ecommerce-header-top show-for-large""",
                            data=(
                                Div(
                                    classs="""row align-justify""",
                                    data=(
                                        Div(
                                            classs="""ecommerce-header-top-message""",
                                            data=(
                                                """
        Tagline Message Can Display Here
      """,
                                            ),
                                        ),
                                        Div(
                                            classs="""ecommerce-header-top-links""",
                                            data=(
                                                Ul(
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=("""Help""",),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Order Status""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Contact""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """My Account""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    target="""_blank""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-shopping-cart""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""ecommerce-header show-for-large""",
                            data=(
                                Div(
                                    classs="""row align-justify align-middle""",
                                    data=(
                                        Div(
                                            classs="""shrink column""",
                                            data=(
                                                Ul(
                                                    classs="""vertical medium-horizontal menu""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        Img(
                                                                            classs="""logo""",
                                                                            src="""https://placehold.it/160x50""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            classs="""main-nav-link""",
                                                            data=(
                                                                A(
                                                                    href="""categories.html""",
                                                                    data=(
                                                                        """Category 1""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""main-nav-link""",
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Category 2""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""main-nav-link""",
                                                            data=(
                                                                A(
                                                                    href="""why.html""",
                                                                    data=(
                                                                        """Category 3""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""main-nav-link""",
                                                            data=(
                                                                A(
                                                                    href="""build.html""",
                                                                    data=(
                                                                        """Category 4""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""main-nav-link""",
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Category 5""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""shrink column""",
                                            data=(
                                                Ul(
                                                    classs="""menu""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                Input(
                                                                    typee="""search""",
                                                                    placeholder="""Search""",
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                Button(
                                                                    typee="""button""",
                                                                    classs="""button search-button""",
                                                                ),
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
                        Div(
                            classs="""ecommerce-header-mobile hide-for-large""",
                            data=(
                                Div(
                                    classs="""ecommerce-header-mobile-left""",
                                    data=(
                                        Button(
                                            classs="""menu-icon""",
                                            typee="""button""",
                                            data_toggle="""ecommerce-header""",
                                        ),
                                        Form(
                                            classs="""ecommerce-header-search-exandable""",
                                            data=(
                                                Input(
                                                    typee="""search""",
                                                    placeholder="""Search""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""ecommerce-header-mobile-center""",
                                    data=(
                                        A(
                                            href="""#""",
                                            data=(
                                                Img(
                                                    classs="""logo""",
                                                    src="""https://placehold.it/130x30""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""ecommerce-header-mobile-right""",
                                    data=(
                                        I(
                                            classs="""fa fa-shopping-cart""",
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
