from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                H6(
                    classs='''text-center''',
                    data = ('''Unit(s)''',)
                ), 
                Div(
                    classs='''input-group input-number-group''',
                    data = (
                        Div(
                            classs='''input-group-button''',
                            data = (
                                Span(
                                    classs='''input-number-decrement''',
                                    data = ('''-''',)
                                ), )
                        ), 
                        Input(
                            classs='''input-number''',
                            typee='''number''',
                            value='''1''',
                            min='''0''',
                            max='''1000''',
                        ), 
                        Div(
                            classs='''input-group-button''',
                            data = (
                                Span(
                                    classs='''input-number-increment''',
                                    data = ('''+''',)
                                ), )
                        ), )
                ), )
        ), )
)