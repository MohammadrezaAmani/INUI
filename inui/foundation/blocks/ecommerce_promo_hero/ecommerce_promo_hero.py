from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''promo-hero promo-hero-bg-image''',
                    data = (
                        Div(
                            classs='''promo-hero-content''',
                            data = (
                                H1(
                                    classs='''promo-hero-title''',
                                    data = ('''Promo Headline Will Display Here''',)
                                ), 
                                P(
                                    classs='''promo-hero-description hide-for-small-only''',
                                    data = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tortor ante, varius eget lacinia porta, faucibus ut eros. Donec quis dui id felis pharetra fermentum.''',)
                                ), 
                                Div(
                                    classs='''promo-hero-ctas''',
                                    data = (
                                        A(
                                            href='''#''',
                                            classs='''promo-section-cta button primary''',
                                            data = ('''Shop Now''',)
                                        ), 
                                        A(
                                            href='''#''',
                                            classs='''promo-section-cta button white-hollow''',
                                            data = ('''Learn More''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)