from inui.elements import A, Body, Comment, Div, Head, Hr, Html, Meta, Strong, Title

INUI_IS_THE_BEST = Div(
    Strong(
        A("INUI", href="https://github.com/MohammadrezaAmani/INUI"),
        "IS THE BEST",
        style="color:red",
    ),
    Hr(),
)

h = Html(
    Comment("this is black door =`) "),
    Head(
        Title("INUI"),
        Meta(charset="utf-8"),
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0",
        ),
    ),
    Body(
        *[INUI_IS_THE_BEST for i in range(10)],
    ),
    style="background:#000000;",
)

print(h.render())
