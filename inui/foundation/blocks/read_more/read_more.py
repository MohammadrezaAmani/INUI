from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''callout''',
                    data = (
                        H4(

                            data = (
                                Strong(

                                    data = ('''FOUNDATION FOR EMAILS''',)
                                ), )
                        ), 
                        P(

                            data = ('''We know building HTML emails is hard, especially responsive emails. That's why we created Foundation for Emails. Get away from complex table markup and inconsistent results. Use Foundation for Emails to spend less time coding emails, and more time
    on other things, like building amazing products.''',)
                        ), 
                        Button(
                            data_toggle='''read-more-content''',
                            href='''#''',
                            data = ('''SHOW MORE ''',
                                I(
                                    classs='''fa fa-plus''',
                                ), )
                        ), 
                        Div(
                            classs='''read-more-content''',
                            id='''read-more-content''',
                            data_toggler='',
                            data_animate='''hinge-in-from-top slide-out-right''',
                            data = (
                                H5(

                                    data = ('''Spend Less Time Coding, Testing, and Preparing:''',)
                                ), 
                                Ul(

                                    data = (
                                        Li(

                                            data = ('''Responsive Grid for Any Layout''',)
                                        ), 
                                        Li(

                                            data = ('''Common UI Patterns to Build Faster''',)
                                        ), 
                                        Li(

                                            data = ('''Make stylish emails fast with Sass''',)
                                        ), 
                                        Li(

                                            data = ('''Inky: A New Templating Language''',)
                                        ), 
                                        Li(

                                            data = ('''The ZURB Email Stack will make you an email pro''',)
                                        ), 
                                        Li(

                                            data = ('''Emails that work in all of the major clients, even Outlook''',)
                                        ), 
                                        Li(

                                            data = ('''Inlining CSS ''',
                                                Strike(

                                                    data = ('''is''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), 
                Div(
                    classs='''callout''',
                    data = (
                        H4(

                            data = (
                                Strong(

                                    data = ('''Motion UI Animations''',)
                                ), )
                        ), 
                        P(

                            data = ('''Choose from the following classes to change the animation:''',)
                        ), 
                        Button(
                            data_toggle='''read-more''',
                            href='''#''',
                            data = ('''SHOW MORE ''',
                                I(
                                    classs='''fa fa-plus''',
                                ), )
                        ), 
                        Div(
                            classs='''read-more''',
                            id='''read-more''',
                            data_toggler='',
                            data_animate='''hinge-in-from-top spin-out''',
                            data = (
                                H5(

                                    data = ('''Spend Less Time Coding, Testing, and Preparing:''',)
                                ), 
                                Ul(

                                    data = (
                                        Li(

                                            data = (
                                                Strong(

                                                    data = ('''Slide:''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-in-down''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-in-left''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-in-up''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-in-right''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-out-down''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-out-left''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-out-up''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.slide-out-right''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Strong(

                                                    data = ('''Fade:''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.fade-in''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.fade-out''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Strong(

                                                    data = ('''Hinge:''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-top''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-right''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-bottom''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-left''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-middle-x''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-in-from-middle-y''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-top''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-right''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-bottom''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-left''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-middle-x''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.hinge-out-from-middle-y''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Strong(

                                                    data = ('''Scale:''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.scale-in-up''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.scale-in-down''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.scale-out-up''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.scale-out-down''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Strong(

                                                    data = ('''Spin:''',)
                                                ), 
                                                Ul(

                                                    data = (
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.spin-in''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.spin-out''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.spin-in-ccw''',)
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                Code(

                                                                    data = ('''.spin-out-ccw''',)
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Button(
                                    data_toggle='''read-more''',
                                    href='''#''',
                                    data = ('''SHOW LESS ''',
                                        I(
                                            classs='''fa fa-plus''',
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)