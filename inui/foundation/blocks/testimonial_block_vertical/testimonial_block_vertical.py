from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""testimonial-block-vertical""",
                    data=(
                        Div(
                            classs="""testimonial-block-vertical-quote""",
                            data=(
                                P(
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultrices, elit sed faucibus pharetra, diam mauris bibendum orci, sit amet ullamcorper purus dui sit amet augue. Donec aliquet diam ut neque mattis, eu tristique sem rutrum.""",
                                    )
                                ),
                            ),
                        ),
                        Div(
                            classs="""testimonial-block-vertical-person""",
                            data=(
                                Img(
                                    classs="""testimonial-block-vertical-avatar""",
                                    src="""https://placehold.it/60""",
                                    alt="",
                                ),
                                Div(
                                    data=(
                                        P(
                                            classs="""testimonial-block-vertical-name""",
                                            data=("""John Doe""",),
                                        ),
                                        P(
                                            classs="""testimonial-block-vertical-info""",
                                            data=(
                                                """Important person, some Company""",
                                            ),
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
