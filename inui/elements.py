from .config.replaces import replace
from .prettify import Pretiffy


class BaseElement:
    def __init__(
        self,
        data=(),
        attributes={},
        classs=None,
        id=None,
        src=None,
        name=None,
        content=None,
        charset=None,
        style=None,
        href=None,
        autocapitalize=None,
        accesskey=None,
        accessskey=None,
        autofocus=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        exportparts=None,
        hidden=None,
        inert=None,
        inputmode=None,
        iss=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=None,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        slot=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        virtualkeyboardpolicy=None,
        accept=None,
        autocomplete=None,
        capture=None,
        crossorigin=None,
        selected=None,
        dirname=None,
        disabled=None,
        elementtiming=None,
        forr=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        pattern=None,
        readonly=None,
        rel=None,
        required=None,
        size=None,
        step=None,
        typee=None,
        placeholder=None,
        text=None,
        scope=None,
        colspan=None,
        aria_describedby=None,
        aria_label=None,
        alt=None,
        startTagName=None,
        endTagName=None,
        tagName=None,
    ):
        self.data = data
        self.attributes = attributes
        self.classs = classs
        self.id = id
        self.src = src
        self.name = name
        self.content = content
        self.charset = charset
        self.style = style
        self.href = href
        self.autocapitalize = autocapitalize
        self.accesskey = accesskey
        self.accessskey = accessskey
        self.autofocus = autofocus
        self.contenteditable = contenteditable
        self.dir = dir
        self.draggable = draggable
        self.enterkeyhint = enterkeyhint
        self.exportparts = exportparts
        self.hidden = hidden
        self.inert = inert
        self.inputmode = inputmode
        self.iss = iss
        self.itemid = itemid
        self.itemprop = itemprop
        self.itemref = itemref
        self.itemscope = itemscope
        self.itemtype = itemtype
        self.lang = lang
        self.nonce = nonce
        self.part = part
        self.popover = popover
        self.slot = slot
        self.spellcheck = spellcheck
        self.tabindex = tabindex
        self.title = title
        self.translate = translate
        self.virtualkeyboardpolicy = virtualkeyboardpolicy
        self.accept = accept
        self.autocomplete = autocomplete
        self.capture = capture
        self.crossorigin = crossorigin
        self.dirname = dirname
        self.disabled = disabled
        self.elementtiming = elementtiming
        self.forr = forr
        self.max = max
        self.maxlength = maxlength
        self.min = min
        self.minlength = minlength
        self.multiple = multiple
        self.pattern = pattern
        self.readonly = readonly
        self.rel = rel
        self.required = required
        self.size = size
        self.step = step
        self.typee = typee
        self.placeholder = placeholder
        self.text = text
        self.scope = scope
        self.colspan = colspan
        self.selected = selected
        self.selected = selected
        self.aria_describedby = aria_describedby
        self.aria_label = aria_label
        self.alt = alt
        self.startTagName = startTagName
        self.endTagName = endTagName
        self.tagname = tagName

    def toHtml(self, prettify: bool = True):
        starttag = ""
        endtag = ""
        if self.tagname != None:
            starttag = self.tagname
            endtag = self.tagname
        if self.startTagName != None:
            starttag = self.tagname
            endtag = self.startTagName
            if self.endTagName != None:
                endtag = self.endTagName
        html = f"""\n<{starttag} {self.attributesToHtml()}>\n{self.dataToHtml()}\n</{endtag}>"""
        if prettify:
            return str(Pretiffy(html))
        return str(html)

    def dataToHtml(self):
        if type(self.data) in [list, set, tuple]:
            text = ""
            for i in self.data:
                text += str(i)
        else:
            return str(self.data)
        return text

    def attributesToHtml(self):
        text = ""
        for i in self.__dict__:
            if self.__dict__[i] != None and i not in [
                "data",
                "attributes",
                "startTagName",
                "tagname",
                "endTagName",
            ]:
                self.attributes[i] = self.__dict__[i]
        for attribute in self.attributes:
            name = attribute
            if attribute in replace:
                name = replace[attribute]
            if type(self.attributes[attribute]) == str:
                text += '%s="%s" ' % (name, self.attributes[attribute])

            if type(self.attributes[attribute]) in [list, set, tuple]:
                text += '%s="%s" ' % (name, " ".join(self.attributes[attribute]))
        return text

    def save(self, filePath: str = "./out.html", prettify: bool = True):
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(self.toHtml(prettify=prettify))

    def __str__(self):
        return self.toHtml()

    def __repr__(self):
        return self.toHtml()


class BaseVoidElement:
    def __init__(
        self,
        data=(),
        attributes={},
        classs=None,
        id=None,
        src=None,
        name=None,
        content=None,
        charset=None,
        style=None,
        href=None,
        autocapitalize=None,
        accesskey=None,
        accessskey=None,
        autofocus=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        exportparts=None,
        hidden=None,
        inert=None,
        inputmode=None,
        iss=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=None,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        slot=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        virtualkeyboardpolicy=None,
        accept=None,
        autocomplete=None,
        capture=None,
        crossorigin=None,
        selected=None,
        dirname=None,
        disabled=None,
        elementtiming=None,
        forr=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        pattern=None,
        readonly=None,
        rel=None,
        required=None,
        size=None,
        step=None,
        typee=None,
        placeholder=None,
        text=None,
        scope=None,
        colspan=None,
        aria_describedby=None,
        aria_label=None,
        alt=None,
        tagName=None,
    ):
        self.data = data
        self.attributes = attributes
        self.classs = classs
        self.id = id
        self.src = src
        self.name = name
        self.content = content
        self.charset = charset
        self.style = style
        self.href = href
        self.autocapitalize = autocapitalize
        self.accesskey = accesskey
        self.accessskey = accessskey
        self.autofocus = autofocus
        self.contenteditable = contenteditable
        self.dir = dir
        self.draggable = draggable
        self.enterkeyhint = enterkeyhint
        self.exportparts = exportparts
        self.hidden = hidden
        self.inert = inert
        self.inputmode = inputmode
        self.iss = iss
        self.itemid = itemid
        self.itemprop = itemprop
        self.itemref = itemref
        self.itemscope = itemscope
        self.itemtype = itemtype
        self.lang = lang
        self.nonce = nonce
        self.part = part
        self.popover = popover
        self.slot = slot
        self.spellcheck = spellcheck
        self.tabindex = tabindex
        self.title = title
        self.translate = translate
        self.virtualkeyboardpolicy = virtualkeyboardpolicy
        self.accept = accept
        self.autocomplete = autocomplete
        self.capture = capture
        self.crossorigin = crossorigin
        self.dirname = dirname
        self.disabled = disabled
        self.elementtiming = elementtiming
        self.forr = forr
        self.max = max
        self.maxlength = maxlength
        self.min = min
        self.minlength = minlength
        self.multiple = multiple
        self.pattern = pattern
        self.readonly = readonly
        self.rel = rel
        self.required = required
        self.size = size
        self.step = step
        self.typee = typee
        self.placeholder = placeholder
        self.text = text
        self.scope = scope
        self.colspan = colspan
        self.selected = selected
        self.selected = selected
        self.aria_describedby = aria_describedby
        self.aria_label = aria_label
        self.alt = alt
        self.tagname = tagName

    def toHtml(self, prettify: bool = True):
        html = f"""\n<{self.tagname} {self.attributesToHtml()}>"""
        if prettify:
            return str(Pretiffy(html))
        return str(html)

    def attributesToHtml(self):
        text = ""
        for i in self.__dict__:
            if self.__dict__[i] != None and i not in [
                "data",
                "attributes",
                "startTagName",
                "tagname",
                "endTagName",
            ]:
                self.attributes[i] = self.__dict__[i]
        for attribute in self.attributes:
            name = attribute
            if attribute in replace:
                name = replace[attribute]
            if type(self.attributes[attribute]) == str:
                text += '%s="%s" ' % (name, self.attributes[attribute])

            if type(self.attributes[attribute]) in [list, set, tuple]:
                text += '%s="%s" ' % (name, " ".join(self.attributes[attribute]))
        return text

    def save(self, filePath: str = "./out.html", prettify: bool = True):
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(self.toHtml(prettify=prettify))

    def __str__(self):
        return self.toHtml()

    def __repr__(self):
        return self.toHtml()


class Abbr(BaseElement):
    """
    The <abbr> tag(Abbreviation) in HTML is used to define the abbreviation or short form of an element. The <abbr> and [<acronym>](https://www.geeksforgeeks.org/html-acronym-tag/) tags are used as shortened versions and used to represent a series of letters. The abbreviation is used to provide useful information to browsers, translation systems, and search-engines.

    `Syntax:`



    <abbr title=""> Short form </abbr>

    `Attribute:` This tag accepts an optional attribute as mentioned above and described below:

    * [`title`](https://www.geeksforgeeks.org/html-title-attribute/):Itis used to specify extra information about the element. When the mouse moves over the element then it shows the information.

    `Example:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>This is abbr Tag</h2><abbr title="GeeksforGeeks">GFG</abbr></body> </html> |

    ```
    `Output:`

    ![abbrTag.png](https://media.geeksforgeeks.org/wp-content/uploads/20230630162948/abbrTag-300.png)abbr Tag

    `Supported Browser:`

    * Google Chrome 2 and above
    * Edge 12 and above
    * Internet Explorer 7 and above
    * Firefox 1 and above
    * Opera
    * Safari
    The <abbr> tag(Abbreviation) in HTML is used to define the abbreviation or short form of an element. The <abbr> and [<acronym>](https://www.geeksforgeeks.org/html-acronym-tag/) tags are used as shortened versions and used to represent a series of letters. The abbreviation is used to provide useful information to browsers, translation systems, and search-engines.

    `Syntax:`



    <abbr title=""> Short form </abbr>

    `Attribute:` This tag accepts an optional attribute as mentioned above and described below:

    * [`title`](https://www.geeksforgeeks.org/html-title-attribute/):Itis used to specify extra information about the element. When the mouse moves over the element then it shows the information.

    `Example:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>This is abbr Tag</h2><abbr title="GeeksforGeeks">GFG</abbr></body> </html> |

    ```
    `Output:`

    ![abbrTag.png](https://media.geeksforgeeks.org/wp-content/uploads/20230630162948/abbrTag-300.png)abbr Tag

    `Supported Browser:`

    * Google Chrome 2 and above
    * Edge 12 and above
    * Internet Explorer 7 and above
    * Firefox 1 and above
    * Opera
    * Safari


    ref = [https://www.geeksforgeeks.org/html-tags-a-to-z-list/](https://www.geeksforgeeks.org/html-tags-a-to-z-list/)
    """

    def __init__(
        self,
        data=(),
        attributes={},
        classs=None,
        id=None,
        src=None,
        name=None,
        content=None,
        charset=None,
        style=None,
        href=None,
        autocapitalize=None,
        accesskey=None,
        accessskey=None,
        autofocus=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        exportparts=None,
        hidden=None,
        inert=None,
        inputmode=None,
        iss=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=None,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        slot=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        virtualkeyboardpolicy=None,
        accept=None,
        autocomplete=None,
        capture=None,
        crossorigin=None,
        selected=None,
        dirname=None,
        disabled=None,
        elementtiming=None,
        forr=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        pattern=None,
        readonly=None,
        rel=None,
        required=None,
        size=None,
        step=None,
        typee=None,
        placeholder=None,
        text=None,
        scope=None,
        colspan=None,
        aria_describedby=None,
        aria_label=None,
        alt=None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            classs=classs,
            id=id,
            src=src,
            name=name,
            content=content,
            charset=charset,
            style=style,
            href=href,
            autocapitalize=autocapitalize,
            accesskey=accesskey,
            accessskey=accessskey,
            autofocus=autofocus,
            contenteditable=contenteditable,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            exportparts=exportparts,
            hidden=hidden,
            inert=inert,
            inputmode=inputmode,
            iss=iss,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            slot=slot,
            spellcheck=spellcheck,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            accept=accept,
            autocomplete=autocomplete,
            capture=capture,
            crossorigin=crossorigin,
            selected=selected,
            dirname=dirname,
            disabled=disabled,
            elementtiming=elementtiming,
            forr=forr,
            max=max,
            maxlength=maxlength,
            min=min,
            minlength=minlength,
            multiple=multiple,
            pattern=pattern,
            readonly=readonly,
            rel=rel,
            required=required,
            size=size,
            step=step,
            typee=typee,
            placeholder=placeholder,
            text=text,
            scope=scope,
            colspan=colspan,
            aria_describedby=aria_describedby,
            aria_label=aria_label,
            alt=alt,
            startTagName=None,
            endTagName=None,
            tagName="abbr",
        )

class Doctype(BaseVoidElement):
    """
 
"""
    def __init__(
        self,
        attributes={},
        classs=None,
        id=None,
        src=None,
        name=None,
        content=None,
        charset=None,
        style=None,
        href=None,
        autocapitalize=None,
        accesskey=None,
        accessskey=None,
        autofocus=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        exportparts=None,
        hidden=None,
        inert=None,
        inputmode=None,
        iss=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=None,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        slot=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        virtualkeyboardpolicy=None,
        accept=None,
        autocomplete=None,
        capture=None,
        crossorigin=None,
        selected=None,
        dirname=None,
        disabled=None,
        elementtiming=None,
        forr=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        pattern=None,
        readonly=None,
        rel=None,
        required=None,
        size=None,
        step=None,
        typee=None,
        placeholder=None,
        text=None,
        scope=None,
        colspan=None,
        aria_describedby=None,
        aria_label=None,
        alt=None,
    ):
        super().__init__(
            attributes=attributes,
            classs=classs,
            id=id,
            src=src,
            name=name,
            content=content,
            charset=charset,
            style=style,
            href=href,
            autocapitalize=autocapitalize,
            accesskey=accesskey,
            accessskey=accessskey,
            autofocus=autofocus,
            contenteditable=contenteditable,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            exportparts=exportparts,
            hidden=hidden,
            inert=inert,
            inputmode=inputmode,
            iss=iss,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            slot=slot,
            spellcheck=spellcheck,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            accept=accept,
            autocomplete=autocomplete,
            capture=capture,
            crossorigin=crossorigin,
            selected=selected,
            dirname=dirname,
            disabled=disabled,
            elementtiming=elementtiming,
            forr=forr,
            max=max,
            maxlength=maxlength,
            min=min,
            minlength=minlength,
            multiple=multiple,
            pattern=pattern,
            readonly=readonly,
            rel=rel,
            required=required,
            size=size,
            step=step,
            typee=typee,
            placeholder=placeholder,
            text=text,
            scope=scope,
            colspan=colspan,
            aria_describedby=aria_describedby,
            aria_label=aria_label,
            alt=alt,
            tagName="!DOCTYPE html",
        )

class Acronym():
    """
The <acronym> tag in HTML is used to define the acronym. The <acronym> tag is used to spell out another word. It is used to give useful information to browsers, translation systems, and search-engines. This tag is not supported in HTML 5 otherwise use [<abbr>](https://geeksforgeeks.org/html-abbr-tag/#:~:text=The%20tag(Abbreviation,systems%2C%20and%20search-engines.) Tag.

`Syntax:` 



<acronym title=""> Short Form </acronym>

`Attribute:` This tag accepts an optional attribute as mentioned above and described below:

* [`title`](https://www.geeksforgeeks.org/html-title-attribute/):Itis used to specify extra information about the element. When the mouse moves over the element then it shows the information.

`Example:` 


```html
<!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>This is HTML acronym Tag</h2><acronym title="GeeksforGeeks">GFG</acronym><br><acronym title="Operating System">OS</acronym></body> </html> |

```
`Output:` 

![Screenshot-from-2023-06-30-16-34-32.png](https://media.geeksforgeeks.org/wp-content/uploads/20230630163728/Screenshot-from-2023-06-30-16-34-32-300.png)acronym Tag

`Supported Browser:` 

* Google Chrome
* Internet Explorer
* Firefox
* Opera
* Safari
The <acronym> tag in HTML is used to define the acronym. The <acronym> tag is used to spell out another word. It is used to give useful information to browsers, translation systems, and search-engines. This tag is not supported in HTML 5 otherwise use [<abbr>](https://geeksforgeeks.org/html-abbr-tag/#:~:text=The%20tag(Abbreviation,systems%2C%20and%20search-engines.) Tag.

`Syntax:` 



<acronym title=""> Short Form </acronym>

`Attribute:` This tag accepts an optional attribute as mentioned above and described below:

* [`title`](https://www.geeksforgeeks.org/html-title-attribute/):Itis used to specify extra information about the element. When the mouse moves over the element then it shows the information.

`Example:` 


```html
<!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>This is HTML acronym Tag</h2><acronym title="GeeksforGeeks">GFG</acronym><br><acronym title="Operating System">OS</acronym></body> </html> |

```
`Output:` 

![Screenshot-from-2023-06-30-16-34-32.png](https://media.geeksforgeeks.org/wp-content/uploads/20230630163728/Screenshot-from-2023-06-30-16-34-32-300.png)acronym Tag

`Supported Browser:` 

* Google Chrome
* Internet Explorer
* Firefox
* Opera
* Safari


ref = [https://www.geeksforgeeks.org/html-tags-a-to-z-list/](https://www.geeksforgeeks.org/html-tags-a-to-z-list/)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        classs=None,
        id=None,
        src=None,
        name=None,
        content=None,
        charset=None,
        style=None,
        href=None,
        autocapitalize=None,
        accesskey=None,
        accessskey=None,
        autofocus=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        exportparts=None,
        hidden=None,
        inert=None,
        inputmode=None,
        iss=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=None,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        slot=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        virtualkeyboardpolicy=None,
        accept=None,
        autocomplete=None,
        capture=None,
        crossorigin=None,
        selected=None,
        dirname=None,
        disabled=None,
        elementtiming=None,
        forr=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        pattern=None,
        readonly=None,
        rel=None,
        required=None,
        size=None,
        step=None,
        typee=None,
        placeholder=None,
        text=None,
        scope=None,
        colspan=None,
        aria_describedby=None,
        aria_label=None,
        alt=None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            classs=classs,
            id=id,
            src=src,
            name=name,
            content=content,
            charset=charset,
            style=style,
            href=href,
            autocapitalize=autocapitalize,
            accesskey=accesskey,
            accessskey=accessskey,
            autofocus=autofocus,
            contenteditable=contenteditable,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            exportparts=exportparts,
            hidden=hidden,
            inert=inert,
            inputmode=inputmode,
            iss=iss,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            slot=slot,
            spellcheck=spellcheck,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            accept=accept,
            autocomplete=autocomplete,
            capture=capture,
            crossorigin=crossorigin,
            selected=selected,
            dirname=dirname,
            disabled=disabled,
            elementtiming=elementtiming,
            forr=forr,
            max=max,
            maxlength=maxlength,
            min=min,
            minlength=minlength,
            multiple=multiple,
            pattern=pattern,
            readonly=readonly,
            rel=rel,
            required=required,
            size=size,
            step=step,
            typee=typee,
            placeholder=placeholder,
            text=text,
            scope=scope,
            colspan=colspan,
            aria_describedby=aria_describedby,
            aria_label=aria_label,
            alt=alt,
            startTagName=None,
            endTagName=None,
            tagName="acronym",
        )
