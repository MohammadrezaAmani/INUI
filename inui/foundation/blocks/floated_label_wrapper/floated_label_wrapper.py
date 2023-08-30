from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Form(
                    classs="""callout text-center""",
                    data=(
                        H2(data=("""Become A Member""",)),
                        Div(
                            classs="""floated-label-wrapper""",
                            data=(
                                Label(forr="""full-name""", data=("""Full name""",)),
                                Input(
                                    typee="""text""",
                                    id="""full-name""",
                                    name="""full name input""",
                                    placeholder="""Full name""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""floated-label-wrapper""",
                            data=(
                                Label(forr="""email""", data=("""Email""",)),
                                Input(
                                    typee="""email""",
                                    id="""email""",
                                    name="""email input""",
                                    placeholder="""Email""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""floated-label-wrapper""",
                            data=(
                                Label(forr="""pass""", data=("""Password""",)),
                                Input(
                                    typee="""password""",
                                    id="""pass""",
                                    name="""password input""",
                                    placeholder="""Password""",
                                ),
                            ),
                        ),
                        Input(
                            classs="""button expanded""",
                            typee="""submit""",
                            value="""Sign up""",
                        ),
                    ),
                ),
            )
        ),
    )
)
