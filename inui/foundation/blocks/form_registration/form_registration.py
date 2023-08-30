from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''form-registration''',
                    data = (
                        Figure(
                            classs='''form-registration-img''',
                            data = (
                                Img(
                                    src='''https://images.pexels.com/photos/221205/pexels-photo-221205.jpeg?h=350&auto=compress&cs=tinysrgb''',
                                    alt='',
                                ), 
                                Figcaption(
                                    classs='''form-registration-img-caption''',
                                    data = ('''Experience everything Yeti+ has to offer through Yeti e-shoppe and our related apps.''',)
                                ), )
                        ), 
                        Form(
                            classs='''form-registration-group''',
                            action='',
                            data = (
                                Input(
                                    classs='''form-registration-input''',
                                    typee='''email''',
                                    placeholder='''Your email''',
                                ), 
                                Input(
                                    classs='''form-registration-submit-button''',
                                    typee='''submit''',
                                    value='''Continue''',
                                ), 
                                P(
                                    classs='''or-divider''',
                                    data = (
                                        Span(

                                            data = ('''or''',)
                                        ), )
                                ), 
                                A(
                                    classs='''form-registration-social-button''',
                                    href='''#''',
                                    data = (
                                        I(
                                            classs='''fa fa-facebook-official''',
                                            aria_hidden='''true''',
                                        ), )
                                ), 
                                P(
                                    classs='''form-registration-member-signin''',
                                    data = ('''Already a member? ''',
                                        A(
                                            href='''#''',
                                            data = ('''Sign in''',)
                                        ), )
                                ), 
                                P(
                                    classs='''form-registration-terms''',
                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Terms & Conditions''',)
                                        ), 
                                        A(
                                            href='''#''',
                                            data = ('''Privacy''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)