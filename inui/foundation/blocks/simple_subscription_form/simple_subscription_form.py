from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''simple-subscription-form''',
                    data = (
                        Form(

                            data = (
                                H4(

                                    data = ('''Subscribe''',)
                                ), 
                                P(

                                    data = ('''Receive updates and latest news direct from our team. Simply enter your email below :''',)
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
                                            typee='''email''',
                                            placeholder='''Email''',
                                            required='',
                                        ), 
                                        Button(
                                            classs='''button''',
                                            data = ('''Sign up now''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)