from inui.base import Class
from inui.elements import H1, Header, Html, Title
from inui import tailwind as tw

print(
    Html(
        Header(Title("Mohammadreza"), tw.TailwindCSS),
        H1("Man Mohammadreza Hastam", classs=Class(tw.capitalize, tw.align)),
    )
)
