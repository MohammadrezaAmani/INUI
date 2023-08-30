from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Table(
                    classs="""dashboard-table""",
                    data=(
                        Colgroup(
                            data=(
                                Col(
                                    width="""150""",
                                ),
                                Col(
                                    width="""80""",
                                ),
                                Col(
                                    width="""200""",
                                ),
                                Col(
                                    width="""60""",
                                ),
                                Col(
                                    width="""220""",
                                ),
                                Col(
                                    width="""170""",
                                ),
                            )
                        ),
                        Thead(
                            data=(
                                Tr(
                                    data=(
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 1 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 2 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 3 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 4 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 5 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Th(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=(
                                                        """Column 6 """,
                                                        I(
                                                            classs="""fa fa-caret-down""",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                    )
                                ),
                            )
                        ),
                        Tbody(data=()),
                        Tr(
                            data=(
                                Td(
                                    data=(
                                        Div(
                                            classs="""flex-container align-justify align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/50/50/people/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child-grow""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=("""A Person""",),
                                                        ),
                                                        Span(
                                                            classs="""dashboard-table-timestamp""",
                                                            data=("""03/04/2017""",),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Td(data=("""Single Line""",)),
                                Td(classs="""bold""", data=("""A Bold Line""",)),
                                Td(data=("""A Date""",)),
                                Td(
                                    data=(
                                        Div(
                                            classs="""flex-container align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/50/50/people/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=(
                                                                """Another person did something""",
                                                            ),
                                                        ),
                                                        Span(
                                                            classs="""dashboard-table-timestamp""",
                                                            data=("""03/08/2017""",),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Td(
                                    classs="""listing-inquiry-status""",
                                    data=(
                                        Div(
                                            classs="""flex-container align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/25/25/abstract/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """A longer wrapping item with an image that is aligned to the top""",
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
                        Tr(
                            data=(
                                Td(
                                    data=(
                                        Div(
                                            classs="""flex-container align-justify align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/50/50/people/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child-grow""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=("""A Person""",),
                                                        ),
                                                        Span(
                                                            classs="""dashboard-table-timestamp""",
                                                            data=("""03/04/2017""",),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Td(data=("""Single Line""",)),
                                Td(classs="""bold""", data=("""A Bold Line""",)),
                                Td(data=("""A Date""",)),
                                Td(
                                    data=(
                                        Div(
                                            classs="""flex-container align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/50/50/people/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=(
                                                                """Another person did something""",
                                                            ),
                                                        ),
                                                        Span(
                                                            classs="""dashboard-table-timestamp""",
                                                            data=("""03/08/2017""",),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                                Td(
                                    classs="""listing-inquiry-status""",
                                    data=(
                                        Div(
                                            classs="""flex-container align-top""",
                                            data=(
                                                Div(
                                                    classs="""flex-child-shrink""",
                                                    data=(
                                                        Img(
                                                            classs="""dashboard-table-image""",
                                                            src="""https://lorempixel.com/25/25/abstract/""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""flex-child""",
                                                    data=(
                                                        H6(
                                                            classs="""dashboard-table-text""",
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """A longer wrapping item with an image that is aligned to the top""",
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
                    ),
                ),
            )
        ),
    )
)
