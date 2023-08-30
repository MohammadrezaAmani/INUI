from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Header(
                    classs="""hero-search-filter""",
                    data=(
                        Div(
                            classs="""hero-search-filter-content""",
                            data=(
                                Img(
                                    classs="""hero-search-filter-logo""",
                                    src="""https://placehold.it/160x80""",
                                    alt="",
                                ),
                                Form(
                                    classs="""hero-search-filter-form""",
                                    action="",
                                    data=(
                                        Label(forr="""findtext""", data=("""Find""",)),
                                        Input(
                                            id="""findtext""",
                                            classs="""hero-search-filter-form-find""",
                                            typee="""text""",
                                        ),
                                        Div(classs="""divider""", data=()),
                                        Label(
                                            forr="""findlocate""", data=("""Near""",)
                                        ),
                                        Input(
                                            id="""findlocate""",
                                            classs="""hero-search-filter-form-near""",
                                            typee="""text""",
                                        ),
                                        Button(
                                            classs="""button""",
                                            data=(
                                                I(
                                                    classs="""fa fa-search""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Ul(
                                    classs="""hero-search-filter-menu menu align-center""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        I(
                                                            classs="""fa fa-cutlery""",
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
                                                    data=(
                                                        I(
                                                            classs="""fa fa-glass""",
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
                                                    data=(
                                                        I(
                                                            classs="""fa fa-wrench""",
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
                                                    data=(
                                                        I(
                                                            classs="""fa fa-cutlery""",
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
            )
        ),
    )
)
