from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    style='''max-width: 440px; margin: 0 auto;''',
                    data = ('''
  {{> mobile-app-message-bar}}
''',)
                ), )
        ), )
)