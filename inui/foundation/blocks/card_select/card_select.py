from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card card-select""",
                    data_cardselect="",
                    data=(
                        Div(
                            classs="""card-divider""",
                            data=(
                                """
    Abby the Cat
  """,
                            ),
                        ),
                        Img(
                            src="""https://placeimg.com/640/480/animals""",
                        ),
                        Div(
                            classs="""card-section""",
                            data=(
                                H5(data=("""I need a new home!""",)),
                                P(
                                    data=(
                                        """Abby loves long naps in the sun, the laser game, and low-fat milk. She is also a great bug exterminator!""",
                                    )
                                ),
                            ),
                        ),
                        Button(
                            classs="""button""",
                            data_cardselectbutton="",
                        ),
                    ),
                ),
            )
        ),
    )
)
