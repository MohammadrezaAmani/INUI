from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''row''',
                    data = (
                        Div(
                            classs='''small-12 medium-8 medium-offset-2 large-6 large-offset-3 columns''',
                            data = ('''
    {{> list-group}}
  ''',)
                        ), )
                ), )
        ), )
)