from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    style='''max-width: 515px; margin: 0 auto; background: #fff; padding: 35px;''',
                    data = (
                        Ol(
                            classs='''progress-indicator''',
                            data = (
                                Li(
                                    classs='''is-complete''',
                                    data_step='''1''',
                                    data = ()
                                ), 
                                Li(
                                    classs='''is-complete''',
                                    data_step='''2''',
                                    data = ()
                                ), 
                                Li(
                                    classs='''is-current''',
                                    data_step='''3''',
                                    data = ()
                                ), )
                        ), 
                        Br(

                        ), 
                        Ol(
                            classs='''progress-indicator''',
                            data = (
                                Li(
                                    classs='''is-complete''',
                                    data_step='''1''',
                                    data = ()
                                ), 
                                Li(
                                    classs='''is-current''',
                                    data_step='''2''',
                                    data = ()
                                ), 
                                Li(
                                    classs='',
                                    data_step='''3''',
                                    data = ()
                                ), )
                        ), 
                        Br(

                        ), 
                        Ol(
                            classs='''progress-indicator''',
                            data = (
                                Li(
                                    classs='''is-complete''',
                                    data_step='',
                                    data = (
                                        Span(

                                            data = ('''Arrive''',)
                                        ), )
                                ), 
                                Li(
                                    classs='''is-current''',
                                    data_step='',
                                    data = (
                                        Span(

                                            data = ('''Check In''',)
                                        ), )
                                ), 
                                Li(
                                    classs='',
                                    data_step='',
                                    data = (
                                        Span(

                                            data = ('''Depart''',)
                                        ), )
                                ), )
                        ), 
                        Br(

                        ), )
                ), )
        ), )
)