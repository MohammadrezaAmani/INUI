from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""multilevel-offcanvas off-canvas position-right""",
                    id="""offCanvasRight""",
                    data_off_canvas="",
                    data=(
                        Ul(
                            classs="""vertical menu""",
                            data_accordion_menu="",
                            data=(
                                Li(
                                    data=(
                                        A(href="""#""", data=("""SERVICES""",)),
                                        Ul(
                                            classs="""menu vertical nested""",
                                            data=(
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Brand""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Web Apps""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Mobile Apps""",),
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Li(
                                    data=(
                                        A(href="""#""", data=("""PRODUCTS""",)),
                                        Ul(
                                            classs="""menu vertical nested""",
                                            data=(
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Product 1""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Product 2""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Product 3""",),
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Li(
                                    data=(
                                        A(href="""#""", data=("""CITIES""",)),
                                        Ul(
                                            classs="""menu vertical nested""",
                                            data=(
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""London""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""New York""",),
                                                        ),
                                                    )
                                                ),
                                                Li(
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""Paris""",),
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        Ul(
                            classs="""vertical menu""",
                            data=(
                                Li(
                                    classs="""off-canvas-menu-item""",
                                    data=(A(href="""#""", data=("""Tour""",)),),
                                ),
                                Li(data=(A(href="""#""", data=("""Login""",)),)),
                                Li(data=(A(href="""#""", data=("""Register""",)),)),
                                Li(data=(A(href="""#""", data=("""Pricing""",)),)),
                                Li(data=(A(href="""#""", data=("""Support""",)),)),
                            ),
                        ),
                        Ul(
                            classs="""vertical menu""",
                            data=(
                                Li(data=(A(href="""#""", data=("""Journal""",)),)),
                                Li(data=(A(href="""#""", data=("""FAQ""",)),)),
                                Li(
                                    data=(
                                        A(
                                            href="""#""",
                                            data=("""Terms & Conditions""",),
                                        ),
                                    )
                                ),
                                Li(data=(A(href="""#""", data=("""Careers""",)),)),
                                Li(data=(A(href="""#""", data=("""Students""",)),)),
                            ),
                        ),
                        Ul(
                            classs="""menu simple social-links""",
                            data=(
                                Li(
                                    data=(
                                        A(
                                            href="""#""",
                                            target="""_blank""",
                                            data=(
                                                I(
                                                    classs="""fa fa-twitter-square""",
                                                    aria_hidden="""true""",
                                                ),
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
                                                    classs="""fa fa-facebook-square""",
                                                    aria_hidden="""true""",
                                                ),
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
                                                    classs="""fa fa-github-square""",
                                                    aria_hidden="""true""",
                                                ),
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
                                                    classs="""fa fa-google-plus-square""",
                                                    aria_hidden="""true""",
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                ),
                Div(
                    classs="""off-canvas-content""",
                    data_off_canvas_content="",
                    data=(
                        Div(
                            classs="""nav-bar""",
                            data=(
                                Div(
                                    classs="""nav-bar-left""",
                                    data=(
                                        A(
                                            classs="""nav-bar-logo""",
                                            data=(
                                                Img(
                                                    classs="""logo""",
                                                    src="""https://placehold.it/150x30""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""nav-bar-right""",
                                    data=(
                                        Ul(
                                            classs="""menu""",
                                            data=(
                                                Li(
                                                    classs="""hide-for-small-only""",
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""TOUR""",),
                                                        ),
                                                    ),
                                                ),
                                                Li(
                                                    classs="""hide-for-small-only""",
                                                    data=(
                                                        A(
                                                            href="""#""",
                                                            data=("""LOGIN""",),
                                                        ),
                                                    ),
                                                ),
                                                Li(data=()),
                                                Li(
                                                    data=(
                                                        Button(
                                                            classs="""offcanvas-trigger""",
                                                            typee="""button""",
                                                            data_open="""offCanvasRight""",
                                                            data=(
                                                                Span(
                                                                    classs="""offcanvas-trigger-text hide-for-small-only""",
                                                                    data=("""Menu""",),
                                                                ),
                                                                Div(
                                                                    classs="""hamburger""",
                                                                    data=(
                                                                        Span(
                                                                            classs="""line""",
                                                                        ),
                                                                        Span(
                                                                            classs="""line""",
                                                                        ),
                                                                        Span(
                                                                            classs="""line""",
                                                                        ),
                                                                    ),
                                                                ),
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
                        Div(
                            classs="""body-info""",
                            data=(
                                H4(data=(""" Multilevel Off-Canvas """,)),
                                A(
                                    classs="""button disabled""",
                                    href="""#""",
                                    data=("""Watch Video (coming soon)""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
