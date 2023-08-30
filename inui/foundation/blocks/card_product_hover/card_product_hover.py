from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card card-product-hover""",
                    data=(
                        Img(
                            src="""https://zurb.com/blog/system/images/690/original/blue_bw_web.jpg?1354921642""",
                            alt="""sweet foundation shirt""",
                        ),
                        Img(
                            src="""https://2.bp.blogspot.com/-luqexZwkPcY/VPamfRCxrmI/AAAAAAAAO8s/R6YaU81Zleo/s1600/foundationzurb-theme-DownloadNewThemes.jpg""",
                            alt="""picture of admin dashboard""",
                        ),
                        Div(
                            classs="""card-product-hover-icons""",
                            data=(
                                A(
                                    href="""#""",
                                    data=(
                                        I(
                                            classs="""fa fa-shopping-cart""",
                                        ),
                                    ),
                                ),
                                A(
                                    href="""#""",
                                    data=(
                                        I(
                                            classs="""fa fa-star-o""",
                                        ),
                                    ),
                                ),
                                A(
                                    href="""#""",
                                    data=(
                                        I(
                                            classs="""fa fa-share-alt""",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-product-hover-details""",
                            data=(
                                H3(
                                    classs="""card-product-hover-title""",
                                    data=("""Legacy Foundation Tee""",),
                                ),
                                Span(
                                    classs="""card-product-hover-price""",
                                    data=("""$15.00""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
