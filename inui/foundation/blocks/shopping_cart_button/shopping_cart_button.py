from inui.elements import *
from inui.svg import *
Html(

    data = (
        Head(

            data = (
                Link(
                    href='''https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css''',
                    rel='''stylesheet''',
                ), 
                Button(
                    typee='''button''',
                    classs='''shopping-cart-button float-right''',
                    data_toggle='''shopping-cart-dropdown''',
                    data = (
                        I(
                            classs='''fa fa-shopping-cart''',
                        ), 
                        Span(
                            classs='''text''',
                            data = ('''Shopping Cart (3)''',)
                        ), )
                ), )
        ), 
        Body(

            data = (
                Div(
                    classs='''shopping-cart-dropdown-pane''',
                    data = (
                        Div(
                            classs='''dropdown-pane bottom ''',
                            id='''shopping-cart-dropdown''',
                            data_dropdown='',
                            data_hover='''true''',
                            data_hover_pane='''true''',
                            data = (
                                Div(
                                    classs='''shopping-cart-item''',
                                    data = (
                                        Img(
                                            src='''https://placeimg.com/60/80/any''',
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-name''',
                                            data = (
                                                A(

                                                    data = ('''Style & Co Knit Blazer''',)
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Color: ''',)
                                                        ), )
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Size: ''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-price''',
                                            data = (
                                                P(
                                                    classs='''shopping-cart-title''',
                                                    data = ('''$24.99''',)
                                                ), 
                                                A(
                                                    href='''#''',
                                                    data = ('''Remove''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''shopping-cart-item''',
                                    data = (
                                        Img(
                                            src='''https://placeimg.com/60/80/any''',
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-name''',
                                            data = (
                                                A(

                                                    data = ('''Style & Co Knit Blazer''',)
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Color: ''',)
                                                        ), )
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Size: ''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-price''',
                                            data = (
                                                P(
                                                    classs='''shopping-cart-title''',
                                                    data = ('''$24.99''',)
                                                ), 
                                                A(
                                                    href='''#''',
                                                    data = ('''Remove''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''shopping-cart-item''',
                                    data = (
                                        Img(
                                            src='''https://placeimg.com/60/80/any''',
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-name''',
                                            data = (
                                                A(

                                                    data = ('''Style & Co Knit Blazer''',)
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Color: ''',)
                                                        ), )
                                                ), 
                                                P(

                                                    data = (
                                                        Span(
                                                            classs='''shopping-cart-title''',
                                                            data = ('''Size: ''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''shopping-cart-item-price''',
                                            data = (
                                                P(
                                                    classs='''shopping-cart-title''',
                                                    data = ('''$24.99''',)
                                                ), 
                                                A(
                                                    href='''#''',
                                                    data = ('''Remove''',)
                                                ), )
                                        ), )
                                ), 
                                A(
                                    href='''#''',
                                    classs='''button shopping-cart-checkout expanded''',
                                    data = ('''Checkout''',)
                                ), )
                        ), )
                ), )
        ), )
)