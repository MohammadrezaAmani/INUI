from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Button(
                    classs='''button-hover-addcart button''',
                    data = (
                        Span(

                            data = ('''Add to cart''',)
                        ), 
                        I(
                            classs='''fa fa-shopping-cart''',
                        ), )
                ), )
        ), )
)