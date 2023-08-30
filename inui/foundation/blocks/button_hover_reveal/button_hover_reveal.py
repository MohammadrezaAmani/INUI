from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''button-hover-reveal-wrapper''',
                    data = (
                        Label(

                            data = ('''Sign Up Now''',)
                        ), 
                        A(
                            href='''#''',
                            classs='''button-hover-reveal''',
                            data = ('''Plan 1''',)
                        ), 
                        A(
                            href='''#''',
                            classs='''button-hover-reveal''',
                            data = ('''Plan 2''',)
                        ), )
                ), )
        ), )
)