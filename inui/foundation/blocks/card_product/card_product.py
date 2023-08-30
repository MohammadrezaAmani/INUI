from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card card-product""",
                    data=(
                        Div(
                            classs="""card-product-img-wrapper""",
                            data=(
                                A(
                                    classs="""button expanded""",
                                    data=("""Add to Cart""",),
                                ),
                                A(
                                    href="""#""",
                                    data=(
                                        Img(
                                            src="""https://demandware.edgesuite.net/sits_pod15/dw/image/v2/AAJE_PRD/on/demandware.static/-/Sites-pacsun_storefront_catalog/default/dw2dd1a5fe/product_images/0702497750034NEW_00_165.jpg?sw=215&sh=334&sm=fit""",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-section""",
                            data=(
                                A(
                                    href="""#""",
                                    data=(
                                        H3(
                                            classs="""card-product-name""",
                                            data=("""Kickin with Kraken Tee""",),
                                        ),
                                    ),
                                ),
                                H5(
                                    classs="""card-product-price""",
                                    data=("""$19.99""",),
                                ),
                                P(
                                    classs="""card-product-description""",
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin posuere sem enim, accumsan convallis risus semper.""",
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
