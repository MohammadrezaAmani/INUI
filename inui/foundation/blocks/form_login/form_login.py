from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Form(
                    classs='''log-in-form''',
                    data = (
                        H4(
                            classs='''text-center''',
                            data = ('''Log in with you email account''',)
                        ), 
                        Label(

                            data = ('''Email
    ''',
                                Input(
                                    typee='''email''',
                                    placeholder='''somebody@example.com''',
                                ), )
                        ), 
                        Label(

                            data = ('''Password
    ''',
                                Input(
                                    typee='''password''',
                                    placeholder='''Password''',
                                ), )
                        ), 
                        Input(
                            id='''show-password''',
                            typee='''checkbox''',
                        ), 
                        Label(
                            forr='''show-password''',
                            data = ('''Show password''',)
                        ), 
                        P(

                            data = (
                                Input(
                                    typee='''submit''',
                                    classs='''button expanded''',
                                    value='''Log in''',
                                ), )
                        ), 
                        P(
                            classs='''text-center''',
                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Forgot your password?''',)
                                ), )
                        ), )
                ), )
        ), )
)