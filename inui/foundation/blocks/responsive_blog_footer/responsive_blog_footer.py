from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Footer(
                    classs='''responsive-blog-footer''',
                    data = (
                        Div(
                            classs='''row''',
                            data = (
                                Div(
                                    classs='''medium-8 columns small-order-2 medium-order-1 about-container''',
                                    data = (
                                        Div(
                                            classs='''row''',
                                            data = (
                                                Div(
                                                    classs='''hide-for-small-only medium-4 columns about-section''',
                                                    data = (
                                                        Img(
                                                            src='''https://placehold.it/250x250''',
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''medium-8 columns about-section''',
                                                    data = (
                                                        H4(

                                                            data = (''' About Me''',)
                                                        ), 
                                                        P(

                                                            data = ('''paragraph about how amazing and awesome i am paragraph about how amazing and awesome i am paragraph about how amazing and awesome i am''',)
                                                        ), 
                                                        A(
                                                            href='',
                                                            data = ('''Read More''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-12 medium-4 columns small-order-1 medium-order-2 mailing-container''',
                                    data = (
                                        H4(
                                            classs='''mailing-list''',
                                            data = ('''Join my mailing list''',)
                                        ), 
                                        Input(
                                            typee='''text''',
                                            placeholder='''Email Address''',
                                        ), 
                                        A(
                                            classs='''button expanded subscribe-button''',
                                            href='''#''',
                                            data = ('''Subscribe Now''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''row tag-search''',
                            data = (
                                Div(
                                    classs='''columns''',
                                    data = (
                                        H4(

                                            data = ('''Search by Tag''',)
                                        ), 
                                        Ul(
                                            classs='''menu simple tag-section''',
                                            data = (
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='',
                                                            data = ('''word''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''row columns flex-container align-justify''',
                            data = (
                                P(

                                    data = (''' all rights reserved''',)
                                ), 
                                Div(
                                    classs='''up-arrow''',
                                    data = (
                                        A(
                                            href='''#top''',
                                            data = (
                                                I(
                                                    classs='''fa fa-chevron-circle-up''',
                                                    aria_hidden='''true''',
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)