from inui.elements import H2, H3, Html
from inui.query import select

print(
    select(
        Html(
            H2("Mobina", "Mohammadreza", style="black"),
            H3("Maryam", style="black"),
        ),
        "___class_name",
    )
)
