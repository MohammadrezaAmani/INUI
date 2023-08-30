from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Section(
                    classs='''contact-us-section''',
                    data = (
                        Div(
                            classs='''row medium-unstack''',
                            data = (
                                Div(
                                    classs='''columns contact-us-section-left''',
                                    data = (
                                        H1(
                                            classs='''contact-us-header''',
                                            data = ('''Get In Touch''',)
                                        ), 
                                        Div(
                                            classs='''responsive-embed''',
                                            data = (
                                                Img(
                                                    src='''https://maps.googleapis.com/maps/api/staticmap?center=campbell&zoom=13&scale=false&size=600x300&maptype=roadmap&sensor=false&format=png&visual_refresh=true''',
                                                    alt='''Google Map of campbell''',
                                                ), )
                                        ), 
                                        Ul(
                                            classs='''contact-us-list''',
                                            data = (
                                                Li(
                                                    classs='''address''',
                                                    data = ('''100 W Rincon Ave, Campbell CA 95008''',)
                                                ), 
                                                Li(
                                                    classs='''email''',
                                                    data = (
                                                        A(
                                                            href='''mailto:''',
                                                            data = ('''hello@yeticave.com''',)
                                                        ), )
                                                ), 
                                                Li(
                                                    classs='''phone''',
                                                    data = ('''
          1 (408) 445 9978
        ''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''columns contact-us-section-right''',
                                    data = (
                                        H1(
                                            classs='''contact-us-header''',
                                            data = ('''Mail Us''',)
                                        ), 
                                        Form(
                                            classs='''contact-us-form''',
                                            data = (
                                                Input(
                                                    typee='''text''',
                                                    placeholder='''Full name''',
                                                ), 
                                                Input(
                                                    typee='''email''',
                                                    placeholder='''Email''',
                                                ), 
                                                Textarea(
                                                    name='''message''',
                                                    id='',
                                                    rows='''12''',
                                                    placeholder='''Type your message here''',
                                                ), 
                                                Div(
                                                    classs='''contact-us-form-actions''',
                                                    data = (
                                                        Input(
                                                            typee='''submit''',
                                                            classs='''button''',
                                                            value='''Send it''',
                                                        ), 
                                                        Div(

                                                            data = (
                                                                Label(
                                                                    forr='''FileUpload''',
                                                                    classs='''button contact-us-file-button''',
                                                                    data = ('''Attach Files''',)
                                                                ), 
                                                                Input(
                                                                    typee='''file''',
                                                                    id='''FileUpload''',
                                                                    classs='''show-for-sr''',
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)