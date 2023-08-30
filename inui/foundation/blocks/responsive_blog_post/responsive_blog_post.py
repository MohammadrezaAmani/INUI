from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''responsive-blog-post''',
                    data = (
                        Div(
                            classs='''individual-post''',
                            data = (
                                H4(

                                    data = ('''Title of Blog''',)
                                ), 
                                P(
                                    classs='''date''',
                                    data = ('''Date''',)
                                ), 
                                Img(
                                    src='''https://placehold.it/1200x650''',
                                ), 
                                P(

                                    data = (''' First few sentences of blog post show here and then eventually cuts out. First few sentences of blog post show here and then eventually cuts out. First few sentences of blog post show here and then eventually cuts out...''',)
                                ), 
                                A(
                                    classs='''button''',
                                    href='''#''',
                                    data = ('''Read On''',)
                                ), )
                        ), )
                ), )
        ), )
)