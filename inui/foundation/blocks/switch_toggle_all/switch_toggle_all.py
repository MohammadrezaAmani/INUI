from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''callout''',
                    id='''switch-toggle-all''',
                    data = (
                        Div(
                            classs='''switch-toggle-wrapper''',
                            data = (
                                Div(
                                    classs='''switch''',
                                    data = (
                                        Input(
                                            classs='''switch-input''',
                                            id='''exampleSwitch1''',
                                            typee='''checkbox''',
                                            name='''exampleSwitch''',
                                            data_toggle_all='',
                                        ), 
                                        Label(
                                            classs='''switch-paddle''',
                                            forr='''exampleSwitch1''',
                                            data = (
                                                Span(
                                                    classs='''show-for-sr''',
                                                    data = ('''Toggle All''',)
                                                ), )
                                        ), )
                                ), 
                                Span(

                                    data = ('''Toggle All''',)
                                ), )
                        ), 
                        Hr(

                        ), 
                        Div(
                            classs='''switch-toggle-wrapper''',
                            data = (
                                Div(
                                    classs='''switch''',
                                    data = (
                                        Input(
                                            classs='''switch-input''',
                                            id='''exampleSwitch2''',
                                            typee='''checkbox''',
                                            name='''exampleSwitch2''',
                                        ), 
                                        Label(
                                            classs='''switch-paddle''',
                                            forr='''exampleSwitch2''',
                                            data = (
                                                Span(
                                                    classs='''show-for-sr''',
                                                    data = ('''Automatic Updates''',)
                                                ), )
                                        ), )
                                ), 
                                Span(

                                    data = ('''Automatic Updates''',)
                                ), )
                        ), 
                        Div(
                            classs='''switch-toggle-wrapper''',
                            data = (
                                Div(
                                    classs='''switch''',
                                    data = (
                                        Input(
                                            classs='''switch-input''',
                                            id='''exampleSwitch3''',
                                            typee='''checkbox''',
                                            name='''exampleSwitch3''',
                                        ), 
                                        Label(
                                            classs='''switch-paddle''',
                                            forr='''exampleSwitch3''',
                                            data = (
                                                Span(
                                                    classs='''show-for-sr''',
                                                    data = ('''Sync Daily''',)
                                                ), )
                                        ), )
                                ), 
                                Span(

                                    data = ('''Sync Daily''',)
                                ), )
                        ), 
                        Div(
                            classs='''switch-toggle-wrapper''',
                            data = (
                                Div(
                                    classs='''switch''',
                                    data = (
                                        Input(
                                            classs='''switch-input''',
                                            id='''exampleSwitch4''',
                                            typee='''checkbox''',
                                            name='''exampleSwitch4''',
                                        ), 
                                        Label(
                                            classs='''switch-paddle''',
                                            forr='''exampleSwitch4''',
                                            data = (
                                                Span(
                                                    classs='''show-for-sr''',
                                                    data = ('''Location''',)
                                                ), )
                                        ), )
                                ), 
                                Span(

                                    data = ('''Location''',)
                                ), )
                        ), 
                        Div(
                            classs='''switch-toggle-wrapper''',
                            data = (
                                Div(
                                    classs='''switch''',
                                    data = (
                                        Input(
                                            classs='''switch-input''',
                                            id='''exampleSwitch5''',
                                            typee='''checkbox''',
                                            name='''exampleSwitch5''',
                                        ), 
                                        Label(
                                            classs='''switch-paddle''',
                                            forr='''exampleSwitch5''',
                                            data = (
                                                Span(
                                                    classs='''show-for-sr''',
                                                    data = ('''push notifications''',)
                                                ), )
                                        ), )
                                ), 
                                Span(

                                    data = ('''Push Notifications''',)
                                ), )
                        ), )
                ), )
        ), )
)