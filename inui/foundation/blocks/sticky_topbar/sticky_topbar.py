from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''top-bar-container''',
                    data_sticky_container='',
                    data = (
                        Div(
                            classs='''sticky sticky-topbar''',
                            data_sticky='',
                            data_options='''anchor: page; marginTop: 0; stickyOn: small;''',
                            data = (
                                Div(
                                    classs='''top-bar''',
                                    data = (
                                        Div(
                                            classs='''top-bar-left''',
                                            data = (
                                                Ul(
                                                    classs='''dropdown menu''',
                                                    data_dropdown_menu='',
                                                    data = (
                                                        Li(
                                                            classs='''menu-text''',
                                                            data = ('''Site Title''',)
                                                        ), 
                                                        Li(
                                                            classs='''has-submenu''',
                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    data = ('''One''',)
                                                                ), 
                                                                Ul(
                                                                    classs='''submenu menu vertical''',
                                                                    data_submenu='',
                                                                    data = (
                                                                        Li(

                                                                            data = (
                                                                                A(
                                                                                    href='''#''',
                                                                                    data = ('''One''',)
                                                                                ), )
                                                                        ), 
                                                                        Li(

                                                                            data = (
                                                                                A(
                                                                                    href='''#''',
                                                                                    data = ('''Two''',)
                                                                                ), )
                                                                        ), 
                                                                        Li(

                                                                            data = (
                                                                                A(
                                                                                    href='''#''',
                                                                                    data = ('''Three''',)
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    data = ('''Two''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    data = ('''Three''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''top-bar-right''',
                                            data = (
                                                Ul(
                                                    classs='''menu''',
                                                    data = (
                                                        Li(

                                                            data = (
                                                                Input(
                                                                    typee='''search''',
                                                                    placeholder='''Search''',
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Button(
                                                                    typee='''button''',
                                                                    classs='''button''',
                                                                    data = ('''Search''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)