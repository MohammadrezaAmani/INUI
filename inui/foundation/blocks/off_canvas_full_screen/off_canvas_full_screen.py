from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    id='''offcanvas-full-screen''',
                    classs='''offcanvas-full-screen''',
                    data_off_canvas='',
                    data_transition='''overlap''',
                    data = (
                        Div(
                            classs='''offcanvas-full-screen-inner''',
                            data = (
                                Button(
                                    classs='''offcanvas-full-screen-close''',
                                    aria_lable='''Close menu''',
                                    typee='''button''',
                                    data_close='',
                                    data = (
                                        Span(
                                            aria_hidden='''true''',
                                            data = ('''×''',)
                                        ), )
                                ), 
                                Ul(
                                    classs='''offcanvas-full-screen-menu''',
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
                                                    data = ('''About us''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Services''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Contact us''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), 
                Div(
                    classs='''off-canvas-content''',
                    data_off_canvas_content='',
                    data = (
                        Div(
                            classs='''top-bar''',
                            data = (
                                Div(
                                    classs='''top-bar-title''',
                                    data = (
                                        Strong(

                                            data = ('''Site Title''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''top-bar-right''',
                                    data = (
                                        Button(
                                            classs='''menu-icon dark''',
                                            typee='''button''',
                                            data_toggle='''offcanvas-full-screen''',
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)