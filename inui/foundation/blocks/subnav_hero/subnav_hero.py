from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Header(
                    classs="""subnav-hero-section""",
                    data=(
                        H1(
                            classs="""subnav-hero-headline""",
                            data=(
                                """Foundation """,
                                Small(data=("""by ZURB""",)),
                            ),
                        ),
                        Ul(
                            classs="""subnav-hero-subnav""",
                            data=(
                                Li(data=(A(href="""#""", data=("""Take Action!""",)),)),
                                Li(
                                    data=(
                                        A(
                                            href="""#""",
                                            classs="""is-active""",
                                            data=("""Carpe Diem!""",),
                                        ),
                                    )
                                ),
                                Li(
                                    data=(
                                        A(
                                            target="""_blank""",
                                            href="""https://zurb.com/responsive""",
                                            data=("""Just do it!""",),
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
