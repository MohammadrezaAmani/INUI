from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card""",
                    data=(
                        Img(
                            classs="""card-img""",
                            src="""https://placehold.it/350x300""",
                            alt="""header""",
                        ),
                        Div(
                            classs="""card-info""",
                            data=(
                                H1(classs="""card-title""", data=("""Card Title""",)),
                                Div(classs="""card-icon""", data=("""6""",)),
                                P(classs="""card-author""", data=("""Author Name""",)),
                                P(
                                    classs="""card-stats""",
                                    data=(
                                        """6 """,
                                        Img(
                                            src="""https://placehold.it/20""",
                                            alt="""hi""",
                                        ),
                                        Img(
                                            src="""https://placehold.it/20""",
                                            alt="""hi""",
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
