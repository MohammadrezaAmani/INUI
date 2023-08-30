from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Form(
                    classs="""show-password""",
                    data=(
                        Label(forr="""username""", data=("""Your login""",)),
                        Input(
                            typee="""text""",
                            value="",
                            placeholder="""Enter Username""",
                            id="""username""",
                        ),
                        Div(
                            classs="""password-wrapper""",
                            data=(
                                Label(forr="""password""", data=("""Your password""",)),
                                Input(
                                    typee="""password""",
                                    value="",
                                    placeholder="""Enter Password""",
                                    id="""password""",
                                    classs="""password""",
                                ),
                                Button(
                                    classs="""unmask""",
                                    typee="""button""",
                                    title="""Mask/Unmask password to check content""",
                                    data=("""Unmask""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
