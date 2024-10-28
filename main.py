from inui.css import CSS, align_content, all, margin
from inui.css.size import Px

print({margin(): margin.auto() + Px(1) + Px(2)})

print(str("salam" > all.inherit()))

print(
    CSS(
        {".h1": align_content + Px(1)},
        {".h1": align_content + Px(1)},
        {".h1": align_content.center + Px(1)},
        h2=align_content + Px(1),
    )
)
