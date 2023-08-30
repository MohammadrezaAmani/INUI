from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''mobile-app-toggle''',
                    data_mobile_app_toggle='',
                    data = (
                        Button(
                            classs='''button is-active''',
                            data = ('''People''',)
                        ), 
                        Button(
                            classs='''button''',
                            data = ('''Tags''',)
                        ), )
                ), 
                Div(
                    classs='''mobile-app-toggle''',
                    data_mobile_app_toggle='',
                    data = (
                        Button(
                            classs='''button is-active''',
                            data = ('''Posts''',)
                        ), 
                        Button(
                            classs='''button''',
                            data = ('''Followers''',)
                        ), 
                        Button(
                            classs='''button''',
                            data = ('''Following''',)
                        ), )
                ), )
        ), )
)