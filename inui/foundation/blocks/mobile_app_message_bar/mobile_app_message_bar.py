from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""mobile-app-message-bar""",
                    data=(
                        Button(
                            classs="""camera-button""",
                            data=(
                                I(
                                    classs="""fa fa-camera""",
                                    aria_hidden="""true""",
                                ),
                            ),
                        ),
                        Div(
                            classs="""message-input""",
                            data=(
                                Input(
                                    typee="""text""",
                                    name="",
                                    value="",
                                    placeholder="""Message""",
                                ),
                            ),
                        ),
                        Button(classs="""send-button""", data=("""Send""",)),
                    ),
                ),
            )
        ),
    )
)
