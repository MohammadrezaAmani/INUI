from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''basic-card''',
                    data = (
                        Div(
                            classs='''basic-card-image''',
                            data = (
                                Img(
                                    src='''https://placeimg.com/640/480/animals''',
                                ), )
                        ), 
                        Div(
                            classs='''basic-card-content content callout secondary''',
                            data = (
                                H5(

                                    data = ('''Content''',)
                                ), 
                                P(

                                    data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi saepe, asperiores dolor nesciunt dolore, accusamus minus repellendus vero odio, quibusdam, ipsum nisi in a molestiae ex assumenda nulla eveniet eos!''',)
                                ), )
                        ), 
                        Div(
                            classs='''links callout primary''',
                            data = (
                                Ul(
                                    classs='''menu''',
                                    data = (
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Link''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Link''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Link''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Link''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)