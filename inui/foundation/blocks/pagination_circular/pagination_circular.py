from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Ul(
                    classs='''pagination pagination-circular''',
                    role='''navigation''',
                    aria_lable='''Pagination''',
                    data = (
                        Li(
                            classs='''disabled''',
                            data = ('''« ''',
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''Previous page''',)
                                ), )
                        ), 
                        Li(
                            classs='''current''',
                            data = (
                                Span(
                                    classs='''show-for-sr''',
                                    data = ('''You're on page''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    aria_lable='''Page 2''',
                                    data = ('''2''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    aria_lable='''Page 3''',
                                    data = ('''3''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    aria_lable='''Page 4''',
                                    data = ('''4''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    aria_lable='''Page 5''',
                                    data = ('''5''',)
                                ), )
                        ), 
                        Li(

                            data = (
                                A(
                                    href='''#''',
                                    aria_lable='''Next page''',
                                    data = ('''» ''',
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''Next page''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)