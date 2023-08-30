from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""pricing-table""",
                    data=(
                        Li(classs="""title""", data=("""Enterprise""",)),
                        Li(classs="""price""", data=("""$99.99""",)),
                        Li(
                            classs="""description""",
                            data=("""An awesome description""",),
                        ),
                        Li(data=("""42 Rad Features""",)),
                        Li(data=("""7GB of Power""",)),
                        Li(
                            data=(
                                A(
                                    classs="""button""",
                                    href="""#""",
                                    data=("""Buy Now""",),
                                ),
                            )
                        ),
                    ),
                ),
            )
        ),
    )
)
