from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''clipped-circle-graph''',
                    data_clipped_circle_graph='',
                    data_percent='''50''',
                    data = (
                        Div(
                            classs='''clipped-circle-graph-progress''',
                            data = (
                                Div(
                                    classs='''clipped-circle-graph-progress-fill''',
                                ), )
                        ), 
                        Div(
                            classs='''clipped-circle-graph-percents''',
                            data = (
                                Div(
                                    classs='''clipped-circle-graph-percents-wrapper''',
                                    data = (
                                        Span(
                                            classs='''clipped-circle-graph-percents-number''',
                                        ), 
                                        Span(
                                            classs='''clipped-circle-graph-percents-units''',
                                            data = ('''of 100''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)