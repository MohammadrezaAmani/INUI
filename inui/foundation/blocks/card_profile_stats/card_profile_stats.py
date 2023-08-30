from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card-profile-stats""",
                    data=(
                        Div(
                            classs="""card-profile-stats-intro""",
                            data=(
                                Img(
                                    classs="""card-profile-stats-intro-pic""",
                                    src="""https://pbs.twimg.com/profile_images/732634911761260544/OxHbNdTF.jpg""",
                                    alt="""profile-image""",
                                ),
                                Div(
                                    classs="""card-profile-stats-intro-content""",
                                    data=(
                                        H3(data=("""Joe Smith""",)),
                                        P(data=("""Joined Jan.16th 2017""",)),
                                    ),
                                ),
                            ),
                        ),
                        Hr(),
                        Div(
                            classs="""card-profile-stats-container""",
                            data=(
                                Div(
                                    classs="""card-profile-stats-statistic""",
                                    data=(
                                        Span(classs="""stat""", data=("""25""",)),
                                        P(data=("""posts""",)),
                                    ),
                                ),
                                Div(
                                    classs="""card-profile-stats-statistic""",
                                    data=(
                                        Span(classs="""stat""", data=("""125""",)),
                                        P(data=("""followers""",)),
                                    ),
                                ),
                                Div(
                                    classs="""card-profile-stats-statistic""",
                                    data=(
                                        Span(classs="""stat""", data=("""88""",)),
                                        P(data=("""likes""",)),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-profile-stats-more""",
                            data=(
                                P(
                                    classs="""card-profile-stats-more-link""",
                                    data=(
                                        A(
                                            href="""#""",
                                            data=(
                                                I(
                                                    classs="""fa fa-angle-down""",
                                                    aria_hidden="""true""",
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""card-profile-stats-more-content""",
                                    data=(
                                        P(
                                            data=(
                                                """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatem libero fugit, pariatur maxime! Optio enim, deserunt quia molestiae fugiat delectus, dolore et esse nostrum, quod autem necessitatibus fugit soluta repellendus.
      """,
                                            )
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
