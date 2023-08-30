from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""off-canvas mobile-action-sheet off-canvas-absolute position-bottom""",
                    id="""payments-action-sheet""",
                    data_off_canvas="",
                    data=(
                        Div(
                            classs="""mobile-action-sheet-inner""",
                            data=(
                                Button(
                                    href="""#""",
                                    classs="""button action-sheet-toggle""",
                                    typee="""button""",
                                    data_toggle="",
                                    data=("""Open Action Sheet""",),
                                ),
                                Button(
                                    classs="""close-button""",
                                    aria_lable="""Close menu""",
                                    typee="""button""",
                                    data_close="",
                                    data=(
                                        Span(aria_hidden="""true""", data=("""×""",)),
                                    ),
                                ),
                                P(
                                    data=(
                                        """This action sheet can contain all sorts of things""",
                                    )
                                ),
                                H5(data=("""Content""",)),
                                P(
                                    data=(
                                        """
      Check Check it
    """,
                                    )
                                ),
                                H5(data=("""Forms""",)),
                                Form(
                                    data=(
                                        Label(
                                            data=(
                                                """Fill me out
        """,
                                                Input(
                                                    typee="""text""",
                                                ),
                                            )
                                        ),
                                    )
                                ),
                                H5(data=("""Buttons""",)),
                                Button(
                                    href="""#""",
                                    classs="""button hollow white""",
                                    data=("""Push the button""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
