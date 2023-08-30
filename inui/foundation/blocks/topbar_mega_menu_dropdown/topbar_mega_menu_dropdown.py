from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

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
                                            classs='''mega-menu''',
                                            data = (
                                                A(
                                                    data_toggle='''mega-menu''',
                                                    href='''#''',
                                                    data = ('''One''',)
                                                ), 
                                                Div(
                                                    classs='''dropdown-pane bottom''',
                                                    id='''mega-menu''',
                                                    data_dropdown='',
                                                    data_options='''closeOnClick:true; hover: true; hoverPane: true; vOffset:11''',
                                                    data = (
                                                        Div(
                                                            classs='''row expanded''',
                                                            data = (
                                                                Div(
                                                                    classs='''column''',
                                                                    data = (
                                                                        Ul(
                                                                            classs='''menu vertical''',
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
                                                                    classs='''column''',
                                                                    data = (
                                                                        Ul(
                                                                            classs='''menu vertical''',
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
                                                                    classs='''column''',
                                                                    data = (
                                                                        Ul(
                                                                            classs='''menu vertical''',
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
)