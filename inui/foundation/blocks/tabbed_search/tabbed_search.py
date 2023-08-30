from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row""",
                    data=(
                        Div(
                            classs="""medium-12 columns""",
                            data=(
                                Ul(
                                    classs="""tabbed-search tabs""",
                                    data_tabs="",
                                    id="""tabbed-search""",
                                    data=(
                                        Li(
                                            classs="""tabs-title is-active""",
                                            data=(
                                                A(
                                                    href="""#panel1""",
                                                    data=("""Flights""",),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""tabs-title""",
                                            data=(
                                                A(
                                                    href="""#panel2""",
                                                    data=("""Hotels""",),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""tabs-title""",
                                            data=(
                                                A(
                                                    href="""#panel3""",
                                                    data=("""Cars""",),
                                                ),
                                            ),
                                        ),
                                        Li(
                                            classs="""tabs-title""",
                                            data=(
                                                A(
                                                    href="""#panel4""",
                                                    aria_selected="""true""",
                                                    data=("""Packages""",),
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
                    classs="""tabbed-search-content tabs-content""",
                    data_tabs_content="""tabbed-search""",
                    data=(
                        Div(
                            classs="""tabs-panel is-active""",
                            id="""panel1""",
                            data=(
                                Form(
                                    data=(
                                        Div(
                                            classs="""row""",
                                            data=(
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""From""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""To""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Start Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Return Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""one""",
                                                                            data=(
                                                                                """1 person""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""two""",
                                                                            data=(
                                                                                """2 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""three""",
                                                                            data=(
                                                                                """3 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""four""",
                                                                            data=(
                                                                                """4 people""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""primary button expanded search-button""",
                                                            data=(
                                                                I(
                                                                    classs="""fa fa-search""",
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
                        Div(
                            classs="""tabs-panel""",
                            id="""panel2""",
                            data=(
                                Form(
                                    data=(
                                        Div(
                                            classs="""row""",
                                            data=(
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""From""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""To""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Start Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Return Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""one""",
                                                                            data=(
                                                                                """1 person""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""two""",
                                                                            data=(
                                                                                """2 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""three""",
                                                                            data=(
                                                                                """3 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""four""",
                                                                            data=(
                                                                                """4 people""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""primary button expanded search-button""",
                                                            data=(
                                                                I(
                                                                    classs="""fa fa-search""",
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
                        Div(
                            classs="""tabs-panel""",
                            id="""panel3""",
                            data=(
                                Form(
                                    data=(
                                        Div(
                                            classs="""row""",
                                            data=(
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""From""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""To""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Start Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Return Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""one""",
                                                                            data=(
                                                                                """1 person""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""two""",
                                                                            data=(
                                                                                """2 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""three""",
                                                                            data=(
                                                                                """3 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""four""",
                                                                            data=(
                                                                                """4 people""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""primary button expanded search-button""",
                                                            data=(
                                                                I(
                                                                    classs="""fa fa-search""",
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
                        Div(
                            classs="""tabs-panel""",
                            id="""panel4""",
                            data=(
                                Form(
                                    data=(
                                        Div(
                                            classs="""row""",
                                            data=(
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""From""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""To""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Start Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""Return Date""",
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Label(
                                                            data=(
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""one""",
                                                                            data=(
                                                                                """1 person""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""two""",
                                                                            data=(
                                                                                """2 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""three""",
                                                                            data=(
                                                                                """3 people""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""four""",
                                                                            data=(
                                                                                """4 people""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""small-12 medium-2 columns""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""primary button expanded search-button""",
                                                            data=(
                                                                I(
                                                                    classs="""fa fa-search""",
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
                    ),
                ),
            )
        ),
    )
)
