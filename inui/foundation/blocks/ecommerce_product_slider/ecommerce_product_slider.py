from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''ecommerce-product-slider orbit''',
                    role='''region''',
                    aria_lable='''Favorite Space Pictures''',
                    data_orbit='',
                    data = (
                        Ul(
                            classs='''orbit-container''',
                            data = (
                                Button(
                                    classs='''orbit-previous''',
                                    data = (
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''Previous Slide''',)
                                        ), )
                                ), 
                                Button(
                                    classs='''orbit-next''',
                                    data = (
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''Next Slide''',)
                                        ), )
                                ), 
                                Li(
                                    classs='''is-active orbit-slide''',
                                    data = (
                                        Div(
                                            classs='''row small-up-2 medium-up-4 large-up-5 align-center''',
                                            data = (
                                                Div(
                                                    classs='''column''',
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
                                                ), 
                                                Div(
                                                    classs='''column''',
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
                                                ), 
                                                Div(
                                                    classs='''column hide-for-small-only''',
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
                                                ), 
                                                Div(
                                                    classs='''column show-for-large''',
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
                                                ), 
                                                Div(
                                                    classs='''column show-for-large''',
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
                                        ), )
                                ), 
                                Li(
                                    classs='''is-active orbit-slide''',
                                    data = (
                                        Div(
                                            classs='''row small-up-2 medium-up-4 large-up-5 align-center''',
                                            data = (
                                                Div(
                                                    classs='''column''',
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
                                                ), 
                                                Div(
                                                    classs='''column''',
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
                                                ), 
                                                Div(
                                                    classs='''column hide-for-small-only''',
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
                                                ), 
                                                Div(
                                                    classs='''column show-for-large''',
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
                                                ), 
                                                Div(
                                                    classs='''column show-for-large''',
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
                                        ), )
                                ), )
                        ), 
                        Nav(
                            classs='''orbit-bullets''',
                            data = (
                                Button(
                                    classs='''is-active''',
                                    data_slide='''0''',
                                    data = (
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''First slide details.''',)
                                        ), 
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''Current Slide''',)
                                        ), )
                                ), 
                                Button(
                                    data_slide='''1''',
                                    data = (
                                        Span(
                                            classs='''show-for-sr''',
                                            data = ('''Second slide details.''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)