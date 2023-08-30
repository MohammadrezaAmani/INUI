from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""featured-items""",
                    data=(
                        Div(
                            classs="""row align-middle align-justify featured-items-wrapper""",
                            data=(
                                H4(
                                    classs="""featured-items-title""",
                                    data=("""As Featured In:""",),
                                ),
                                Div(
                                    classs="""featured-items-brands""",
                                    data=(
                                        Img(
                                            src="""https://placehold.it/150x70""",
                                        ),
                                        Img(
                                            src="""https://placehold.it/125x60""",
                                        ),
                                        Img(
                                            src="""https://placehold.it/150x70""",
                                        ),
                                        Img(
                                            src="""https://placehold.it/130x50""",
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
