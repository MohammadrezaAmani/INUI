from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''portfolio-resume row''',
                    data = (
                        Div(
                            classs='''large-4 columns''',
                            data = (
                                Div(
                                    classs='''portfolio-resume-wrapper''',
                                    data = (
                                        Img(
                                            classs='''portfolio-resume-headshot''',
                                            src='''https://placehold.it/175''',
                                            alt='''headshot''',
                                        ), 
                                        H3(
                                            classs='''portfolio-resume-header''',
                                            data = ('''Skills''',)
                                        ), 
                                        Ul(

                                            data = (
                                                Li(

                                                    data = ('''Playing Cornhole''',)
                                                ), 
                                                Li(

                                                    data = ('''Balancing on my head''',)
                                                ), 
                                                Li(

                                                    data = ('''Drinking milk''',)
                                                ), 
                                                Li(

                                                    data = ('''Going to sleep''',)
                                                ), 
                                                Li(

                                                    data = ('''Not updating my phone apps''',)
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''large-4 columns''',
                            data = (
                                Div(
                                    classs='''portfolio-resume-wrapper''',
                                    data = (
                                        H3(
                                            classs='''portfolio-resume-header''',
                                            data = ('''Experience''',)
                                        ), 
                                        Div(
                                            classs='''portfolio-resume-spacing''',
                                            data = (
                                                H5(

                                                    data = (
                                                        Strong(

                                                            data = ('''Nanny for Goats''',)
                                                        ), )
                                                ), 
                                                P(

                                                    data = ('''I spent a year at a farm in Ireland raising baby goats. I had to feed them, pet them and play. ''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = ('''Making goats noises''',)
                                                        ), 
                                                        Li(

                                                            data = ('''Cleaning their stalls''',)
                                                        ), 
                                                        Li(

                                                            data = ('''Milking the goats''',)
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''portfolio-resume-spacing''',
                                            data = (
                                                H5(

                                                    data = (
                                                        Strong(

                                                            data = ('''SandCastle Builder''',)
                                                        ), )
                                                ), 
                                                P(

                                                    data = ('''I have crafted the skill of sandcastles growing up on the beaches of Galveston.''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = ('''Avoiding Jellyfish''',)
                                                        ), 
                                                        Li(

                                                            data = ('''Applying the right amount of water''',)
                                                        ), 
                                                        Li(

                                                            data = ('''Wearing sunscreen''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''large-4 columns''',
                            data = (
                                Div(
                                    classs='''portfolio-resume-wrapper''',
                                    data = (
                                        H3(
                                            classs='''portfolio-resume-header''',
                                            data = ('''About Me''',)
                                        ), 
                                        P(

                                            data = ('''My eclectic background and hippy upbringing makes me a rare commodity. I'd love to get together and talk over a non-GMO kale smoothie. Email or call me anytime!''',)
                                        ), 
                                        Div(
                                            classs='''portfolio-resume-contact-info''',
                                            data = (
                                                A(
                                                    href='''mailto:#''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-envelope''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''portfolio-resume-contact-info''',
                                            data = (
                                                A(
                                                    href='''tel:+14083410600''',
                                                    data = (
                                                        I(
                                                            classs='''fa fa-phone''',
                                                            aria_hidden='''true''',
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)