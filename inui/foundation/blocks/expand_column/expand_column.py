from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""row expand-column-wrapper""",
                    data=(
                        Div(
                            classs="""column""",
                            data=(
                                P(
                                    classs="""expand-column-content""",
                                    data=("""Hello there.""",),
                                ),
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                P(
                                    classs="""expand-column-content""",
                                    data=("""If you hover""",),
                                ),
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                P(
                                    classs="""expand-column-content""",
                                    data=("""over each section""",),
                                ),
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                P(
                                    classs="""expand-column-content""",
                                    data=("""a couple of words""",),
                                ),
                            ),
                        ),
                        Div(
                            classs="""column""",
                            data=(
                                P(
                                    classs="""expand-column-content""",
                                    data=("""will appear""",),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
