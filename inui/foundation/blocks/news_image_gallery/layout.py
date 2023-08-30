from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row medium-12 large-10 columns align-center""",
                    data=(
                        """
    {{>news-image-gallery}}
  """,
                    ),
                ),
            )
        ),
    )
)
