from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Button(
                    classs="""button button-like""",
                    data=(
                        I(
                            classs="""fa fa-heart""",
                        ),
                        Span(data=("""Like""",)),
                    ),
                ),
            )
        ),
    )
)
