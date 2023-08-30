from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                P(
                    data=(
                        """{{> responsive-sticky-menu }}

""",
                    )
                ),
                Div(
                    classs="""grid-container""",
                    data=(
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-12 cell""",
                                    data=(
                                        H1(
                                            data=(
                                                """Welcome to Foundation for Sites""",
                                            )
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-12 cell""",
                                    data=(
                                        Div(
                                            classs="""callout""",
                                            data=(
                                                H3(
                                                    data=(
                                                        """We’re stoked you want to try Foundation! """,
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """To get going, this file (index.html) includes some basic styles you can modify, play around with, or totally destroy to get going.""",
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """Once you've exhausted the fun in this document, you should check out:""",
                                                    )
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://get.foundation/docs""",
                                                                            data=(
                                                                                """Foundation Documentation""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://zurb.com/university/code-skills""",
                                                                            data=(
                                                                                """Foundation Code Skills""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://foundation.discourse.group""",
                                                                            data=(
                                                                                """Foundation Forum""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 medium-push-2 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://github.com/zurb/foundation""",
                                                                            data=(
                                                                                """Foundation on Github""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 medium-pull-2 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://twitter.com/ZURBfoundation""",
                                                                            data=(
                                                                                """@zurbfoundation""",
                                                                            ),
                                                                        ),
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
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-8 medium-8 cell""",
                                    data=(
                                        H5(data=("""Here’s your basic grid:""",)),
                                        Div(
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-12 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        Strong(
                                                                            data=(
                                                                                """This is a twelve column section in a grid-x with grid-margin-x.""",
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
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-6 medium-6 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Six cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-6 medium-6 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Six cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Hr(),
                                        H5(
                                            data=(
                                                """We bet you’ll need a form somewhere:""",
                                            )
                                        ),
                                        Form(
                                            data=(
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-12.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-4.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-4.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Div(
                                                                    classs="""grid-x grid-margin-x collapse""",
                                                                    data=(
                                                                        Label(
                                                                            data=(
                                                                                """Input Label""",
                                                                            )
                                                                        ),
                                                                        Div(
                                                                            classs="""input-group""",
                                                                            data=(
                                                                                Input(
                                                                                    classs="""input-group-field""",
                                                                                    typee="""text""",
                                                                                    placeholder="""input-group""",
                                                                                ),
                                                                                Span(
                                                                                    classs="""input-group-label""",
                                                                                    data=(
                                                                                        """.com""",
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
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Select Box""",
                                                                    )
                                                                ),
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""husker""",
                                                                            data=(
                                                                                """Husker""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""starbuck""",
                                                                            data=(
                                                                                """Starbuck""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""hotdog""",
                                                                            data=(
                                                                                """Hot Dog""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""apollo""",
                                                                            data=(
                                                                                """Apollo""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-6 medium-6 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Choose Your Favorite""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""radio""",
                                                                    name="""pokemon""",
                                                                    value="""Red""",
                                                                    id="""pokemonRed""",
                                                                ),
                                                                Label(
                                                                    forr="""pokemonRed""",
                                                                    data=(
                                                                        """Radio 1""",
                                                                    ),
                                                                ),
                                                                Input(
                                                                    typee="""radio""",
                                                                    name="""pokemon""",
                                                                    value="""Blue""",
                                                                    id="""pokemonBlue""",
                                                                ),
                                                                Label(
                                                                    forr="""pokemonBlue""",
                                                                    data=(
                                                                        """Radio 2""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-6 medium-6 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Check these out""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    id="""checkbox1""",
                                                                    typee="""checkbox""",
                                                                ),
                                                                Label(
                                                                    forr="""checkbox1""",
                                                                    data=(
                                                                        """Checkbox 1""",
                                                                    ),
                                                                ),
                                                                Input(
                                                                    id="""checkbox2""",
                                                                    typee="""checkbox""",
                                                                ),
                                                                Label(
                                                                    forr="""checkbox2""",
                                                                    data=(
                                                                        """Checkbox 2""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Textarea Label""",
                                                                    )
                                                                ),
                                                                Textarea(
                                                                    placeholder="""small-12.cell""",
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
                                    classs="""large-4 medium-4 cell""",
                                    data=(
                                        H5(data=("""Try one of these buttons:""",)),
                                        P(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    classs="""small button""",
                                                    data=("""Simple Button""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium success button""",
                                                    data=("""Success Btn""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium alert button""",
                                                    data=("""Alert Btn""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium secondary button""",
                                                    data=("""Secondary Btn""",),
                                                ),
                                            )
                                        ),
                                        Div(
                                            classs="""callout""",
                                            data=(
                                                H5(
                                                    data=(
                                                        """So many components, girl!""",
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """A whole kitchen sink of goodies comes with Foundation. Check out the docs to see them all, along with details on making them your own.""",
                                                    )
                                                ),
                                                A(
                                                    href="""https://get.foundation/docs/""",
                                                    classs="""small button""",
                                                    data=("""Go to Foundation Docs""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-12 cell""",
                                    data=(
                                        H1(
                                            data=(
                                                """Welcome to Foundation for Sites""",
                                            )
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-12 cell""",
                                    data=(
                                        Div(
                                            classs="""callout""",
                                            data=(
                                                H3(
                                                    data=(
                                                        """We’re stoked you want to try Foundation! """,
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """To get going, this file (index.html) includes some basic styles you can modify, play around with, or totally destroy to get going.""",
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """Once you've exhausted the fun in this document, you should check out:""",
                                                    )
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://get.foundation/docs""",
                                                                            data=(
                                                                                """Foundation Documentation""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://zurb.com/university/code-skills""",
                                                                            data=(
                                                                                """Foundation Code Skills""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://foundation.discourse.group""",
                                                                            data=(
                                                                                """Foundation Forum""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 medium-push-2 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://github.com/zurb/foundation""",
                                                                            data=(
                                                                                """Foundation on Github""",
                                                                            ),
                                                                        ),
                                                                        Br(),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 medium-pull-2 cell""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        A(
                                                                            href="""https://twitter.com/ZURBfoundation""",
                                                                            data=(
                                                                                """@zurbfoundation""",
                                                                            ),
                                                                        ),
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
                        Div(
                            classs="""grid-x grid-margin-x""",
                            data=(
                                Div(
                                    classs="""large-8 medium-8 cell""",
                                    data=(
                                        H5(data=("""Here’s your basic grid:""",)),
                                        Div(
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-12 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        Strong(
                                                                            data=(
                                                                                """This is a twelve column section in a grid-x with grid-margin-x.""",
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
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-6 medium-6 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Six cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-6 medium-6 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Six cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""grid-x grid-margin-x""",
                                            data=(
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""large-4 medium-4 small-4 cell""",
                                                    data=(
                                                        Div(
                                                            classs="""primary callout""",
                                                            data=(
                                                                P(
                                                                    data=(
                                                                        """Four cell""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Hr(),
                                        H5(
                                            data=(
                                                """We bet you’ll need a form somewhere:""",
                                            )
                                        ),
                                        Form(
                                            data=(
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-12.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-4.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Input Label""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""text""",
                                                                    placeholder="""large-4.cell""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-4 medium-4 cell""",
                                                            data=(
                                                                Div(
                                                                    classs="""grid-x grid-margin-x collapse""",
                                                                    data=(
                                                                        Label(
                                                                            data=(
                                                                                """Input Label""",
                                                                            )
                                                                        ),
                                                                        Div(
                                                                            classs="""input-group""",
                                                                            data=(
                                                                                Input(
                                                                                    classs="""input-group-field""",
                                                                                    typee="""text""",
                                                                                    placeholder="""input-group""",
                                                                                ),
                                                                                Span(
                                                                                    classs="""input-group-label""",
                                                                                    data=(
                                                                                        """.com""",
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
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Select Box""",
                                                                    )
                                                                ),
                                                                Select(
                                                                    data=(
                                                                        Option(
                                                                            value="""husker""",
                                                                            data=(
                                                                                """Husker""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""starbuck""",
                                                                            data=(
                                                                                """Starbuck""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""hotdog""",
                                                                            data=(
                                                                                """Hot Dog""",
                                                                            ),
                                                                        ),
                                                                        Option(
                                                                            value="""apollo""",
                                                                            data=(
                                                                                """Apollo""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-6 medium-6 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Choose Your Favorite""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    typee="""radio""",
                                                                    name="""pokemon""",
                                                                    value="""Red""",
                                                                    id="""pokemonRed""",
                                                                ),
                                                                Label(
                                                                    forr="""pokemonRed""",
                                                                    data=(
                                                                        """Radio 1""",
                                                                    ),
                                                                ),
                                                                Input(
                                                                    typee="""radio""",
                                                                    name="""pokemon""",
                                                                    value="""Blue""",
                                                                    id="""pokemonBlue""",
                                                                ),
                                                                Label(
                                                                    forr="""pokemonBlue""",
                                                                    data=(
                                                                        """Radio 2""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""large-6 medium-6 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Check these out""",
                                                                    )
                                                                ),
                                                                Input(
                                                                    id="""checkbox1""",
                                                                    typee="""checkbox""",
                                                                ),
                                                                Label(
                                                                    forr="""checkbox1""",
                                                                    data=(
                                                                        """Checkbox 1""",
                                                                    ),
                                                                ),
                                                                Input(
                                                                    id="""checkbox2""",
                                                                    typee="""checkbox""",
                                                                ),
                                                                Label(
                                                                    forr="""checkbox2""",
                                                                    data=(
                                                                        """Checkbox 2""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""grid-x grid-margin-x""",
                                                    data=(
                                                        Div(
                                                            classs="""large-12 cell""",
                                                            data=(
                                                                Label(
                                                                    data=(
                                                                        """Textarea Label""",
                                                                    )
                                                                ),
                                                                Textarea(
                                                                    placeholder="""small-12.cell""",
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
                                    classs="""large-4 medium-4 cell""",
                                    data=(
                                        H5(data=("""Try one of these buttons:""",)),
                                        P(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    classs="""small button""",
                                                    data=("""Simple Button""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium success button""",
                                                    data=("""Success Btn""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium alert button""",
                                                    data=("""Alert Btn""",),
                                                ),
                                                Br(),
                                                A(
                                                    href="""#""",
                                                    classs="""medium secondary button""",
                                                    data=("""Secondary Btn""",),
                                                ),
                                            )
                                        ),
                                        Div(
                                            classs="""callout""",
                                            data=(
                                                H5(
                                                    data=(
                                                        """So many components, girl!""",
                                                    )
                                                ),
                                                P(
                                                    data=(
                                                        """A whole kitchen sink of goodies comes with Foundation. Check out the docs to see them all, along with details on making them your own.""",
                                                    )
                                                ),
                                                A(
                                                    href="""https://get.foundation/docs/""",
                                                    classs="""small button""",
                                                    data=("""Go to Foundation Docs""",),
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
