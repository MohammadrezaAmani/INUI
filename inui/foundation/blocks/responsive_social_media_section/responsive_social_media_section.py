from inui.elements import *
from inui.svg import *
Html(

    data = (
        Head(

            data = (
                Link(
                    href='''https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css''',
                    rel='''stylesheet''',
                ), )
        ), 
        Body(

            data = (
                Div(
                    classs='''social-links''',
                    data = (
                        Div(
                            classs='''row''',
                            data = (
                                Div(
                                    classs='''small-6 medium-3 columns text-center mobile-stack''',
                                    data = (
                                        A(
                                            href='''https://www.facebook.com/''',
                                            data = (
                                                I(
                                                    classs='''fa fa-facebook''',
                                                    aria_hidden='''true''',
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-6 medium-3 columns text-center mobile-stack''',
                                    data = (
                                        A(
                                            href='''https://www.instagram.com/?hl=en''',
                                            data = (
                                                I(
                                                    classs='''fa fa-instagram''',
                                                    aria_hidden='''true''',
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-6 medium-3 columns text-center mobile-stack''',
                                    data = (
                                        A(
                                            href='''https://www.pinterest.com/''',
                                            data = (
                                                I(
                                                    classs='''fa fa-pinterest-p''',
                                                    aria_hidden='''true''',
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-6 medium-3 columns text-center mobile-stack''',
                                    data = (
                                        A(
                                            href='''https://twitter.com/?lang=en''',
                                            data = (
                                                I(
                                                    classs='''fa fa-twitter''',
                                                    aria_hidden='''true''',
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)