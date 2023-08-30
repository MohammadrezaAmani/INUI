from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Ul(
                    classs='''list-group''',
                    data = (
                        Li(
                            classs='''list-group-item active''',
                            data = ('''List Group Item 1 (Active)''',)
                        ), 
                        Li(
                            classs='''list-group-item''',
                            data = ('''List Group Item 2''',)
                        ), 
                        Li(
                            classs='''list-group-item''',
                            data = ('''List Group Item 3''',)
                        ), 
                        Li(
                            classs='''list-group-item disabled''',
                            data = ('''List Group Item 4 (Disabled)''',)
                        ), )
                ), )
        ), )
)