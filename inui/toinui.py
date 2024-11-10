import argparse
import re

try:
    from lxml import etree
except ImportError:
    raise "you must install lxml, run `python3 -m pip install lxml"
try:

    from black import FileMode, format_str
except ImportError:
    raise "you must install black, run `python3 -m pip install black"
import inui
import inui.base
import inui.bootstrap
import inui.colors
import inui.css
import inui.elements
import inui.svg
import inui.tailwind
from inui.config.replaces import reverse_replace

create_inui_template = """

#* This Element Not Found in inui project, we will create an equivalent element for you."

from inui.base import BaseElement, _Meta

class %s(BaseElement):
    _Meta = _Meta("%s", "%s")


#* -------------------------------------------------------------------------------------
"""


class Element:
    def __init__(self, name="", children=None, attributes=None, data=None):
        self.name = name
        self.children = children if children is not None else []
        self.attributes = attributes if attributes is not None else {}
        self.data = data

    def add_child(self, child):
        self.children.append(child)

    def string_quote(self, value):
        if "\n" not in value:
            if "'" in value and '"' in value:
                #! handle both ''' and """ in text
                if '"""' not in value:
                    return f'"""{value}"""'
                elif "''''" not in value:
                    return f"''''{value}''''"
            elif "'" not in value:
                return f"'{value}'"
            elif '"' not in value:
                return f'"{value}"'
        return f"'''{value}'''"

    def __str__(self, indent=0):
        element_str = ""
        # if indent == 0:
        #     element_str += self
        attind = " " * (indent + 4)
        attributes_str = "\n".join(
            [
                f"{attind}{reverse_replace(attr)}={self.string_quote(value)},"
                for attr, value in self.attributes.items()
            ]
        )
        element_str += f"{' ' * indent}{self.name}(\n"

        # element_str = f"{' ' * indent}"
        if self.data or self.children:
            element_str += "\n" + attind
        if self.data:
            if self.data.strip():
                # print(self.data)
                element_str += f"{self.string_quote(self.data)}," if self.data else ""
        for child in self.children:
            if isinstance(child, str):
                # print(type(child))
                element_str += "\n'''" + child.__str__(indent + 8) + ", '''"
            else:
                element_str += "\n" + child.__str__(indent + 8) + ", "

        element_str += f"\n{' ' * indent}"
        element_str += f"{attributes_str}"
        element_str += ")"
        while "''''''" in element_str:
            element_str = element_str.replace("''''''", "''")
        while "''''" in element_str:
            element_str = element_str.replace("''''", "'''")
        return element_str


def create_element_tree(html_text):
    root = etree.HTML(html_text)
    return create_element_from_etree(root)


def create_element_from_etree(element: etree._Element):
    attributes = {}
    if element.attrib:
        attributes = element.attrib

    children = []
    for child in element:
        children.append(create_element_from_etree(child))

    data = element.text if element.text else None

    return Element(
        name=reverse_replace(element.tag).capitalize(),
        children=children,
        attributes=attributes,
        data=data,
    )


class HtmlTo_inui:
    def __init__(
        self, html=None, url=None, fileName=None, saveTo=None, indent=4
    ) -> None:
        self.html = html
        self.url = url
        self.filename = fileName
        self.indent = indent
        self.inui = None
        self.imports = []
        self.not_imported = []

    def to_inui(self, html_text=None):
        root = etree.HTML(self._remove_html_comments(html_text or self.html or ""))
        return self.add_imports(self._create_element_from_etree(root))

    def add_imports(self, code: str):
        imports = self.manage_imports(self.imports)
        not_imported = self.create_unknown_elements()
        return self.format(
            imports
            + not_imported
            + "content = "
            + str(code)
            + "\n\n #? run via: `inui file_name:content`"
        )

    def format(self, code):
        try:
            return format_str(str(code), mode=FileMode())
        except Exception as _:
            return str(code)

    def _remove_html_comments(self, html):
        pattern = r"<!--(.*?)-->"
        clean_html = re.sub(pattern, "", html, flags=re.DOTALL)
        return clean_html

    def manage_imports(self, imports):
        places = {
            "base": [],
            "elements": [],
            "svg": [],
            "tailwind": [],
            "bootstrap": [],
            "css": [],
            "colors": [],
        }
        for imp in set(imports):
            imported = False
            for place in places:
                if imported:
                    continue
                if hasattr(getattr(inui, place), imp):
                    places[place].append(imp)
                    imported = True

            if not imported:
                self.not_imported.append(imp)

        res = ""
        for module, item in places.items():
            if item:
                res += f"from inui.{module} import {self.print_list(sorted(item))}\n"
        return res

    def print_list(self, data: tuple):
        return (
            "(" + ", ".join([str(i) for i in data]) + ")"
            if len(data) > 1
            else str(data[0]) if len(data) > 0 else ""
        )

    def _create_element_from_etree(self, element: etree._Element):
        self.imports.append(reverse_replace(element.tag).capitalize())
        attributes = {}
        if element.attrib:
            attributes = element.attrib

        children = []
        for child in element:
            children.append(self._create_element_from_etree(child))

        data = element.text if element.text else None

        self.inui = Element(
            name=reverse_replace(element.tag).capitalize(),
            children=children,
            attributes=attributes,
            data=data,
        )
        return self.inui

    def _create_element(self, name: str):
        return create_inui_template % (reverse_replace(name).capitalize(), name, name)

    def create_unknown_elements(self):
        res = ""
        for i in self.not_imported:
            res += self._create_element(i) + "\n"

        return res

    def from_url(self, url):
        try:
            import requests
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                'requests package not found, try: "python3 -m pip install requests"'
            )
        self.url = url
        self.html = requests.get(self.url).text
        return self.to_inui(self.html)

    def file(self, path=None):
        if path is not None:
            self.filename = path
        with open(self.filename, "r", encoding="utf-8") as f:
            self.html = f.read()
        return self.to_inui(self.html)

    def save(self, path):
        if self.inui:
            self.to_inui(self.html)
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(self.inui))
        return True


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to inui format")
    parser.add_argument("--html", type=str, help="HTML content as a string")
    parser.add_argument("--url", type=str, help="URL to fetch HTML content from")
    parser.add_argument("--fileName", type=str, help="Path to the HTML file")
    parser.add_argument("--saveTo", type=str, help="Path to save the output file")
    parser.add_argument(
        "--indent", type=int, default=4, help="Indentation level for output"
    )

    args = parser.parse_args()

    converter = HtmlTo_inui(
        html=args.html,
        url=args.url,
        fileName=args.fileName,
        saveTo=args.saveTo,
        indent=args.indent,
    )

    if args.url:
        output = converter.from_url(args.url)
    elif args.fileName:
        output = converter.file(args.fileName)
    elif args.html:
        output = converter.to_inui(args.html)
    else:
        raise ValueError("Either --html, --url or --fileName must be provided")

    if args.saveTo:
        converter.save(args.saveTo)
        print(f"Output saved to {args.saveTo}")
    else:
        print(output)


if __name__ == "__main__":
    main()
