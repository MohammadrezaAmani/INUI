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

## LICENSE

Distributed under the MIT License. See `LICENSE` for more information.
