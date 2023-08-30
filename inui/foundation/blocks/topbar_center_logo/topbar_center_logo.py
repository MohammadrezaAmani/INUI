from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''title-bar topbar-center-logo-mobile''',
                    data_responsive_toggle='''topbar-center-logo''',
                    data_hide_for='''medium''',
                    data = (
                        Div(
                            classs='''title-bar-left''',
                            data = (
                                Div(
                                    classs='''title-bar-title''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/100x39''',
                                            alt='',
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''title-bar-right''',
                            data = (
                                Button(
                                    classs='''menu-icon''',
                                    typee='''button''',
                                    data_toggle='''topbar-center-logo''',
                                ), )
                        ), )
                ), 
                Div(
                    classs='''top-bar topbar-center-logo''',
                    id='''topbar-center-logo''',
                    data = (
                        Div(
                            classs='''top-bar-left''',
                            data = (
                                Ul(
                                    classs='''menu vertical medium-horizontal''',
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
                        Div(
                            classs='''top-bar-center''',
                            data = (
                                A(
                                    href='''#''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/100x39''',
                                            alt='',
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''top-bar-right''',
                            data = (
                                Ul(
                                    classs='''menu vertical medium-horizontal''',
                                    data = (
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Four''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Five''',)
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''Six''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)