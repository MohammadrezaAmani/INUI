from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""mobile-app-dashboard-header""",
                    data=(H1(data=("""Your Next Adventure Awaits""",)),),
                ),
                Div(
                    classs="""mobile-app-dashboard""",
                    data=(
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-plane""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""Book Flights""",)),
                                    ),
                                ),
                            ),
                        ),
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-clock-o mobile-app-dashboard-icon""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""Flight Status""",)),
                                    ),
                                ),
                            ),
                        ),
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-check-square-o""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""Check In""",)),
                                    ),
                                ),
                            ),
                        ),
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-cutlery""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""Eat Well""",)),
                                    ),
                                ),
                            ),
                        ),
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-question""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""FAQ""",)),
                                    ),
                                ),
                            ),
                        ),
                        A(
                            href="",
                            data=(
                                Div(
                                    classs="""mobile-app-dashboard-inner""",
                                    data=(
                                        I(
                                            classs="""fa fa-plus""",
                                            aria_hidden="""true""",
                                        ),
                                        Span(data=("""Miles and Benefits""",)),
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
