from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Header(
                    classs="""portfolio-hero-header""",
                    data=(
                        Img(
                            classs="""portfolio-hero-header-logo""",
                            src="""https://placehold.it/200""",
                        ),
                        H1(
                            classs="""portfolio-hero-header-h1""",
                            data=("""My Portfolio""",),
                        ),
                        Ul(
                            classs="""portfolio-hero-header-description""",
                            data=(
                                Li(data=("""Portfolio Example""",)),
                                Li(data=("""Super Clean""",)),
                                Li(data=("""Super Simple""",)),
                            ),
                        ),
                        Ul(
                            classs="""portfolio-hero-header-menu""",
                            data=(
                                Li(
                                    data=(
                                        A(
                                            classs="""button primary""",
                                            href="""#""",
                                            data=("""Link 1""",),
                                        ),
                                    )
                                ),
                                Li(
                                    data=(
                                        A(
                                            classs="""button primary""",
                                            href="""#""",
                                            data=("""Link 2""",),
                                        ),
                                    )
                                ),
                                Li(
                                    data=(
                                        A(
                                            classs="""button primary""",
                                            href="""#""",
                                            data=("""Link 3""",),
                                        ),
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
