from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''top-bar foundation-5-top-bar''',
                    data = (
                        Div(
                            classs='''top-bar-title''',
                            data = (
                                Span(
                                    data_responsive_toggle='''responsive-menu''',
                                    data_hide_for='''medium''',
                                    data = (
                                        Button(
                                            classs='''menu-icon''',
                                            typee='''button''',
                                            data_toggle='',
                                        ), )
                                ), 
                                Strong(

                                    data = ('''Site Title''',)
                                ), )
                        ), 
                        Div(
                            id='''responsive-menu''',
                            data = (
                                Div(
                                    classs='''top-bar-left''',
                                    data = (
                                        Ul(
                                            classs='''dropdown vertical medium-horizontal menu''',
                                            data_responsive_menu='''drilldown medium-dropdown''',
                                            data_auto_height='''true''',
                                            data_animate_height='''true''',
                                            data = (
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''One''',)
                                                        ), 
                                                        Ul(
                                                            classs='''menu''',
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
                                                                        ), 
                                                                        Ul(
                                                                            classs='''menu''',
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
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''menu''',
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
                                                                                ), )
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
)