from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''card card-tabs''',
                    data = (
                        Div(
                            classs='''card-divider''',
                            data = (
                                H6(
                                    classs='''float-left''',
                                    data = ('''Title''',)
                                ), 
                                Ul(
                                    classs='''tabs menu align-right''',
                                    data_active_collapse='''true''',
                                    data_tabs='',
                                    id='''collapsing-tabs''',
                                    data = (
                                        Li(
                                            classs='''tabs-title''',
                                            data = (
                                                A(
                                                    href='''#panel3c''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-cog''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), 
                                        Li(
                                            classs='''tabs-title''',
                                            data = (
                                                A(
                                                    href='''#panel2c''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-area-chart''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), 
                                        Li(
                                            classs='''tabs-title is-active''',
                                            data = (
                                                A(
                                                    href='''#panel1c''',
                                                    aria_selected='''true''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-home''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''tabs-content''',
                            data_tabs_content='''collapsing-tabs''',
                            data = (
                                Div(
                                    classs='''tabs-panel is-active''',
                                    id='''panel1c''',
                                    data = (
                                        Img(
                                            src='''https://lorempixel.com/485/248/cats/7/''',
                                        ), 
                                        Div(
                                            classs='''card-section''',
                                            data = (
                                                H4(

                                                    data = ('''This is a card.''',)
                                                ), 
                                                P(

                                                    data = ('''It has an easy to override visual style, and is appropriately subdued.''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''tabs-panel''',
                                    id='''panel2c''',
                                    data = (
                                        Div(
                                            classs='''card-section''',
                                            data = (
                                                H4(

                                                    data = ('''This is a card.''',)
                                                ), 
                                                P(

                                                    data = ('''It has an easy to override visual style, and has a cat on the bottom.''',)
                                                ), )
                                        ), 
                                        Img(
                                            src='''https://lorempixel.com/485/248/cats/5/''',
                                        ), )
                                ), 
                                Div(
                                    classs='''tabs-panel''',
                                    id='''panel3c''',
                                    data = (
                                        Div(
                                            classs='''card-section''',
                                            data = (
                                                H4(

                                                    data = ('''This is a card.''',)
                                                ), 
                                                Img(
                                                    src='''https://lorempixel.com/485/248/cats/6/''',
                                                ), 
                                                P(

                                                    data = ('''It has an easy to override visual style, it has an image in the card section.''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)