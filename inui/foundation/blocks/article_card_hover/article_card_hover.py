from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card-article-hover card""",
                    data=(
                        A(
                            href="",
                            data=(
                                Img(
                                    src="""https://unsplash.it/600/400""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-section""",
                            data=(
                                P(
                                    classs="""meta-data article-subtext""",
                                    data=("""GARDENING | 10 MIN READ""",),
                                ),
                                A(
                                    href="",
                                    data=(
                                        H3(
                                            classs="""article-title""",
                                            data=(
                                                """Succulents, how much water do they need?""",
                                            ),
                                        ),
                                    ),
                                ),
                                P(
                                    classs="""article-desc""",
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos corporis autem, iusto impedit veniam unde earum neque...""",
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-divider flex-container align-middle""",
                            data=(
                                Img(
                                    classs="""avatar""",
                                    src="""https://placehold.it/50x50""",
                                    alt="""avatar""",
                                ),
                                A(
                                    href="",
                                    classs="""author""",
                                    data=("""BEAN MCGRUBER""",),
                                ),
                            ),
                        ),
                        Div(classs="""hover-border""", data=()),
                    ),
                ),
            )
        ),
    )
)
