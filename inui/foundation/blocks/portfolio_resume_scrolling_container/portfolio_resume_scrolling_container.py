from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""portfolio-resume-scrolling-container row""",
                    data=(
                        Div(
                            classs="""columns small-12 medium-5 portfolio-resume-overview""",
                            data=(
                                Div(
                                    classs="""portfolio-resume-overview-content""",
                                    data=(
                                        H3(
                                            classs="""portfolio-resume-name""",
                                            data=("""Name""",),
                                        ),
                                        P(
                                            data=(
                                                """I'm kind of awesome. No really.""",
                                            )
                                        ),
                                        A(
                                            classs="""button primary expanded""",
                                            href="""#""",
                                            data=("""Contact Me""",),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""columns small-12 medium-7 portfolio-resume-scrolling""",
                            data=(
                                H3(data=("""SKILLS""",)),
                                Ul(
                                    classs="""portfolio-resume-side-list""",
                                    data=(
                                        Li(data=("""Foundation""",)),
                                        Li(data=("""Moar Foundation""",)),
                                        Li(data=("""SCSS""",)),
                                        Li(data=("""CSS""",)),
                                        Li(data=("""JavaScript""",)),
                                        Li(data=("""HTML""",)),
                                    ),
                                ),
                                H3(data=("""EXPERIENCE""",)),
                                P(
                                    data=(
                                        """Look at all this amazing stuff that I've done!""",
                                    )
                                ),
                                Ul(
                                    data=(
                                        Li(data=("""Just one damned thing""",)),
                                        Li(data=("""After another""",)),
                                        Li(data=("""Like history""",)),
                                        Li(data=("""One thing""",)),
                                        Li(data=("""After another""",)),
                                    )
                                ),
                                H3(data=("""WORK""",)),
                                P(data=("""I've done work too""",)),
                                Ul(
                                    data=(
                                        Li(data=("""A Site""",)),
                                        Li(data=("""Another Site""",)),
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
