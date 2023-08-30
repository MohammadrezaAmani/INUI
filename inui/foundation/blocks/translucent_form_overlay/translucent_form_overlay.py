from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""translucent-form-overlay""",
                    data=(
                        Form(
                            data=(
                                H3(data=("""Search for Properties""",)),
                                Div(
                                    classs="""row columns""",
                                    data=(
                                        Label(
                                            data=(
                                                """Keyword
        """,
                                                Input(
                                                    typee="""text""",
                                                    name="""keyword""",
                                                    placeholder="""Any""",
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row columns""",
                                    data=(
                                        Label(
                                            data=(
                                                """Property Status
        """,
                                                Select(
                                                    name="""status""",
                                                    typee="""text""",
                                                    data=(
                                                        Option(data=("""Any""",)),
                                                        Option(
                                                            value="""rent""",
                                                            data=("""Rent""",),
                                                        ),
                                                        Option(
                                                            value="""buy""",
                                                            data=("""Buy""",),
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row columns""",
                                    data=(
                                        Label(
                                            data=(
                                                """Property Type
        """,
                                                Select(
                                                    name="""status""",
                                                    typee="""text""",
                                                    data=(
                                                        Option(data=("""Any""",)),
                                                        Option(
                                                            value="""office""",
                                                            data=("""Office""",),
                                                        ),
                                                        Option(
                                                            value="""building""",
                                                            data=("""Building""",),
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row columns""",
                                    data=(
                                        Label(
                                            data=(
                                                """Location
        """,
                                                Input(
                                                    typee="""text""",
                                                    name="""location""",
                                                    placeholder="""Any""",
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row""",
                                    data=(
                                        Label(
                                            classs="""columns small-12""",
                                            data=("""Price""",),
                                        ),
                                        Div(
                                            classs="""columns small-6""",
                                            data=(
                                                Input(
                                                    typee="""number""",
                                                    min="""0""",
                                                    name="""min""",
                                                    placeholder="""Min""",
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""columns small-6""",
                                            data=(
                                                Input(
                                                    typee="""number""",
                                                    min="""0""",
                                                    name="""max""",
                                                    placeholder="""Max""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Button(
                                    typee="""button""",
                                    classs="""primary button expanded search-button""",
                                    data=(
                                        """
      Search
    """,
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
