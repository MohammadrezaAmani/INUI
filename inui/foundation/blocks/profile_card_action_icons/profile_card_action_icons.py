from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''card profile-card-action-icons''',
                    data = (
                        Div(
                            classs='''card-section''',
                            data = (
                                Div(
                                    classs='''profile-card-header''',
                                    data = (
                                        Div(
                                            classs='''profile-card-avatar''',
                                            data = (
                                                Img(
                                                    classs='''avatar-image''',
                                                    src='''https://i.imgur.com/3AeQRbR.jpg''',
                                                    alt='''Harry Manchanda''',
                                                ), )
                                        ), 
                                        Div(
                                            classs='''profile-card-author''',
                                            data = (
                                                H5(
                                                    classs='''author-title''',
                                                    data = ('''Harry Manchanda''',)
                                                ), 
                                                P(
                                                    classs='''author-description''',
                                                    data = ('''Front End Web Developer''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''profile-card-about''',
                                    data = (
                                        H5(
                                            classs='''about-title separator-left''',
                                            data = ('''About Me''',)
                                        ), 
                                        P(
                                            classs='''about-content''',
                                            data = ('''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet autem eveniet nulla quae ullam sit iure voluptatum, nesciunt voluptas perferendis, minus natus in quaerat?
      ''',)
                                        ), 
                                        Div(
                                            classs='''row about-skills''',
                                            data = (
                                                Div(
                                                    classs='''small-6 columns''',
                                                    data = (
                                                        Ul(
                                                            classs='''arrow''',
                                                            data = (
                                                                Li(

                                                                    data = ('''Coding''',)
                                                                ), 
                                                                Li(

                                                                    data = ('''Cricket''',)
                                                                ), 
                                                                Li(

                                                                    data = ('''Enjoying''',)
                                                                ), )
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''small-6 columns''',
                                                    data = (
                                                        Ul(
                                                            classs='''arrow''',
                                                            data = (
                                                                Li(

                                                                    data = ('''Maths''',)
                                                                ), 
                                                                Li(

                                                                    data = ('''Dancing''',)
                                                                ), 
                                                                Li(

                                                                    data = ('''Smiling''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''profile-card-action''',
                                    data = (
                                        Div(
                                            classs='''action-area''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''action-anchor has-tip bottom''',
                                                    data_tooltip='',
                                                    aria_haspopup='''true''',
                                                    data_disable_hover='''false''',
                                                    tabindex='''2''',
                                                    title='''Like Harry Profile''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-thumbs-o-up''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Like Harry Profile''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''action-area''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''action-anchor has-tip bottom''',
                                                    data_tooltip='',
                                                    aria_haspopup='''true''',
                                                    data_disable_hover='''false''',
                                                    tabindex='''2''',
                                                    title='''Comment on Harry Profile''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-comments-o''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Comment on Harry Profile''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''action-area''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''action-anchor has-tip bottom''',
                                                    data_tooltip='',
                                                    aria_haspopup='''true''',
                                                    data_disable_hover='''false''',
                                                    tabindex='''2''',
                                                    title='''Add Harry as a Friend''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-user-plus''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Add Harry as a Friend''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''action-area''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''action-anchor has-tip bottom''',
                                                    data_tooltip='',
                                                    aria_haspopup='''true''',
                                                    data_disable_hover='''false''',
                                                    tabindex='''2''',
                                                    title='''Send Harry a Gift''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-gift''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Send Harry a Gift''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''action-area''',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''action-anchor has-tip bottom''',
                                                    data_tooltip='',
                                                    aria_haspopup='''true''',
                                                    data_disable_hover='''false''',
                                                    tabindex='''2''',
                                                    title='''Block Harry!''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-ban''',
                                                            aria_hidden='''true''',
                                                        ), 
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Block Harry!''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)