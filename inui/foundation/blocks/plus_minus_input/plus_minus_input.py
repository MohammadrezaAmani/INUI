from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''input-group plus-minus-input''',
                    data = (
                        Div(
                            classs='''input-group-button''',
                            data = (
                                Button(
                                    typee='''button''',
                                    classs='''button hollow circle''',
                                    data_quantity='''minus''',
                                    data_field='''quantity''',
                                    data = (
                                        I(
                                            classs='''fa fa-minus''',
                                            aria_hidden='''true''',
                                        ), )
                                ), )
                        ), 
                        Input(
                            classs='''input-group-field''',
                            typee='''number''',
                            name='''quantity''',
                            value='''0''',
                        ), 
                        Div(
                            classs='''input-group-button''',
                            data = (
                                Button(
                                    typee='''button''',
                                    classs='''button hollow circle''',
                                    data_quantity='''plus''',
                                    data_field='''quantity''',
                                    data = (
                                        I(
                                            classs='''fa fa-plus''',
                                            aria_hidden='''true''',
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)