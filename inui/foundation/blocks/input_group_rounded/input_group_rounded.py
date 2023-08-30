from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""input-group input-group-rounded""",
                    data=(
                        Input(
                            classs="""input-group-field""",
                            typee="""search""",
                        ),
                        Div(
                            classs="""input-group-button""",
                            data=(
                                Input(
                                    typee="""submit""",
                                    classs="""button secondary""",
                                    value="""Search""",
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
