from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''comment-section-container''',
                    data = (
                        H3(

                            data = ('''Comments (2)''',)
                        ), 
                        Div(
                            classs='''comment-section-author''',
                            data = (
                                Img(
                                    src='''https://placehold.it/50x50''',
                                    alt='',
                                ), 
                                Div(
                                    classs='''comment-section-name''',
                                    data = (
                                        H5(

                                            data = (
                                                A(
                                                    href='',
                                                    data = ('''Janice Jones''',)
                                                ), )
                                        ), 
                                        P(

                                            data = ('''March 12, 2017 at 1:28pm''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''comment-section-text''',
                            data = (
                                P(

                                    data = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean lacinia bibendum nulla sed consectetur. Nulla vitae elit libero, a pharetra augue. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum facilis tenetur a voluptatibus quia
      deserunt.
    ''',)
                                ), )
                        ), 
                        Div(
                            classs='''comment-section-author''',
                            data = (
                                Img(
                                    src='''https://placehold.it/50x50''',
                                    alt='',
                                ), 
                                Div(
                                    classs='''comment-section-name''',
                                    data = (
                                        H5(

                                            data = (
                                                A(
                                                    href='',
                                                    data = ('''Janice Jones''',)
                                                ), )
                                        ), 
                                        P(

                                            data = ('''March 12, 2017 at 1:28pm''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''comment-section-text''',
                            data = (
                                P(

                                    data = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean lacinia bibendum nulla sed consectetur. Nulla vitae elit libero, a pharetra augue. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum facilis tenetur a voluptatibus quia deserunt.
    ''',)
                                ), )
                        ), )
                ), 
                Form(
                    classs='''comment-section-form''',
                    data = (
                        Div(
                            classs='''comment-section-box''',
                            data = (
                                Div(
                                    classs='''row''',
                                    data = (
                                        Div(
                                            classs='''small-12 column''',
                                            data = (
                                                H4(

                                                    data = ('''Leave a Comment''',)
                                                ), 
                                                Label(

                                                    data = ('''Name
          ''',
                                                        Input(
                                                            typee='''text''',
                                                        ), )
                                                ), 
                                                Label(

                                                    data = ('''Email
          ''',
                                                        Input(
                                                            typee='''text''',
                                                        ), )
                                                ), 
                                                Label(

                                                    data = ('''Comment
          ''',
                                                        Textarea(
                                                            rows='''10''',
                                                            typee='''text''',
                                                        ), )
                                                ), 
                                                Button(
                                                    classs='''button expanded''',
                                                    data = ('''Submit''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)