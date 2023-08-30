from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    id='''page''',
                    data = ('''
  {{> sticky-topbar}}

  ''',
                        Div(
                            classs='''column row''',
                            id='''content''',
                            data = (
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/100''',
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/200''',
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/300''',
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/400''',
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/500''',
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x300&text=content/600''',
                                ), )
                        ), )
                ), )
        ), )
)