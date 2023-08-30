from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Footer(
                    classs='''social-footer''',
                    data = (
                        Div(
                            classs='''social-footer-left''',
                            data = (
                                A(
                                    href='''#''',
                                    data = (
                                        Img(
                                            classs='''logo''',
                                            src='''https://placehold.it/150x30''',
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''social-footer-icons''',
                            data = (
                                Ul(
                                    classs='''menu simple''',
                                    data = (
                                        Li(

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
                                        Li(

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
                                        Li(

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
                                        Li(

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
        ), )
)