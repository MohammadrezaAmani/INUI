from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Div(
                    classs="""ecommerce-loading-button text-center""",
                    data=(
                        Div(
                            classs="""loading-button""",
                            data=(
                                Button(
                                    typee="""button""",
                                    classs="""primary button""",
                                    data_loading_start="",
                                    data=(
                                        """
      Submit Order
    """,
                                    ),
                                ),
                                Button(
                                    typee="""button""",
                                    classs="""primary button hide""",
                                    data_loading_end="",
                                    data=(
                                        I(
                                            classs="""fa fa-refresh fa-spin""",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Div(
                            data_success_message="",
                            classs="""callout success hide""",
                            data=(
                                """
    Thanks, your order has been processed!
  """,
                            ),
                        ),
                    ),
                ),
            )
        ),
    )
)
