from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                P(
                    data=(
                        """{{#repeat 20}}
""",
                    )
                ),
                P(
                    data=(
                        """
  The signup bar is stuck until you scroll past me
""",
                    )
                ),
                P(
                    data=(
                        """
  Sticky will now be in the page.
""",
                    )
                ),
            )
        ),
    )
)
