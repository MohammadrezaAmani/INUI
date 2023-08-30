from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''flip-card card''',
                    ontouchstart='''this.classList.toggle('hover');''',
                    data = (
                        Div(
                            classs='''flip-card-inner''',
                            data = (
                                Div(
                                    classs='''flip-card-inner-front''',
                                    data = (
                                        Span(

                                            data = ('''Book your next adventure''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''flip-card-inner-back''',
                                    data = (
                                        H3(
                                            classs='''flip-card-inner-back-title''',
                                            data = ('''Visit Yetiland''',)
                                        ), 
                                        P(
                                            classs='''flip-card-inner-back-text''',
                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nemo doloremque accusantium, repellendus ex debitis molestias, recusandae dignissimos delectus.''',)
                                        ), 
                                        A(
                                            href='''#''',
                                            classs='''button success''',
                                            data = ('''Book now''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)