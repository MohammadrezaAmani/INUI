from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''multi-step-checkout-process''',
                    data = (
                        Div(
                            classs='''multi-step-checkout-process-step''',
                            data = (
                                Ul(
                                    classs='''accordion''',
                                    data_accordion='',
                                    data = (
                                        Li(
                                            classs='''accordion-item is-active''',
                                            data_accordion_item='',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''accordion-title''',
                                                    data = ('''1. Shipping ''',
                                                        Span(
                                                            classs='''multi-step-checkout-step-title-subheader''',
                                                            data = ('''Step 1 of 3''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''accordion-content''',
                                                    data_tab_content='',
                                                    data = (
                                                        Form(
                                                            classs='''multi-step-checkout-form''',
                                                            data = (
                                                                Div(
                                                                    classs='''row''',
                                                                    data = (
                                                                        Div(
                                                                            classs='''small-12 medium-9 column''',
                                                                            data = (
                                                                                Div(
                                                                                    classs='''shipping-address multi-step-checkout-step-section''',
                                                                                    data = (
                                                                                        H6(
                                                                                            classs='''multi-step-checkout-step-subheader''',
                                                                                            data = ('''Shipping Address''',)
                                                                                        ), 
                                                                                        P(
                                                                                            classs='''multi-step-checkout-step-subdesc''',
                                                                                            data = ('''Please enter your shipping address. Only USPS ships to APO, FPO, or PO Boxes. ''',
                                                                                                A(
                                                                                                    href='''#''',
                                                                                                    classs='''text-link''',
                                                                                                    data = ('''Shipping Rates and Delivery Times''',)
                                                                                                ), )
                                                                                        ), 
                                                                                        Label(

                                                                                            data = (
                                                                                                Input(
                                                                                                    typee='''text''',
                                                                                                    placeholder='''First Name''',
                                                                                                    required='',
                                                                                                ), 
                                                                                                Input(
                                                                                                    typee='''text''',
                                                                                                    placeholder='''Last Name''',
                                                                                                    required='',
                                                                                                ), 
                                                                                                Input(
                                                                                                    typee='''text''',
                                                                                                    placeholder='''Address''',
                                                                                                    required='',
                                                                                                ), 
                                                                                                Div(
                                                                                                    classs='''row''',
                                                                                                    data = (
                                                                                                        Div(
                                                                                                            classs='''small-12 medium-7 column''',
                                                                                                            data = (
                                                                                                                Input(
                                                                                                                    typee='''text''',
                                                                                                                    placeholder='''City''',
                                                                                                                    required='',
                                                                                                                ), )
                                                                                                        ), 
                                                                                                        Div(
                                                                                                            classs='''small-6 medium-2 column''',
                                                                                                            data = (
                                                                                                                Select(
                                                                                                                    required='',
                                                                                                                    data = (
                                                                                                                        Option(
                                                                                                                            value='''state1''',
                                                                                                                            data = ('''AL''',)
                                                                                                                        ), 
                                                                                                                        Option(
                                                                                                                            value='''state2''',
                                                                                                                            data = ('''AK''',)
                                                                                                                        ), 
                                                                                                                        Option(
                                                                                                                            value='''state3''',
                                                                                                                            data = ('''AZ''',)
                                                                                                                        ), 
                                                                                                                        Option(
                                                                                                                            value='''state4''',
                                                                                                                            data = ('''AR''',)
                                                                                                                        ), 
                                                                                                                        Option(
                                                                                                                            value='''state5''',
                                                                                                                            data = ('''CA''',)
                                                                                                                        ), )
                                                                                                                ), )
                                                                                                        ), 
                                                                                                        Div(
                                                                                                            classs='''small-6 medium-3 column''',
                                                                                                            data = (
                                                                                                                Input(
                                                                                                                    typee='''text''',
                                                                                                                    placeholder='''ZIP''',
                                                                                                                    required='',
                                                                                                                ), )
                                                                                                        ), )
                                                                                                ), 
                                                                                                Div(

                                                                                                    data = (
                                                                                                        Hr(
                                                                                                            classs='''multi-step-checkout-form-divider''',
                                                                                                        ), )
                                                                                                ), 
                                                                                                Input(
                                                                                                    typee='''text''',
                                                                                                    placeholder='''Email''',
                                                                                                    required='',
                                                                                                ), 
                                                                                                Input(
                                                                                                    typee='''text''',
                                                                                                    placeholder='''Phone''',
                                                                                                    required='',
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Div(
                                                                                    classs='''multi-step-checkout-shipping-options multi-step-checkout-step-section''',
                                                                                    data = (
                                                                                        H6(
                                                                                            classs='''multi-step-checkout-step-subheader''',
                                                                                            data = ('''Shipping Options''',)
                                                                                        ), 
                                                                                        Div(
                                                                                            classs='''row multi-step-checkout-shipping-option''',
                                                                                            data = (
                                                                                                Label(

                                                                                                    data = (
                                                                                                        Div(
                                                                                                            classs='''small-10 column''',
                                                                                                            data = (
                                                                                                                Input(
                                                                                                                    typee='''radio''',
                                                                                                                    name='''multi-step-checkout-shipping-option''',
                                                                                                                    value='''ups-ground-shipping''',
                                                                                                                    classs='''multi-step-checkout-shipping-option-selection''',
                                                                                                                    checked='''checked''',
                                                                                                                ), 
                                                                                                                Span(
                                                                                                                    classs='''multi-step-checkout-shipping-option-title''',
                                                                                                                    data = ('''UPS Ground (4–5 business days) - Recommended''',)
                                                                                                                ), 
                                                                                                                Div(
                                                                                                                    classs='''multi-step-checkout-shipping-option-desc''',
                                                                                                                    data = ('''Same-day shipping of in-stock items for orders placed before 3pm EST. Realtime tracking included.''',)
                                                                                                                ), )
                                                                                                        ), 
                                                                                                        Div(
                                                                                                            classs='''small-2 column multi-step-checkout-shipping-cost''',
                                                                                                            data = ('''
                        $25.00
                      ''',)
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), 
                                                                                        Div(
                                                                                            classs='''row multi-step-checkout-shipping-option''',
                                                                                            data = (
                                                                                                Label(

                                                                                                    data = (
                                                                                                        Div(
                                                                                                            classs='''small-10 column''',
                                                                                                            data = (
                                                                                                                Input(
                                                                                                                    typee='''radio''',
                                                                                                                    name='''multi-step-checkout-shipping-option''',
                                                                                                                    value='''usps-shipping''',
                                                                                                                    classs='''multi-step-checkout-shipping-option-selection''',
                                                                                                                ), 
                                                                                                                Span(
                                                                                                                    classs='''multi-step-checkout-shipping-option-title''',
                                                                                                                    data = ('''USPS  (6–12 business days)''',)
                                                                                                                ), 
                                                                                                                Div(
                                                                                                                    classs='''multi-step-checkout-shipping-option-desc''',
                                                                                                                    data = ('''Tracking is available after 48 hours.''',)
                                                                                                                ), )
                                                                                                        ), 
                                                                                                        Div(
                                                                                                            classs='''small-2 column multi-step-checkout-shipping-cost''',
                                                                                                            data = ('''
                        $15.00
                      ''',)
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Div(
                                                                                    classs='''multi-step-checkout-enews-sign-up''',
                                                                                    data = (
                                                                                        Fieldset(

                                                                                            data = (
                                                                                                Input(
                                                                                                    classs='''multi-step-checkout-enews-sign-up-checkbox''',
                                                                                                    id='''multi-step-checkout-enews-sign-up-checkbox''',
                                                                                                    typee='''checkbox''',
                                                                                                ), 
                                                                                                Label(
                                                                                                    forr='''#multi-step-checkout-enews-sign-up-checkbox''',
                                                                                                    data = ('''Please add me to your eNewsletter list so I can receive special promotions and product updates.''',)
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Button(
                                                                                    classs='''primary button expanded''',
                                                                                    data = ('''Continue to Payment''',)
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(
                                            classs='''accordion-item''',
                                            data_accordion_item='',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''accordion-title''',
                                                    data = ('''2. Payment ''',
                                                        Span(
                                                            classs='''multi-step-checkout-step-title-subheader''',
                                                            data = ('''Step 2 of 3''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''accordion-content''',
                                                    data_tab_content='',
                                                    data = (
                                                        Form(
                                                            classs='''multi-step-checkout-form''',
                                                            data = (
                                                                Div(
                                                                    classs='''row''',
                                                                    data = (
                                                                        Div(
                                                                            classs='''small-12 medium-9 column''',
                                                                            data = (
                                                                                Div(
                                                                                    classs='''multi-step-checkout-billing-address''',
                                                                                    data = (
                                                                                        Fieldset(

                                                                                            data = (
                                                                                                Input(
                                                                                                    classs='''multi-step-checkout-billing-address-checkbox''',
                                                                                                    id='''multi-step-checkout-billing-address-checkbox''',
                                                                                                    typee='''checkbox''',
                                                                                                    checked='''checked''',
                                                                                                ), 
                                                                                                Label(
                                                                                                    forr='''multi-step-checkout-billing-address-checkbox''',
                                                                                                    data = ('''My Billing Address is the same as my Shipping Address.''',)
                                                                                                ), )
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''multi-step-checkout-billing-address-list''',
                                                                                            data = (
                                                                                                Li(
                                                                                                    classs='''multi-step-checkout-billing-name''',
                                                                                                    data = ('''John Smith''',)
                                                                                                ), 
                                                                                                Li(
                                                                                                    classs='''multi-step-checkout-billing-street''',
                                                                                                    data = ('''123 Market St.''',)
                                                                                                ), 
                                                                                                Li(
                                                                                                    classs='''multi-step-checkout-billing-city-state''',
                                                                                                    data = ('''San Francisco, CA 94134''',)
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Div(

                                                                                    data = (
                                                                                        Hr(
                                                                                            classs='''multi-step-checkout-form-divider''',
                                                                                        ), )
                                                                                ), 
                                                                                Div(
                                                                                    classs='''multi-step-checkout-credit-card-info''',
                                                                                    data = (
                                                                                        H6(
                                                                                            classs='''multi-step-checkout-step-subheader''',
                                                                                            data = ('''Credit Card''',)
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''multi-step-checkout-payment-icons''',
                                                                                            data = (
                                                                                                Li(

                                                                                                    data = (
                                                                                                        Img(
                                                                                                            classs='''multi-step-checkout-payment-icon''',
                                                                                                            src='''https://placehold.it/50x50''',
                                                                                                        ), )
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = (
                                                                                                        Img(
                                                                                                            classs='''multi-step-checkout-payment-icon''',
                                                                                                            src='''https://placehold.it/50x50''',
                                                                                                        ), )
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = (
                                                                                                        Img(
                                                                                                            classs='''multi-step-checkout-payment-icon''',
                                                                                                            src='''https://placehold.it/50x50''',
                                                                                                        ), )
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = (
                                                                                                        Img(
                                                                                                            classs='''multi-step-checkout-payment-icon''',
                                                                                                            src='''https://placehold.it/50x50''',
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), 
                                                                                        Input(
                                                                                            typee='''text''',
                                                                                            placeholder='''Card Name''',
                                                                                            required='',
                                                                                        ), 
                                                                                        Input(
                                                                                            typee='''text''',
                                                                                            placeholder='''Card Number''',
                                                                                            required='',
                                                                                        ), 
                                                                                        Div(
                                                                                            classs='''row''',
                                                                                            data = (
                                                                                                Div(
                                                                                                    classs='''small-4 column''',
                                                                                                    data = (
                                                                                                        Select(
                                                                                                            required='',
                                                                                                            data = (
                                                                                                                Option(
                                                                                                                    value='''january''',
                                                                                                                    data = ('''01''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''february''',
                                                                                                                    data = ('''02''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''march''',
                                                                                                                    data = ('''03''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''april''',
                                                                                                                    data = ('''04''',)
                                                                                                                ), )
                                                                                                        ), )
                                                                                                ), 
                                                                                                Div(
                                                                                                    classs='''small-4 column''',
                                                                                                    data = (
                                                                                                        Select(
                                                                                                            required='',
                                                                                                            data = (
                                                                                                                Option(
                                                                                                                    value='''year1''',
                                                                                                                    data = ('''2019''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''year2''',
                                                                                                                    data = ('''2018''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''year3''',
                                                                                                                    data = ('''2017''',)
                                                                                                                ), 
                                                                                                                Option(
                                                                                                                    value='''year4''',
                                                                                                                    data = ('''2016''',)
                                                                                                                ), )
                                                                                                        ), )
                                                                                                ), 
                                                                                                Div(
                                                                                                    classs='''small-4 column''',
                                                                                                    data = (
                                                                                                        Input(
                                                                                                            typee='''text''',
                                                                                                            placeholder='''CVV''',
                                                                                                            required='',
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), 
                                                                                        Div(

                                                                                            data = (
                                                                                                Hr(
                                                                                                    classs='''multi-step-checkout-form-divider''',
                                                                                                ), )
                                                                                        ), 
                                                                                        Label(
                                                                                            forr='''apply-gift-card-code''',
                                                                                            data = (''' Gift Card ''',
                                                                                                Span(

                                                                                                    data = ('''(optional)''',)
                                                                                                ), 
                                                                                                Div(
                                                                                                    classs='''input-group gift-card''',
                                                                                                    data = (
                                                                                                        Input(
                                                                                                            classs='''input-group-field''',
                                                                                                            typee='''text''',
                                                                                                            placeholder='''Code''',
                                                                                                        ), 
                                                                                                        Div(
                                                                                                            classs='''input-group-button''',
                                                                                                            placeholder='''$''',
                                                                                                            data = (
                                                                                                                Input(
                                                                                                                    typee='''submit''',
                                                                                                                    classs='''button primary''',
                                                                                                                    value='''Apply''',
                                                                                                                    id='''apply-gift-card-code''',
                                                                                                                ), )
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), 
                                                                                        Div(

                                                                                            data = (
                                                                                                Hr(
                                                                                                    classs='''multi-step-checkout-form-divider''',
                                                                                                ), )
                                                                                        ), 
                                                                                        Button(
                                                                                            classs='''primary button expanded''',
                                                                                            data = ('''Continue to Review Order''',)
                                                                                        ), )
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), 
                                        Li(
                                            classs='''accordion-item''',
                                            data_accordion_item='',
                                            data = (
                                                A(
                                                    href='''#''',
                                                    classs='''accordion-title''',
                                                    data = ('''3. Review Order ''',
                                                        Span(
                                                            classs='''multi-step-checkout-step-title-subheader''',
                                                            data = ('''Step 3 of 3''',)
                                                        ), )
                                                ), 
                                                Div(
                                                    classs='''accordion-content''',
                                                    data_tab_content='',
                                                    data = (
                                                        Hr(
                                                            classs='''show-for-small-only order-table-divider''',
                                                        ), 
                                                        Table(
                                                            classs='''order-table-content stack''',
                                                            data = (
                                                                Thead(

                                                                    data = (
                                                                        Tr(

                                                                            data = (
                                                                                Th(
                                                                                    width='''120''',
                                                                                    data = ('''Order''',)
                                                                                ), 
                                                                                Th(
                                                                                    width='''350''',
                                                                                ), 
                                                                                Th(
                                                                                    width='''80''',
                                                                                    data = ('''Quantity''',)
                                                                                ), 
                                                                                Th(
                                                                                    width='''100''',
                                                                                    data = ('''Price Each''',)
                                                                                ), 
                                                                                Th(
                                                                                    width='''60''',
                                                                                    data = ('''Total''',)
                                                                                ), )
                                                                        ), )
                                                                ), 
                                                                Tbody(

                                                                    data = (
                                                                        Tr(
                                                                            classs='''order-item''',
                                                                            data = (
                                                                                Td(

                                                                                    data = (
                                                                                        Img(
                                                                                            classs='''order-product-image''',
                                                                                            src='''https://placehold.it/100x100''',
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''order-product-title''',
                                                                                            data = ('''Product 1''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-vendor''',
                                                                                            data = ('''Vendor 1''',)
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''order-product-info''',
                                                                                            data = (
                                                                                                Li(

                                                                                                    data = ('''In Stock''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Product SKU: 12345''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''A great Product''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Details: You won't be sad''',)
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Qty:''',)
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Price Each: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = (''',''',)
                                                                                        ), 
                                                                                        Br(
                                                                                            classs='''hide-for-small-only''',
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price-saving''',
                                                                                            data = ('''
                  You save:
                  ''',
                                                                                                Br(
                                                                                                    classs='''hide-for-small-only''',
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Total: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-total''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), )
                                                                                ), )
                                                                        ), 
                                                                        Tr(
                                                                            classs='''order-item''',
                                                                            data = (
                                                                                Td(

                                                                                    data = (
                                                                                        Img(
                                                                                            classs='''order-product-image''',
                                                                                            src='''https://placehold.it/100x100''',
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''order-product-title''',
                                                                                            data = ('''Product 2''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-vendor''',
                                                                                            data = ('''Vendor 1''',)
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''order-product-info''',
                                                                                            data = (
                                                                                                Li(

                                                                                                    data = ('''In Stock''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Product SKU: 12345''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''A great Product''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Details: You won't be sad''',)
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Qty:''',)
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Price Each: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = (''',''',)
                                                                                        ), 
                                                                                        Br(
                                                                                            classs='''hide-for-small-only''',
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price-saving''',
                                                                                            data = ('''
                  You save:
                  ''',
                                                                                                Br(
                                                                                                    classs='''hide-for-small-only''',
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Total: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-total''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), )
                                                                                ), )
                                                                        ), 
                                                                        Tr(
                                                                            classs='''order-item''',
                                                                            data = (
                                                                                Td(

                                                                                    data = (
                                                                                        Img(
                                                                                            classs='''order-product-image''',
                                                                                            src='''https://placehold.it/100x100''',
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''order-product-title''',
                                                                                            data = ('''Product 3''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-vendor''',
                                                                                            data = ('''Vendor 1''',)
                                                                                        ), 
                                                                                        Ul(
                                                                                            classs='''order-product-info''',
                                                                                            data = (
                                                                                                Li(

                                                                                                    data = ('''In Stock''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Product SKU: 12345''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''A great Product''',)
                                                                                                ), 
                                                                                                Li(

                                                                                                    data = ('''Details: You won't be sad''',)
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Qty:''',)
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Price Each: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = (''',''',)
                                                                                        ), 
                                                                                        Br(
                                                                                            classs='''hide-for-small-only''',
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-price-saving''',
                                                                                            data = ('''
                  You save:
                  ''',
                                                                                                Br(
                                                                                                    classs='''hide-for-small-only''',
                                                                                                ), )
                                                                                        ), )
                                                                                ), 
                                                                                Td(

                                                                                    data = (
                                                                                        Span(
                                                                                            classs='''show-for-small-only''',
                                                                                            data = ('''Total: ''',)
                                                                                        ), 
                                                                                        Span(
                                                                                            classs='''order-product-total''',
                                                                                            data = ('''$25.00''',)
                                                                                        ), )
                                                                                ), )
                                                                        ), )
                                                                ), )
                                                        ), 
                                                        Div(
                                                            classs='',
                                                            data = (
                                                                Div(
                                                                    classs='''row''',
                                                                    data = (
                                                                        Div(
                                                                            classs='''small-12 medium-9 column multi-step-checkout-create-account''',
                                                                            data = (
                                                                                H6(
                                                                                    classs='''multi-step-checkout-step-subheader''',
                                                                                    data = ('''Create an Account ''',
                                                                                        Span(

                                                                                            data = ('''(optional)''',)
                                                                                        ), )
                                                                                ), 
                                                                                P(
                                                                                    classs='''create-account-desc''',
                                                                                    data = ('''Save and review your orders in your account.''',)
                                                                                ), 
                                                                                Form(

                                                                                    data = (
                                                                                        Div(
                                                                                            classs='''row''',
                                                                                            data = (
                                                                                                Div(
                                                                                                    classs='''small-12 medium-6 column''',
                                                                                                    data = (
                                                                                                        Input(
                                                                                                            typee='''text''',
                                                                                                            placeholder='''Password''',
                                                                                                        ), )
                                                                                                ), 
                                                                                                Div(
                                                                                                    classs='''small-12 medium-6 column''',
                                                                                                    data = (
                                                                                                        Input(
                                                                                                            typee='''text''',
                                                                                                            placeholder='''Confirm Password''',
                                                                                                        ), )
                                                                                                ), )
                                                                                        ), )
                                                                                ), )
                                                                        ), )
                                                                ), 
                                                                Div(

                                                                    data = (
                                                                        Hr(
                                                                            classs='''multi-step-checkout-form-divider''',
                                                                        ), )
                                                                ), 
                                                                Form(

                                                                    data = (
                                                                        Label(
                                                                            forr='',
                                                                            data = ('''Comments
                ''',
                                                                                Textarea(
                                                                                    name='',
                                                                                    id='',
                                                                                    cols='''30''',
                                                                                    rows='''2''',
                                                                                ), )
                                                                        ), 
                                                                        Button(
                                                                            classs='''primary button expanded''',
                                                                            data = ('''Submit Order''',)
                                                                        ), )
                                                                ), )
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)