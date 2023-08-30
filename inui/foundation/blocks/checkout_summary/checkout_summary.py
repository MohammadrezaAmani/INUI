from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""checkout-summary""",
                    data=(
                        Div(
                            classs="""checkout-summary-title""",
                            data=(
                                H5(data=("""Your Order""",)),
                                H5(data=("""2 Items""",)),
                            ),
                        ),
                        Div(
                            classs="""checkout-summary-item""",
                            data=(
                                Img(
                                    src="""https://placeimg.com/100/80/any""",
                                ),
                                Div(
                                    classs="""item-name""",
                                    data=(
                                        A(data=("""Comfy Knit Blazer""",)),
                                        P(
                                            data=(
                                                Span(
                                                    classs="""title""",
                                                    data=("""Color: """,),
                                                ),
                                            )
                                        ),
                                        P(
                                            data=(
                                                Span(
                                                    classs="""title""",
                                                    data=("""Size: """,),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""item-price""",
                                    data=(
                                        P(classs="""title""", data=("""$24.99""",)),
                                        A(href="""#""", data=("""Remove""",)),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""checkout-summary-item""",
                            data=(
                                Img(
                                    src="""https://placeimg.com/100/80/any""",
                                ),
                                Div(
                                    classs="""item-name""",
                                    data=(
                                        A(data=("""Comfy Knit Blazer""",)),
                                        P(
                                            data=(
                                                Span(
                                                    classs="""title""",
                                                    data=("""Color: """,),
                                                ),
                                            )
                                        ),
                                        P(
                                            data=(
                                                Span(
                                                    classs="""title""",
                                                    data=("""Size: """,),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""item-price""",
                                    data=(
                                        P(classs="""title""", data=("""$24.99""",)),
                                        A(href="""#""", data=("""Remove""",)),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""checkout-summary-details""",
                            data=(
                                Div(
                                    classs="""left""",
                                    data=(
                                        P(data=(Strong(data=("""Subtotal:""",)),)),
                                        P(data=(Strong(data=("""Tax:""",)),)),
                                        P(data=(Strong(data=("""Total:""",)),)),
                                    ),
                                ),
                                Div(
                                    classs="""right""",
                                    data=(
                                        P(data=("""$10.99""",)),
                                        P(data=("""$2.00""",)),
                                        P(data=("""$12.99""",)),
                                    ),
                                ),
                            ),
                        ),
                        Button(
                            classs="""button expanded""",
                            data=("""Proceed to Checkout""",),
                        ),
                    ),
                ),
            )
        ),
    )
)
