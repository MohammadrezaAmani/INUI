from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''button-group-option''',
                    data_grouptype='''OR''',
                    data = (
                        A(
                            href='''#''',
                            classs='''button success radius''',
                            data = ('''Buy it now''',)
                        ), 
                        A(
                            href='''#''',
                            classs='''button primary radius''',
                            data = ('''Learn More''',)
                        ), )
                ), )
        ), )
)