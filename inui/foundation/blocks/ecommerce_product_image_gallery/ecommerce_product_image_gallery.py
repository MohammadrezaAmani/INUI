from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row align-center""",
                    data=(
                        Div(
                            classs="""product-image-gallery""",
                            data=(
                                Img(
                                    classs="""pdp-product-image""",
                                    id="""main-product-image""",
                                    src="""https://placehold.it/350x350?text=Image+1""",
                                    alt="",
                                ),
                                Br(),
                                Ul(
                                    classs="""menu product-thumbs align-center""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    classs="""sim-thumb""",
                                                    data_image="""https://placehold.it/350x350?text=Image+1""",
                                                    data=(
                                                        Img(
                                                            src="""https://placehold.it/50x50""",
                                                            alt="",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""sim-thumb""",
                                                    data_image="""https://placehold.it/350x350?text=Image+2""",
                                                    data=(
                                                        Img(
                                                            src="""https://placehold.it/50x50""",
                                                            alt="",
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""sim-thumb""",
                                                    data_image="""https://placehold.it/350x350?text=Image+3""",
                                                    data=(
                                                        Img(
                                                            src="""https://placehold.it/50x50""",
                                                            alt="",
                                                        ),
                                                    ),
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
