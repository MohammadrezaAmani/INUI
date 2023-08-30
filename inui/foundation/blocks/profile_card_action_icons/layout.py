from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''row small-up-1 medium-up-2 large-up-3 align-center''',
                    data = (
                        Div(
                            classs='''column''',
                            data = ('''
    {{> profile-card-action-icons}}
  ''',)
                        ), 
                        Div(
                            classs='''column''',
                            data = ('''
    {{> profile-card-action-icons}}
  ''',)
                        ), 
                        Div(
                            classs='''column''',
                            data = ('''
    {{> profile-card-action-icons}}
  ''',)
                        ), )
                ), )
        ), )
)