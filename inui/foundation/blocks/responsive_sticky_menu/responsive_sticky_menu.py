from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    data_sticky_container='',
                    data = (
                        Div(
                            data_sticky='',
                            data_options='''marginTop:0;''',
                            data = (
                                Div(
                                    classs='''title-bar''',
                                    data_responsive_toggle='''example-menu''',
                                    data_hide_for='''medium''',
                                    data = (
                                        Button(
                                            classs='''menu-icon''',
                                            typee='''button''',
                                            data_toggle='''example-menu''',
                                        ), 
                                        Div(
                                            classs='''title-bar-title''',
                                            data = ('''Menu''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''top-bar''',
                                    id='''example-menu''',
                                    data = (
                                        Ul(
                                            classs='''vertical medium-horizontal dropdown menu''',
                                            data_responsive_menu='''accordion medium-dropdown''',
                                            data = (
                                                Li(
                                                    classs='''menu-text''',
                                                    data = ('''Site Title''',)
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''One''',)
                                                        ), 
                                                        Ul(
                                                            classs='''menu vertical nested''',
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
                                ), )
                        ), )
                ), )
        ), )
)