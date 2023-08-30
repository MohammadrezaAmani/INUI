from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''status-update-input-box''',
                    data = (
                        Form(

                            data = (
                                Div(
                                    classs='''row input-box-container''',
                                    data = (
                                        Div(
                                            classs='''columns''',
                                            data = (
                                                Label(

                                                    data = (
                                                        Textarea(
                                                            rows='''5''',
                                                            placeholder='''Hey Harry, What's on your mind?''',
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''row medium-collapse user-action-container''',
                                    data = (
                                        Div(
                                            classs='''small-12 medium-7 columns''',
                                            data = (
                                                Div(
                                                    classs='''user-action-box''',
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
                                                                    title='''Upload a Photo''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-picture-o''',
                                                                            aria_hidden='''true''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''show-for-sr''',
                                                                            data = ('''Upload a Photo''',)
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
                                                                    title='''Upload a Video''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-video-camera''',
                                                                            aria_hidden='''true''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''show-for-sr''',
                                                                            data = ('''Upload a Video''',)
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
                                                                    title='''Check in''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-map-marker''',
                                                                            aria_hidden='''true''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''show-for-sr''',
                                                                            data = ('''Check in''',)
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
                                                                    title='''Add a Feeling''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-smile-o''',
                                                                            aria_hidden='''true''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''show-for-sr''',
                                                                            data = ('''Add a Feeling''',)
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
                                                                    title='''Tag a Friend''',
                                                                    data = (
                                                                        I(
                                                                            classs='''fa fa-tags''',
                                                                            aria_hidden='''true''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''show-for-sr''',
                                                                            data = ('''Tag a Friend''',)
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''small-12 medium-5 columns''',
                                            data = (
                                                Div(
                                                    classs='''user-submit-box''',
                                                    data = (
                                                        Input(
                                                            typee='''submit''',
                                                            classs='''button small''',
                                                            value='''POST''',
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)