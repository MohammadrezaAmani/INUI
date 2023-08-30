from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Button(
                    data_addcart="",
                    classs="""button button-add-cart""",
                    data=(Span(data=("""Add To Cart""",)),),
                ),
                Div(
                    data_successmessage="",
                    classs="""callout success hide""",
                    data=(
                        """
    Added to cart, Yay!
  """,
                    ),
                ),
            )
        ),
    )
)
