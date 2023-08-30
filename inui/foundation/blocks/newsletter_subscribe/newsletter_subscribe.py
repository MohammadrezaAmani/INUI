from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Section(
                    classs="""newsletter-subscribe""",
                    data=(
                        Div(
                            classs="""newsletter-subscribe-inner""",
                            data=(
                                P(
                                    classs="""subheader""",
                                    data=(
                                        """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi, officiis! Laudantium tenetur modi, voluptatum placeat illo, nisi aliquam nam dolore  reiciendis vel.""",
                                    ),
                                ),
                                Form(
                                    action="",
                                    data=(
                                        Div(
                                            classs="""input-group""",
                                            data=(
                                                Input(
                                                    classs="""input-group-field""",
                                                    typee="""email""",
                                                    placeholder="""Enter your email for Yeti live streaming""",
                                                ),
                                                Div(
                                                    classs="""input-group-button""",
                                                    data=(
                                                        Input(
                                                            typee="""submit""",
                                                            classs="""button""",
                                                            value="""Submit""",
                                                        ),
                                                    ),
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
