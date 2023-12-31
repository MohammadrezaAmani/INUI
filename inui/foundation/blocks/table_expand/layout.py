from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""grid-container grid-container-padded""",
                    data=(
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-12 cell""",
                                    data=(
                                        Table(
                                            classs="""table-expand""",
                                            data=(
                                                Thead(
                                                    data=(
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data=(
                                                                Th(
                                                                    width="""200""",
                                                                    data=("""Date""",),
                                                                ),
                                                                Th(
                                                                    data=(
                                                                        """Number of items""",
                                                                    )
                                                                ),
                                                                Th(
                                                                    classs="""text-right""",
                                                                    width="""150""",
                                                                    data=(
                                                                        """Amount""",
                                                                    ),
                                                                ),
                                                                Th(
                                                                    width="""150""",
                                                                    data=(
                                                                        """Status""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                ),
                                                Tbody(
                                                    data=(
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """August 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """2 items""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.50""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """in progress """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """July 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """4 items""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$1.30""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """scheduled """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """June 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=("""1 item""",)
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.10""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=("""May 15""",)
                                                                ),
                                                                Td(
                                                                    data=("""1 item""",)
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.10""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """April 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=("""1 item""",)
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.10""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """March 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=("""1 item""",)
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.10""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """February 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """2 items""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$1.20""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """paid """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """January 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """5 items""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.50""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row""",
                                                            data_open_details="",
                                                            data=(
                                                                Td(
                                                                    data=(
                                                                        """December 15""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """2 items""",
                                                                    )
                                                                ),
                                                                Td(
                                                                    classs="""text-right""",
                                                                    data=("""$0.20""",),
                                                                ),
                                                                Td(
                                                                    data=(
                                                                        """carried over """,
                                                                        Span(
                                                                            classs="""expand-icon""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Tr(
                                                            classs="""table-expand-row-content""",
                                                            data=(
                                                                Td(
                                                                    colspan="""8""",
                                                                    classs="""table-expand-row-nested""",
                                                                    data=(
                                                                        P(
                                                                            data=(
                                                                                """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque unde quaerat reprehenderit ipsa ipsam, adipisci facere repellendus impedit at, quisquam dicta optio veniam quia nesciunt, inventore quod in neque magni?""",
                                                                            )
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
                    ),
                ),
            )
        ),
    )
)
