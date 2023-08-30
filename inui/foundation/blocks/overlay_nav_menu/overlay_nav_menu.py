from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Nav(
                    role='''navigation''',
                    data = (
                        Ul(
                            id='''overlay-nav-menu''',
                            classs='''overlay-nav-menu''',
                            data = (
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Home''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''About''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Contact''',)
                                        ), )
                                ), )
                        ), 
                        A(
                            data_toggle_menu='',
                            classs='''overlay-nav-menu-toggle''',
                            href='''#overlay-nav-menu''',
                            data = (
                                I(
                                    classs='''fa fa-plus''',
                                ), )
                        ), )
                ), )
        ), )
)