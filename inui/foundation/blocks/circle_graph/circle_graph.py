from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''circle-graph''',
                    data_circle_graph='',
                    data_percent='''50''',
                    data = (
                        Div(
                            classs='''circle-graph-progress''',
                            data = (
                                Div(
                                    classs='''circle-graph-progress-fill''',
                                ), )
                        ), 
                        Div(
                            classs='''circle-graph-percents''',
                            data = (
                                Div(
                                    classs='''circle-graph-percents-wrapper''',
                                    data = (
                                        Span(
                                            classs='''circle-graph-percents-number''',
                                        ), 
                                        Span(
                                            classs='''circle-graph-percents-units''',
                                            data = ('''of 100''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)