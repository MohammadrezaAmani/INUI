from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''card-user-profile''',
                    data = (
                        Img(
                            classs='''card-user-profile-img''',
                            src='''https://images.pexels.com/photos/5439/earth-space.jpg?h=350&auto=compress&cs=tinysrgb''',
                            alt='''picture of space''',
                        ), 
                        Div(
                            classs='''card-user-profile-content card-section''',
                            data = (
                                Div(
                                    classs='''card-user-profile-avatar''',
                                    data = (
                                        Img(
                                            src='''https://pbs.twimg.com/profile_images/422887689612820482/sZtHMJu5.png''',
                                            alt='''picture of yeti''',
                                        ), )
                                ), 
                                P(
                                    classs='''card-user-profile-name''',
                                    data = ('''Abominable Snowman''',)
                                ), 
                                P(
                                    classs='''card-user-profile-status''',
                                    data = ('''Yeti Web Designer''',)
                                ), 
                                P(
                                    classs='''card-user-profile-info''',
                                    data = ('''The Yeti, once better known as the Abominable Snowman, is a mysterious bipedal creature said to live in the mountains of Asia. It sometimes leaves tracks in snow, but is also said to dwell below the Himalayan snow line.''',)
                                ), )
                        ), 
                        Div(
                            classs='''card-user-profile-actions''',
                            data = (
                                A(
                                    href='''#''',
                                    classs='''card-user-profile-button button hollow''',
                                    data = ('''Follow''',)
                                ), 
                                A(
                                    href='''#''',
                                    classs='''card-user-profile-button button hollow secondary''',
                                    data = ('''More Info''',)
                                ), )
                        ), )
                ), )
        ), )
)