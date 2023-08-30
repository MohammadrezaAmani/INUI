from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                A(
                    classs='''dashboard-nav-card''',
                    href='''#''',
                    data = (
                        I(
                            classs='''dashboard-nav-card-icon fa fa-users''',
                            aria_hidden='''true''',
                        ), 
                        H3(
                            classs='''dashboard-nav-card-title''',
                            data = ('''Visitors''',)
                        ), )
                ), )
        ), )
)