from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    data_closable='',
                    classs='''alert-box callout alert''',
                    data = (
                        I(
                            classs='''fa fa-ban''',
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''&CircleTimes;''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''alert-box callout warning''',
                    data = (
                        I(
                            classs='''fa fa-exclamation-triangle''',
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''&CircleTimes;''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''alert-box callout success''',
                    data = (
                        I(
                            classs='''fa fa-check''',
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''&CircleTimes;''',)
                                ), )
                        ), )
                ), 
                Div(
                    data_closable='',
                    classs='''alert-box callout info''',
                    data = (
                        I(
                            classs='''fa fa-eye''',
                        ), 
                        Button(
                            classs='''close-button''',
                            aria_lable='''Dismiss alert''',
                            typee='''button''',
                            data_close='',
                            data = (
                                Span(
                                    aria_hidden='''true''',
                                    data = ('''&CircleTimes;''',)
                                ), )
                        ), )
                ), )
        ), )
)