from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Ul(
                    classs="""multilevel-accordion-menu vertical menu""",
                    data_accordion_menu="",
                    data=(
                        Li(
                            data=(
                                A(href="""#""", data=("""Item 1""",)),
                                Ul(
                                    classs="""menu vertical sublevel-1""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""Sub-item 1""",),
                                                ),
                                                Ul(
                                                    classs="""menu vertical sublevel-2""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 1""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 2""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 3""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""Sub-item 2""",),
                                                ),
                                                Ul(
                                                    classs="""menu vertical sublevel-2""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Super-sub-item 1""",
                                                                    ),
                                                                ),
                                                                Ul(
                                                                    classs="""menu vertical sublevel-3""",
                                                                    data=(
                                                                        Li(
                                                                            data=(
                                                                                A(
                                                                                    classs="""subitem""",
                                                                                    href="""#""",
                                                                                    data=(
                                                                                        """Thing 1""",
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                        Li(
                                                                            data=(
                                                                                A(
                                                                                    classs="""subitem""",
                                                                                    href="""#""",
                                                                                    data=(
                                                                                        """Thing 2""",
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 2""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 1""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 2""",),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(href="""#""", data=("""Item 2""",)),
                                Ul(
                                    classs="""menu vertical sublevel-1""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 1""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 2""",),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(href="""#""", data=("""Item 3""",)),
                                Ul(
                                    classs="""menu vertical sublevel-1""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 1""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 2""",),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            )
                        ),
                        Li(
                            data=(
                                A(href="""#""", data=("""Item 4""",)),
                                Ul(
                                    classs="""menu vertical sublevel-1""",
                                    data=(
                                        Li(
                                            data=(
                                                A(
                                                    href="""#""",
                                                    data=("""Sub-item 3""",),
                                                ),
                                                Ul(
                                                    classs="""menu vertical sublevel-2""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 1""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    classs="""subitem""",
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 2""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 1""",),
                                                ),
                                            )
                                        ),
                                        Li(
                                            data=(
                                                A(
                                                    classs="""subitem""",
                                                    href="""#""",
                                                    data=("""Thing 2""",),
                                                ),
                                            )
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
