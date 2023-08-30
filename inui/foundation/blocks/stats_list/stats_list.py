from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""stats-list""",
                    data=(
                        Li(
                            data=(
                                """
    135 """,
                                Span(
                                    classs="""stats-list-label""", data=("""Commits""",)
                                ),
                            )
                        ),
                        Li(
                            classs="""stats-list-positive""",
                            data=(
                                """
    17,678 """,
                                Span(
                                    classs="""stats-list-label""",
                                    data=("""Additions""",),
                                ),
                            ),
                        ),
                        Li(
                            classs="""stats-list-negative""",
                            data=(
                                """
    2,390 """,
                                Span(
                                    classs="""stats-list-label""",
                                    data=("""Deletions""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
