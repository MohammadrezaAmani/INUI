from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''button-group align-center''',
                    data = (
                        Button(
                            href='''#''',
                            classs='''button''',
                            data_open='''mobile-ios-modal''',
                            data = (
                                I(
                                    classs='''fa fa-cogs''',
                                ), )
                        ), 
                        Button(
                            href='''#''',
                            classs='''button''',
                            data_open='''mobile-ios-modal-2''',
                            data = (
                                I(
                                    classs='''fa fa-warning''',
                                ), )
                        ), 
                        Button(
                            href='''#''',
                            classs='''button''',
                            data_open='''mobile-ios-modal-3''',
                            data = (
                                I(
                                    classs='''fa fa-cogs''',
                                ), )
                        ), 
                        Button(
                            href='''#''',
                            classs='''button''',
                            data_open='''mobile-ios-modal-4''',
                            data = (
                                I(
                                    classs='''fa fa-cogs''',
                                ), )
                        ), )
                ), 
                Div(
                    classs='''reveal mobile-ios-modal''',
                    id='''mobile-ios-modal''',
                    data_reveal='',
                    data = (
                        Div(
                            classs='''mobile-ios-modal-inner''',
                            data = (
                                P(

                                    data = ('''Number of Yetis''',)
                                ), 
                                Input(
                                    typee='''number''',
                                ), )
                        ), 
                        Div(
                            classs='''mobile-ios-modal-options''',
                            data = (
                                Button(
                                    data_close='',
                                    classs='''button''',
                                    data = ('''Cancel''',)
                                ), 
                                Button(
                                    classs='''button''',
                                    data = ('''Ok''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''reveal mobile-ios-modal''',
                    id='''mobile-ios-modal-2''',
                    data_reveal='',
                    data = (
                        Div(
                            classs='''mobile-ios-modal-inner''',
                            data = (
                                P(

                                    data = ('''Your password does not match our records. Please re-enter your password.''',)
                                ), )
                        ), 
                        Div(
                            classs='''mobile-ios-modal-options''',
                            data = (
                                Button(
                                    data_close='',
                                    classs='''button''',
                                    data = ('''Cancel''',)
                                ), 
                                Button(
                                    classs='''button''',
                                    data = ('''Ok''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''reveal mobile-ios-modal''',
                    id='''mobile-ios-modal-3''',
                    data_reveal='',
                    data = (
                        Div(
                            classs='''mobile-ios-modal-inner''',
                            data = (
                                P(

                                    data = ('''Plase enter your 4-digit passcode''',)
                                ), 
                                Input(
                                    typee='''text''',
                                ), )
                        ), 
                        Div(
                            classs='''mobile-ios-modal-options''',
                            data = (
                                Button(
                                    data_close='',
                                    classs='''button''',
                                    data = ('''Cancel''',)
                                ), 
                                Button(
                                    classs='''button''',
                                    data = ('''Ok''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''reveal mobile-ios-modal''',
                    id='''mobile-ios-modal-4''',
                    data_reveal='',
                    data = (
                        Div(
                            classs='''mobile-ios-modal-options-stacked''',
                            data = (
                                Button(
                                    classs='''button''',
                                    data = ('''Search for Image''',)
                                ), 
                                Button(
                                    classs='''button''',
                                    data = ('''Choose Photo''',)
                                ), 
                                Button(
                                    classs='''button''',
                                    data = ('''Take Photo''',)
                                ), 
                                Button(
                                    data_close='',
                                    classs='''button''',
                                    data = ('''Cancel''',)
                                ), )
                        ), )
                ), )
        ), )
)