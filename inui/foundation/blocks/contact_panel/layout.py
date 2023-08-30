from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                P(

                    data = ('''{{> contact-panel}}


''',)
                ), 
                Div(
                    style='''position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);''',
                    data = (
                        H4(

                            data = ('''Just click on the "Contact us" below''',)
                        ), )
                ), )
        ), )
)