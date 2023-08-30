from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row medium-12 large-6 column align-center""",
                    data=(
                        """
  {{> status-update-input-box}}
""",
                    ),
                ),
            )
        ),
    )
)
