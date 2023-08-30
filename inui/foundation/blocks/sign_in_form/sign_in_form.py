from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Form(

                    data = (
                        Div(
                            classs='''sign-in-form''',
                            data = (
                                H4(
                                    classs='''text-center''',
                                    data = ('''Sign In''',)
                                ), 
                                Label(
                                    forr='''sign-in-form-username''',
                                    data = ('''Username''',)
                                ), 
                                Input(
                                    typee='''text''',
                                    classs='''sign-in-form-username''',
                                    id='''sign-in-form-username''',
                                ), 
                                Label(
                                    forr='''sign-in-form-password''',
                                    data = ('''Password''',)
                                ), 
                                Input(
                                    typee='''text''',
                                    classs='''sign-in-form-password''',
                                    id='''sign-in-form-password''',
                                ), 
                                Button(
                                    typee='''submit''',
                                    classs='''sign-in-form-button''',
                                    data = ('''Sign In''',)
                                ), )
                        ), )
                ), )
        ), )
)