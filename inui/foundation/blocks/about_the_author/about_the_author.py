from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''about-the-author''',
                    data = (
                        H3(
                            classs='''author-title''',
                            data = ('''About the Author''',)
                        ), 
                        Div(
                            classs='''row''',
                            data = (
                                Div(
                                    classs='''small-12 medium-4 columns''',
                                    data = (
                                        Div(
                                            classs='''author-image''',
                                            data = (
                                                Img(
                                                    src='''https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/480px-President_Barack_Obama.jpg''',
                                                ), )
                                        ), 
                                        Div(
                                            classs='''author-social''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = (
                                                        Span(
                                                            classs='''fa-stack fa-lg facebook''',
                                                            data = (
                                                                I(
                                                                    classs='''fa fa-circle fa-stack-2x''',
                                                                ), 
                                                                I(
                                                                    classs='''fa fa-facebook fa-stack-1x fa-inverse''',
                                                                ), )
                                                        ), )
                                                ), 
                                                A(
                                                    href='''#''',
                                                    data = (
                                                        Span(
                                                            classs='''fa-stack fa-lg twitter''',
                                                            data = (
                                                                I(
                                                                    classs='''fa fa-circle fa-stack-2x''',
                                                                ), 
                                                                I(
                                                                    classs='''fa fa-twitter fa-stack-1x fa-inverse''',
                                                                ), )
                                                        ), )
                                                ), 
                                                A(
                                                    href='''#''',
                                                    data = (
                                                        Span(
                                                            classs='''fa-stack fa-lg linkedin''',
                                                            data = (
                                                                I(
                                                                    classs='''fa fa-circle fa-stack-2x''',
                                                                ), 
                                                                I(
                                                                    classs='''fa fa-linkedin fa-stack-1x fa-inverse''',
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-12 medium-8 columns''',
                                    data = (
                                        H4(
                                            classs='''separator-left''',
                                            data = ('''Barack Obama''',)
                                        ), 
                                        P(

                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores eum, iusto vel repudiandae, quaerat soluta sequi officia. Blanditiis atque, illo eaque sint in architecto illum nostrum repudiandae labore tenetur! Eaque impedit pariatur odio ad ipsum qui aspernatur dolorem consequuntur a molestias nisi, quae voluptatem expedita, inventore voluptatibus dolores, veritatis corporis facilis laudantium explicabo vero! Non hic quia facilis blanditiis eum.''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)