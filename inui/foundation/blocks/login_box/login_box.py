from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''login-box''',
                    data = (
                        Div(
                            classs='''row collapse expanded''',
                            data = (
                                Div(
                                    classs='''small-12 medium-6 column small-order-2 medium-order-1''',
                                    data = (
                                        Div(
                                            classs='''login-box-form-section''',
                                            data = (
                                                H1(
                                                    classs='''login-box-title''',
                                                    data = ('''Sign up''',)
                                                ), 
                                                Input(
                                                    classs='''login-box-input''',
                                                    typee='''text''',
                                                    name='''username''',
                                                    placeholder='''Username''',
                                                ), 
                                                Input(
                                                    classs='''login-box-input''',
                                                    typee='''email''',
                                                    name='''email''',
                                                    placeholder='''E-mail''',
                                                ), 
                                                Input(
                                                    classs='''login-box-input''',
                                                    typee='''password''',
                                                    name='''password''',
                                                    placeholder='''Password''',
                                                ), 
                                                Input(
                                                    classs='''login-box-input''',
                                                    typee='''password''',
                                                    name='''password2''',
                                                    placeholder='''Retype password''',
                                                ), 
                                                Input(
                                                    classs='''login-box-submit-button''',
                                                    typee='''submit''',
                                                    name='''signup_submit''',
                                                    value='''Sign me up''',
                                                ), )
                                        ), 
                                        Div(
                                            classs='''or''',
                                            data = ('''OR''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''small-12 medium-6 column small-order-1 medium-order-2 login-box-social-section''',
                                    data = (
                                        Div(
                                            classs='''login-box-social-section-inner''',
                                            data = (
                                                Span(
                                                    classs='''login-box-social-headline''',
                                                    data = ('''Sign in with''',
                                                        Br(

                                                        ), )
                                                ), 
                                                A(
                                                    classs='''login-box-social-button-facebook''',
                                                    data = ('''Log in with facebook''',)
                                                ), 
                                                A(
                                                    classs='''login-box-social-button-twitter''',
                                                    data = ('''Log in with Twitter''',)
                                                ), 
                                                A(
                                                    classs='''login-box-social-button-google''',
                                                    data = ('''Log in with Google+''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)