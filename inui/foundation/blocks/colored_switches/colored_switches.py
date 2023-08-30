from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''switch''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''defaultSwitch''',
                            typee='''checkbox''',
                            name='''defaultSwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''defaultSwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Default Switch''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''switch primary''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''primarySwitch''',
                            typee='''checkbox''',
                            name='''primarySwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''primarySwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Primary Switch''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''switch secondary''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''secondarySwitch''',
                            typee='''checkbox''',
                            name='''secondarySwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''secondarySwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Secondary Switch''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''switch success''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''successSwitch''',
                            typee='''checkbox''',
                            name='''successSwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''successSwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Success Switch''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''switch alert''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''alertSwitch''',
                            typee='''checkbox''',
                            name='''alertSwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''alertSwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Alert Switch''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''switch warning''',
                    data = (
                        Input(
                            classs='''switch-input''',
                            id='''warningSwitch''',
                            typee='''checkbox''',
                            name='''warningSwitch''',
                        ), 
                        Label(
                            classs='''switch-paddle''',
                            forr='''warningSwitch''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Warning Switch''',)
                                ), )
                        ), )
                ), )
        ), )
)