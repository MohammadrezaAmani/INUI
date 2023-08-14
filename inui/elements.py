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

class Acronym(BaseElement):
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

class Address(BaseElement):
    """
The <address> tag in HTML indicates the contact information of a person or an organization. If <address> tag is used inside the [<body>](https://www.geeksforgeeks.org/html-body-tag/) tag then it represents the contact information of the document and if the <address> tag is used inside the [<article>](https://www.geeksforgeeks.org/html5-article-tag/) tag, then it represents the contact information of the article. The text inside the <address> tag will display in italic format. Some browsers add a line break before and after the address element.

`Syntax:` 



<address> Address... </address>

`Example:` 


```html
<!DOCTYPE html><html><body> <!-- address tag starts from here --><address>Organization Name: GeeksforGeeks <br>Web Site:<a href="<https://www.geeksforgeeks.org/about/contact-us/>">GeeksforGeeks</a><br>visit us:<br>GeeksforGeeks<br>710-B, Advant Navis Business Park, <br>Sector-142, Noida Uttar Pradesh – 201305</address><!-- address tag ends here --> </body></html> |

```
`Output:`   
 

![address](https://media.geeksforgeeks.org/wp-content/uploads/address-1.png)

`Supported Browsers:` 

* Google Chrome
* Edge 12 and above
* Internet Explorer
* Firefox 1 and above
* Opera
* Safari 1 and above
The <address> tag in HTML indicates the contact information of a person or an organization. If <address> tag is used inside the [<body>](https://www.geeksforgeeks.org/html-body-tag/) tag then it represents the contact information of the document and if the <address> tag is used inside the [<article>](https://www.geeksforgeeks.org/html5-article-tag/) tag, then it represents the contact information of the article. The text inside the <address> tag will display in italic format. Some browsers add a line break before and after the address element.

`Syntax:` 



<address> Address... </address>

`Example:` 


```html
<!DOCTYPE html><html><body> <!-- address tag starts from here --><address>Organization Name: GeeksforGeeks <br>Web Site:<a href="<https://www.geeksforgeeks.org/about/contact-us/>">GeeksforGeeks</a><br>visit us:<br>GeeksforGeeks<br>710-B, Advant Navis Business Park, <br>Sector-142, Noida Uttar Pradesh – 201305</address><!-- address tag ends here --> </body></html> |

```
`Output:`   
 

![address](https://media.geeksforgeeks.org/wp-content/uploads/address-1.png)

`Supported Browsers:` 

* Google Chrome
* Edge 12 and above
* Internet Explorer
* Firefox 1 and above
* Opera
* Safari 1 and above


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
            tagName="address",
        )
  
class A(BaseElement):
    """
The `<a> tag (anchor tag)` in HTML is used to create a hyperlink on the webpage. This hyperlink is used to link the webpage to other web pages or some section of the same web page. It’s either used to provide an absolute reference or a relative reference as its “href” value.

`Syntax:` 



<a href = "link"> Link Name </a>

`Attribute:` The anchor tag contains many attributes which are listed below.

* [`HTML <a> charset Attribute`](https://www.geeksforgeeks.org/html-a-charset-attribute/)`:` This attribute is used to specifies the character-set. It is not supported by HTML 5.
* [`HTML <a> download Attribute`](https://www.geeksforgeeks.org/html-a-download-attribute/#:~:text=The%20download%20attribute%20is%20used,name%20of%20the%20downloaded%20file.)`:` It is used to specify the target link to download when the user clicks.
* [`HTML <a> hreflang Attribute`](https://www.geeksforgeeks.org/html-a-hreflang-attribute/)`:` It is used to specify the language of the linked document.
* [`HTML <a> media Attribute`](https://www.geeksforgeeks.org/html-a-media-attribute/)`:` It is used to specify the linked media.
* `HTML <a> coords Attribute:` It is used to specify the coordinate of links. It is not supported by HTML 5.
* [`HTML <a> name Attribute`](https://www.geeksforgeeks.org/html-a-name-attribute/)`:` It is used to specify the anchor name. It is not supported by HTML 5 you can use the global `id attribute` instead.
* [`HTML <a> rel Attribute`](https://www.geeksforgeeks.org/html-a-rel-attribute/)`:` It is used to specify the relation between the current document and the linked document.
* [`HTML <a> shape Attribute`](https://www.geeksforgeeks.org/html-a-shape-attribute/)`:` It is used to specify the shape of the link. It is not supported by HTML 5.
* [`HTML <a> type Attribute`](https://www.geeksforgeeks.org/html-a-type-attribute/)`:` It is used to specify the type of links.
* [`HTML <a> target Attribute`](https://www.geeksforgeeks.org/html-a-target-attribute/)`:` It specifies the target link.
* [`HTML <a> rev Attribute`](https://www.geeksforgeeks.org/html-a-rev-attribute/)`:` It is used to specify the relation between the linked document and the current document. It is not supported by HTML 5.

`Example 1:` In this example, the GeeksforGeeks HTML Tutorial page will open when you click on the GeeksforGeeks HTML Tutorial link.

```html
<!DOCTYPE html><html> <body><h2>Welcome to GeeksforGeeksHTML Tutorial</h2> <a href="<https://www.geeksforgeeks.org/html-tutorials/>">GeeksforGeeks HTML Tutorial</a></body> </html> |

```
`Output:`

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920162041/2013.gif)HTML <a> tag

`Example 2:` In this example, we simply redirect from the GeeksforGeeks to the Geeksforgeeks page.

```html
<!DOCTYPE html><html> <body><h1>Welcome to<a href="<https://www.geeksforgeeks.org/>">GeeksforGeeks</a></h1><h2>This is anchor Tag</h2></body> </html> |

```
`Output:` 

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920150045/2012.gif)Redirecting the linked text to the site using <a> tag

`Example 3:` In this example, we will use an image to redirect to the Geeksforgeeks page.

```html
<!DOCTYPE html><html> <body><p>Click on the image to open web page.</p> <!-- anchor tag starts here --><a href="<https://www.geeksforgeeks.org/>"><img src="<https://media.geeksforgeeks.org/wp-content/uploads/gfg1-11.png>"width="300" height="250" /></a><!-- anchor tag ends here --></body> </html> |

```
`Output:`

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920142903/2011.gif)Redirecting the linked image to website using HTML <a> tag

`Example 4:` In this example, we see how an anchor tag can be used to link different sections on the same web page using `*href`* attribute and `*id selector`*.

```html
<!DOCTYPE html><html> <head><title>Example 4</title></head> <body><div class="nav"><p>GeeksforGeeks</p><ul><li><a href="#section1" class="btn">Section 1</a></li><li><a href="#section2" class="btn">Section 2</a></li><li><a href="#section3" class="btn">Section 3</a></li><li><a href="#section4" class="btn">Section 4</a></li><li><a href="#section5" class="btn">Section 5</a></li><li><a href="#section6" class="btn">Section 6</a></li><li><a href="#section7" class="btn">Section 7</a></li><li><a href="#section8" class="btn">Section 8</a></li><li><a href="#section9" class="btn">Section 9</a></li><li><a href="#section10" class="btn">Section 10</a></li></ul></div><div class="sections" id="section1">Section 1</div><div class="sections" id="section2">Section 2</div><div class="sections" id="section3">Section 3</div><div class="sections" id="section4">Section 4</div><div class="sections" id="section5">Section 5</div><div class="sections" id="section6">Section 6</div><div class="sections" id="section7">Section 7</div><div class="sections" id="section8">Section 8</div><div class="sections" id="section9">Section 9</div><div class="sections" id="section10">Section 10</div></body> </html> |

CSS
---

  


  
  




|  |
```html
/* Write CSS Here */* {margin: 0px;padding: 0px;}.nav {height: 250px;width: 250px;text-align: center;background-color: green;color: whitesmoke;font-size: 18px;}p {font-size: 28px;}ul {list-style: none;}a:hover {color: whitesmoke;}.sections {width: 12vw;height: 15vh;background-color: #7EC8E3;font-size: 25px;color: white;text-align: center;margin: 8px 5px;}.sections:nth-of-type(2n) {background-color: #FB4570;} |

`Output :`

![](https://media.geeksforgeeks.org/wp-content/uploads/20220522003529/20220522002835AdobeCreativeCloudExpressAdobeCreativeCloudExpress.gif)Redirecting to different section on the same page

`Supported Browsers:` 

* Google Chrome
* Internet Explorer
* Firefox
* Opera
* Safari
* Microsoft Edge 12 and above

  
The `<a> tag (anchor tag)` in HTML is used to create a hyperlink on the webpage. This hyperlink is used to link the webpage to other web pages or some section of the same web page. It’s either used to provide an absolute reference or a relative reference as its “href” value.

`Syntax:` 



<a href = "link"> Link Name </a>

`Attribute:` The anchor tag contains many attributes which are listed below.

* [`HTML <a> charset Attribute`](https://www.geeksforgeeks.org/html-a-charset-attribute/)`:` This attribute is used to specifies the character-set. It is not supported by HTML 5.
* [`HTML <a> download Attribute`](https://www.geeksforgeeks.org/html-a-download-attribute/#:~:text=The%20download%20attribute%20is%20used,name%20of%20the%20downloaded%20file.)`:` It is used to specify the target link to download when the user clicks.
* [`HTML <a> hreflang Attribute`](https://www.geeksforgeeks.org/html-a-hreflang-attribute/)`:` It is used to specify the language of the linked document.
* [`HTML <a> media Attribute`](https://www.geeksforgeeks.org/html-a-media-attribute/)`:` It is used to specify the linked media.
* `HTML <a> coords Attribute:` It is used to specify the coordinate of links. It is not supported by HTML 5.
* [`HTML <a> name Attribute`](https://www.geeksforgeeks.org/html-a-name-attribute/)`:` It is used to specify the anchor name. It is not supported by HTML 5 you can use the global `id attribute` instead.
* [`HTML <a> rel Attribute`](https://www.geeksforgeeks.org/html-a-rel-attribute/)`:` It is used to specify the relation between the current document and the linked document.
* [`HTML <a> shape Attribute`](https://www.geeksforgeeks.org/html-a-shape-attribute/)`:` It is used to specify the shape of the link. It is not supported by HTML 5.
* [`HTML <a> type Attribute`](https://www.geeksforgeeks.org/html-a-type-attribute/)`:` It is used to specify the type of links.
* [`HTML <a> target Attribute`](https://www.geeksforgeeks.org/html-a-target-attribute/)`:` It specifies the target link.
* [`HTML <a> rev Attribute`](https://www.geeksforgeeks.org/html-a-rev-attribute/)`:` It is used to specify the relation between the linked document and the current document. It is not supported by HTML 5.

`Example 1:` In this example, the GeeksforGeeks HTML Tutorial page will open when you click on the GeeksforGeeks HTML Tutorial link.

```html
<!DOCTYPE html><html> <body><h2>Welcome to GeeksforGeeksHTML Tutorial</h2> <a href="<https://www.geeksforgeeks.org/html-tutorials/>">GeeksforGeeks HTML Tutorial</a></body> </html> |

```
`Output:`

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920162041/2013.gif)HTML <a> tag

`Example 2:` In this example, we simply redirect from the GeeksforGeeks to the Geeksforgeeks page.

```html
<!DOCTYPE html><html> <body><h1>Welcome to<a href="<https://www.geeksforgeeks.org/>">GeeksforGeeks</a></h1><h2>This is anchor Tag</h2></body> </html> |

```
`Output:` 

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920150045/2012.gif)Redirecting the linked text to the site using <a> tag

`Example 3:` In this example, we will use an image to redirect to the Geeksforgeeks page.

```html
<!DOCTYPE html><html> <body><p>Click on the image to open web page.</p> <!-- anchor tag starts here --><a href="<https://www.geeksforgeeks.org/>"><img src="<https://media.geeksforgeeks.org/wp-content/uploads/gfg1-11.png>"width="300" height="250" /></a><!-- anchor tag ends here --></body> </html> |

```
`Output:`

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920142903/2011.gif)Redirecting the linked image to website using HTML <a> tag

`Example 4:` In this example, we see how an anchor tag can be used to link different sections on the same web page using `*href`* attribute and `*id selector`*.

```html
<!DOCTYPE html><html> <head><title>Example 4</title></head> <body><div class="nav"><p>GeeksforGeeks</p><ul><li><a href="#section1" class="btn">Section 1</a></li><li><a href="#section2" class="btn">Section 2</a></li><li><a href="#section3" class="btn">Section 3</a></li><li><a href="#section4" class="btn">Section 4</a></li><li><a href="#section5" class="btn">Section 5</a></li><li><a href="#section6" class="btn">Section 6</a></li><li><a href="#section7" class="btn">Section 7</a></li><li><a href="#section8" class="btn">Section 8</a></li><li><a href="#section9" class="btn">Section 9</a></li><li><a href="#section10" class="btn">Section 10</a></li></ul></div><div class="sections" id="section1">Section 1</div><div class="sections" id="section2">Section 2</div><div class="sections" id="section3">Section 3</div><div class="sections" id="section4">Section 4</div><div class="sections" id="section5">Section 5</div><div class="sections" id="section6">Section 6</div><div class="sections" id="section7">Section 7</div><div class="sections" id="section8">Section 8</div><div class="sections" id="section9">Section 9</div><div class="sections" id="section10">Section 10</div></body> </html> |

CSS
---

  


  
  




|  |
```html
/* Write CSS Here */* {margin: 0px;padding: 0px;}.nav {height: 250px;width: 250px;text-align: center;background-color: green;color: whitesmoke;font-size: 18px;}p {font-size: 28px;}ul {list-style: none;}a:hover {color: whitesmoke;}.sections {width: 12vw;height: 15vh;background-color: #7EC8E3;font-size: 25px;color: white;text-align: center;margin: 8px 5px;}.sections:nth-of-type(2n) {background-color: #FB4570;} |

`Output :`

![](https://media.geeksforgeeks.org/wp-content/uploads/20220522003529/20220522002835AdobeCreativeCloudExpressAdobeCreativeCloudExpress.gif)Redirecting to different section on the same page

`Supported Browsers:` 

* Google Chrome
* Internet Explorer
* Firefox
* Opera
* Safari
* Microsoft Edge 12 and above

  


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
            tagName="a",
        )

class Link(BaseVoidElement):
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
            tagName="link",
        )
