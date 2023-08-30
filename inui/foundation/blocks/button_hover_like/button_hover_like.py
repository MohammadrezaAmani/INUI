from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Button(
                    classs='''button-hover-like button''',
                    data = (
                        Span(

                            data = ('''Like me''',)
                        ), 
                        I(
                            classs='''fa fa-heart''',
                        ), )
                ), )
        ), )
)