from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Form(
                    action="",
                    data=(
                        Div(
                            classs="""row""",
                            data=(
                                Div(
                                    classs="""small-12 column""",
                                    data=(
                                        Div(
                                            classs="""form-floating-label""",
                                            data=(
                                                Input(
                                                    typee="""email""",
                                                    id="""email""",
                                                    name="""email""",
                                                    required="",
                                                ),
                                                Label(
                                                    forr="""email""",
                                                    data=("""Email float up""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""small-12 column""",
                                    data=(
                                        Div(
                                            classs="""form-floating-label""",
                                            data=(
                                                Input(
                                                    typee="""text""",
                                                    id="""password""",
                                                    name="""password""",
                                                ),
                                                Label(
                                                    forr="""password""",
                                                    data=("""Float password up""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""small-12 column""",
                                    data=(
                                        Div(
                                            classs="""form-floating-label""",
                                            data=(
                                                Input(
                                                    typee="""tel""",
                                                    id="""tel""",
                                                    name="""tel""",
                                                ),
                                                Label(
                                                    forr="""tel""",
                                                    data=("""Float phone up""",),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""small-12 column""",
                                    data=(
                                        Div(
                                            classs="""form-floating-label""",
                                            data=(
                                                Textarea(
                                                    name="",
                                                    id="",
                                                    rows="""5""",
                                                    placeholder="",
                                                ),
                                                Label(
                                                    forr="""textarea""",
                                                    data=("""Float textarea up""",),
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
