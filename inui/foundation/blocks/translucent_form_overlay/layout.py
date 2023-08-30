from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''hero-background''',
                    data = (
                        Div(
                            classs='''row''',
                            data = (
                                Div(
                                    classs='''columns small-12 medium-8''',
                                    data = (
                                        H1(

                                            data = ('''A translucent overlay form''',)
                                        ), 
                                        P(

                                            data = ('''The overlay is the building block - the rest of this is just context to show how you might use it''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''columns small-12 medium-4''',
                                    data = ('''
      {{> translucent-form-overlay}}
    ''',)
                                ), )
                        ), )
                ), )
        ), )
)