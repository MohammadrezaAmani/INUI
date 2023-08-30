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
                            classs="""large-6 columns""",
                            data=(
                                """
    {{> comment-section}}
  """,
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
