from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''product-card''',
                    data = (
                        Div(
                            classs='''product-card-thumbnail''',
                            data = (
                                A(
                                    href='''#''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/180x180''',
                                        ), )
                                ), )
                        ), 
                        H2(
                            classs='''product-card-title''',
                            data = (
                                A(
                                    href='''#''',
                                    data = ('''Product Name''',)
                                ), )
                        ), 
                        Span(
                            classs='''product-card-desc''',
                            data = ('''Product Description''',)
                        ), 
                        Span(
                            classs='''product-card-price''',
                            data = ('''$9.99''',)
                        ), 
                        Span(
                            classs='''product-card-sale''',
                            data = ('''$12.99''',)
                        ), 
                        Div(
                            classs='''product-card-colors''',
                            data = (
                                Button(
                                    href='''#''',
                                    classs='''product-card-color-option''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/30x30''',
                                        ), )
                                ), 
                                Button(
                                    href='''#''',
                                    classs='''product-card-color-option''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/30x30''',
                                        ), )
                                ), 
                                Button(
                                    href='''#''',
                                    classs='''product-card-color-option''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/30x30''',
                                        ), )
                                ), 
                                Button(
                                    href='''#''',
                                    classs='''product-card-color-option''',
                                    data = (
                                        Img(
                                            src='''https://placehold.it/30x30''',
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)