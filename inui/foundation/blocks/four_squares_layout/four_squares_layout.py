from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''container''',
                    data = (
                        Div(
                            classs='''grid-1 callout primary''',
                            data = ('''
    Square 1
  ''',)
                        ), 
                        Div(
                            classs='''grid-2 callout warning''',
                            data = ('''
    Square 2
  ''',)
                        ), 
                        Div(
                            classs='''grid-3 callout alert''',
                            data = ('''
    Square 3
  ''',)
                        ), 
                        Div(
                            classs='''grid-4 callout success''',
                            data = ('''
    Square 4
  ''',)
                        ), )
                ), )
        ), )
)