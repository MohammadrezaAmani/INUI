from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                A(
                    classs='''button button-rounded-hover''',
                    data = ('''Hover Link''',)
                ), 
                Button(
                    classs='''button button-rounded-hover''',
                    data = ('''Hover Button''',)
                ), )
        ), )
)