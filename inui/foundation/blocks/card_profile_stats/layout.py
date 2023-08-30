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
                            classs="""medium-8 columns""",
                            data=(
                                """
    {{> card-profile-stats}}
  """,
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
