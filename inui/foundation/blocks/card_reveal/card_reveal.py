from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''card card-reveal-wrapper''',
                    data = (
                        Img(
                            src='''https://placehold.it/568x150''',
                        ), 
                        Div(
                            classs='''card-section''',
                            data = (
                                I(
                                    classs='''fa fa-angle-up open-button''',
                                    data = (
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''More''',)
                                        ), )
                                ), 
                                P(

                                    data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fuga et voluptas, praesentium temporibus est? Recusandae blanditiis eaque ea quam omnis, expedita amet, et eius ipsum quod ipsa, veritatis doloribus enim.''',)
                                ), 
                                Div(
                                    classs='''card-reveal''',
                                    data = (
                                        Span(
                                            classs='''card-reveal-title''',
                                            data = (
                                                H4(

                                                    data = ('''Card Title''',)
                                                ), 
                                                I(
                                                    classs='''fa fa-angle-down close-button''',
                                                    data = (
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Close''',)
                                                        ), )
                                                ), )
                                        ), 
                                        P(

                                            data = ('''Here is some more information. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis.''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)