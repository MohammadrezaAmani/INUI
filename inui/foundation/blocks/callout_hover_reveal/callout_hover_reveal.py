from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''callout callout-hover-reveal''',
                    data_callout_hover_reveal='',
                    data = (
                        Div(
                            classs='''callout-body''',
                            data = (
                                H2(

                                    data = ('''Hover me''',)
                                ), 
                                P(

                                    data = ('''I'll show you Bill Murray in the callout footer.''',)
                                ), )
                        ), 
                        Div(
                            classs='''callout-footer''',
                            data = (
                                Img(
                                    src='''https://fillmurray.com/300/200''',
                                    alt='',
                                ), )
                        ), )
                ), )
        ), )
)