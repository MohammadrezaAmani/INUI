from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Header(
                    classs='''sticky-shrinknav-header''',
                    data = (
                        H1(
                            classs='''sticky-shrinknav-header-title''',
                            data = ('''sticky-shrinknav''',)
                        ), 
                        Ul(
                            classs='''menu align-center sticky-shrinknav-menu''',
                            data = (
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Home''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''About''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Gallery''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Contact''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)