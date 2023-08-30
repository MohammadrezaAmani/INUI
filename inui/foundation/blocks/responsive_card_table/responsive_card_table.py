from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Table(
                    classs="""responsive-card-table unstriped""",
                    data=(
                        Thead(
                            data=(
                                Tr(
                                    data=(
                                        Th(data=("""First Name""",)),
                                        Th(data=("""Last Name""",)),
                                        Th(data=("""Hero Title""",)),
                                    )
                                ),
                            )
                        ),
                        Tbody(
                            data=(
                                Tr(
                                    data=(
                                        Td(
                                            data_label="""First Name""",
                                            data=("""Bruce""",),
                                        ),
                                        Td(
                                            data_label="""Last Name""",
                                            data=("""Wayne""",),
                                        ),
                                        Td(
                                            data_label="""Hero Title""",
                                            data=("""Batman""",),
                                        ),
                                    )
                                ),
                                Tr(
                                    data=(
                                        Td(
                                            data_label="""First Name""",
                                            data=("""Peter""",),
                                        ),
                                        Td(
                                            data_label="""Last Name""",
                                            data=("""Parker""",),
                                        ),
                                        Td(
                                            data_label="""Hero Title""",
                                            data=("""Spiderman""",),
                                        ),
                                    )
                                ),
                                Tr(
                                    data=(
                                        Td(
                                            data_label="""First Name""",
                                            data=("""Bruce""",),
                                        ),
                                        Td(
                                            data_label="""Last Name""",
                                            data=("""Banner""",),
                                        ),
                                        Td(
                                            data_label="""Hero Title""",
                                            data=("""The Hulk""",),
                                        ),
                                    )
                                ),
                                Tr(
                                    data=(
                                        Td(
                                            data_label="""First Name""",
                                            data=("""Clark""",),
                                        ),
                                        Td(
                                            data_label="""Last Name""",
                                            data=("""Kent""",),
                                        ),
                                        Td(
                                            data_label="""Hero Title""",
                                            data=("""Superman""",),
                                        ),
                                    )
                                ),
                            )
                        ),
                    ),
                ),
            )
        ),
    )
)
