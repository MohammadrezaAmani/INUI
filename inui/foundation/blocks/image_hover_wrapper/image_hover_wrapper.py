from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""image-hover-wrapper""",
                    data=(
                        Span(
                            classs="""image-hover-wrapper-banner""",
                            data=("""Old Junky Bikes""",),
                        ),
                        A(
                            href="""#""",
                            data=(
                                Img(
                                    src="""https://images.pexels.com/photos/163704/bike-old-wheel-two-wheeled-vehicle-163704.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb""",
                                ),
                                Span(
                                    classs="""image-hover-wrapper-reveal""",
                                    data=(
                                        P(
                                            data=(
                                                """Check it""",
                                                Br(),
                                                I(
                                                    classs="""fa fa-link""",
                                                    aria_hidden="""true""",
                                                ),
                                            )
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
