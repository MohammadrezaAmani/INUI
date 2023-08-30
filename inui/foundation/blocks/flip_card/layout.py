from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''row small-up-1 medium-up-2 align-center''',
                    data = (
                        Div(
                            classs='''column''',
                            data = (
                                Div(
                                    classs='''flip-card card''',
                                    ontouchstart='''this.classList.toggle('hover');''',
                                    data = (
                                        Div(
                                            classs='''flip-card-inner''',
                                            data = (
                                                Div(
                                                    classs='''flip-card-inner-front''',
                                                    data = (
                                                        Span(

                                                            data = ('''Book Your Next Adventure''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''flip-card-inner-back''',
                                                    data = (
                                                        H3(
                                                            classs='''flip-card-inner-back-title''',
                                                            data = ('''Visit Yetiland''',)
                                                        ), 
                                                        P(
                                                            classs='''flip-card-inner-back-text''',
                                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nemo doloremque accusantium, repellendus ex debitis molestias, recusandae dignissimos delectus.''',)
                                                        ), 
                                                        A(
                                                            href='''#''',
                                                            classs='''button success''',
                                                            data = ('''Book now''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''column''',
                            data = (
                                Div(
                                    classs='''flip-card card''',
                                    ontouchstart='''this.classList.toggle('hover');''',
                                    data = (
                                        Div(
                                            classs='''flip-card-inner''',
                                            data = (
                                                Div(
                                                    classs='''flip-card-inner-front two''',
                                                    data = (
                                                        Span(

                                                            data = ('''Roll To A Hot Spot''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''flip-card-inner-back''',
                                                    data = (
                                                        Img(
                                                            src='''https://www.virginamerica.com/cms/dam/promos/homepage/HPM-Icon-ogg.png''',
                                                            classs='',
                                                            height='''75''',
                                                            width='''75''',
                                                            alt='',
                                                        ), 
                                                        H3(
                                                            classs='''flip-card-inner-back-title''',
                                                            data = ('''Visit Yetiland''',)
                                                        ), 
                                                        P(
                                                            classs='''flip-card-inner-back-text''',
                                                            data = ('''Plan a getaway with sweet low fares from $49 one way.''',)
                                                        ), 
                                                        A(
                                                            href='''#''',
                                                            classs='''button success''',
                                                            data = ('''Grab A Seat''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''column''',
                            data = (
                                Div(
                                    classs='''flip-card card''',
                                    ontouchstart='''this.classList.toggle('hover');''',
                                    data = (
                                        Div(
                                            classs='''flip-card-inner''',
                                            data = (
                                                Div(
                                                    classs='''flip-card-inner-front three''',
                                                    data = (
                                                        Span(

                                                            data = ('''Oodles and Oodles Of Flights''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''flip-card-inner-back''',
                                                    data = (
                                                        H3(
                                                            classs='''flip-card-inner-back-title''',
                                                            data = ('''Visit Yetiland''',)
                                                        ), 
                                                        P(
                                                            classs='''flip-card-inner-back-text''',
                                                            data = ('''Together, with Alaska Airlines, we are launching more new routes from the west coast.''',)
                                                        ), 
                                                        A(
                                                            href='''#''',
                                                            classs='''button success''',
                                                            data = ('''Learn More''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''column''',
                            data = (
                                Div(
                                    classs='''flip-card card''',
                                    ontouchstart='''this.classList.toggle('hover');''',
                                    data = (
                                        Div(
                                            classs='''flip-card-inner''',
                                            data = (
                                                Div(
                                                    classs='''flip-card-inner-front four''',
                                                    data = (
                                                        Span(

                                                            data = ('''Make Business A Pleasure''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''flip-card-inner-back''',
                                                    data = (
                                                        Img(
                                                            src='''https://www.virginamerica.com/cms/dam/promos/homepage/HPM-Icon-new-routes.png''',
                                                            classs='',
                                                            height='''75''',
                                                            width='''75''',
                                                            alt='',
                                                        ), 
                                                        H3(
                                                            classs='''flip-card-inner-back-title''',
                                                            data = ('''Score More Points''',)
                                                        ), 
                                                        P(
                                                            classs='''flip-card-inner-back-text''',
                                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipisicing elit.''',)
                                                        ), 
                                                        A(
                                                            href='''#''',
                                                            classs='''button success''',
                                                            data = ('''Book Now''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)