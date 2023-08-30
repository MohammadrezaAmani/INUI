from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""dropdown menu""",
                    data_dropdown_menu="",
                    id="""primary-menu""",
                    data=(
                        Li(
                            data=(
                                A(href="""#""", data=("""Item 1""",)),
                                Ul(
                                    classs="""menu""",
                                    data=(
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""Item 1A""",)),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""Item 1A""",)),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""Item 1A""",)),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(href="""#""", data=("""Item 1A""",)),
                                            )
                                        ),
                                    ),
                                ),
                            )
                        ),
                        Li(data=(A(href="""#""", data=("""Item 2""",)),)),
                        Li(data=(A(href="""#""", data=("""Item 3""",)),)),
                        Li(data=(A(href="""#""", data=("""Item 4""",)),)),
                    ),
                ),
            )
        ),
    )
)
