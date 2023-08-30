from inui.config.replaces import reverse_replace

try:
    from lxml import etree
except:
    raise "you have to install lxml module: python3 -m pip install lxml"

import re


class Element:
    def __init__(self, name="", children=None, attributes=None, data=None):
        self.name = reverse_replace(name).capitalize()
        self.children = children if children is not None else []
        self.attributes = attributes if attributes is not None else {}
        self.data = data

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, indent=0):
        element_str = ""
        if indent == 0:
            element_str += "from inui.elements import *\nfrom inui.svg import *\n"
        attind = " " * (indent + 4)
        attributes_str = "\n".join(
            [
                f"{attind}{reverse_replace(attr)}='''{value}''',"
                for attr, value in self.attributes.items()
            ]
        )
        element_str += f"{' ' * indent}{self.name}(\n{attributes_str}"

        # element_str = f"{' ' * indent}"
        if self.data or self.children:
            element_str += "\n" + attind + "data = ("
        if self.data:
            if self.data.strip():
                # print(self.data)
                element_str += f"'''{self.data}'''," if self.data else ""
        for child in self.children:
            if type(child) == str:
                # print(type(child))
                element_str += "\n'''" + child.__str__(indent + 8) + ", '''"
            else:
                element_str += "\n" + child.__str__(indent + 8) + ", "
        if self.data or self.children:
            element_str += ")"
        element_str += f"\n{' ' * indent})"
        while "''''''" in element_str:
            element_str = element_str.replace("''''''", "''")
        while "''''" in element_str:
            element_str = element_str.replace("''''", "'''")
        return element_str


def create_element_tree(html_text):
    root = etree.HTML(html_text)
    return create_element_from_etree(root)


def create_element_from_etree(element):
    attributes = {}
    if element.attrib:
        attributes = element.attrib

    children = []
    for child in element:
        children.append(create_element_from_etree(child))

    data = element.text if element.text else None

    return Element(
        name=element.tag, children=children, attributes=attributes, data=data
    )


class HtmlToInui:
    def __init__(
        self, html=None, url=None, fileName=None, saveTo=None, indent=4
    ) -> None:
        self.html = html
        self.url = url
        self.filename = fileName
        self.indent = indent
        self.inui = None

    def toInui(self, html_text):
        root = etree.HTML(self.remove_html_comments(html_text))
        return self.__create_element_from_etree(root)

    def remove_html_comments(self, html):
        pattern = r"<!--(.*?)-->"
        clean_html = re.sub(pattern, "", html, flags=re.DOTALL)
        return clean_html

    def __create_element_from_etree(self, element):
        attributes = {}
        if element.attrib:
            attributes = element.attrib

        children = []
        for child in element:
            children.append(self.__create_element_from_etree(child))

        data = element.text if element.text else None

        self.inui = Element(
            name=element.tag, children=children, attributes=attributes, data=data
        )
        return self.inui

    def fromUrl(self, url):
        try:
            import requests
        except:
            raise 'requests package not found, try: "python3 -m pip install requests"'
        self.url = url
        self.html = requests.get(self.url).text
        return self.toInui(self.html)

    def fromFile(self, path=None):
        if path != None:
            self.filename = path
        with open(self.filename, "r", encoding="utf-8") as f:
            self.html = f.read()
        return self.toInui(self.html)

    def save(self, path):
        if self.inui:
            self.toInui(self.html)
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(self.inui))
        return True
