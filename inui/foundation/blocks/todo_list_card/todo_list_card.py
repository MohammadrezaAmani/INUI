from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    data_closable='''fade-out''',
                    classs='''todo-list-card card''',
                    data = (
                        Div(
                            classs='''card-divider''',
                            data = (
                                H3(

                                    data = ('''To Do List''',)
                                ), 
                                Button(
                                    classs='''close-button''',
                                    data_close='',
                                    data = ('''x''',)
                                ), )
                        ), 
                        Div(
                            classs='''card-section''',
                            data = (
                                Ul(

                                    data = (
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item1''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item1''',
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item2''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item2''',
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item3''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item3''',
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item4''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item4''',
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item5''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item5''',
                                                ), )
                                        ), 
                                        Li(

                                            data = (
                                                Input(
                                                    id='''item6''',
                                                    typee='''checkbox''',
                                                ), 
                                                Label(
                                                    forr='''item6''',
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)