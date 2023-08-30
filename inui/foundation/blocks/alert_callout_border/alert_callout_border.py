from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border primary''',
                    data = (
                        Strong(

                            data = ('''Whoops!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border secondary''',
                    data = (
                        Strong(

                            data = ('''Mistake''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border radius''',
                    data = (
                        Strong(

                            data = ('''Oops''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border alert radius''',
                    data = (
                        Strong(

                            data = ('''Error''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border success''',
                    data = (
                        Strong(

                            data = ('''Yay!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-border warning''',
                    data = (
                        Strong(

                            data = ('''Caution''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''×''',)
                                ), )
                        ), )
                ), )
        ), )
)