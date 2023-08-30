from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Ul(
                    classs='''mobile-app-filter-menu''',
                    data_mobile_app_filter_menu='',
                    data = (
                        Li(
                            classs='''is-active''',
                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Day''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Week''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Month''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Year''',)
                                ), )
                        ), )
                ), )
        ), )
)