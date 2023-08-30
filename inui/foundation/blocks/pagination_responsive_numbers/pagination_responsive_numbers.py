from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""pagination text-center""",
                    role="""navigation""",
                    aria_lable="""Pagination""",
                    data_page="""6""",
                    data_total="""16""",
                    data=(
                        Li(
                            classs="""pagination-previous disabled""",
                            data=(
                                """Previous """,
                                Span(classs="""show-for-sr""", data=("""page""",)),
                            ),
                        ),
                        Li(
                            classs="""current""",
                            data=(
                                Span(
                                    classs="""show-for-sr""",
                                    data=("""You're on page""",),
                                ),
                            ),
                        ),
                        Li(
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Page 2""",
                                    data=("""2""",),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Page 3""",
                                    data=("""3""",),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Page 4""",
                                    data=("""4""",),
                                ),
                            )
                        ),
                        Li(
                            classs="""ellipsis""",
                            aria_hidden="""true""",
                        ),
                        Li(
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Page 12""",
                                    data=("""12""",),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Page 13""",
                                    data=("""13""",),
                                ),
                            )
                        ),
                        Li(
                            classs="""pagination-next""",
                            data=(
                                A(
                                    href="""#""",
                                    aria_lable="""Next page""",
                                    data=(
                                        """Next """,
                                        Span(
                                            classs="""show-for-sr""", data=("""page""",)
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
