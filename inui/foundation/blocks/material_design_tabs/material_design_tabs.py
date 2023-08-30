from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''md-tabs''',
                    data = (
                        Div(
                            classs='''mobile-nav-bar title-bar''',
                            data = (
                                Div(
                                    classs='''title-bar-left''',
                                    data = (
                                        Button(
                                            classs='''menu-icon''',
                                            typee='''button''',
                                        ), )
                                ), 
                                Div(
                                    classs='''title-bar-center''',
                                    data = (
                                        Span(
                                            classs='''title-bar-text''',
                                            data = ('''Material Design Tabs''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''title-bar-right''',
                                    data = (
                                        Button(
                                            classs='''menu-icon''',
                                            typee='''button''',
                                        ), )
                                ), )
                        ), 
                        Ul(
                            classs='''tabs''',
                            data_responsive_accordion_tabs='''tabs small-accordion medium-tabs large-tabs''',
                            id='''collapsing-tabs''',
                            data_allow_all_closed='''true''',
                            data_multi_expand='''true''',
                            data = (
                                Li(
                                    classs='''tabs-title is-active''',
                                    data = (
                                        A(
                                            href='''#panel1c''',
                                            aria_selected='''true''',
                                            data = ('''Tab 1''',)
                                        ), )
                                ), 
                                Li(
                                    classs='''tabs-title''',
                                    data = (
                                        A(
                                            href='''#panel2c''',
                                            data = ('''Tab 2''',)
                                        ), )
                                ), 
                                Li(
                                    classs='''tabs-title''',
                                    data = (
                                        A(
                                            href='''#panel3c''',
                                            data = ('''Tab 3''',)
                                        ), )
                                ), 
                                Li(
                                    classs='''tabs-title''',
                                    data = (
                                        A(
                                            href='''#panel4c''',
                                            data = ('''Tab 4''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''slide''',
                                ), )
                        ), 
                        Div(
                            classs='''tabs-content''',
                            data_tabs_content='''collapsing-tabs''',
                            data = (
                                Div(
                                    classs='''tabs-panel is-active''',
                                    id='''panel1c''',
                                    data = (
                                        P(

                                            data = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sit amet pulvinar enim. Donec mattis metus a hendrerit aliquam. Nulla facilisi. Etiam facilisis, nisi eu varius gravida, tellus odio blandit mauris, et egestas neque sapien sit amet massa.
        Morbi ullamcorper, metus nec dictum faucibus, mauris dolor semper purus, quis tincidunt sapien nibh ut tellus. Suspendisse at lectus ac dolor commodo malesuada in non elit. Donec nibh nulla, vehicula a quam quis, luctus interdum est.
      ''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''tabs-panel''',
                                    id='''panel2c''',
                                    data = (
                                        P(

                                            data = ('''Nunc ipsum massa, venenatis sed fringilla ut, elementum eu sapien. In eget dolor volutpat, fringilla metus et, dignissim lectus. Proin interdum sit amet odio ut varius. Nam id quam lacus. Aenean et tellus a sapien pulvinar sollicitudin. Mauris posuere
        tellus urna, non fermentum urna scelerisque in. Nulla scelerisque est leo, non tempus purus laoreet in. Aliquam erat volutpat. Nunc nulla eros, blandit quis nunc vel, luctus fermentum nisi. Phasellus ullamcorper gravida facilisis.''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''tabs-panel''',
                                    id='''panel3c''',
                                    data = (
                                        P(

                                            data = ('''Donec ornare, ex quis volutpat vulputate, dui eros fermentum tellus, id eleifend velit diam non leo. Aliquam convallis vestibulum elementum. Phasellus facilisis tempus nisi eget lobortis. Duis magna sem, placerat vel tellus sed, auctor laoreet enim.
        Integer sit amet libero rutrum, vestibulum massa at, volutpat leo. Proin id ex porta, hendrerit erat sed, fringilla urna. Phasellus hendrerit consequat arcu non pretium. Proin vel velit vitae nisl aliquet rutrum. Maecenas quis lectus sit amet
        mi fermentum pulvinar. Mauris fermentum tortor id ipsum tristique sollicitudin.''',)
                                        ), )
                                ), 
                                Div(
                                    classs='''tabs-panel''',
                                    id='''panel4c''',
                                    data = (
                                        P(

                                            data = ('''Fusce justo velit, pulvinar eu sem eu, fringilla sodales urna. Mauris mollis aliquet nibh. Suspendisse porttitor, nisi a egestas iaculis, augue metus semper tortor, eget tristique leo enim mollis libero. Integer et lacus non ipsum finibus pharetra
        sit amet quis ipsum. Mauris vitae elementum lorem. Quisque vel mauris magna. Duis non nisl neque. Suspendisse posuere magna id risus sodales bibendum.''',)
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)