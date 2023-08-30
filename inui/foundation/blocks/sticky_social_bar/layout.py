from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                P(
                    data=(
                        """{{> sticky-social-bar}} 
""",
                    )
                ),
                Div(
                    classs="""row""",
                    data=(
                        Div(
                            classs="""columns""",
                            data=(
                                """
    {{#repeat 30}}
      """,
                                P(
                                    data=(
                                        """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto, voluptates nemo iste quaerat aliquid tenetur dolorum quam dignissimos, eaque et quo, distinctio recusandae nostrum quasi. Nobis laboriosam repudiandae atque odio qui expedita doloremque, explicabo nisi quasi quod? Nisi commodi natus maxime odit, facilis in odio mollitia obcaecati sapiente reprehenderit voluptates! Dolor est velit voluptatibus vel magnam vero dolorem dignissimos unde.
      """,
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
