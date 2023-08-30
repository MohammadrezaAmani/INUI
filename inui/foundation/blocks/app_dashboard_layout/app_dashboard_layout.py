from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''app-dashboard shrink-medium''',
                    data = (
                        Div(
                            classs='''row expanded app-dashboard-top-nav-bar''',
                            data = (
                                Div(
                                    classs='''columns medium-2''',
                                    data = (
                                        Button(
                                            data_toggle='''app-dashboard-sidebar''',
                                            classs='''menu-icon hide-for-medium''',
                                        ), 
                                        A(
                                            classs='''app-dashboard-logo''',
                                            data = ('''Foundation''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''columns show-for-medium''',
                                    data = (
                                        Div(
                                            classs='''app-dashboard-search-bar-container''',
                                            data = (
                                                Input(
                                                    classs='''app-dashboard-search''',
                                                    typee='''search''',
                                                    placeholder='''Search''',
                                                ), 
                                                I(
                                                    classs='''app-dashboard-search-icon fa fa-search''',
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''columns shrink app-dashboard-top-bar-actions''',
                                    data = (
                                        Button(
                                            href='''#''',
                                            classs='''button hollow''',
                                            data = ('''Logout''',)
                                        ), 
                                        A(
                                            href='''#''',
                                            height='''30''',
                                            width='''30''',
                                            alt='',
                                            data = (
                                                I(
                                                    classs='''fa fa-info-circle''',
                                                ), )
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''app-dashboard-body off-canvas-wrapper''',
                            data = (
                                Div(
                                    id='''app-dashboard-sidebar''',
                                    classs='''app-dashboard-sidebar position-left off-canvas off-canvas-absolute reveal-for-medium''',
                                    data_off_canvas='',
                                    data = (
                                        Div(
                                            classs='''app-dashboard-sidebar-title-area''',
                                            data = (
                                                Div(
                                                    classs='''app-dashboard-close-sidebar''',
                                                    data = (
                                                        H3(
                                                            classs='''app-dashboard-sidebar-block-title''',
                                                            data = ('''Items''',)
                                                        ), 
                                                        Button(
                                                            id='''close-sidebar''',
                                                            data_app_dashboard_toggle_shrink='',
                                                            classs='''app-dashboard-sidebar-close-button show-for-medium''',
                                                            aria_lable='''Close menu''',
                                                            typee='''button''',
                                                            data = (
                                                                Span(
                                                                    aria_hidden='''true''',
                                                                    data = (
                                                                        A(
                                                                            href='''#''',
                                                                            data = (
                                                                                I(
                                                                                    classs='''large fa fa-angle-double-left''',
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''app-dashboard-open-sidebar''',
                                                    data = (
                                                        Button(
                                                            id='''open-sidebar''',
                                                            data_app_dashboard_toggle_shrink='',
                                                            classs='''app-dashboard-open-sidebar-button show-for-medium''',
                                                            aria_lable='''open menu''',
                                                            typee='''button''',
                                                            data = (
                                                                Span(
                                                                    aria_hidden='''true''',
                                                                    data = (
                                                                        A(
                                                                            href='''#''',
                                                                            data = (
                                                                                I(
                                                                                    classs='''large fa fa-angle-double-right''',
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Div(
                                            classs='''app-dashboard-sidebar-inner''',
                                            data = (
                                                Ul(
                                                    classs='''menu vertical''',
                                                    data = (
                                                        Li(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    classs='''is-active''',
                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-institution''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Buildings''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-hourglass''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Time''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-industry''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Industry''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    classs='''is-active''',
                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-institution''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Buildings''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-hourglass''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Time''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-industry''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Industry''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(
                                                                    href='''#''',
                                                                    classs='''is-active''',
                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-institution''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Buildings''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-hourglass''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Time''',)
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Li(

                                                            data = (
                                                                A(

                                                                    data = (
                                                                        I(
                                                                            classs='''large fa fa-industry''',
                                                                        ), 
                                                                        Span(
                                                                            classs='''app-dashboard-sidebar-text''',
                                                                            data = ('''Industry''',)
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''app-dashboard-body-content off-canvas-content''',
                                    data_off_canvas_content='',
                                    data = (
                                        H2(
                                            classs='''text-center''',
                                            data = ('''Lorem Ipsum''',)
                                        ), 
                                        P(

                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit ligula eget est feugiat viverra. Duis a arcu laoreet, rhoncus libero imperdiet, placerat velit. Vestibulum euismod mi et ornare sodales. Donec efficitur mattis blandit. Proin in massa elit. Praesent malesuada iaculis nisl, a venenatis dui. Nullam venenatis tincidunt placerat. Suspendisse egestas urna a aliquet pretium.''',)
                                        ), 
                                        P(

                                            data = ('''Curabitur ullamcorper mollis lobortis. Integer a scelerisque turpis, sed dictum lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam quis placerat sem. Suspendisse vulputate, leo ac sollicitudin lobortis, dui dui blandit justo, ut molestie justo sem in ipsum. Vestibulum convallis ex ac est tristique tincidunt. Vivamus dui dui, viverra et urna vitae, aliquam facilisis erat. Nam lorem nibh, elementum semper commodo at, fermentum quis justo. Donec finibus sapien eget scelerisque rhoncus. Nullam at nisi sed mi congue vestibulum. Vivamus nec scelerisque orci, vel fringilla nisi. Sed dictum, leo in consectetur porttitor, quam nibh aliquet nisi, in pulvinar sapien ante id dui. Aliquam massa nisl, auctor eget nisl in, faucibus gravida lectus. Nullam mattis orci at turpis finibus egestas. Nam vitae lorem accumsan, tempus lectus vitae, rutrum diam. Integer pulvinar placerat magna aliquam scelerisque.''',)
                                        ), 
                                        P(

                                            data = ('''Duis consectetur magna velit, nec porttitor velit fermentum pulvinar. Duis varius justo eu varius pellentesque. Curabitur aliquet velit mauris, quis aliquam leo pharetra in. Integer rhoncus ut dui in rhoncus. Maecenas nec libero neque. Duis ac lacus at justo ullamcorper efficitur. Praesent ornare urna ante. Aliquam dapibus posuere nisl sit amet vestibulum. Quisque dapibus iaculis justo non egestas. Curabitur interdum semper justo, eget condimentum orci bibendum nec.''',)
                                        ), 
                                        P(

                                            data = ('''Vivamus pharetra massa non risus sollicitudin iaculis. Donec semper finibus hendrerit. Nam ut volutpat mauris, sit amet molestie nisi. Curabitur ac nisi urna. Nulla id turpis nec dui ornare tempor in ac justo. Cras quis cursus nisi. Donec vel pellentesque ante. Maecenas non nisi risus. Praesent posuere scelerisque varius. Cras vitae mollis quam. Etiam ut dui massa. Etiam mattis aliquam enim, eget facilisis erat elementum eu. Proin et lorem volutpat, pretium massa a, venenatis mi. Suspendisse quam orci, feugiat eget suscipit ac, vehicula a ante. Nam ut mauris at tortor cursus interdum.''',)
                                        ), 
                                        P(

                                            data = ('''Nullam hendrerit tincidunt risus. Sed nec nibh vel nibh euismod lobortis sed a sem. Nulla nec libero dolor. Pellentesque non sodales orci. Phasellus odio ligula, varius non orci ac, fermentum pulvinar nibh. Aliquam erat volutpat. Curabitur vehicula varius porttitor. Integer purus sapien, placerat sodales eros et, interdum vestibulum sem. Duis faucibus felis vitae augue ultricies, aliquet tempor orci vestibulum. Duis eu justo mi. Praesent feugiat, ante interdum fringilla auctor, ex nibh aliquet neque, sed feugiat tellus tortor non dui. Suspendisse potenti. Aliquam fringilla sapien felis, at faucibus justo interdum congue.''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)