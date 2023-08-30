from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""card-flex-article card""",
                    data=(
                        Div(
                            classs="""card-image""",
                            data=(
                                Img(
                                    src="""https://images.pexels.com/photos/132987/pexels-photo-132987.jpeg?w=940&h=650&auto=compress&cs=tinysrgb""",
                                ),
                                Span(
                                    classs="""label alert card-tag""",
                                    data=("""#Birdie""",),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-section""",
                            data=(
                                H3(
                                    classs="""article-title""",
                                    data=("""This is a card.""",),
                                ),
                                Div(
                                    classs="""article-details""",
                                    data=(
                                        Span(
                                            classs="""website""", data=("""Website""",)
                                        ),
                                        Span(classs="""time""", data=("""Time""",)),
                                        Span(
                                            classs="""author""",
                                            data=("""Author Name""",),
                                        ),
                                    ),
                                ),
                                P(
                                    classs="""article-summary""",
                                    data=(
                                        """This is a quick summary area of the first few sentences from the post. It will be a few sentences.""",
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-divider align-middle""",
                            data=(
                                Div(
                                    classs="""avatar with-add-icon""",
                                    data=(
                                        Img(
                                            src="""https://placehold.it/35""",
                                            alt="""avatar""",
                                        ),
                                        I(
                                            classs="""fa fa-plus-circle""",
                                            aria_hidden="""true""",
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""user-info""",
                                    data=(
                                        P(classs="""user-name""", data=("""Name""",)),
                                        P(
                                            classs="""category""",
                                            data=(
                                                """added to """,
                                                Strong(data=("""Category""",)),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            classs="""card-divider align-justify""",
                            data=(
                                Div(
                                    classs="""notability""",
                                    data=(
                                        Span(
                                            classs="""publications""",
                                            data=("""Publication Number""",),
                                        ),
                                        Span(classs="""likes""", data=("""# Likes""",)),
                                    ),
                                ),
                                Div(
                                    classs="""card-actions""",
                                    data=(
                                        I(
                                            classs="""fa fa-heart-o""",
                                            aria_hidden="""true""",
                                        ),
                                        I(
                                            classs="""fa fa-plus""",
                                            aria_hidden="""true""",
                                        ),
                                        I(
                                            classs="""fa fa-ellipsis-v""",
                                            aria_hidden="""true""",
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
