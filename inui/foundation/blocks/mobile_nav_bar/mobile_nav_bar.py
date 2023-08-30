from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""mobile-nav-bar title-bar""",
                    data=(
                        Div(
                            classs="""title-bar-left""",
                            data=(
                                Button(
                                    classs="""menu-icon""",
                                    typee="""button""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""title-bar-center""",
                            data=(
                                Span(
                                    classs="""title-bar-text""", data=("""My Page""",)
                                ),
                            ),
                        ),
                        Div(
                            classs="""title-bar-right""",
                            data=(
                                Span(
                                    classs="""title-bar-text""", data=("""Actions""",)
                                ),
                                Span(
                                    classs="""title-bar-text""",
                                    data=(
                                        A(
                                            href="""#""",
                                            data=(
                                                I(
                                                    classs="""fa fa-home title-bar-logo""",
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
