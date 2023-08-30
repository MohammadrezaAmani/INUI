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
                            classs="""product-details column medium-6 center-text-for-small-only""",
                            data=(
                                H1(data=("""Product Name""",)),
                                P(
                                    classs="""product-description""",
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas id magna ac quam semper.deta""",
                                    ),
                                ),
                                Div(
                                    classs="""row""",
                                    data=(
                                        Div(
                                            classs="""column small-12 large-6""",
                                            data=(
                                                H6(
                                                    classs="""product-color-title""",
                                                    data=("""Colors""",),
                                                ),
                                                Form(
                                                    classs="""product-option-selection""",
                                                    data=(
                                                        Input(
                                                            typee="""radio""",
                                                            name="""radios""",
                                                            value="""red""",
                                                            id="""radio1""",
                                                            checked="""checked""",
                                                        ),
                                                        Label(
                                                            forr="""radio1""",
                                                            classs=""" dark-hollow expand""",
                                                            data=(
                                                                Img(
                                                                    src="""https://placehold.it/30x30""",
                                                                ),
                                                            ),
                                                        ),
                                                        Input(
                                                            typee="""radio""",
                                                            name="""radios""",
                                                            value="""blue""",
                                                            id="""radio2""",
                                                        ),
                                                        Label(
                                                            forr="""radio2""",
                                                            classs=""" dark-hollow expand""",
                                                            data=(
                                                                Img(
                                                                    src="""https://placehold.it/30x30""",
                                                                ),
                                                            ),
                                                        ),
                                                        Input(
                                                            typee="""radio""",
                                                            name="""radios""",
                                                            value="""yellow""",
                                                            id="""radio3""",
                                                        ),
                                                        Label(
                                                            forr="""radio3""",
                                                            classs=""" dark-hollow expand""",
                                                            data=(
                                                                Img(
                                                                    src="""https://placehold.it/30x30""",
                                                                ),
                                                            ),
                                                        ),
                                                        Input(
                                                            typee="""radio""",
                                                            name="""radios""",
                                                            value="""orange""",
                                                            id="""radio4""",
                                                        ),
                                                        Label(
                                                            forr="""radio4""",
                                                            classs=""" dark-hollow expand""",
                                                            data=(
                                                                Img(
                                                                    src="""https://placehold.it/30x30""",
                                                                ),
                                                            ),
                                                        ),
                                                        Input(
                                                            typee="""radio""",
                                                            name="""radios""",
                                                            value="""green""",
                                                            id="""radio5""",
                                                        ),
                                                        Label(
                                                            forr="""radio5""",
                                                            classs=""" dark-hollow expand""",
                                                            data=(
                                                                Img(
                                                                    src="""https://placehold.it/30x30""",
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""column small-12 large-6""",
                                            data=(
                                                H6(
                                                    classs="""product-color-title""",
                                                    data=("""Size""",),
                                                ),
                                                Form(
                                                    classs="""product-option-selection""",
                                                    data=(
                                                        Select(
                                                            data=(
                                                                Option(
                                                                    value="""husker""",
                                                                    data=("""Small""",),
                                                                ),
                                                                Option(
                                                                    value="""starbuck""",
                                                                    data=(
                                                                        """Medium""",
                                                                    ),
                                                                ),
                                                                Option(
                                                                    value="""hotdog""",
                                                                    data=("""Large""",),
                                                                ),
                                                                Option(
                                                                    value="""apollo""",
                                                                    data=(
                                                                        """X-Large""",
                                                                    ),
                                                                ),
                                                                Option(
                                                                    value="""apollo""",
                                                                    data=(
                                                                        """XX-Large""",
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
                                Div(
                                    classs="""product-details-add-to-cart""",
                                    data=(
                                        P(
                                            data=(
                                                Span(
                                                    classs="""in-stock""",
                                                    data=("""In Stock""",),
                                                ),
                                                Span(
                                                    classs="""dim-text""",
                                                    data=(
                                                        """(Only 3 left in Stock)""",
                                                    ),
                                                ),
                                            )
                                        ),
                                        Hr(),
                                        P(classs="""price""", data=("""$19.99""",)),
                                        P(
                                            data=(
                                                Span(data=("""Qty:""",)),
                                                Input(
                                                    classs="""qty""",
                                                    typee="""text""",
                                                    value="""1""",
                                                ),
                                            )
                                        ),
                                        Button(
                                            classs="""button expanded""",
                                            data=("""Add to Cart""",),
                                        ),
                                    ),
                                ),
                                P(
                                    classs="""shipping""",
                                    data=(
                                        """Available for Free Ground Shipping & Return""",
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
