from inui.elements import *
from inui.svg import *

Html(
    data=(
        Head(
            data=(
                Link(
                    href="""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css""",
                    rel="""stylesheet""",
                ),
            )
        ),
        Body(
            data=(
                Div(
                    classs="""responsive-nav-social-mobile""",
                    data_responsive_toggle="""responsive-nav-social""",
                    data_hide_for="""medium""",
                    data=(
                        Div(
                            classs="""responsive-nav-social-mobile-left""",
                            data=(
                                Ul(
                                    classs="""menu""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    href="""https://www.facebook.com/""",
                                                    data=(
                                                        I(
                                                            classs="""fa fa-facebook""",
                                                            aria_hidden="""true""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""https://www.instagram.com/?hl=en""",
                                                    data=(
                                                        I(
                                                            classs="""fa fa-instagram""",
                                                            aria_hidden="""true""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""https://www.pinterest.com/""",
                                                    data=(
                                                        I(
                                                            classs="""fa fa-pinterest-p""",
                                                            aria_hidden="""true""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""https://twitter.com/?lang=en""",
                                                    data=(
                                                        I(
                                                            classs="""fa fa-twitter""",
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
                            classs="""responsive-nav-social-mobile-right""",
                            data=(
                                Button(
                                    classs="""menu-icon""",
                                    typee="""button""",
                                    data_toggle="""responsive-nav-social""",
                                ),
                            ),
                        ),
                    ),
                ),
                Div(
                    data_sticky_container="",
                    data=(
                        Div(
                            classs="""responsive-nav-social""",
                            id="""responsive-nav-social""",
                            data_sticky="",
                            data_options="""marginTop:0;""",
                            data=(
                                Div(
                                    classs="""row align-justify align-middle""",
                                    id="""responsive-menu""",
                                    data=(
                                        Div(
                                            classs="""responsive-nav-social-left""",
                                            data=(
                                                Ul(
                                                    classs="""menu vertical medium-horizontal""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=("""Home""",),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=("""About""",),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Travel""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=("""Eat""",),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=("""Relax""",),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Videos""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""responsive-nav-social-right hide-for-small-only""",
                                            data=(
                                                Ul(
                                                    classs="""menu""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""https://www.facebook.com/""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-facebook""",
                                                                            aria_hidden="""true""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""https://www.instagram.com/?hl=en""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-instagram""",
                                                                            aria_hidden="""true""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""https://www.pinterest.com/""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-pinterest-p""",
                                                                            aria_hidden="""true""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""https://twitter.com/?lang=en""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-twitter""",
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
