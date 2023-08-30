from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""mobile-container off-canvas-wrapper""",
                    data=(
                        """
  {{> mobile-action-sheet}}
""",
                    ),
                ),
            )
        ),
    )
)
