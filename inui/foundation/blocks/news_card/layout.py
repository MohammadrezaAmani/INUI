from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row small-up-1 medium-up-3""",
                    data=(
                        Div(
                            classs="""column""",
                            data=(
                                """
    {{> news-card}}
  """,
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                """
    {{> news-card}}
  """,
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                """
    {{> news-card}}
  """,
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
