from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''three-column-footer-contact-form-container''',
                    data = (
                        Footer(
                            classs='''three-column-footer-contact-form''',
                            data_equalizer='',
                            data_equalize_by_row='''true''',
                            data = (
                                Div(
                                    classs='''footer-left''',
                                    data_equalizer_watch='',
                                    data = (
                                        Div(
                                            classs='''baseline''',
                                            data = (
                                                Div(
                                                    classs='''contact-details''',
                                                    data = (
                                                        H6(

                                                            data = ('''Contact details''',)
                                                        ), 
                                                        P(

                                                            data = (
                                                                I(
                                                                    classs='''fa fa-phone fa-lg''',
                                                                    aria_hidden='''true''',
                                                                ), )
                                                        ), 
                                                        P(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-envelope-o''',
                                                                            aria_hidden='''true''',
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        P(

                                                            data = (
                                                                I(
                                                                    classs='''fa fa-map-marker fa-lg''',
                                                                    aria_hidden='''true''',
                                                                ), )
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''newsletter''',
                                                    data = (
                                                        Div(
                                                            classs='''input-group''',
                                                            data = (
                                                                H6(

                                                                    data = ('''Sign up for our newsletter''',)
                                                                ), 
                                                                Input(
                                                                    classs='''input-group-field''',
                                                                    typee='''email''',
                                                                    placeholder='''Email address''',
                                                                ), )
                                                        ), 
                                                        A(
                                                            classs='''button expanded''',
                                                            href='''#''',
                                                            data = ('''Submit''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''footer-center''',
                                    data_equalizer_watch='',
                                    data = (
                                        Div(
                                            classs='''baseline''',
                                            data = (
                                                Div(
                                                    classs='''newsletter''',
                                                    data = (
                                                        H6(

                                                            data = ('''Contact form''',)
                                                        ), 
                                                        Div(
                                                            classs='''input-group''',
                                                            data = (
                                                                Input(
                                                                    classs='''input-group-field''',
                                                                    typee='''text''',
                                                                    placeholder='''Name''',
                                                                ), 
                                                                Input(
                                                                    classs='''input-group-field''',
                                                                    typee='''email''',
                                                                    placeholder='''Email address''',
                                                                ), 
                                                                Textarea(
                                                                    placeholder='''Message''',
                                                                ), )
                                                        ), 
                                                        A(
                                                            classs='''button expanded''',
                                                            href='''#''',
                                                            data = ('''Submit''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''footer-right''',
                                    data_equalizer_watch='',
                                    data = (
                                        Div(
                                            classs='''baseline''',
                                            data = (
                                                Img(
                                                    classs='''thumbnail''',
                                                    src='''https://placehold.it/100''',
                                                ), 
                                                H6(

                                                    data = ('''Opening times''',)
                                                ), 
                                                P(

                                                    data = ('''Mon - Fri 9:00am - 5:00pm''',)
                                                ), 
                                                P(

                                                    data = ('''Sat 9:00am - 8:00pm''',)
                                                ), 
                                                P(

                                                    data = ('''Sun 9:00am - 4:00pm''',)
                                                ), 
                                                Div(
                                                    classs='''social''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-facebook-square fa-2x''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        I(
                                                            classs='''fa fa-twitter-square fa-2x''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        I(
                                                            classs='''fa fa-google-plus-square fa-2x''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        I(
                                                            classs='''fa fa-linkedin-square fa-2x''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)