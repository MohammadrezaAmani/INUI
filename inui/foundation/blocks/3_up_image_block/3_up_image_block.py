from inui.elements import *
from inui.svg import *

Html(
    data=(
        Head(
            data=(
                Link(
                    href="""https://fonts.googleapis.com/css?family=Sanchez""",
                    rel="""stylesheet""",
                ),
            )
        ),
        Body(
            data=(
                Div(
                    classs="""row main-links""",
                    data=(
                        Div(
                            classs="""small-12 medium-4 columns""",
                            data=(
                                Div(
                                    classs="""title-box""",
                                    data=(
                                        H4(
                                            classs="""title-box-title""",
                                            data=("""Image 1""",),
                                        ),
                                    ),
                                ),
                                Img(
                                    src="""https://placehold.it/400x300""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""small-12 medium-4 columns""",
                            data=(
                                Div(
                                    classs="""title-box""",
                                    data=(
                                        H4(
                                            classs="""title-box-title""",
                                            data=("""Image 2""",),
                                        ),
                                    ),
                                ),
                                Img(
                                    src="""https://placehold.it/400x300""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""small-12 medium-4 columns""",
                            data=(
                                Div(
                                    classs="""title-box""",
                                    data=(
                                        H4(
                                            classs="""title-box-title""",
                                            data=("""Image 3""",),
                                        ),
                                    ),
                                ),
                                Img(
                                    src="""https://placehold.it/400x300""",
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
