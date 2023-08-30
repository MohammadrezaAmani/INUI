from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                A(
                    href='''#''',
                    classs='''button button-icon-badge''',
                    data = (
                        I(
                            classs='''fa fa-envelope''',
                        ), 
                        Span(
                            classs='''button-icon-badge-text''',
                            data = ('''Emails''',)
                        ), 
                        Span(
                            classs='''badge success''',
                            data = ('''1''',)
                        ), )
                ), )
        ), )
)