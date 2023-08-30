from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""travel-feature-card""",
                    data=(
                        Div(
                            classs="""travel-feature-card-header{{#if type}} icon {{type}}-icon{{/if}}""",
                            data=(
                                Div(
                                    classs="""row""",
                                    data=(
                                        Div(
                                            classs="""medium-12 columns""",
                                            data=(
                                                H5(
                                                    classs="""travel-feature-card-subtitle""",
                                                    data=(
                                                        """{{#if title}}{{title}}{{else}}Hotel{{/if}}""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""travel-feature-card-header-controls""",
                                                    data=(
                                                        Span(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-edit""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Span(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        I(
                                                                            classs="""fa fa-remove""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""travel-feature-card-details""",
                            data=(
                                """
    {{#if date}}
    """,
                                H6(
                                    classs="""travel-feature-card-date-range""",
                                    data=("""{{date}}""",),
                                ),
                                Div(
                                    classs="""row""",
                                    data=(
                                        Div(
                                            classs="""small-12 medium-9 columns travel-feature-card-content""",
                                            data=(
                                                Div(
                                                    classs="""row""",
                                                    data=(
                                                        Div(
                                                            classs="""small-4 medium-2 columns""",
                                                            data=(
                                                                Img(
                                                                    classs="""travel-feature-card-image""",
                                                                    src="""https://unsplash.it/600/600/?image=1081""",
                                                                    alt="",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""small-8 medium-10 columns""",
                                                            data=(
                                                                H6(
                                                                    classs="""travel-feature-card-title""",
                                                                    data=(
                                                                        """New York Royale""",
                                                                    ),
                                                                ),
                                                                P(
                                                                    data=(
                                                                        """The rooms and suites have free WiFi and flat-screen TVs. Upgrades include outdoor decks with the gorgeous Manhattan views, 24-hour room service, and  cocktail bars.""",
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""small-12 medium-3 columns travel-feature-card-price""",
                                            data=(
                                                H6(data=("""$2,000.00""",)),
                                                P(
                                                    classs="""travel-feature-card-price-subtext""",
                                                    data=("""2 adults for 2 nights""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
