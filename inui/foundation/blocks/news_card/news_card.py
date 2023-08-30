from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''news-card-tag''',
                    data = (
                        Span(
                            classs='''label''',
                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Angular 2''',)
                                ), )
                        ), 
                        Span(
                            classs='''label''',
                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Angular 4''',)
                                ), )
                        ), )
                ), 
                Div(
                    classs='''card news-card''',
                    data = (
                        Img(
                            src='''https://i.imgur.com/6jMbuU1.jpg''',
                        ), 
                        Div(
                            classs='''card-section''',
                            data = (
                                Div(
                                    classs='''news-card-date''',
                                    data = ('''Sunday, 16th April''',)
                                ), 
                                Article(
                                    classs='''news-card-article''',
                                    data = (
                                        H4(
                                            classs='''news-card-title''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    data = ('''5 Features To Watch Out For in Angular v4''',)
                                                ), )
                                        ), 
                                        P(
                                            classs='''news-card-description''',
                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae facere, ipsam quae sit, eaque perferendis commodi!...''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''news-card-author''',
                                    data = (
                                        Div(
                                            classs='''news-card-author-image''',
                                            data = (
                                                Img(
                                                    src='''https://i.imgur.com/lAMD2kS.jpg''',
                                                    alt='''user''',
                                                ), )
                                        ), 
                                        Div(
                                            classs='''news-card-author-name''',
                                            data = ('''
        By ''',
                                                A(
                                                    href='''#''',
                                                    data = ('''Harry Manchanda''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)