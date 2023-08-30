from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''curtain-menu-button''',
                    data_curtain_menu_button='',
                    data = (
                        Div(
                            classs='''curtain-menu-button-toggle''',
                            data = (
                                Div(
                                    classs='''bar1''',
                                ), 
                                Div(
                                    classs='''bar2''',
                                ), )
                        ), )
                ), 
                Div(
                    classs='''curtain-menu''',
                    data = (
                        Div(
                            classs='''curtain''',
                        ), 
                        Div(
                            classs='''curtain''',
                        ), 
                        Div(
                            classs='''curtain''',
                        ), 
                        Div(
                            classs='''curtain-menu-wrapper''',
                            data = (
                                Ul(
                                    classs='''curtain-menu-list menu vertical''',
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
                                                    data = ('''Work''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Contact''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)