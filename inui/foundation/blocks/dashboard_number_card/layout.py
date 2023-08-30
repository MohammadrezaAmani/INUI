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
                            classs='''columns''',
                            data = ('''
    {{> dashboard-number-card positive=true}}
  ''',)
                        ), 
                        Div(
                            classs='''columns''',
                            data = ('''
    {{> dashboard-number-card negative=true}}
  ''',)
                        ), 
                        Div(
                            classs='''columns''',
                            data = ('''
    {{> dashboard-number-card}}
  ''',)
                        ), )
                ), )
        ), )
)