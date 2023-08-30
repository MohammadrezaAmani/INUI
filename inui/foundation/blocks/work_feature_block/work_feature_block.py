from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""work-feature-block row""",
                    data=(
                        Div(
                            classs="""columns medium-7""",
                            data=(
                                Img(
                                    classs="""work-feature-block-image""",
                                    src="""https://placehold.it/600x400""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""columns medium-5""",
                            data=(
                                H2(
                                    classs="""work-feature-block-header""",
                                    data=("""Project Description""",),
                                ),
                                P(
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sodales diam ac hendrerit aliquet. Phasellus pretium libero vel molestie maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam quis est quam. Aenean blandit a urna laoreet tincidunt.""",
                                    )
                                ),
                                H2(data=("""Project Details""",)),
                                Ul(
                                    data=(
                                        Li(data=("""Item 1""",)),
                                        Li(data=("""Item 2""",)),
                                        Li(data=("""Item 3""",)),
                                        Li(data=("""Item 4""",)),
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
