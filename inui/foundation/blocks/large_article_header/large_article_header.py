from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''row expanded collapse''',
                    data = (
                        Div(
                            classs='''column''',
                            data = (
                                Div(
                                    classs='''large-article-header''',
                                    data = (
                                        Div(
                                            classs='''large-article-header-content''',
                                            data = (
                                                Div(
                                                    classs='''center-container''',
                                                    data = (
                                                        Div(
                                                            classs='''article-date''',
                                                            data = (
                                                                P(

                                                                    data = ('''Published on Jan 12, 2016''',)
                                                                ), )
                                                        ), 
                                                        Div(
                                                            classs='''article-title''',
                                                            data = (
                                                                H1(

                                                                    data = ('''A Great Big Article Title Goes Here''',)
                                                                ), )
                                                        ), 
                                                        Div(
                                                            classs='''article-details''',
                                                            data = (
                                                                Div(
                                                                    classs='''article-author''',
                                                                    data = (
                                                                        Img(
                                                                            src='''https://unsplash.it/50/50?image=1005''',
                                                                            alt='',
                                                                        ), 
                                                                        A(
                                                                            href='''#''',
                                                                            data = ('''Jane Austen''',)
                                                                        ), )
                                                                ), 
                                                                Div(
                                                                    classs='''article-comments''',
                                                                    data = (
                                                                        A(
                                                                            href='''#''',
                                                                            data = (
                                                                                I(
                                                                                    classs='''fa fa-comment''',
                                                                                    aria_hidden='''true''',
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)