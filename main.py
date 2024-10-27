from inui import bootstrap as bs
from inui.base import Class
from inui.elements import H1, Body, Header, Hr, Html, Title

print(
    Html(
        Header(
            Title("Mohammadreza"),
            bs.BootStrapCSS,
        ),
        Body(
            H1(
                "salam Man Mohammadreza Hastam.",
                class_=Class(bs.AccordionBody, bs.Active),
            ),
            Hr,
            bs.BootStrapJS,
        ),
    )
)
