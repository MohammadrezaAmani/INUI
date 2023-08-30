from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""dashboard-number-card{{#if positive}} positive{{/if}}{{#if negative}} negative{{/if}}""",
                    data=(
                        H5(classs="""dashboard-number-value""", data=("""$20,000""",)),
                        Div(
                            data=(
                                P(
                                    classs="""dashboard-number-area""",
                                    data=("""Category""",),
                                ),
                                P(
                                    classs="""dashboard-number-delta""",
                                    data=(
                                        """
    {{#if positive}}
      """,
                                        I(
                                            classs="""fa fa-arrow-up""",
                                            aria_hidden="""true""",
                                        ),
                                        I(
                                            classs="""fa fa-arrow-down""",
                                            aria_hidden="""true""",
                                        ),
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
            )
        ),
    )
)
