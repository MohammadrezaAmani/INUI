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
                Form(

                    data = (
                        Div(
                            classs='''form-icons''',
                            data = (
                                H4(

                                    data = ('''Register for an account''',)
                                ), 
                                Div(
                                    classs='''input-group''',
                                    data = (
                                        Span(
                                            classs='''input-group-label''',
                                            data = (
                                                I(
                                                    classs='''fa fa-user''',
                                                ), )
                                        ), 
                                        Input(
                                            classs='''input-group-field''',
                                            typee='''text''',
                                            placeholder='''Full name''',
                                        ), )
                                ), 
                                Div(
                                    classs='''input-group''',
                                    data = (
                                        Span(
                                            classs='''input-group-label''',
                                            data = (
                                                I(
                                                    classs='''fa fa-envelope''',
                                                ), )
                                        ), 
                                        Input(
                                            classs='''input-group-field''',
                                            typee='''text''',
                                            placeholder='''Email''',
                                        ), )
                                ), 
                                Div(
                                    classs='''input-group''',
                                    data = (
                                        Span(
                                            classs='''input-group-label''',
                                            data = (
                                                I(
                                                    classs='''fa fa-key''',
                                                ), )
                                        ), 
                                        Input(
                                            classs='''input-group-field''',
                                            typee='''text''',
                                            placeholder='''Password''',
                                        ), )
                                ), )
                        ), 
                        Button(
                            classs='''button expanded''',
                            data = ('''Sign Up''',)
                        ), )
                ), )
        ), )
)