# INUI

<p align="center">
    <a>
        <img src="./assets/images/inui.png" alt="UniLand" width="256">
    </a>
    <br>
    <b>Powerful and Highly Customizable Python Library for UI</b>
    <br>
    <a href="https://github.com/MohammadrezaAmani/INUI">
        GitHub
    </a>
    •
    <a href="#">
        Documentation
    </a>
    •
    <a href="https://t.me/PyINUI">
        Channel
    </a>
    •
    <a href="mailto:More.amani@yahoo.com">
        Support
    </a>
</p>

<br>

# Py INUI

**INUI** is a powerful and highly customizable Python language library for **UI**, which supports all the components and elements of the html markup language in [Python](https://python.org/), as well as the ability to use libraries such as [Bootstrap](https://getbootstrap.com/), etc. And it brings a new experience of easier work with frontend in Python.

## Contents

<!-- vscode-markdown-toc -->

- [INUI](#inui)
- [Py INUI](#py-inui)
  - [Contents](#contents)
  - [Requirements](#requirements)
    - [**Python Compatibility**](#python-compatibility)
    - [**Dependencies**](#dependencies)
  - [In A Nutshell](#in-a-nutshell)
  - [How to Use?](#how-to-use)
  - [Supported Elements](#supported-elements)
  - [LICENSE](#license)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->

<!-- /vscode-markdown-toc -->

## Requirements

### **Python Compatibility**

This Library is written entirely in python. tested versions are `python 3.11, 3.10, 3.9, 3.8, 3.7` while older versions
should not cause any problem, we recommend using the latest version of `python3`.

### **Dependencies**

This package requires the following packages:

* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/ "BeautifulSoup4") - for Prettifing Code

## In A Nutshell

> you can find more examples in [examples](./examples) directory

```python3
from inui.elements import (
    Body,
    Head,
    Html,
    Title,
    H1,
    Div,
    Button,
    Link,
    Meta,
    Span,
    Form,
    Input,
    Script,
    Comment,
)

h = Html(data=(
    Comment("this is black door =`) "),
    Head(
        (
            Title("Wiki Clone"),
            Meta(charset="utf-8"),
            Meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0",
            ),
            Link(rel="stylesheet", href="./style.css"),
        )
    ),
    Body(
        (

            Div(
                (
                    Div(
                        (
                            H1("search wiki"),
                            Span("light", id="theme-toggler"),
                        ),
                        classs="header-container",
                    )
                ),
                classs="container",
            ),
            Form(
                (
                    Input(
                        typee="text", placeholder="search wiki", id="search-input"
                    ),
                    Button(typee="submit", text="search",
                           id="search-button"),
                ),
                id="search-form",
            ),
            Div(id="search-results"),
            Script(src="./script.js"),
        ),
    ),
),)

```

## How to Use?

> read the [documentation](https://inui.readthedocs.io/en/latest/) for more information



```bash
pip install inui --upgrade
```

## Supported Elements

| id | HTML | INUI | id | HTML | INUI | id | HTML | INUI |
| --|-- | --------- | --|-- | --------- |--|-- | --------- |
| 1|'<> </> ' | BaseElement| 45|figure | Figure|89|em | Em|
| 2|</> | BaseVoidElement | 46|font | Font|90|pre | Pre|
| 3|!DOCTYPE html | Doctype| 47|footer | Footer|91|progress | Progress|
| 4|abbr | Abbr| 48|form | Form|92|q | Q|
| 5|acronym | Acronym| 49|frame | Frame|93|rp | Rp|
| 6|address | Address| 50|frameset | Frameset|94|rt | Rt|
| 7|a | A| 51|head | Head|95|ruby | Ruby|
| 8|applet | Applet| 52|header | Header|96|s | S|
| 9|area | Area| 53|h1 | H1|97|samp | Samp|
| 10|article | Article| 54|h2 | H2|98|script | Script|
| 11|aside | Aside| 55|h3 | H3|99|section | Section|
| 12|audio | Audio| 56|h4 | H4|100|small | Small|
| 13|base | Base| 57|h5 | H5|101|source | Source|
| 14|basefont | Basefont| 58|h6 | H6|102|spacer | Spacer|
| 15|bdi | Bdi| 59|hgroup | Hgroup|103|span | Span|
| 16|bdo | Bdo| 60|hr | Hr|104|strike | Strike|
| 17|bgsound | Bgsound| 61|html | Html|105|strong | Strong|
| 18|big | Big| 62|iframe | Iframe|106|style | Style|
| 19|blockquote | Blockquote| 63|img | Img|107|sub | Sub|
| 20|body | Body| 64|input | Input|108|sup | Sup|
| 21|b | B| 65|ins | Ins|109|summary | Summary|
| 22|br | Br| 66|isindex | Isindex|110|svg | Svg|
| 23|button | Button| 67|i | I|111|table | Table|
| 24|caption | Caption| 68|kbd | Kbd|112|tbody | Tbody|
| 25|canvas | Canvas| 69|keygen | Keygen|113|td | Td|
| 26|center | Center| 70|label | Label|114|template | Template|
| 27|cite | Cite| 71|legend | Legend|115|tfoot | Tfoot|
| 28|code | Code| 72|li | Li|116|th | Th|
| 29|colgroup | Colgroup| 73|main | Main|117|thead | Thead|
| 30|col | Col| 74|mark | Mark|118|time | Time|
| 31|comment | Comment| 75|marquee | Marquee|119|title | Title|
| 32|data | Data| 76|menuitem | Menuitem|120|tr | Tr|
| 33|datalist | Datalist| 77|meta | Meta|121|track | Track|
| 34|dd | Dd| 78|meter | Meter|122|tt | Tt|
| 35|dfn | Dfn| 79|nav | Nav|123|u | U|
| 36|del | Del| 80|nobr | Nobr|124|var | Var|
| 37|details | Details| 81|noembed | Noembed|125|video | Video|
| 38|dialog | Dialog| 82|noscript | Noscript|126|wbr | Wbr|
| 39|dir | Dir| 83|object | Object|127|xmp | Xmp|
| 40|div | Div| 84|ol | Ol|
| 41|dl | Dl| 85|optgroup | Optgroup|
| 42|embed | Embed| 86|option | Option|
| 43|fieldset | Fieldset| 87|output | Output|
| 44|figcaption | Figcaption| 88|p | P|

## LICENSE

Distributed under the MIT License. See `LICENSE` for more information.
