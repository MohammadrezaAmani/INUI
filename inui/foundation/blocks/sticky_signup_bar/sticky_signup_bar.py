from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''row column''',
                    id='''subscription-container''',
                    data = (
                        Div(
                            classs='''subscription-footer''',
                            id='''email-subscription-footer''',
                            data = (
                                Div(
                                    classs='''subscription-wrapper''',
                                    data = (
                                        P(
                                            classs='''subscription-description''',
                                            data = ('''Get design articles delivered to your inbox!''',)
                                        ), 
                                        Div(
                                            classs='''subscription-form-wrapper''',
                                            data = (
                                                Form(
                                                    classs='''subscription-form''',
                                                    data = (
                                                        Div(
                                                            classs='''row collapse''',
                                                            data = (
                                                                Div(
                                                                    classs='''small-7 columns''',
                                                                    data = (
                                                                        Input(
                                                                            classs='''input-text subscription-input''',
                                                                            placeholder='''getupdates@example.com''',
                                                                            size='''21''',
                                                                            typee='''text''',
                                                                        ), )
                                                                ), 
                                                                Div(
                                                                    classs='''small-5 columns''',
                                                                    data = (
                                                                        Button(
                                                                            classs='''button''',
                                                                            data = ('''Get Updates''',)
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)