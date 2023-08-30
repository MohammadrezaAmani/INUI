from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row""",
                    data=(
                        Div(
                            classs="""columns""",
                            data=(
                                """
    {{> polls}}
  """,
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
