from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""bar-graph""",
                    data=(
                        Li(
                            classs="""bar-graph-axis""",
                            data=(
                                Div(classs="""bar-graph-label""", data=("""100%""",)),
                                Div(classs="""bar-graph-label""", data=("""80%""",)),
                                Div(classs="""bar-graph-label""", data=("""60%""",)),
                                Div(classs="""bar-graph-label""", data=("""40%""",)),
                                Div(classs="""bar-graph-label""", data=("""20%""",)),
                                Div(classs="""bar-graph-label""", data=("""0%""",)),
                            ),
                        ),
                        Li(
                            classs="""bar primary""",
                            style="""height: 95%;""",
                            title="""95""",
                            data=(
                                Div(
                                    classs="""percent""",
                                    data=(
                                        """95""",
                                        Span(data=("""%""",)),
                                    ),
                                ),
                                Div(classs="""description""", data=("""Yetis""",)),
                            ),
                        ),
                        Li(
                            classs="""bar secondary""",
                            style="""height: 90%;""",
                            title="""90""",
                            data=(
                                Div(
                                    classs="""percent""",
                                    data=(
                                        """90""",
                                        Span(data=("""%""",)),
                                    ),
                                ),
                                Div(classs="""description""", data=("""ZURBians""",)),
                            ),
                        ),
                        Li(
                            classs="""bar success""",
                            style="""height: 80%;""",
                            title="""80""",
                            data=(
                                Div(
                                    classs="""percent""",
                                    data=(
                                        """80""",
                                        Span(data=("""%""",)),
                                    ),
                                ),
                                Div(classs="""description""", data=("""Cows""",)),
                            ),
                        ),
                        Li(
                            classs="""bar warning""",
                            style="""height: 75%;""",
                            title="""75""",
                            data=(
                                Div(
                                    classs="""percent""",
                                    data=(
                                        """75""",
                                        Span(data=("""%""",)),
                                    ),
                                ),
                                Div(
                                    classs="""description""",
                                    data=("""Cows that think they're Yetis""",),
                                ),
                            ),
                        ),
                        Li(
                            classs="""bar alert""",
                            style="""height: 40%;""",
                            title="""40""",
                            data=(
                                Div(
                                    classs="""percent""",
                                    data=(
                                        """40""",
                                        Span(data=("""%""",)),
                                    ),
                                ),
                                Div(classs="""description""", data=("""Who knows""",)),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
