from inui.base import __from_context__, __out__
from inui.colors import Black
from inui.css import color
from inui.elements import H1

html = H1()
a = 12
result = H1()
for i in __from_context__("a", "my"):
    result | i | " "

html | (result | "Mohammadreza Amani") @ {color: Black}


__out__(html)

print(html)
