from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""contact-panel""",
                    id="""contact-panel""",
                    data_toggler=""".is-active""",
                    data=(
                        A(
                            classs="""contact-panel-button""",
                            data_toggle="""contact-panel""",
                            data=("""Contact us""",),
                        ),
                        Form(
                            action="",
                            data=(
                                Div(
                                    classs="""row""",
                                    data=(
                                        Label(
                                            data=(
                                                """Full name *
        """,
                                                Input(
                                                    typee="""text""",
                                                    placeholder="""Full name""",
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row""",
                                    data=(
                                        Label(
                                            data=(
                                                """Email *
        """,
                                                Input(
                                                    typee="""email""",
                                                    placeholder="""Email address""",
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""row""",
                                    data=(
                                        Label(
                                            data=(
                                                """Message *
        """,
                                                Textarea(
                                                    placeholder="""Describe your needs""",
                                                    rows="""3""",
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""contact-panel-actions""",
                                    data=(
                                        Button(
                                            classs="""cancel-button""",
                                            data_toggle="""contact-panel""",
                                            data=("""Nevermind""",),
                                        ),
                                        Input(
                                            typee="""submit""",
                                            classs="""button submit-button""",
                                            value="""Submit""",
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
