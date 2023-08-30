from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle success''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle alert''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle primary radius''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle warning radius''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle primary large''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''callout alert-callout-subtle primary small''',
                    data = (
                        Strong(

                            data = ('''Yo!''',)
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''⊗''',)
                                ), )
                        ), )
                ), )
        ), )
)