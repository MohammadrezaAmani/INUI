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
                text += '%s="%s" ' % (name,
                                      " ".join(self.attributes[attribute]))
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
                text += '%s="%s" ' % (name,
                                      " ".join(self.attributes[attribute]))
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
    """ """

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
    """ """

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


class Doctype(BaseVoidElement):
    """ """

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
            tagName="doctype",
        )


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
    """ """

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


class Script(BaseElement):
    """
    The <script> tag in HTML is used to define the client-side script. The <script> tag contains the scripting statements, or it points to an external script file. The JavaScript is mainly used in form validation, dynamic changes of content, image manipulation, etc.
    `Syntax:`




    <script> Script Contents... </script>

    `Attributes:` Many attribute associated with script tag.


    * [`async`](https://www.geeksforgeeks.org/html-script-async-attribute/)`:` It is used to specify the script is executed asynchronously.
    * [`charset`](https://www.geeksforgeeks.org/html-script-charset-attribute/)`:` It is used to specify the character encoding used in an external script file.
    * [`defer`](https://www.geeksforgeeks.org/html-script-defer-attribute/)`:` It is used to specify that the script is executed when the page has finished parsing.
    * [`src`](https://www.geeksforgeeks.org/html-script-src-attribute/)`:` It is used to specify the URL of an external script file.
    * [`type`](https://www.geeksforgeeks.org/html-script-type-attribute/)`:` It is used to specify the media type of the script.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><script> Tag</h2><p id="Geeks"></p>  <!-- html script tag starts here --><script>document.getElementById("Geeks").innerHTML ="Hello GeeksforGeeks!";</script><!-- html script tag ends here --> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210615133553/script1.png)

    `Example 2(script outside body tag):`

    ```html
    <!DOCTYPE html><html><head><title>script tag</title><style>body {text-align:center;}h1 {color:green;}</style><script>function Geeks() {alert('Welcome to GeeksforGeeks!');}</script></head><body><h1>GeeksforGeeks</h1><h2><script> Tag</h2><button type="button" onclick="Geeks()">Hello GeeksforGeeks</button></body></html> |

    ```
    `Output:`


    ![script tag](https://media.geeksforgeeks.org/wp-content/uploads/script.png)

    `Supported Browsers:`


    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <script> tag in HTML is used to define the client-side script. The <script> tag contains the scripting statements, or it points to an external script file. The JavaScript is mainly used in form validation, dynamic changes of content, image manipulation, etc.
    `Syntax:`




    <script> Script Contents... </script>

    `Attributes:` Many attribute associated with script tag.


    * [`async`](https://www.geeksforgeeks.org/html-script-async-attribute/)`:` It is used to specify the script is executed asynchronously.
    * [`charset`](https://www.geeksforgeeks.org/html-script-charset-attribute/)`:` It is used to specify the character encoding used in an external script file.
    * [`defer`](https://www.geeksforgeeks.org/html-script-defer-attribute/)`:` It is used to specify that the script is executed when the page has finished parsing.
    * [`src`](https://www.geeksforgeeks.org/html-script-src-attribute/)`:` It is used to specify the URL of an external script file.
    * [`type`](https://www.geeksforgeeks.org/html-script-type-attribute/)`:` It is used to specify the media type of the script.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><script> Tag</h2><p id="Geeks"></p>  <!-- html script tag starts here --><script>document.getElementById("Geeks").innerHTML ="Hello GeeksforGeeks!";</script><!-- html script tag ends here --> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210615133553/script1.png)

    `Example 2(script outside body tag):`

    ```html
    <!DOCTYPE html><html><head><title>script tag</title><style>body {text-align:center;}h1 {color:green;}</style><script>function Geeks() {alert('Welcome to GeeksforGeeks!');}</script></head><body><h1>GeeksforGeeks</h1><h2><script> Tag</h2><button type="button" onclick="Geeks()">Hello GeeksforGeeks</button></body></html> |

    ```
    `Output:`


    ![script tag](https://media.geeksforgeeks.org/wp-content/uploads/script.png)

    `Supported Browsers:`


    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
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
            tagName="script",
        )


class Applet(BaseElement):
    """
    The `<applet>` tag in HTML was used to *embed Java applets into any HTML document*. The `<applet>` tag was deprecated in HTML 4.01, and it’s support has been completely discontinued starting from HTML 5. Alternatives available in HTML 5 are the [`<embed>`](https://www.geeksforgeeks.org/html-embed-tag/) and the [`<object>`](https://www.geeksforgeeks.org/html-object-tag/) tags. There are still some browsers that support the <applet> tag with the help of some additional plug-ins/installations to work. Internet Explorer 11 and earlier versions with the help of plug-ins.
    Applet Tag is not supported in HTML5. The <applet> tag takes a number of attributes, with one of the most important being the `code` attribute. This `code` attribute is used to link a Java applet to the concerned HTML document. It specifies the file name of the Java applet.

    `Attributes:` This tag accepts the following attributes:

    * [align](https://www.geeksforgeeks.org/html-align-attribute/): Specifies the alignment of an applet.
    * [alt](https://www.geeksforgeeks.org/html-alt-attribute/): Specifies an alternate text for an applet.
    * archive: Specifies the location of an archive file.
    * [border](https://www.geeksforgeeks.org/html-border-attribute/): Specifies the border around the applet panel.
    * codebase: Specifies a relative base URL for applets specified in the code attribute.
    * [height](https://www.geeksforgeeks.org/html-height-attribute/): Specifies the height of an applet.
    * [hspace](https://www.geeksforgeeks.org/html-applet-hspace-attribute/): Defines the horizontal spacing around an applet.
    * mayscript: Indicates whether the Java applet is allowed to access the scripting objects of the web page.
    * [name](https://www.geeksforgeeks.org/html-name-attribute/): Defines the name for an applet (to use in scripts)
    * [vspace:](https://www.geeksforgeeks.org/html-img-vspace-attribute/) Defines the vertical spacing around an applet.
    * [width:](https://www.geeksforgeeks.org/html-img-width-attribute/) Specifies the width of an applet.

    `Syntax:`




    <applet *attribute1 attribute2....*>
       <param *parameter1*>
       <param *parameter2*>
       ....
    </applet>

    The following Examples explain the applet tag:


    `Example 1:` Here, `HelloWorld` is the class file, which contains the applet. The `width` and `height` attributes determine the width and height of the applet in pixels when it is opened in the browser.
    Attributes available to be used in conjunction with the `<applet>` tag are as follows:

    ```html
    <!DOCTYPE html><html><!-- applet code starts here --><applet code="HelloWorld"><!-- applet code ends here --></applet></html> |

    `Parameters:` Parameters are quite similar to command-line arguments in the sense that they provide a way to pass information to the applet after it has started. All the information available to the applet before it starts is said to be hard-coded i.e. embedded within it. Parameters make it possible to generate and use data during run-time of the applet.


    `Syntax:`




    <param name=*parameter\_name* value=*parameter\_value*>

    The name assigned to the `name` attribute of the `param` tag is used by the applet code as a variable to access the parameter value specified in the `value` attribute. In this way, the applet is able to interact with the HTML page where it is embedded, and can work on values provided to it by the page during run-time.


    `Example 2:` In this piece of code, the applet file HelloWorld can use the variable named `message` to access the value stored in it, which is `“HelloWorld”`.

    ```html
    <!DOCTYPE html><html><!-- applet code starts here --><applet code="HelloWorld"><param name="message" value="HelloWorld"><!-- applet code ends here --></applet> </html> |



    `Supported Browsers:`

    * Firefox
    * Safari


    The `<applet>` tag in HTML was used to *embed Java applets into any HTML document*. The `<applet>` tag was deprecated in HTML 4.01, and it’s support has been completely discontinued starting from HTML 5. Alternatives available in HTML 5 are the [`<embed>`](https://www.geeksforgeeks.org/html-embed-tag/) and the [`<object>`](https://www.geeksforgeeks.org/html-object-tag/) tags. There are still some browsers that support the <applet> tag with the help of some additional plug-ins/installations to work. Internet Explorer 11 and earlier versions with the help of plug-ins.
    Applet Tag is not supported in HTML5. The <applet> tag takes a number of attributes, with one of the most important being the `code` attribute. This `code` attribute is used to link a Java applet to the concerned HTML document. It specifies the file name of the Java applet.

    `Attributes:` This tag accepts the following attributes:

    * [align](https://www.geeksforgeeks.org/html-align-attribute/): Specifies the alignment of an applet.
    * [alt](https://www.geeksforgeeks.org/html-alt-attribute/): Specifies an alternate text for an applet.
    * archive: Specifies the location of an archive file.
    * [border](https://www.geeksforgeeks.org/html-border-attribute/): Specifies the border around the applet panel.
    * codebase: Specifies a relative base URL for applets specified in the code attribute.
    * [height](https://www.geeksforgeeks.org/html-height-attribute/): Specifies the height of an applet.
    * [hspace](https://www.geeksforgeeks.org/html-applet-hspace-attribute/): Defines the horizontal spacing around an applet.
    * mayscript: Indicates whether the Java applet is allowed to access the scripting objects of the web page.
    * [name](https://www.geeksforgeeks.org/html-name-attribute/): Defines the name for an applet (to use in scripts)
    * [vspace:](https://www.geeksforgeeks.org/html-img-vspace-attribute/) Defines the vertical spacing around an applet.
    * [width:](https://www.geeksforgeeks.org/html-img-width-attribute/) Specifies the width of an applet.

    `Syntax:`




    <applet *attribute1 attribute2....*>
       <param *parameter1*>
       <param *parameter2*>
       ....
    </applet>

    The following Examples explain the applet tag:


    `Example 1:` Here, `HelloWorld` is the class file, which contains the applet. The `width` and `height` attributes determine the width and height of the applet in pixels when it is opened in the browser.
    Attributes available to be used in conjunction with the `<applet>` tag are as follows:

    ```html
    <!DOCTYPE html><html><!-- applet code starts here --><applet code="HelloWorld"><!-- applet code ends here --></applet></html> |

    `Parameters:` Parameters are quite similar to command-line arguments in the sense that they provide a way to pass information to the applet after it has started. All the information available to the applet before it starts is said to be hard-coded i.e. embedded within it. Parameters make it possible to generate and use data during run-time of the applet.


    `Syntax:`




    <param name=*parameter\_name* value=*parameter\_value*>

    The name assigned to the `name` attribute of the `param` tag is used by the applet code as a variable to access the parameter value specified in the `value` attribute. In this way, the applet is able to interact with the HTML page where it is embedded, and can work on values provided to it by the page during run-time.


    `Example 2:` In this piece of code, the applet file HelloWorld can use the variable named `message` to access the value stored in it, which is `“HelloWorld”`.

    ```html
    <!DOCTYPE html><html><!-- applet code starts here --><applet code="HelloWorld"><param name="message" value="HelloWorld"><!-- applet code ends here --></applet> </html> |



    `Supported Browsers:`

    * Firefox
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
            tagName="applet",
        )


class Area(BaseVoidElement):
    """ """

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
            tagName="area",
        )


class Article(BaseElement):
    """
    The `<article>` tag is independent of the other content of the page (even though it can be related).

    In other words, The article element represents a component of a page that consists of self-contained composition in a document, page, or site. For Ex. in syndication.

    `A potential source for Article Element is:`

    * A magazine/newspaper article
    * A blog entry
    * A forum post
    * A user-submitted a comment

    `This tag is most often used in two contexts:`

    * On a page with a single piece of content, a single <article> element can be used to contain the main content and set it off from the rest of the page.
    * On a page with multiple pieces of content (a blog index page, a search results page, a category page, news feed), multiple <article> elements can be used to contain each individual piece of content.

    Either way, it is similar to the <div> element and displays the stylish work the same. However, using the <article> element instead of <div> provides more semantic information to screen readers, search engines, and third-party applications.

    `Note:` This tag does not render as anything special in a browser, you have to use CSS for that.

    `Default CSS setting:` Most browsers will display the Article element with the following values.



    <article> {
        display:block;
    }

    `Example:` Using inline styling in an article element

    ```html
    <!DOCTYPE html><html> <body><articlestyle="width: 300px;border: 2px solid gray;padding: 10px;border-radius: 10px;margin: 5px;"><imgsrc="<https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png>"alt=""width="300"height="250"class="alignnone size-medium wp-image-560930" /> <h1>GeeksforGeeks</h1><p>Sandeep Jain(FOUNDER) An IIT Roorkee alumnus andfounder of GeeksforGeeks. Apart from GeeksforGeeks,he has worked with DE Shaw and Co. as a softwaredeveloper and JIIT Noida as an assistant professor.</p></article></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190717121605/Screenshot-from-2019-07-17-12-12-55.png)

    `Supported Browsers:`

    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above


    The `<article>` tag is independent of the other content of the page (even though it can be related).

    In other words, The article element represents a component of a page that consists of self-contained composition in a document, page, or site. For Ex. in syndication.

    `A potential source for Article Element is:`

    * A magazine/newspaper article
    * A blog entry
    * A forum post
    * A user-submitted a comment

    `This tag is most often used in two contexts:`

    * On a page with a single piece of content, a single <article> element can be used to contain the main content and set it off from the rest of the page.
    * On a page with multiple pieces of content (a blog index page, a search results page, a category page, news feed), multiple <article> elements can be used to contain each individual piece of content.

    Either way, it is similar to the <div> element and displays the stylish work the same. However, using the <article> element instead of <div> provides more semantic information to screen readers, search engines, and third-party applications.

    `Note:` This tag does not render as anything special in a browser, you have to use CSS for that.

    `Default CSS setting:` Most browsers will display the Article element with the following values.



    <article> {
        display:block;
    }

    `Example:` Using inline styling in an article element

    ```html
    <!DOCTYPE html><html> <body><articlestyle="width: 300px;border: 2px solid gray;padding: 10px;border-radius: 10px;margin: 5px;"><imgsrc="<https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png>"alt=""width="300"height="250"class="alignnone size-medium wp-image-560930" /> <h1>GeeksforGeeks</h1><p>Sandeep Jain(FOUNDER) An IIT Roorkee alumnus andfounder of GeeksforGeeks. Apart from GeeksforGeeks,he has worked with DE Shaw and Co. as a softwaredeveloper and JIIT Noida as an assistant professor.</p></article></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190717121605/Screenshot-from-2019-07-17-12-12-55.png)

    `Supported Browsers:`

    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above




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
            tagName="article",
        )


class Aside(BaseElement):
    """
    The `<aside>` tag is used to describe the main object of the web page in a shorter way like a highlighter. It basically identifies the content that is related to the primary content of the web page but does not constitute the main intent of the primary page. The <aside> tag contains mainly author information, links, related content, and so on.

    `<aside> vs <div>:` Both tags have the same behavior with a different meanings.

    * [`<div>`](https://www.geeksforgeeks.org/div-tag-html/)`:` It defines or creates a division or section in the web page.
    * `<aside>:` It does the same job by creating a section or division but it contains only the content that is related to the main web page.

    The <aside> tag makes it easy to design the page and it enhances the clarity of the HTML document. It let us easily recognize the main text and subordinate text. In both the time <div> and <aside> need CSS for specific design. The <aside> tag supports `Global attributes` and `Event attributes` in HTML.

    `Note:` The <aside> tag is new in HTML5. This tag does not render anything special in a browser you have to use CSS for that.

    `Syntax:`



    <aside>
          <h1>Contents...</h1>
          <p>Contents...</p>
    </aside>

    `Example:` HTML aside Tag

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML aside Tag</h2><h1>This is normal heading Tag</h1><p>This is normal paragraph text</p><aside><h1>This is heading text in aside Tag</h1><p>This is paragraph text in aside Tag</p></aside></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204133431/aside.png)

    `Example:` Using Style in HTML aside Tag:

    ```html
    <!DOCTYPE html><html> <head><style>article {width: 50%;padding: 10px;float: left;}aside {width: 40%;float: right;background-color: green;color: white;padding: 5px;margin: 10px;height: 100px;}</style></head> <body><h1>GeeksforGeeks</h1><article><h1>Heading . . .</h1> <p>Aside tag is use to display importantinformation about the primary page.</p> </article><aside><h1>Aside tag example</h1> <p>Aside tag content. . .</p> </aside></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210204152328/Screenshot-2021-02-04-152259.png)

    `Supported Browser:`

    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above


    The `<aside>` tag is used to describe the main object of the web page in a shorter way like a highlighter. It basically identifies the content that is related to the primary content of the web page but does not constitute the main intent of the primary page. The <aside> tag contains mainly author information, links, related content, and so on.

    `<aside> vs <div>:` Both tags have the same behavior with a different meanings.

    * [`<div>`](https://www.geeksforgeeks.org/div-tag-html/)`:` It defines or creates a division or section in the web page.
    * `<aside>:` It does the same job by creating a section or division but it contains only the content that is related to the main web page.

    The <aside> tag makes it easy to design the page and it enhances the clarity of the HTML document. It let us easily recognize the main text and subordinate text. In both the time <div> and <aside> need CSS for specific design. The <aside> tag supports `Global attributes` and `Event attributes` in HTML.

    `Note:` The <aside> tag is new in HTML5. This tag does not render anything special in a browser you have to use CSS for that.

    `Syntax:`



    <aside>
          <h1>Contents...</h1>
          <p>Contents...</p>
    </aside>

    `Example:` HTML aside Tag

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML aside Tag</h2><h1>This is normal heading Tag</h1><p>This is normal paragraph text</p><aside><h1>This is heading text in aside Tag</h1><p>This is paragraph text in aside Tag</p></aside></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204133431/aside.png)

    `Example:` Using Style in HTML aside Tag:

    ```html
    <!DOCTYPE html><html> <head><style>article {width: 50%;padding: 10px;float: left;}aside {width: 40%;float: right;background-color: green;color: white;padding: 5px;margin: 10px;height: 100px;}</style></head> <body><h1>GeeksforGeeks</h1><article><h1>Heading . . .</h1> <p>Aside tag is use to display importantinformation about the primary page.</p> </article><aside><h1>Aside tag example</h1> <p>Aside tag content. . .</p> </aside></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210204152328/Screenshot-2021-02-04-152259.png)

    `Supported Browser:`

    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above




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
            tagName="aside",
        )


class Audio(BaseElement):
    """ """

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
            tagName="audio",
        )


class Base(BaseVoidElement):
    """ """

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
            tagName="base",
        )


class Basefont(BaseVoidElement):
    """ """

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
            tagName="basefont",
        )


class Bdi(BaseElement):
    """
    The <bdi> tag refers to the Bi-Directional Isolation. It differentiates a text from other text that may be formatted in a different direction. This tag is used when a user-generated text with unknown directions.
    `Note:` This tag is new in HTML5.

    `Syntax:`



    <bdi> Contents... </bdi>

    `Example:` The below example illustrate the bdi tag.


    ```html
    <!DOCTYPE html><html><body><!--This is heading Tag --><h1>GeeksforGeeks</h1><!--bdi Tag used in unordered list --><ul><li><bdi class="name">Himanshu Jha</bdi>: indian name</li><li><bdi class="name">الرجل القوي إيان</bdi>: arabic name</li></ul></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205174618/bdoo.png)

    `Supported Browsers:`

    * Google Chrome 16 and above
    * Edge 79 and above
    * Firefox 10 and above
    * Internet Explorer not supported
    * Opera 15 and above
    * Safari 6 and above
    The <bdi> tag refers to the Bi-Directional Isolation. It differentiates a text from other text that may be formatted in a different direction. This tag is used when a user-generated text with unknown directions.
    `Note:` This tag is new in HTML5.

    `Syntax:`



    <bdi> Contents... </bdi>

    `Example:` The below example illustrate the bdi tag.


    ```html
    <!DOCTYPE html><html><body><!--This is heading Tag --><h1>GeeksforGeeks</h1><!--bdi Tag used in unordered list --><ul><li><bdi class="name">Himanshu Jha</bdi>: indian name</li><li><bdi class="name">الرجل القوي إيان</bdi>: arabic name</li></ul></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205174618/bdoo.png)

    `Supported Browsers:`

    * Google Chrome 16 and above
    * Edge 79 and above
    * Firefox 10 and above
    * Internet Explorer not supported
    * Opera 15 and above
    * Safari 6 and above


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
            tagName="bdi",
        )


class Bdo(BaseElement):
    """
    The <bdo> stands for Bi-Directional Override. This tag is used to specify the text direction or used to change the current direction.

    `Syntax:`




    <bdo dir> Contents... </bdo>

    `Attributes:` This element contains dir attributes which are used to specify the direction of text written inside the <bdo> element. The [dir attribute](https://www.geeksforgeeks.org/html-dir-attribute/) contains two values which are listed below:


    * `rtl:` The text direction from right to left (reverse the text).
    * `ltr:` The text direction from left to right.

    `Example:` The below example illustrate the bdo tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><bdo> Tag</h2><!--This is bdo ltr Tag--><bdo dir="ltr">GeeksforGeeks</bdo><br><!--This is bdo rtl Tag--><bdo dir="rtl">GeeksforGeeks</bdo></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205172022/bd.png)

    `Supported Browsers:`

    * Apple Safari
    * Edge 12 and above
    * Google Chrome
    * Firefox
    * Opera
    * Internet Explorer
    The <bdo> stands for Bi-Directional Override. This tag is used to specify the text direction or used to change the current direction.

    `Syntax:`




    <bdo dir> Contents... </bdo>

    `Attributes:` This element contains dir attributes which are used to specify the direction of text written inside the <bdo> element. The [dir attribute](https://www.geeksforgeeks.org/html-dir-attribute/) contains two values which are listed below:


    * `rtl:` The text direction from right to left (reverse the text).
    * `ltr:` The text direction from left to right.

    `Example:` The below example illustrate the bdo tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><bdo> Tag</h2><!--This is bdo ltr Tag--><bdo dir="ltr">GeeksforGeeks</bdo><br><!--This is bdo rtl Tag--><bdo dir="rtl">GeeksforGeeks</bdo></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205172022/bd.png)

    `Supported Browsers:`

    * Apple Safari
    * Edge 12 and above
    * Google Chrome
    * Firefox
    * Opera
    * Internet Explorer


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
            tagName="bdo",
        )


class Bgsound(BaseVoidElement):
    """ """

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
            tagName="bgsound",
        )


class Big(BaseElement):
    """
    The <big> tag in HTML is used to increase the selected text size by one larger than the surrounding text. In HTML 5, it can be used by CSS.

    `Note:` It is not supported in HTML 5

    `Syntax:`




    <big> Contents... </big>

    Below examples illustrate the <big> tag in HTML:

    `Example 1:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!--Paragraph Tag --><p>This is paragraph text</p> <!--Big Tag--><big>This is big Tag text</big></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205171110/b1-200x127.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!--Paragraph Tag --><p>This is normal paragraph text</p> <!--CSS Style used in big Tag --><big style="font-size:40px;font-weight:bold;color:green; ">Using CSS style in big Tag</big></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205171132/b2.png)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    The <big> tag in HTML is used to increase the selected text size by one larger than the surrounding text. In HTML 5, it can be used by CSS.

    `Note:` It is not supported in HTML 5

    `Syntax:`




    <big> Contents... </big>

    Below examples illustrate the <big> tag in HTML:

    `Example 1:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!--Paragraph Tag --><p>This is paragraph text</p> <!--Big Tag--><big>This is big Tag text</big></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205171110/b1-200x127.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!--Paragraph Tag --><p>This is normal paragraph text</p> <!--CSS Style used in big Tag --><big style="font-size:40px;font-weight:bold;color:green; ">Using CSS style in big Tag</big></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205171132/b2.png)

    `Supported Browsers:`

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
            tagName="big",
        )


class Blockquote(BaseElement):
    """
    The <blockquote> tag in [`HTML`](https://www.geeksforgeeks.org/html/) is used to display long quotations (a section that is quoted from another source). It changes the alignment to make it unique from others. It contains both opening and closing tags. In blockquote tags, we can use elements like headings, lists, paragraphs, etc.

    `Note:` The <blockquote> tag in HTML4.1 defines the long quotation i.e. quotations that span multiple lines. But in HTML5, the <blockquote> tag specifies the section that is quoted from other sources.
      `Syntax:`



    <blockquote> Contents... </blockquote>

    `Attribute:` It contains a single attribute *cite* which is used to specify the source of the quotation.

    `Example 1:` This example illustrates the blockquote tag

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2><blockquote> Tag</h2><!--blockquote Tag starts here --><blockquote cite="<https://www.geeksforgeeks.org/html-tutorials/>"> <p>HTML stands for HyperText Markup Language. Itis used to design web pages using a markup language.HTML is the combination of Hypertext and Markup language.Hypertext defines the link between the web pages. Amarkup language is used to define the text document withintag which defines the structure of web pages.</p> </blockquote><!--blockquote Tag ends here --></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205163700/updatebq.png)

    `Example 2:` This example illustrates the blockquote tag

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2> <blockquote> Tag</h2> <p>This is blockquote Tag text with attribute cite</p> <!--blockquote Tag starts here --><blockquote cite="www.geeksforgeeks.org">GeeksforGeeks:A computer science portal for geeks</blockquote><!--blockquote Tag ends here --></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205160240/bq.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera


    The <blockquote> tag in [`HTML`](https://www.geeksforgeeks.org/html/) is used to display long quotations (a section that is quoted from another source). It changes the alignment to make it unique from others. It contains both opening and closing tags. In blockquote tags, we can use elements like headings, lists, paragraphs, etc.

    `Note:` The <blockquote> tag in HTML4.1 defines the long quotation i.e. quotations that span multiple lines. But in HTML5, the <blockquote> tag specifies the section that is quoted from other sources.
      `Syntax:`



    <blockquote> Contents... </blockquote>

    `Attribute:` It contains a single attribute *cite* which is used to specify the source of the quotation.

    `Example 1:` This example illustrates the blockquote tag

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2><blockquote> Tag</h2><!--blockquote Tag starts here --><blockquote cite="<https://www.geeksforgeeks.org/html-tutorials/>"> <p>HTML stands for HyperText Markup Language. Itis used to design web pages using a markup language.HTML is the combination of Hypertext and Markup language.Hypertext defines the link between the web pages. Amarkup language is used to define the text document withintag which defines the structure of web pages.</p> </blockquote><!--blockquote Tag ends here --></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205163700/updatebq.png)

    `Example 2:` This example illustrates the blockquote tag

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2> <blockquote> Tag</h2> <p>This is blockquote Tag text with attribute cite</p> <!--blockquote Tag starts here --><blockquote cite="www.geeksforgeeks.org">GeeksforGeeks:A computer science portal for geeks</blockquote><!--blockquote Tag ends here --></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205160240/bq.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera




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
            tagName="blockquote",
        )


class Body(BaseElement):
    """
      The <body> tag in HTML is used to define the main content present inside an HTML page. It is always enclosed within <html>tag. The <body> tag is the last child of <html> tag. A body tag contains starting as well as an ending tag.


    `Syntax:`



    <body> Body Contents... </body>

    `Attributes:` There are many attributes in the <body> tag which are depreciated from HTML5 are listed below:

    * [`background`](https://www.geeksforgeeks.org/html-body-background-attribute/)`:` It contains the URL of the background image. It is used to set the background image.
    * [`bgcolor`](https://www.geeksforgeeks.org/html-bgcolor-attribute/)`:` It is used to specify the background color of an image.
    * [`alink`](https://www.geeksforgeeks.org/html-body-alink-attribute/)`:` It is used to specify the color of the active link.
    * [`link`](https://www.geeksforgeeks.org/html-links/)`:` It is used to specify the color of visited links.
    * [`text`](https://www.geeksforgeeks.org/html-body-text-attribute/)`:` It specifies the color of the text in a document.
    * [`vlink`](https://www.geeksforgeeks.org/html-body-vlink-attribute/)`:` It specifies the color of visited links.

    `Example :` Using HTML body tag. All then content placed inside the body tag.

    ```html
    <!DOCTYPE html><html> <!-- body tag starts here --><body><h1>GeeksforGeeks</h1><h2>body Tag</h2>  <p>This is paragraph text</p>   </body><!-- body tag ends here --> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205145207/bdy.png)

    `Example 2:` Example to show the functioning of a Body tag along with its CSS implementation.

    ```html
    <!DOCTYPE html><html> <!-- style on the body tag --><!-- body tag starts here --><body style="background-color:seagreen"><h1>GeeksforGeeks</h1><h2>HTML body Tag</h2>  <p>This is paragraph Tag</p>  </body><!-- body tag ends here --></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205145419/para.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari


      The <body> tag in HTML is used to define the main content present inside an HTML page. It is always enclosed within <html>tag. The <body> tag is the last child of <html> tag. A body tag contains starting as well as an ending tag.


    `Syntax:`



    <body> Body Contents... </body>

    `Attributes:` There are many attributes in the <body> tag which are depreciated from HTML5 are listed below:

    * [`background`](https://www.geeksforgeeks.org/html-body-background-attribute/)`:` It contains the URL of the background image. It is used to set the background image.
    * [`bgcolor`](https://www.geeksforgeeks.org/html-bgcolor-attribute/)`:` It is used to specify the background color of an image.
    * [`alink`](https://www.geeksforgeeks.org/html-body-alink-attribute/)`:` It is used to specify the color of the active link.
    * [`link`](https://www.geeksforgeeks.org/html-links/)`:` It is used to specify the color of visited links.
    * [`text`](https://www.geeksforgeeks.org/html-body-text-attribute/)`:` It specifies the color of the text in a document.
    * [`vlink`](https://www.geeksforgeeks.org/html-body-vlink-attribute/)`:` It specifies the color of visited links.

    `Example :` Using HTML body tag. All then content placed inside the body tag.

    ```html
    <!DOCTYPE html><html> <!-- body tag starts here --><body><h1>GeeksforGeeks</h1><h2>body Tag</h2>  <p>This is paragraph text</p>   </body><!-- body tag ends here --> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205145207/bdy.png)

    `Example 2:` Example to show the functioning of a Body tag along with its CSS implementation.

    ```html
    <!DOCTYPE html><html> <!-- style on the body tag --><!-- body tag starts here --><body style="background-color:seagreen"><h1>GeeksforGeeks</h1><h2>HTML body Tag</h2>  <p>This is paragraph Tag</p>  </body><!-- body tag ends here --></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205145419/para.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
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
            tagName="body",
        )


class B(BaseElement):
    """
    The <b> tag in HTML is used to specify the bold text without any extra importance. The text is written within <b> tag display in bold size. You can do that by using *font-weight: bold;* property in CSS. It is a container tag that contains an opening tag, content & closing tag. There is a similar tag, [<strong>](https://www.geeksforgeeks.org/html-strong-tag/#:~:text=The%20tag%20in%20HTML,Make%20that%20text%20bold.) tag that is the parsed tag and used to show the importance of the text & has a similar effect on content.

    As per the HTML5 specification, the <b> tag should be used as a last option to resort when no other tag is more appropriate. The HTML5 specification states that for headings, it should be depicted by the [<h1> to <h6>](https://www.geeksforgeeks.org/html-heading/) tags, for emphasized text, it must be depicted by the [<em>](https://www.geeksforgeeks.org/html-em-tag/) tag & similar wise, the important text by the [<strong>](https://www.geeksforgeeks.org/html-strong-tag/#:~:text=The%20tag%20in%20HTML,Make%20that%20text%20bold.) tag, & for marked/highlighted text, it should be denoted with the [<mark>](https://www.geeksforgeeks.org/html-mark-tag/#:~:text=The%20tag%20in%20HTML,the%20text%20in%20a%20paragraph.&text=Example%201%3A%20This%20example%20uses,text%20content%20in%20yellow%20color.) tag.

    `Syntax:`



    <b> Contents... </b>

    `Accepted Attributes:` This is a [Global attribute](https://www.geeksforgeeks.org/html-global-attributes/), and can be used on any HTML element.

    `Example 1:` This simple code example illustrates highlighting the text by making it as bold text in HTML.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3><p>A <b>Computer Science portal</b> for geeks.It contains well written, well thought andwell explained <b>computer science andprogramming articles.</b></p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921171114/8.jpg)

    `Example 2:` In this example, we have used the <b> tag & <p> tag to illustrates the difference in the text appearance & their sizes.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3> <!--paragraph Tag --><p>This is normal paragraph Tag text</p> <!--bold Tag --><b>This is bold Tag text</b></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921165842/6.jpg)

    `Example 3:` In this example, we have used the [CSS font-weight property](https://www.geeksforgeeks.org/css-font-weight-property/) whose value is set to bold to make the text bold.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3> <!--paragraph Tag --><p>This is normal paragraph Tag text</p> <!--Using CSS in paragraph Tag for making text bold  --><p style="font-weight: bold">This is bold text using CSS</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921170143/7.jpg)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Microsoft Edge
    * Firefox 1 and above
    * Opera
    * Safari


    The <b> tag in HTML is used to specify the bold text without any extra importance. The text is written within <b> tag display in bold size. You can do that by using *font-weight: bold;* property in CSS. It is a container tag that contains an opening tag, content & closing tag. There is a similar tag, [<strong>](https://www.geeksforgeeks.org/html-strong-tag/#:~:text=The%20tag%20in%20HTML,Make%20that%20text%20bold.) tag that is the parsed tag and used to show the importance of the text & has a similar effect on content.

    As per the HTML5 specification, the <b> tag should be used as a last option to resort when no other tag is more appropriate. The HTML5 specification states that for headings, it should be depicted by the [<h1> to <h6>](https://www.geeksforgeeks.org/html-heading/) tags, for emphasized text, it must be depicted by the [<em>](https://www.geeksforgeeks.org/html-em-tag/) tag & similar wise, the important text by the [<strong>](https://www.geeksforgeeks.org/html-strong-tag/#:~:text=The%20tag%20in%20HTML,Make%20that%20text%20bold.) tag, & for marked/highlighted text, it should be denoted with the [<mark>](https://www.geeksforgeeks.org/html-mark-tag/#:~:text=The%20tag%20in%20HTML,the%20text%20in%20a%20paragraph.&text=Example%201%3A%20This%20example%20uses,text%20content%20in%20yellow%20color.) tag.

    `Syntax:`



    <b> Contents... </b>

    `Accepted Attributes:` This is a [Global attribute](https://www.geeksforgeeks.org/html-global-attributes/), and can be used on any HTML element.

    `Example 1:` This simple code example illustrates highlighting the text by making it as bold text in HTML.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3><p>A <b>Computer Science portal</b> for geeks.It contains well written, well thought andwell explained <b>computer science andprogramming articles.</b></p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921171114/8.jpg)

    `Example 2:` In this example, we have used the <b> tag & <p> tag to illustrates the difference in the text appearance & their sizes.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3> <!--paragraph Tag --><p>This is normal paragraph Tag text</p> <!--bold Tag --><b>This is bold Tag text</b></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921165842/6.jpg)

    `Example 3:` In this example, we have used the [CSS font-weight property](https://www.geeksforgeeks.org/css-font-weight-property/) whose value is set to bold to make the text bold.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h3>HTML b tag</h3> <!--paragraph Tag --><p>This is normal paragraph Tag text</p> <!--Using CSS in paragraph Tag for making text bold  --><p style="font-weight: bold">This is bold text using CSS</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921170143/7.jpg)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Microsoft Edge
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
            tagName="b",
        )


class Br(BaseVoidElement):
    """ """

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
            tagName="br",
        )


class Button(BaseElement):
    """
    The <button> tag in HTML is used to define the clickable button. <button> tag is used to submit the content. The images and text content can use inside <button> tag.Different browsers use different default types for <button>. Buttons can be styled using CSS.

      `Syntax:`



    <button type = "button">

    `Attributes:` The various attributes that can be used with the “button” tag are listed below:

    * [autofocus](https://www.geeksforgeeks.org/html-button-autofocus-attribute/): It is used to specify that the button should get automatically get focus or not when the page loads
    * [disabled](https://www.geeksforgeeks.org/html-disabled-attribute/): It is used indicates whether the element is disabled or not. If this attribute is set, the element is disabled.
    * [form](https://www.geeksforgeeks.org/html-form-tag/): It is used to create a form for user input. There are many elements that> are used within the >form tag.
    * [formaction](https://www.geeksforgeeks.org/html-button-formaction-attribute/): It is used to specify where to send the data of the form.
    * [formnovalidate](https://www.geeksforgeeks.org/html-input-formnovalidate-attribute/): It is used to specify that the Input Element should not be validated when submitting the form.
    * [formenctype](https://www.geeksforgeeks.org/html-button-formenctype-attribute/): It is used to specify that the form data should be encoded when submitting to the server.
    * [formmethod](https://www.geeksforgeeks.org/html-button-formmethod-attribute/): It is used to specify the HTTP method used to send data while submitting the form.
    * [formtarget](https://www.geeksforgeeks.org/html-input-formtarget-attribute/): It is used to specify the name or a keyword which indicates where to display the response after submitting the form.
    * [type](https://www.geeksforgeeks.org/html-type-attribute/): It is used to specify the type of button for button elements. It is also used in <input> element to specify the type of input to display.
    * [value](https://www.geeksforgeeks.org/html-value-attribute/): It is used to specify the value of the element with which it is used. It has different meaning for different HTML elements.

    `Example:` The below example explain the HTML button Tag.

    ```html
    <!DOCTYPE html><html><body><h3>HTML button Tag</h3> <!-- button tag starts from here --><button type = "button" onclick ="alert('Welcome to GeeksforGeeks')">Click Here</button><!-- button tag ends here --> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210223181040/Screenshot-2021-02-23-180946.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox
    * Safari
    * Opera
    The <button> tag in HTML is used to define the clickable button. <button> tag is used to submit the content. The images and text content can use inside <button> tag.Different browsers use different default types for <button>. Buttons can be styled using CSS.

      `Syntax:`



    <button type = "button">

    `Attributes:` The various attributes that can be used with the “button” tag are listed below:

    * [autofocus](https://www.geeksforgeeks.org/html-button-autofocus-attribute/): It is used to specify that the button should get automatically get focus or not when the page loads
    * [disabled](https://www.geeksforgeeks.org/html-disabled-attribute/): It is used indicates whether the element is disabled or not. If this attribute is set, the element is disabled.
    * [form](https://www.geeksforgeeks.org/html-form-tag/): It is used to create a form for user input. There are many elements that> are used within the >form tag.
    * [formaction](https://www.geeksforgeeks.org/html-button-formaction-attribute/): It is used to specify where to send the data of the form.
    * [formnovalidate](https://www.geeksforgeeks.org/html-input-formnovalidate-attribute/): It is used to specify that the Input Element should not be validated when submitting the form.
    * [formenctype](https://www.geeksforgeeks.org/html-button-formenctype-attribute/): It is used to specify that the form data should be encoded when submitting to the server.
    * [formmethod](https://www.geeksforgeeks.org/html-button-formmethod-attribute/): It is used to specify the HTTP method used to send data while submitting the form.
    * [formtarget](https://www.geeksforgeeks.org/html-input-formtarget-attribute/): It is used to specify the name or a keyword which indicates where to display the response after submitting the form.
    * [type](https://www.geeksforgeeks.org/html-type-attribute/): It is used to specify the type of button for button elements. It is also used in <input> element to specify the type of input to display.
    * [value](https://www.geeksforgeeks.org/html-value-attribute/): It is used to specify the value of the element with which it is used. It has different meaning for different HTML elements.

    `Example:` The below example explain the HTML button Tag.

    ```html
    <!DOCTYPE html><html><body><h3>HTML button Tag</h3> <!-- button tag starts from here --><button type = "button" onclick ="alert('Welcome to GeeksforGeeks')">Click Here</button><!-- button tag ends here --> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210223181040/Screenshot-2021-02-23-180946.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox
    * Safari
    * Opera


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
            tagName="button",
        )


class Caption(BaseElement):
    """
    The `caption` tagis used to specify the caption of a table. This tag will be inserted just after the <table> tag. Only one caption can be specified for one table. It is by default aligned to the center.


    `Syntax:`



    <caption align = "value" ></caption>

    `Attributes:` This tag accepts a single attribute as mentioned above and described below.

    * [`align`](https://www.geeksforgeeks.org/html-align-attribute/)`:` This attribute is used to specify the alignment of text content.

    Below examples illustrate the <caption> tag in HTML:

    `Example 1:` Adding a caption to the table i.e. by default aligned to the center.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksForGeeks</h1><h2>HTML <Caption> Tag</h2> <table><!-- Adding caption to the table --><caption>Students</caption><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr><tr><td>Priya</td><td>Sharma</td><td>24</td></tr><tr><td>Arun</td><td>Singh</td><td>32</td></tr><tr><td>Sam</td><td>Watson</td><td>41</td></tr></table></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208120049/caption.png)

    `Example 2:` Adding a caption to the table and adding align attribute to it to align the caption to the left.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <Caption> Tag</h2> <table><!-- Adding a caption to the tableand aligning it to the left--><caption style="text-align: left">Students</caption><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr><tr><td>Priya</td><td>Sharma</td><td>24</td></tr><tr><td>Arun</td><td>Singh</td><td>32</td></tr><tr><td>Sam</td><td>Watson</td><td>41</td></tr></table></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208120113/caption2.png)



    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari


    The `caption` tagis used to specify the caption of a table. This tag will be inserted just after the <table> tag. Only one caption can be specified for one table. It is by default aligned to the center.


    `Syntax:`



    <caption align = "value" ></caption>

    `Attributes:` This tag accepts a single attribute as mentioned above and described below.

    * [`align`](https://www.geeksforgeeks.org/html-align-attribute/)`:` This attribute is used to specify the alignment of text content.

    Below examples illustrate the <caption> tag in HTML:

    `Example 1:` Adding a caption to the table i.e. by default aligned to the center.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksForGeeks</h1><h2>HTML <Caption> Tag</h2> <table><!-- Adding caption to the table --><caption>Students</caption><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr><tr><td>Priya</td><td>Sharma</td><td>24</td></tr><tr><td>Arun</td><td>Singh</td><td>32</td></tr><tr><td>Sam</td><td>Watson</td><td>41</td></tr></table></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208120049/caption.png)

    `Example 2:` Adding a caption to the table and adding align attribute to it to align the caption to the left.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <Caption> Tag</h2> <table><!-- Adding a caption to the tableand aligning it to the left--><caption style="text-align: left">Students</caption><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr><tr><td>Priya</td><td>Sharma</td><td>24</td></tr><tr><td>Arun</td><td>Singh</td><td>32</td></tr><tr><td>Sam</td><td>Watson</td><td>41</td></tr></table></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208120113/caption2.png)



    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="caption",
        )


class Canvas(BaseElement):
    """
    The <canvas> tag in HTML is used to draw graphics on a web page using JavaScript. It can be used to draw paths, boxes, texts, gradients, and adding images. By default, it does not contain borders and text.

    `Note:` The <canvas> tag is new in HTML5.

    `Syntax:`



    <canvas id = "script"> Contents... </canvas>

    `Attributes:` The tag accepts two attributes as mentioned above and described below.

    * [`height`](https://www.geeksforgeeks.org/html-dom-style-height-property/)`:` This attribute is used to set the height of the canvas.
    * [`width`](https://www.geeksforgeeks.org/html-object-width-attribute/)`:` This attribute is used to set the width of the canvas.

    `Example 1:`

    ```html
    <!DOCTYPE html><html><body> <!-- canvas Tag starts here --><canvas id = "GeeksforGeeks" width = "200"height = "100" style = "border:1px solid black"></canvas><!-- canvas Tag ends here --> </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas1.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><!-- HTML code to illustrate canvas tag --><canvas id = "geeks" height = "200" width = "200"style = "border:1px solid black"></canvas> <script>var c = document.getElementById("geeks");var cx = c.getContext("2d");cx.beginPath();cx.arc(100, 100, 90, 0, 2 * Math.PI);cx.stroke();</script> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas2.png)

    `Example 3:`

    ```html
    <!DOCTYPE html><html><body> <!-- canvas tag starts here --><canvas id = "geeks" width = "200" height = "200"style = "border:1px solid black"></canvas><!-- canvas tag ends here --> <script>var c=document.getElementById("geeks");var cx = c.getContext("2d");var grd = cx.createRadialGradient(100,100, 5, 100, 100, 100);grd.addColorStop(0, "red");grd.addColorStop(1, "green");cx.fillStyle = grd;cx.fillRect(0, 0, 200, 200);</script> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas3.png)

    `Supported Browsers:`

    * Google Chrome 1.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 1.5 and above
    * Opera 9.0 and above
    * Safari 2.0 and above


    The <canvas> tag in HTML is used to draw graphics on a web page using JavaScript. It can be used to draw paths, boxes, texts, gradients, and adding images. By default, it does not contain borders and text.

    `Note:` The <canvas> tag is new in HTML5.

    `Syntax:`



    <canvas id = "script"> Contents... </canvas>

    `Attributes:` The tag accepts two attributes as mentioned above and described below.

    * [`height`](https://www.geeksforgeeks.org/html-dom-style-height-property/)`:` This attribute is used to set the height of the canvas.
    * [`width`](https://www.geeksforgeeks.org/html-object-width-attribute/)`:` This attribute is used to set the width of the canvas.

    `Example 1:`

    ```html
    <!DOCTYPE html><html><body> <!-- canvas Tag starts here --><canvas id = "GeeksforGeeks" width = "200"height = "100" style = "border:1px solid black"></canvas><!-- canvas Tag ends here --> </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas1.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><!-- HTML code to illustrate canvas tag --><canvas id = "geeks" height = "200" width = "200"style = "border:1px solid black"></canvas> <script>var c = document.getElementById("geeks");var cx = c.getContext("2d");cx.beginPath();cx.arc(100, 100, 90, 0, 2 * Math.PI);cx.stroke();</script> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas2.png)

    `Example 3:`

    ```html
    <!DOCTYPE html><html><body> <!-- canvas tag starts here --><canvas id = "geeks" width = "200" height = "200"style = "border:1px solid black"></canvas><!-- canvas tag ends here --> <script>var c=document.getElementById("geeks");var cx = c.getContext("2d");var grd = cx.createRadialGradient(100,100, 5, 100, 100, 100);grd.addColorStop(0, "red");grd.addColorStop(1, "green");cx.fillStyle = grd;cx.fillRect(0, 0, 200, 200);</script> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/canvas3.png)

    `Supported Browsers:`

    * Google Chrome 1.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 1.5 and above
    * Opera 9.0 and above
    * Safari 2.0 and above




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
            tagName="canvas",
        )


class Center(BaseElement):
    """
    The `<center> tag` in HTML is used to set the alignment of text into the center. This tag is not supported in HTML5. CSS’s property is used to set the alignment of the element instead of the center tag in HTML5.

    `Syntax:`



    <center> Contents... </center>

    `Attributes:` This tag does not accept any attribute.

    `Example 1:` In this example, we simply used the Hi Geeks content in the HTML center tag.

    ```html
    <!DOCTYPE html><html> <body><h2>Welcome to GeeksforGeeks</h2><!--center tag is used here--><center>Hi Geeks</center> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210916173151/162.png)HTML <center> tag

    `Example 2:` This example illustrates the HTML center tag.

    ```html
    <!DOCTYPE html><html><body><!--center tag starts here --><center><h1>GeeksforGeeks</h1><h2>html center tag</h2> <p>GeeksforGeeks: A computer science portal for geeks</p> <!--center tag ends here --></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220914155852/htmlcentertag.png)

    `Example 3:` Use CSS property in HTML5 to set the text alignment into the center.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><!--center using CSS style  --><h2 style="text-align: center">CSS center property</h2></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208122101/scrn.png)HTML <center> tag

    `Supported Browsers:`

    * Google Chrome
    * Microsoft Edge 12 and above
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    The `<center> tag` in HTML is used to set the alignment of text into the center. This tag is not supported in HTML5. CSS’s property is used to set the alignment of the element instead of the center tag in HTML5.

    `Syntax:`



    <center> Contents... </center>

    `Attributes:` This tag does not accept any attribute.

    `Example 1:` In this example, we simply used the Hi Geeks content in the HTML center tag.

    ```html
    <!DOCTYPE html><html> <body><h2>Welcome to GeeksforGeeks</h2><!--center tag is used here--><center>Hi Geeks</center> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210916173151/162.png)HTML <center> tag

    `Example 2:` This example illustrates the HTML center tag.

    ```html
    <!DOCTYPE html><html><body><!--center tag starts here --><center><h1>GeeksforGeeks</h1><h2>html center tag</h2> <p>GeeksforGeeks: A computer science portal for geeks</p> <!--center tag ends here --></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220914155852/htmlcentertag.png)

    `Example 3:` Use CSS property in HTML5 to set the text alignment into the center.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><!--center using CSS style  --><h2 style="text-align: center">CSS center property</h2></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208122101/scrn.png)HTML <center> tag

    `Supported Browsers:`

    * Google Chrome
    * Microsoft Edge 12 and above
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
            tagName="center",
        )


class Cite(BaseElement):
    """
    The <cite> tag in HTML is used to define the title of a work. The <cite> tag in HTML 4.1 define the citation and in HTML5 define the title of work. It displays the text in italic format.

    `Syntax:`



    <cite> Title.. </cite>

    `Example:`


    ```html
    <!DOCTYPE html><html><body><h1 style="color: green;">GeeksforGeeks</h1> <h2>HTML cite Tag</h2> <p>This is normal paragraph text</p> <cite>This is cite tag text</cite></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205112939/cite1-300x151.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari
    The <cite> tag in HTML is used to define the title of a work. The <cite> tag in HTML 4.1 define the citation and in HTML5 define the title of work. It displays the text in italic format.

    `Syntax:`



    <cite> Title.. </cite>

    `Example:`


    ```html
    <!DOCTYPE html><html><body><h1 style="color: green;">GeeksforGeeks</h1> <h2>HTML cite Tag</h2> <p>This is normal paragraph text</p> <cite>This is cite tag text</cite></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205112939/cite1-300x151.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="cite",
        )


class Code(BaseElement):
    """
    The <code> tag in HTML is used to define the piece of computer code. During the creation of web pages sometimes there is a need to display computer programming code. It could be done by any basic heading tag of HTML but HTML provides a separated tag which is <code>.

    The code tag is a specific type of text which represents computer output. HTML provides many methods for text-formatting but <code> tag is displayed with fixed letter size, font, and spacing.

    `Some points about <code> tag:`

    * It is mainly used to display the code snippet into the web browser.
    * This tag styles its element to match the computer’s default text format.
    * The web browsers by default use a monospace font family for displaying <code< tags element content.

    `Syntax:`



    <code> Contents... </code>

    The below examples illustrates the HTML code Tag.

    `Example 1:`

    ```html
    <!DOCTYPE html><html> <body><pre><!--code Tag starts here --><code>#include<stdio.h>int main() {printf("Hello Geeks");}<!--code Tag starts here --></code></pre></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/code1-1.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><pre><!--code Tag starts here --><code>class GFG{// Program begins with a call to main()// Print "Hello, World" to the terminal windowpublic static void main(String args[]){System.out.println("Hello, World");}}<!--code Tag ends here --></code></pre> </body> </html> |

    ```
    `Output:` The program which is written inside the <code> tag has some different font size and font type to the basic heading tag and paragraph tag.

    ![](https://media.geeksforgeeks.org/wp-content/uploads/code2-2.png)

    `Note:` <pre> tag is used to display code snippets because it always keeps the text formatting as it.

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari


    The <code> tag in HTML is used to define the piece of computer code. During the creation of web pages sometimes there is a need to display computer programming code. It could be done by any basic heading tag of HTML but HTML provides a separated tag which is <code>.

    The code tag is a specific type of text which represents computer output. HTML provides many methods for text-formatting but <code> tag is displayed with fixed letter size, font, and spacing.

    `Some points about <code> tag:`

    * It is mainly used to display the code snippet into the web browser.
    * This tag styles its element to match the computer’s default text format.
    * The web browsers by default use a monospace font family for displaying <code< tags element content.

    `Syntax:`



    <code> Contents... </code>

    The below examples illustrates the HTML code Tag.

    `Example 1:`

    ```html
    <!DOCTYPE html><html> <body><pre><!--code Tag starts here --><code>#include<stdio.h>int main() {printf("Hello Geeks");}<!--code Tag starts here --></code></pre></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/code1-1.png)

    `Example 2:`

    ```html
    <!DOCTYPE html><html> <body><pre><!--code Tag starts here --><code>class GFG{// Program begins with a call to main()// Print "Hello, World" to the terminal windowpublic static void main(String args[]){System.out.println("Hello, World");}}<!--code Tag ends here --></code></pre> </body> </html> |

    ```
    `Output:` The program which is written inside the <code> tag has some different font size and font type to the basic heading tag and paragraph tag.

    ![](https://media.geeksforgeeks.org/wp-content/uploads/code2-2.png)

    `Note:` <pre> tag is used to display code snippets because it always keeps the text formatting as it.

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="code",
        )


class Colgroup(BaseElement):
    """
      This tag is used to specify the group of one or more columns in a table for formatting. It is useful for applying styles to entire columns, instead of repeating the styles for each column, and for each row. Use the [<col>](https://www.geeksforgeeks.org/html-col-tag/) tag within the <colgroup> tag to define different properties to a column within a <colgroup>. Most of the attributes in HTML 4.01 <colgroup> are not supported in HTML5.

    `Syntax:`



    <colgroup> Column lists... </colgroup>

    `Attributes:`

    * [`align:`](https://www.geeksforgeeks.org/html-align-attribute/) It is used to align the text or content in the group of columns. The value of the aligned property is left, right, center, justify, char.
    * [`char`](https://www.geeksforgeeks.org/html-col-char-attribute/)`:` It is used to align the character in a column group and the value of these attributes is the character.
    * [`charoff`](https://www.geeksforgeeks.org/html-tr-charoff-attribute/)`:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.
    * [`span`](https://www.geeksforgeeks.org/span-tag-html/)`:` It is used to specify the number of columns that have colgroup tag. The values are in numeric form.
    * [`valign`](https://www.geeksforgeeks.org/html-td-valign-attribute/)`:` It specifies the vertical alignment of content in a colgroup. It’s values are the top, middle, bottom, baseline.
    * [`width`](https://www.geeksforgeeks.org/html-table-width-attribute/)`:` It defines the width of a column group. It’s values are pixels, %, relative\_length.

    `Example:` The below example explains the HTML colgroup tag.



    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML colgroup tag</h2><table><!-- colgroup tag starts here--><colgroup><col span="2" style="background-color: green; color: white" /><col style="background-color: tomato" /><!-- colgroup tag ends here--> </colgroup><tr><th>STUDENT</th><th>COURSE</th><th>AGE</th></tr><tr><td>Manas Chhabra</td><td>BCA</td><td>19</td></tr><tr><td>Anurag Gupta</td><td>B.TECH</td><td>23</td></tr></table></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219163541/colgr.png)

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari




      This tag is used to specify the group of one or more columns in a table for formatting. It is useful for applying styles to entire columns, instead of repeating the styles for each column, and for each row. Use the [<col>](https://www.geeksforgeeks.org/html-col-tag/) tag within the <colgroup> tag to define different properties to a column within a <colgroup>. Most of the attributes in HTML 4.01 <colgroup> are not supported in HTML5.

    `Syntax:`



    <colgroup> Column lists... </colgroup>

    `Attributes:`

    * [`align:`](https://www.geeksforgeeks.org/html-align-attribute/) It is used to align the text or content in the group of columns. The value of the aligned property is left, right, center, justify, char.
    * [`char`](https://www.geeksforgeeks.org/html-col-char-attribute/)`:` It is used to align the character in a column group and the value of these attributes is the character.
    * [`charoff`](https://www.geeksforgeeks.org/html-tr-charoff-attribute/)`:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.
    * [`span`](https://www.geeksforgeeks.org/span-tag-html/)`:` It is used to specify the number of columns that have colgroup tag. The values are in numeric form.
    * [`valign`](https://www.geeksforgeeks.org/html-td-valign-attribute/)`:` It specifies the vertical alignment of content in a colgroup. It’s values are the top, middle, bottom, baseline.
    * [`width`](https://www.geeksforgeeks.org/html-table-width-attribute/)`:` It defines the width of a column group. It’s values are pixels, %, relative\_length.

    `Example:` The below example explains the HTML colgroup tag.



    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML colgroup tag</h2><table><!-- colgroup tag starts here--><colgroup><col span="2" style="background-color: green; color: white" /><col style="background-color: tomato" /><!-- colgroup tag ends here--> </colgroup><tr><th>STUDENT</th><th>COURSE</th><th>AGE</th></tr><tr><td>Manas Chhabra</td><td>BCA</td><td>19</td></tr><tr><td>Anurag Gupta</td><td>B.TECH</td><td>23</td></tr></table></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219163541/colgr.png)

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="colgroup",
        )


class Col(BaseVoidElement):
    """ """

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
            tagName="col",
        )


class Comment(BaseElement):
    """ """

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
            startTagName='!--',
            endTagName='--',
            tagName=None,
        )
    def toHtml(self, prettify: bool = True):
        
        html = f"""\n<!-- {self.attributesToHtml()}>\n{self.dataToHtml()}\n -->"""
        if prettify:
            return str(Pretiffy(html))
        return str(html)


class Data(BaseElement):
    """
    The <data> element gives an address to a given content with a machine-readable translator. This element provides a machine-readable value for the processors and a human-readable value that rendered in the browser.


    `Syntax:`



    <data value=""> Contents... </data>

    `Attributes:` This tag accepts a single attribute as mentioned above and described below.

    * [`value:`](https://www.geeksforgeeks.org/html-value-attribute/) It contains a single machine-readable translation of the content.

    `Note:` If the content is a date or time-related content, then use <time> element instead of the data element.
    `Example:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2><data> Tag</h2>   <p>GeeksforGeeks Subject List:</p>   <ul><!-- data Tag starts here --><li><data value="009">Data Structure</data></li><li><data value="010">Algorithm</data></li><li><data value="011">HTML</data></li><li><data value="019">Operating System</data></li><li><data value="110">Computer Network</data></li><li><data value="111">DBMS</data></li><!-- data Tag ends here --></ul></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208130437/datatag.png)

    `Supported Browsers:`

    * Google Chrome 62.0 and above
    * Edge 18.0 and above
    * Internet Explorer not supported
    * Apple Safari 10 and above
    * Firefox 22.0 and above
    * Opera 49.0 and above


    The <data> element gives an address to a given content with a machine-readable translator. This element provides a machine-readable value for the processors and a human-readable value that rendered in the browser.


    `Syntax:`



    <data value=""> Contents... </data>

    `Attributes:` This tag accepts a single attribute as mentioned above and described below.

    * [`value:`](https://www.geeksforgeeks.org/html-value-attribute/) It contains a single machine-readable translation of the content.

    `Note:` If the content is a date or time-related content, then use <time> element instead of the data element.
    `Example:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2><data> Tag</h2>   <p>GeeksforGeeks Subject List:</p>   <ul><!-- data Tag starts here --><li><data value="009">Data Structure</data></li><li><data value="010">Algorithm</data></li><li><data value="011">HTML</data></li><li><data value="019">Operating System</data></li><li><data value="110">Computer Network</data></li><li><data value="111">DBMS</data></li><!-- data Tag ends here --></ul></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210208130437/datatag.png)

    `Supported Browsers:`

    * Google Chrome 62.0 and above
    * Edge 18.0 and above
    * Internet Explorer not supported
    * Apple Safari 10 and above
    * Firefox 22.0 and above
    * Opera 49.0 and above




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
            tagName="data",
        )


class Datalist(BaseElement):
    """
    The <datalist> tag is used to provide autocomplete feature in the HTML files. It can be used with an input tag so that users can easily fill the data in the forms using select the data.
    `Syntax:`



    <datalist> ... </datalist>

    `Example 1:` The below code explains datalist Tag.

    ```html
    <!DOCTYPE html><html><body><form action=""><label>Your Cars Name: </label><input list="cars"> <!--datalist Tag starts here --><datalist id="cars"><option value="BMW"/><option value="Bentley"/><option value="Mercedes"/><option value="Audi"/><option value="Volkswagen"/></datalist><!--datalist Tag ends here --> </form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210302190750/Screenshot20210302190735.png)

    `Example 2:` The <datalist> tag object can be easily accessed by an input attribute type.

    ```html
    <!DOCTYPE html><html><body><form action=""><label>Your Cars Name: </label><input list="cars" id="carsInput" /> <!--datalist Tag starts here --><datalist id="cars"><option value="BMW" /><option value="Bentley" /><option value="Mercedes" /><option value="Audi" /><option value="Volkswagen" /></datalist><!--datalist Tag ends here --> <button onclick="datalistcall()" type="button">Click Here</button></form><p id="output"></p>   <!-- Will display the select option --><script type="text/javascript">function datalistcall() {var o1 = document.getElementById("carsInput").value;document.getElementById("output").innerHTML ="You select " + o1 + " option";}</script></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210302190852/Screenshot20210302190837.png)

    `Supported Browsers:`

    * Google Chrome 20.0 and above
    * Edge 12.0 and above
    * Internet Explorer 10.0 and above
    * Firefox 4.0 and above
    * Opera 9.5 and above
    * Safari 12.1 and above




    The <datalist> tag is used to provide autocomplete feature in the HTML files. It can be used with an input tag so that users can easily fill the data in the forms using select the data.
    `Syntax:`



    <datalist> ... </datalist>

    `Example 1:` The below code explains datalist Tag.

    ```html
    <!DOCTYPE html><html><body><form action=""><label>Your Cars Name: </label><input list="cars"> <!--datalist Tag starts here --><datalist id="cars"><option value="BMW"/><option value="Bentley"/><option value="Mercedes"/><option value="Audi"/><option value="Volkswagen"/></datalist><!--datalist Tag ends here --> </form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210302190750/Screenshot20210302190735.png)

    `Example 2:` The <datalist> tag object can be easily accessed by an input attribute type.

    ```html
    <!DOCTYPE html><html><body><form action=""><label>Your Cars Name: </label><input list="cars" id="carsInput" /> <!--datalist Tag starts here --><datalist id="cars"><option value="BMW" /><option value="Bentley" /><option value="Mercedes" /><option value="Audi" /><option value="Volkswagen" /></datalist><!--datalist Tag ends here --> <button onclick="datalistcall()" type="button">Click Here</button></form><p id="output"></p>   <!-- Will display the select option --><script type="text/javascript">function datalistcall() {var o1 = document.getElementById("carsInput").value;document.getElementById("output").innerHTML ="You select " + o1 + " option";}</script></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210302190852/Screenshot20210302190837.png)

    `Supported Browsers:`

    * Google Chrome 20.0 and above
    * Edge 12.0 and above
    * Internet Explorer 10.0 and above
    * Firefox 4.0 and above
    * Opera 9.5 and above
    * Safari 12.1 and above






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
            tagName="datalist",
        )


class Dd(BaseElement):
    """
    The <dd> tag in HTML stands for definition description and is used to denote the description or definition of an item in a description list. Paragraphs, line breaks, images, links, lists can be inserted inside a <dd> tag. The <dd> tag in HTML is used along with [<dl>](https://www.geeksforgeeks.org/html-dl-tag/) tag which defines the description list and [<dt>](https://www.geeksforgeeks.org/html-dt-tag/) tag which defines the terms in the description list. The <dd> tag requires a starting, but the end tag is optional.

    `Syntax:`



    <dd> Contents... </dd>

    `Example 1:` Below programs illustrate the <dd> element in HTML.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML dd Tag</h2><dl><dt>Geeks Classes</dt><dd>It is an extensive classroom programmefor enhancing DS and Algo concepts.</dd><br><dt>Fork Python</dt><dd>It is a course designed for beginnersin python.</dd><br><dt>Interview Preparation</dt><dd>It is a course designed for preparationof interviews in top product based companies.</dd></dl></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219183445/dd.png)

    `Example 2:` This example uses the <dd> tag with display property.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML dd Tag</h2><dl><dt>Geeks Classes</dt><dd style="display: inline; margin-left: 60px">It is an extensive classroom programmefor enhancing DS and Algo concepts.</dd></dl></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219184635/dd2.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari


    The <dd> tag in HTML stands for definition description and is used to denote the description or definition of an item in a description list. Paragraphs, line breaks, images, links, lists can be inserted inside a <dd> tag. The <dd> tag in HTML is used along with [<dl>](https://www.geeksforgeeks.org/html-dl-tag/) tag which defines the description list and [<dt>](https://www.geeksforgeeks.org/html-dt-tag/) tag which defines the terms in the description list. The <dd> tag requires a starting, but the end tag is optional.

    `Syntax:`



    <dd> Contents... </dd>

    `Example 1:` Below programs illustrate the <dd> element in HTML.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML dd Tag</h2><dl><dt>Geeks Classes</dt><dd>It is an extensive classroom programmefor enhancing DS and Algo concepts.</dd><br><dt>Fork Python</dt><dd>It is a course designed for beginnersin python.</dd><br><dt>Interview Preparation</dt><dd>It is a course designed for preparationof interviews in top product based companies.</dd></dl></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219183445/dd.png)

    `Example 2:` This example uses the <dd> tag with display property.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML dd Tag</h2><dl><dt>Geeks Classes</dt><dd style="display: inline; margin-left: 60px">It is an extensive classroom programmefor enhancing DS and Algo concepts.</dd></dl></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219184635/dd2.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="dd",
        )


class Dfn(BaseElement):
    """
    The <dfn> tag in HTML represents definition element and is used to representing a defining instance in HTML. Generally, the defining instance is the first use of a term in a document. The <dfn> tag requires a starting as well as an ending tag.


    `Syntax:`



    <dfn>.....</dfn>

    Below examples illustrate the <dfn> tag in HTML:

    `Example 1:`


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag-->  <p><dfn>Geeksforgeeks</dfn> is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.45.19-PM-300x47.png)

    `Example 2:` Using [title attribute](https://www.geeksforgeeks.org/html-title-attribute/) of the <dfn> tag.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with title attribute-->  <p><dfn title="Geeksforgeeks">GFG</dfn>is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.49.13-PM-300x59.png)

    `Example 3:` Using [title attribute](https://www.geeksforgeeks.org/html-title-attribute/) of the [<abbr> tag](https://www.geeksforgeeks.org/html-abbr-tag/) inside the <dfn> element.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with title attribute and abbr tag-->  <p><dfn><abbr title="Geeksforgeeks">GFG</abbr></dfn> is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604131913/dfnex3.png)

    `Example 4:` Using [id attribute](https://www.geeksforgeeks.org/html-id-attributes/) along with the <dfn> tag.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with id attribute-->  <p><dfn id="Geeksforgeeks">GFG</dfn> is aportal for geeks.</p>    <p>Practice questions for crackingtechnical interviews.</p>    <p>Prepare for GATE CSE – 2019</p>    <p>Visit <a href="#Geeksforgeeks">GFG</a>.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.57.46-PM-300x110.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <dfn> tag in HTML represents definition element and is used to representing a defining instance in HTML. Generally, the defining instance is the first use of a term in a document. The <dfn> tag requires a starting as well as an ending tag.


    `Syntax:`



    <dfn>.....</dfn>

    Below examples illustrate the <dfn> tag in HTML:

    `Example 1:`


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag-->  <p><dfn>Geeksforgeeks</dfn> is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.45.19-PM-300x47.png)

    `Example 2:` Using [title attribute](https://www.geeksforgeeks.org/html-title-attribute/) of the <dfn> tag.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with title attribute-->  <p><dfn title="Geeksforgeeks">GFG</dfn>is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.49.13-PM-300x59.png)

    `Example 3:` Using [title attribute](https://www.geeksforgeeks.org/html-title-attribute/) of the [<abbr> tag](https://www.geeksforgeeks.org/html-abbr-tag/) inside the <dfn> element.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with title attribute and abbr tag-->  <p><dfn><abbr title="Geeksforgeeks">GFG</abbr></dfn> is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604131913/dfnex3.png)

    `Example 4:` Using [id attribute](https://www.geeksforgeeks.org/html-id-attributes/) along with the <dfn> tag.


    ```html
    <!DOCTYPE html> <html> <body> <!--HTML dfn tag with id attribute-->  <p><dfn id="Geeksforgeeks">GFG</dfn> is aportal for geeks.</p>    <p>Practice questions for crackingtechnical interviews.</p>    <p>Prepare for GATE CSE – 2019</p>    <p>Visit <a href="#Geeksforgeeks">GFG</a>.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-2.57.46-PM-300x110.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="dfn",
        )


class Del(BaseElement):
    """
    The <del> tag in HTML stands for delete and is used to mark a portion of text which has been deleted from the document. The deleted text is rendered as strike-through text by the web browsers although this property can be changed using [CSS text-decoration property](https://www.geeksforgeeks.org/css-text-decoration-property/). The <del> tag requires a starting and ending tag.

    `Attributes:` The <del> tag contains two attributes which are listed below:

    * [`cite`](https://www.geeksforgeeks.org/html-cite-attribute/)`:` It is used to specify the URL of the document or message which denotes the reason for deleting the text.
    * [`datetime`](https://www.geeksforgeeks.org/html-datetime-attribute/)`:` It is used to specify the date and time of the deleted text.

    `Syntax:`



    <del> Contents... </del>

    `Example 1:` Below example illustrate the <del> element in HTML:

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML del Tag</h2><!-- HTML del tag is used in paragraph Tag -->   <p>GeeksforGeeks is a <del>mathematical</del>science portal</p>   </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219172506/del.png)

    `Example 2:` This example use the <del> tag with the datetime attribute.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML del Tag</h2><!-- HTML del tag is used in paragraph Tag -->   <p>GeeksforGeeks is a <del>mathematical</del>science portal</p>   </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219172557/del.png)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari
    * Edge 12 and above


    The <del> tag in HTML stands for delete and is used to mark a portion of text which has been deleted from the document. The deleted text is rendered as strike-through text by the web browsers although this property can be changed using [CSS text-decoration property](https://www.geeksforgeeks.org/css-text-decoration-property/). The <del> tag requires a starting and ending tag.

    `Attributes:` The <del> tag contains two attributes which are listed below:

    * [`cite`](https://www.geeksforgeeks.org/html-cite-attribute/)`:` It is used to specify the URL of the document or message which denotes the reason for deleting the text.
    * [`datetime`](https://www.geeksforgeeks.org/html-datetime-attribute/)`:` It is used to specify the date and time of the deleted text.

    `Syntax:`



    <del> Contents... </del>

    `Example 1:` Below example illustrate the <del> element in HTML:

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML del Tag</h2><!-- HTML del tag is used in paragraph Tag -->   <p>GeeksforGeeks is a <del>mathematical</del>science portal</p>   </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219172506/del.png)

    `Example 2:` This example use the <del> tag with the datetime attribute.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML del Tag</h2><!-- HTML del tag is used in paragraph Tag -->   <p>GeeksforGeeks is a <del>mathematical</del>science portal</p>   </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210219172557/del.png)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari
    * Edge 12 and above




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
            tagName="del",
        )


class Details(BaseElement):
    """
    The <details> tag is used for the content/information which is initially hidden but could be displayed if the user wishes to see it. This tag is used to create an interactive widget that the user can open or close. The content of the details tag is visible when open the set attributes. The summary tag is used with the ``details`` tag for specifying visible heading.

    This tag is new in HTML5.

    ``Syntax:``



    <details>
     <summary> Text content </summary>
     <div> Content . . . >
    </details>


    ``Attributes:``

    [``details open``](https://www.geeksforgeeks.org/html-details-open-attribute/)``:`` The detail tag has an attribute called ``open`` which is used to display the hidden information by default.

    ``Example:`` The below code explains the details tag.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!-- details tag starts here --><details><summary>GeeksforGeeks</summary><p>A computer science portal for geeks</p><div>It is a computer science portalwhere you can learn programming.</div><!-- details tag ends here --></details></body> </html> |

    ````
    `Output:``

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210222173342/details.png)

    ``Syntax:``



    <details open>
     <summary> Text content </summary>
     <div> Content . . . >
    </details>



    ``Example:`` The below code explains the details open tag in details tag.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!-- details open tag starts here --><details open><summary>GeeksforGeeks</summary><p>A computer science portal for geeks</p><div>It is a computer science portal where youcan learn programming.</div><!-- details open tag ends here --></details></body> </html> |

    ````
    `Output:``


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210222173408/detailopen.png)

    ``Supported Browsers:``

    * Google Chrome
    * Edge
    * Firefox
    * Opera
    * Safari


    The <details> tag is used for the content/information which is initially hidden but could be displayed if the user wishes to see it. This tag is used to create an interactive widget that the user can open or close. The content of the details tag is visible when open the set attributes. The summary tag is used with the ``details`` tag for specifying visible heading.

    This tag is new in HTML5.

    ``Syntax:``



    <details>
     <summary> Text content </summary>
     <div> Content . . . >
    </details>


    ``Attributes:``

    [``details open``](https://www.geeksforgeeks.org/html-details-open-attribute/)``:`` The detail tag has an attribute called ``open`` which is used to display the hidden information by default.

    ``Example:`` The below code explains the details tag.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!-- details tag starts here --><details><summary>GeeksforGeeks</summary><p>A computer science portal for geeks</p><div>It is a computer science portalwhere you can learn programming.</div><!-- details tag ends here --></details></body> </html> |

    ````
    `Output:``

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210222173342/details.png)

    ``Syntax:``



    <details open>
     <summary> Text content </summary>
     <div> Content . . . >
    </details>



    ``Example:`` The below code explains the details open tag in details tag.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><!-- details open tag starts here --><details open><summary>GeeksforGeeks</summary><p>A computer science portal for geeks</p><div>It is a computer science portal where youcan learn programming.</div><!-- details open tag ends here --></details></body> </html> |

    ````
    `Output:``


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210222173408/detailopen.png)

    ``Supported Browsers:``

    * Google Chrome
    * Edge
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
            tagName="details",
        )


class Dialog(BaseElement):
    """
    The <dialog> tag is used to specify the dialog box or window. This tag is used to create a popup dialog and models on a web page. This tag is new in HTML5.


    `Syntax:`



    <dialog open> Contents... </dialog>

    `Attributes:` This tag accepts a single attribute [*open*](https://www.geeksforgeeks.org/html-open-attribute/) which is used to specify the dialog element is active and the user can interact with the tag element.
    `Example:`

    ```html
    <!DOCTYPE html><html><body><h1><dialog> tag</h1> <!--This is an open dialog Tag--><dialog open>Welcome to GeeksforGeeks</dialog></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604122941/opendialog.png)

    `Supported Browsers:`

    * Google Chrome 37.0
    * Edge 79.0
    * Firefox 98.0
    * Opera 24.0
    * Safari 15.4
    The <dialog> tag is used to specify the dialog box or window. This tag is used to create a popup dialog and models on a web page. This tag is new in HTML5.


    `Syntax:`



    <dialog open> Contents... </dialog>

    `Attributes:` This tag accepts a single attribute [*open*](https://www.geeksforgeeks.org/html-open-attribute/) which is used to specify the dialog element is active and the user can interact with the tag element.
    `Example:`

    ```html
    <!DOCTYPE html><html><body><h1><dialog> tag</h1> <!--This is an open dialog Tag--><dialog open>Welcome to GeeksforGeeks</dialog></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604122941/opendialog.png)

    `Supported Browsers:`

    * Google Chrome 37.0
    * Edge 79.0
    * Firefox 98.0
    * Opera 24.0
    * Safari 15.4


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
            tagName="dialog",
        )


class Dir(BaseElement):
    """
    It is used to make a list of directory titles. It is not supported in HTML 5 <ul> or CSS are used instead of <dir> tag.

    `Syntax:`



    <dir> Lists... </dir>

    Below example illustrates the <dir> tag in HTML:
    `Example:`

    ```html
    <!DOCTYPE html><html><body> <h1>GeeksforGeeks</h1><h2><dir> Tag</h2> <p>List of all computer science subjects:</p> <!-- dir tag starts here--><dir><li>Operating system</li><li>Data Structures</li><li>computer network</li><li>Dbms</li><li>Oops</li></dir><!-- dir tag ends here--> </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702114451/dir.png)

    `Optional Attributes:` This tag contains single attributes *Compact* which is optional. It is used to specify the list size render smaller than normal by reducing the space between list items. It is a boolean attribute.
    `Example:`

    ```html
    <!DOCTYPE html><html><head><title>dir tag</title><style>.gfg {font-size:40px;font-weight:bold;color:green;}.geeks {font-size:25px;font-weight:bold;}</style></head><body><div class = "gfg">GeeksforGeeks</div><div class = "geeks"><dir> Tag</div> <p>List of all computer science subjects:</p> <dir compact><li>Operating system</li><li>Data Structures</li><li>computer network</li><li>Dbms</li><li>Oops</li></dir></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/dir-1.png)

    `Note:` The compact attribute is not supported by any browser.

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    It is used to make a list of directory titles. It is not supported in HTML 5 <ul> or CSS are used instead of <dir> tag.

    `Syntax:`



    <dir> Lists... </dir>

    Below example illustrates the <dir> tag in HTML:
    `Example:`

    ```html
    <!DOCTYPE html><html><body> <h1>GeeksforGeeks</h1><h2><dir> Tag</h2> <p>List of all computer science subjects:</p> <!-- dir tag starts here--><dir><li>Operating system</li><li>Data Structures</li><li>computer network</li><li>Dbms</li><li>Oops</li></dir><!-- dir tag ends here--> </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702114451/dir.png)

    `Optional Attributes:` This tag contains single attributes *Compact* which is optional. It is used to specify the list size render smaller than normal by reducing the space between list items. It is a boolean attribute.
    `Example:`

    ```html
    <!DOCTYPE html><html><head><title>dir tag</title><style>.gfg {font-size:40px;font-weight:bold;color:green;}.geeks {font-size:25px;font-weight:bold;}</style></head><body><div class = "gfg">GeeksforGeeks</div><div class = "geeks"><dir> Tag</div> <p>List of all computer science subjects:</p> <dir compact><li>Operating system</li><li>Data Structures</li><li>computer network</li><li>Dbms</li><li>Oops</li></dir></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/dir-1.png)

    `Note:` The compact attribute is not supported by any browser.

    `Supported Browsers:`

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
            tagName="dir",
        )


class Div(BaseElement):
    """ """

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
            tagName="div",
        )


class Dl(BaseElement):
    """
    The <dl> tag in HTML is used to represent the description list. This tag is used with [<dt>](https://www.geeksforgeeks.org/html-dt-tag/) and [<dd> tag](https://www.geeksforgeeks.org/html-dd-tag/). In HTML4.1, it defines definition list and in HTML5, it defines description list.


    `Syntax:`



    <dl> Contents... </dl>

    `Example:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2>dl Tag</h2><!-- HTML dl tag --><dl><dt>GeeksforGeeks</dt><dd>A Computer Science Portal For Geeks</dd></dl> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604133521/dl.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Safari
    * Opera



    The <dl> tag in HTML is used to represent the description list. This tag is used with [<dt>](https://www.geeksforgeeks.org/html-dt-tag/) and [<dd> tag](https://www.geeksforgeeks.org/html-dd-tag/). In HTML4.1, it defines definition list and in HTML5, it defines description list.


    `Syntax:`



    <dl> Contents... </dl>

    `Example:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2>dl Tag</h2><!-- HTML dl tag --><dl><dt>GeeksforGeeks</dt><dd>A Computer Science Portal For Geeks</dd></dl> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604133521/dl.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Safari
    * Opera





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
            tagName="dl",
        )


class Ulembed(BaseElement):
    """ """

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
            tagName="ulembed",
        )


class Fieldset(BaseElement):
    """
    The `<fieldset> tag` in HTML5 is used to make a group of related elements in the form, and it creates the box over the elements. The <fieldset> tag is new in HTML5. The [<legend> tag](https://www.geeksforgeeks.org/html-legend-tag/#:~:text=The%20legend%20tag%20is%20used,for%20the%20element.) is used to define the title for the child’s contents. The legend elements are the parent element. This tag is used to define the caption for the <fieldset> element.

    `Syntax:`



    <fieldset>Contents</fieldset>

    `Attribute:`

    * [`disabled`](https://www.geeksforgeeks.org/html-fieldset-disabled-attribute/)`:` It is used to specify that the group of related form elements is disabled. A disabled fieldset is un-clickable and unusable.
    * [`form`](https://www.geeksforgeeks.org/html-fieldset-form-attribute/)`:` It is used to specify the one or more forms that the <fieldset> element belongs to.
    * [`name`](https://www.geeksforgeeks.org/html-fieldset-name-attribute/)`:` It is used to specify the name for the Fieldset element.
    * [`autocomplete`](https://www.geeksforgeeks.org/html-fieldset-autocomplete-attribute/#:~:text=The%20HTML%20autocomplete%20attribute,which%20the%20user%20entered%20before.)`:` It is used to specify that the fieldset has autocompleted on or off value.

    `Example:` This simple example illustrates the use of the <fieldset> tag in order to make a group of related elements in the HTML Form.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <fieldset> Tag</h2><form><div class="title">Employee Personal Details:</div> <!--HTML fieldset tag starts here--><fieldset><legend>Details:</legend>Name:<input type="text">Emp_Id:<input type="text">Designation:<input type="text"></fieldset><!--HTML fieldset tag ends here--></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921114948/Screenshot20210921114929.png)HTML <fieldset> tag

    `Example:` In this example, we will know the use of <fieldset> tag to make the group of related elements.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <fieldset> Tag</h2><form><div class="title">Suggest article for video:</div> <!--HTML fieldset tag starts here--><fieldset><legend>JAVA:</legend>Title:<input type="text"><br>Link:<input type="text"><br>User ID:<input type="text"></fieldset><!--HTML fieldset tag ends here--> <br> <!--HTML fieldset tag starts here--><fieldset><legend>PHP:</legend>Title:<input type="text"><br>Link:<input type="text"><br>User ID:<input type="text"></fieldset><!--HTML fieldset tag ends here--></form></body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921111740/Screenshot20210921111714.png)<fieldset> tag to group the related element

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Microsoft Edge 12.0 and above
    * Firefox
    * Safari
    * Opera


    The `<fieldset> tag` in HTML5 is used to make a group of related elements in the form, and it creates the box over the elements. The <fieldset> tag is new in HTML5. The [<legend> tag](https://www.geeksforgeeks.org/html-legend-tag/#:~:text=The%20legend%20tag%20is%20used,for%20the%20element.) is used to define the title for the child’s contents. The legend elements are the parent element. This tag is used to define the caption for the <fieldset> element.

    `Syntax:`



    <fieldset>Contents</fieldset>

    `Attribute:`

    * [`disabled`](https://www.geeksforgeeks.org/html-fieldset-disabled-attribute/)`:` It is used to specify that the group of related form elements is disabled. A disabled fieldset is un-clickable and unusable.
    * [`form`](https://www.geeksforgeeks.org/html-fieldset-form-attribute/)`:` It is used to specify the one or more forms that the <fieldset> element belongs to.
    * [`name`](https://www.geeksforgeeks.org/html-fieldset-name-attribute/)`:` It is used to specify the name for the Fieldset element.
    * [`autocomplete`](https://www.geeksforgeeks.org/html-fieldset-autocomplete-attribute/#:~:text=The%20HTML%20autocomplete%20attribute,which%20the%20user%20entered%20before.)`:` It is used to specify that the fieldset has autocompleted on or off value.

    `Example:` This simple example illustrates the use of the <fieldset> tag in order to make a group of related elements in the HTML Form.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <fieldset> Tag</h2><form><div class="title">Employee Personal Details:</div> <!--HTML fieldset tag starts here--><fieldset><legend>Details:</legend>Name:<input type="text">Emp_Id:<input type="text">Designation:<input type="text"></fieldset><!--HTML fieldset tag ends here--></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921114948/Screenshot20210921114929.png)HTML <fieldset> tag

    `Example:` In this example, we will know the use of <fieldset> tag to make the group of related elements.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML <fieldset> Tag</h2><form><div class="title">Suggest article for video:</div> <!--HTML fieldset tag starts here--><fieldset><legend>JAVA:</legend>Title:<input type="text"><br>Link:<input type="text"><br>User ID:<input type="text"></fieldset><!--HTML fieldset tag ends here--> <br> <!--HTML fieldset tag starts here--><fieldset><legend>PHP:</legend>Title:<input type="text"><br>Link:<input type="text"><br>User ID:<input type="text"></fieldset><!--HTML fieldset tag ends here--></form></body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921111740/Screenshot20210921111714.png)<fieldset> tag to group the related element

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Microsoft Edge 12.0 and above
    * Firefox
    * Safari
    * Opera




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
            tagName="fieldset",
        )


class Figcaption(BaseElement):
    """
    The <figurecaption> tag in HTML is used to set a caption to the figure element in a document. This tag is new in HTML5.


    `Syntax:`



    <figcaption> Figure caption </figcaption>

    `Example 1:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figcaption Tag></h2><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeks-25.png>"alt="gfglogo" style="width:50%"><!--HTML figcaption tag starts here--><figcaption>GeeksforGeeks Logo</figcaption><!--HTML figcaption tag ends here--></figure> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604144929/fignew.png)

    `Example 2:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figcaption> Tag</h2><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeksforgeeks-20.png>"alt="gfglogo"><!--HTML figcaption tag starts here--><figcaption>GFG Logo</figcaption><!--HTML figcaption tag ends here--></figure> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604145226/figcap2.png)

    `Supported Browsers:`

    * Google Chrome 8.0
    * Edge 12.0
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0


    The <figurecaption> tag in HTML is used to set a caption to the figure element in a document. This tag is new in HTML5.


    `Syntax:`



    <figcaption> Figure caption </figcaption>

    `Example 1:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figcaption Tag></h2><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeks-25.png>"alt="gfglogo" style="width:50%"><!--HTML figcaption tag starts here--><figcaption>GeeksforGeeks Logo</figcaption><!--HTML figcaption tag ends here--></figure> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604144929/fignew.png)

    `Example 2:`

    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figcaption> Tag</h2><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeksforgeeks-20.png>"alt="gfglogo"><!--HTML figcaption tag starts here--><figcaption>GFG Logo</figcaption><!--HTML figcaption tag ends here--></figure> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604145226/figcap2.png)

    `Supported Browsers:`

    * Google Chrome 8.0
    * Edge 12.0
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0




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
            tagName="figcaption",
        )


class Figure(BaseElement):
    """
    The <figure> tag in HTML is used to add self-contained content like illustrations, diagrams, photos, or codes listing in a document. It is related to main flow, but it can be used in any position of a document and the figure goes with the flow of the document and if remove it then it should not affect the flow of the document. This tag is new in HTML5.


    `Syntax:`



    <figure> Image content... </figure>

    `Attributes:` It contains mostly two tags which are listed below:


    * [`img src`](https://www.geeksforgeeks.org/html-img-src-attribute/)`:` This tag is used to add an image source in the document.
    * [`figcaption`](https://www.geeksforgeeks.org/html5-figcaption-tag/)`:` This tag is used to set the caption to the image.

    `Example:`


    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figure> Tag</h2><!--HTML figure tag starts here--><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeks-25.png>"alt="The Pulpit Rock" width="304" height="228"><figcaption>Geeks logo</figcaption></figure><!--HTML figure tag ends here--> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604150233/figure.png)

    `Supported Browsers:`


    * Google Chrome 8
    * Edge 12
    * Firefox 4
    * Internet Explorer 9
    * Safari 5.1
    * Opera 11



    The <figure> tag in HTML is used to add self-contained content like illustrations, diagrams, photos, or codes listing in a document. It is related to main flow, but it can be used in any position of a document and the figure goes with the flow of the document and if remove it then it should not affect the flow of the document. This tag is new in HTML5.


    `Syntax:`



    <figure> Image content... </figure>

    `Attributes:` It contains mostly two tags which are listed below:


    * [`img src`](https://www.geeksforgeeks.org/html-img-src-attribute/)`:` This tag is used to add an image source in the document.
    * [`figcaption`](https://www.geeksforgeeks.org/html5-figcaption-tag/)`:` This tag is used to set the caption to the image.

    `Example:`


    ```html
    <!DOCTYPE html> <html> <body> <h1>GeeksforGeeks</h1><h2><figure> Tag</h2><!--HTML figure tag starts here--><figure><img src="<https://media.geeksforgeeks.org/wp-content/uploads/geeks-25.png>"alt="The Pulpit Rock" width="304" height="228"><figcaption>Geeks logo</figcaption></figure><!--HTML figure tag ends here--> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604150233/figure.png)

    `Supported Browsers:`


    * Google Chrome 8
    * Edge 12
    * Firefox 4
    * Internet Explorer 9
    * Safari 5.1
    * Opera 11





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
            tagName="figure",
        )


class Font(BaseElement):
    """
    The `<font> tag` in HTML plays an important role in the web page to create an attractive and readable web page. The font tag is used to change the color, size, and style of a text. The base font tag is used to set all the text to the same size, color and face.

    `Syntax:`



    <font attribute = "value"> Content </font>

    `Example:` In this example, we have used the <font> tag with a font size as 5.

    ```html
    <!DOCTYPE html><html> <body><h2>GeeksforGeeks</h2> <!--Normal paragraph tag--> <p>Hello Geeks!.</p>  <!--font tag--><font size="5"> Welcome to GeeksforGeeks </font></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210916180011/164.png)HTML <font> tag

    The font tag has basically three attributes which are given below:

    * [Font Size attribute](https://www.geeksforgeeks.org/html-font-size-attribute/)
    * [Face/Type attribute](https://www.geeksforgeeks.org/html-font-face-attribute/)
    * [Color attribute](https://www.geeksforgeeks.org/html-font-color-attribute/)

    `Note:` Font tag is not supported in HTML5.

    We will discuss all these attributes & understand them through the examples.

    [`font Size:`](https://www.geeksforgeeks.org/html-font-size-attribute/) This attribute is used to adjust the size of the text in the HTML document using a font tag with the size attribute. The range of size of the font in HTML is from 1 to 7 and the default size is 3.

    `Syntax:`



    <font size="number">

    `Example:` This example uses the <font> tag where different font sizes are specified.

    ```html
    <!DOCTYPE html><html> <body><!--HTML font size tag starts here--><font size="1">GeeksforGeeks!</font><br /><font size="2">GeeksforGeeks!</font><br /><font size="3">GeeksforGeeks!</font><br /><font size="4">GeeksforGeeks!</font><br /><font size="5">GeeksforGeeks!</font><br /><font size="6">GeeksforGeeks!</font><br /><font size="7">GeeksforGeeks!</font><!--HTML font size tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604165350/font1.png)font size attribute

    [`Font Type`](https://www.geeksforgeeks.org/html-font-face-attribute/)`:` Font type can be set by using face attribute with font tag in HTML document. But the fonts used by the user need to be installed in the system first.

    `Syntax:`



    <font face="font_family">

    `Example:` This example describes the <font> tag with different font type & font size.

    ```html
    <!DOCTYPE html><html> <body><!--HTML font face tag starts here--><font face="Times New Roman" size="6">GeeksforGeeks!!</font>    <br /><font face="Verdana" size="6">GeeksforGeeks!!</font><br /><font face="Comic sans MS" size=" 6">GeeksforGeeks!!</font><br /><font face="WildWest" size="6">GeeksforGeeks!!</font><br /><font face="Bedrock" size="6">GeeksforGeeks!!</font><br /><!--HTML font face tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20211215073008/1.png)font type attribute

    [`Font Color:`](https://www.geeksforgeeks.org/html-font-color-attribute/) Font color is used to set the text color using a font tag with the color attribute in an HTML document. Color can be specified either with its name or with its hex code.

    `Syntax:`



    <font color="color_name|hex_number|rgb_number">

    `Example:` This example describes the <font> tag with different font colors.

    ```html
    <!DOCTYPE html><html> <body> <!--HTML font color tag starts here--><font color="#009900">GeeksforGeeks</font><br /><font color="green">GeeksforGeeks</font><!--HTML font color tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604170736/fontlast.png)font color attribute

    `Supported Browsers:`

    * Google Chrome
    * Microsoft Edge 12 and above
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    The `<font> tag` in HTML plays an important role in the web page to create an attractive and readable web page. The font tag is used to change the color, size, and style of a text. The base font tag is used to set all the text to the same size, color and face.

    `Syntax:`



    <font attribute = "value"> Content </font>

    `Example:` In this example, we have used the <font> tag with a font size as 5.

    ```html
    <!DOCTYPE html><html> <body><h2>GeeksforGeeks</h2> <!--Normal paragraph tag--> <p>Hello Geeks!.</p>  <!--font tag--><font size="5"> Welcome to GeeksforGeeks </font></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210916180011/164.png)HTML <font> tag

    The font tag has basically three attributes which are given below:

    * [Font Size attribute](https://www.geeksforgeeks.org/html-font-size-attribute/)
    * [Face/Type attribute](https://www.geeksforgeeks.org/html-font-face-attribute/)
    * [Color attribute](https://www.geeksforgeeks.org/html-font-color-attribute/)

    `Note:` Font tag is not supported in HTML5.

    We will discuss all these attributes & understand them through the examples.

    [`font Size:`](https://www.geeksforgeeks.org/html-font-size-attribute/) This attribute is used to adjust the size of the text in the HTML document using a font tag with the size attribute. The range of size of the font in HTML is from 1 to 7 and the default size is 3.

    `Syntax:`



    <font size="number">

    `Example:` This example uses the <font> tag where different font sizes are specified.

    ```html
    <!DOCTYPE html><html> <body><!--HTML font size tag starts here--><font size="1">GeeksforGeeks!</font><br /><font size="2">GeeksforGeeks!</font><br /><font size="3">GeeksforGeeks!</font><br /><font size="4">GeeksforGeeks!</font><br /><font size="5">GeeksforGeeks!</font><br /><font size="6">GeeksforGeeks!</font><br /><font size="7">GeeksforGeeks!</font><!--HTML font size tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604165350/font1.png)font size attribute

    [`Font Type`](https://www.geeksforgeeks.org/html-font-face-attribute/)`:` Font type can be set by using face attribute with font tag in HTML document. But the fonts used by the user need to be installed in the system first.

    `Syntax:`



    <font face="font_family">

    `Example:` This example describes the <font> tag with different font type & font size.

    ```html
    <!DOCTYPE html><html> <body><!--HTML font face tag starts here--><font face="Times New Roman" size="6">GeeksforGeeks!!</font>    <br /><font face="Verdana" size="6">GeeksforGeeks!!</font><br /><font face="Comic sans MS" size=" 6">GeeksforGeeks!!</font><br /><font face="WildWest" size="6">GeeksforGeeks!!</font><br /><font face="Bedrock" size="6">GeeksforGeeks!!</font><br /><!--HTML font face tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20211215073008/1.png)font type attribute

    [`Font Color:`](https://www.geeksforgeeks.org/html-font-color-attribute/) Font color is used to set the text color using a font tag with the color attribute in an HTML document. Color can be specified either with its name or with its hex code.

    `Syntax:`



    <font color="color_name|hex_number|rgb_number">

    `Example:` This example describes the <font> tag with different font colors.

    ```html
    <!DOCTYPE html><html> <body> <!--HTML font color tag starts here--><font color="#009900">GeeksforGeeks</font><br /><font color="green">GeeksforGeeks</font><!--HTML font color tag ends here--></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604170736/fontlast.png)font color attribute

    `Supported Browsers:`

    * Google Chrome
    * Microsoft Edge 12 and above
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
            tagName="font",
        )


class Footer(BaseElement):
    """
    The <footer> tag in HTML is used to define a footer of HTML document. This section contains the footer information (author information, copyright information, carriers, etc). The footer tag is used within the body tag. The <footer> tag is new in the HTML5. The footer elements require a start tag as well as an end tag.


    `Syntax :`



    <footer> ... </footer>

    A footer element typically contains authorship information, copyright information, contact information, sitemap, back-to-top links, related documents, etc.

    Below examples illustrate the <footer> Tag in HTML elements:


    `Example 1:`


    ```html
    <!DOCTYPE html> <html> <body><!--HTML footer tag starts here--><footer> <a href="<https://www.geeksforgeeks.org/about/>">About Us</a>|<a href="<https://www.geeksforgeeks.org/privacy-policy/>">Privacy Policy</a>|<a href="<https://www.geeksforgeeks.org/careers/>">Careers</a>   <p>@geeksforgeeks, Some rights reserved</p>   </footer><!--HTML figcaption tag ends here--></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604164327/footerex1.png)

    `Example 2:` Using CSS in footer Tag


    ```html
    <!DOCTYPE html><html><head><title>footer tag</title><style>.column {float: left;width: 27%;height: 300px;}p {font-size:20px;font-weight:bold;}</style></head><body><!--HTML footer tag starts here--><footer><div class="column">  <p>Company</p>  <ul style="list-style-type:disc"><li>About Us</li><li>Careers</li><li>Privacy Policy</li><li>Contact Us</li></ul></div> <div class="column">  <p>Learn</p>  <ul><li>Algorithms</li><li>Data Structures</li><li>Languages</li><li>CS Subjects</li><li>Video Tutorials</li></ul></div> <div class="column">  <p>Practice</p>  <ul><li>Company-wise</li><li>Topic-wise</li><li>Contests</li><li>Subjective Questions</li></ul></div></footer><!--HTML figcaption tag ends here--></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-01-at-8.24.49-AM.png)

    `Browsers Supported:`


    * Google Chrome 5
    * Edge 12
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0




    The <footer> tag in HTML is used to define a footer of HTML document. This section contains the footer information (author information, copyright information, carriers, etc). The footer tag is used within the body tag. The <footer> tag is new in the HTML5. The footer elements require a start tag as well as an end tag.


    `Syntax :`



    <footer> ... </footer>

    A footer element typically contains authorship information, copyright information, contact information, sitemap, back-to-top links, related documents, etc.

    Below examples illustrate the <footer> Tag in HTML elements:


    `Example 1:`


    ```html
    <!DOCTYPE html> <html> <body><!--HTML footer tag starts here--><footer> <a href="<https://www.geeksforgeeks.org/about/>">About Us</a>|<a href="<https://www.geeksforgeeks.org/privacy-policy/>">Privacy Policy</a>|<a href="<https://www.geeksforgeeks.org/careers/>">Careers</a>   <p>@geeksforgeeks, Some rights reserved</p>   </footer><!--HTML figcaption tag ends here--></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210604164327/footerex1.png)

    `Example 2:` Using CSS in footer Tag


    ```html
    <!DOCTYPE html><html><head><title>footer tag</title><style>.column {float: left;width: 27%;height: 300px;}p {font-size:20px;font-weight:bold;}</style></head><body><!--HTML footer tag starts here--><footer><div class="column">  <p>Company</p>  <ul style="list-style-type:disc"><li>About Us</li><li>Careers</li><li>Privacy Policy</li><li>Contact Us</li></ul></div> <div class="column">  <p>Learn</p>  <ul><li>Algorithms</li><li>Data Structures</li><li>Languages</li><li>CS Subjects</li><li>Video Tutorials</li></ul></div> <div class="column">  <p>Practice</p>  <ul><li>Company-wise</li><li>Topic-wise</li><li>Contests</li><li>Subjective Questions</li></ul></div></footer><!--HTML figcaption tag ends here--></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-01-at-8.24.49-AM.png)

    `Browsers Supported:`


    * Google Chrome 5
    * Edge 12
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0






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
            tagName="footer",
        )


class Form(BaseElement):
    """
    `Form Tag`

    Forms are required to take input from the user who visits the website. This form is used basically for the registration process, logging into your profile on a website or to create your profile on a website, etc … The information that is collected from the form is -1. Name 2.Email Addresses etc. Now the form will take input from the form and post that data in backend applications (like PHP). So the backend application will process the data which is received by them. There are various form elements that we can use like text fields, text area, drop-down list, select, checkboxes, radio, etc.

    `Syntax:`



    <form> Form Content... </form>

    `Attributes:` There are many attributes that are associated with the <form> tag. Some of them are listed below:

    * [`Action Attribute`](https://www.geeksforgeeks.org/html-formaction-attribute/)`:` -This is used to send the data to the server after the submission of the form.
    * [`Method`](https://www.geeksforgeeks.org/html-form-method-attribute/)`:` -This is used to upload the data by using two methods that are Get and Post. Get Method: -It has a limited length of characters of URL. -we should not use get to send some sensitive data. -This method is better for non-secure data. Post Method: -1. It has no size limitations 2. The submission of the form with the method post, can not be bookmarked.
    * [`Enctype attribute`](https://www.geeksforgeeks.org/html-form-enctype-attribute/): -This attribute is used to specify that how a browser decodes the data before it sends it to the server .so the values of this attribute are: -1.application/x-www-form-urlencoded − It is the standard method most forms used 2.multipart/form-data -it is used when you have something to upload like files of images, word files, etc.

    `Example of the` `form tag:-`

    ```html
    <!DOCTYPE html> <html> <body> <h1>form tag </h1> <!--Here we have not used the action attributeas we are not submitting the data to the server--> <form> <label for="fname">FirstName</label><!-- Here i have used label todefine the label for input --> <input type="text" name="fname" placeholder="enter your name" required><!--Itdefines a text field by using input tag  --> <label for="lname">LastName</label> <input type="text" name="lname" placeholder="enter your name" required> </form> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210323111427/Capture-300x58.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox
    * Opera
    * Safari
    `Form Tag`

    Forms are required to take input from the user who visits the website. This form is used basically for the registration process, logging into your profile on a website or to create your profile on a website, etc … The information that is collected from the form is -1. Name 2.Email Addresses etc. Now the form will take input from the form and post that data in backend applications (like PHP). So the backend application will process the data which is received by them. There are various form elements that we can use like text fields, text area, drop-down list, select, checkboxes, radio, etc.

    `Syntax:`



    <form> Form Content... </form>

    `Attributes:` There are many attributes that are associated with the <form> tag. Some of them are listed below:

    * [`Action Attribute`](https://www.geeksforgeeks.org/html-formaction-attribute/)`:` -This is used to send the data to the server after the submission of the form.
    * [`Method`](https://www.geeksforgeeks.org/html-form-method-attribute/)`:` -This is used to upload the data by using two methods that are Get and Post. Get Method: -It has a limited length of characters of URL. -we should not use get to send some sensitive data. -This method is better for non-secure data. Post Method: -1. It has no size limitations 2. The submission of the form with the method post, can not be bookmarked.
    * [`Enctype attribute`](https://www.geeksforgeeks.org/html-form-enctype-attribute/): -This attribute is used to specify that how a browser decodes the data before it sends it to the server .so the values of this attribute are: -1.application/x-www-form-urlencoded − It is the standard method most forms used 2.multipart/form-data -it is used when you have something to upload like files of images, word files, etc.

    `Example of the` `form tag:-`

    ```html
    <!DOCTYPE html> <html> <body> <h1>form tag </h1> <!--Here we have not used the action attributeas we are not submitting the data to the server--> <form> <label for="fname">FirstName</label><!-- Here i have used label todefine the label for input --> <input type="text" name="fname" placeholder="enter your name" required><!--Itdefines a text field by using input tag  --> <label for="lname">LastName</label> <input type="text" name="lname" placeholder="enter your name" required> </form> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210323111427/Capture-300x58.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
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
            tagName="form",
        )


class Frame(BaseVoidElement):
    """ """

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
            tagName="frame",
        )


class Frameset(BaseElement):
    """
    The <frameset> tag in HTML is used to define the frameset. The <frameset> element contains one or more frame elements. It is used to specify the number of rows and columns in frameset with their pixel of spaces. Each element can hold a separate document.

    `Note:` The <frameset> tag is not supported in HTML5.

    `Syntax:`



    <frameset cols = "pixels|%|*">

    `Attributes:` The list of frameset attributes are given below:


    * [`cols`](https://www.geeksforgeeks.org/html-cols-attribute/)`:` The cols attribute is used to create vertical frames in a web browser. This attribute is basically used to define the no. of columns and their size inside the frameset tag.
    * [`rows`](https://www.geeksforgeeks.org/html-rows-attribute/)`:` The rows attribute is used to create horizontal frames in the web browser. This attribute is used to define the no. of rows and their size inside the frameset tag.
    * [`border`](https://www.geeksforgeeks.org/html-border-attribute/)`:` This attribute of frameset tag defines the width of the border of each frame in pixels. Zero value is used for no border.
    * [`frameborder`](https://www.geeksforgeeks.org/html-frame-frameborder-attribute/)`:` This attribute of frameset tag is used to specify whether a three-dimensional border should be displayed between the frames or not for this use two values 0 and 1, where 0 defines no border and value 1 signifies for yes there will be a border.
    * [`framespacing`](https://www.geeksforgeeks.org/html5-mathml-framespacing-attribute/)`:` This attribute of frameset tag is used to specify the amount of spacing between the frames in a frameset. This can take any integer value as a parameter which basically denotes the value in pixel.

    Below examples illustrate the <frameset> element in HTML:
    `Example 1:`

    ```html
    <!DOCTYPE html><html><head><title>frameset attribute</title></head> <!-- frameset attribute starts here -->   <frameset rows = "20%, 60%, 20%"><frame name = "top" src = "attr1.png" /><frame name = "main" src = "gradient3.png" /><frame name = "bottom" src = "col_last.png" /><noframes><body>The browser you are working does notsupport frames.</body></noframes></frameset><!-- frameset attribute ends here --></html> |

    ```
    `Output:`
    The above example basically used to create three horizontal frames: top, middle, and bottom using row attribute of frameset tag, and the noframe tag is used for that browser that doesn’t support noframe.


    ![](https://media.geeksforgeeks.org/wp-content/uploads/frame-1-2.png)

    `Example 2:`


    ```html
    <!DOCTYPE html><html><head><title>frameset attribute</title></head> <frameset cols = "30%, 40%, 30%"><frame name = "top" src = "attr1.png" /><frame name = "main" src = "gradient3.png" /><frame name = "bottom" src = "col_last.png" /><noframes><body>The browser you are working doesnot support frames.</body></noframes></frameset></html> |

    ```
    `Output:`
    The above example basically used to create three vertical frames: left, center, and right using col attribute of frameset tag.


    ![](https://media.geeksforgeeks.org/wp-content/uploads/frame-2-2.png)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari




    The <frameset> tag in HTML is used to define the frameset. The <frameset> element contains one or more frame elements. It is used to specify the number of rows and columns in frameset with their pixel of spaces. Each element can hold a separate document.

    `Note:` The <frameset> tag is not supported in HTML5.

    `Syntax:`



    <frameset cols = "pixels|%|*">

    `Attributes:` The list of frameset attributes are given below:


    * [`cols`](https://www.geeksforgeeks.org/html-cols-attribute/)`:` The cols attribute is used to create vertical frames in a web browser. This attribute is basically used to define the no. of columns and their size inside the frameset tag.
    * [`rows`](https://www.geeksforgeeks.org/html-rows-attribute/)`:` The rows attribute is used to create horizontal frames in the web browser. This attribute is used to define the no. of rows and their size inside the frameset tag.
    * [`border`](https://www.geeksforgeeks.org/html-border-attribute/)`:` This attribute of frameset tag defines the width of the border of each frame in pixels. Zero value is used for no border.
    * [`frameborder`](https://www.geeksforgeeks.org/html-frame-frameborder-attribute/)`:` This attribute of frameset tag is used to specify whether a three-dimensional border should be displayed between the frames or not for this use two values 0 and 1, where 0 defines no border and value 1 signifies for yes there will be a border.
    * [`framespacing`](https://www.geeksforgeeks.org/html5-mathml-framespacing-attribute/)`:` This attribute of frameset tag is used to specify the amount of spacing between the frames in a frameset. This can take any integer value as a parameter which basically denotes the value in pixel.

    Below examples illustrate the <frameset> element in HTML:
    `Example 1:`

    ```html
    <!DOCTYPE html><html><head><title>frameset attribute</title></head> <!-- frameset attribute starts here -->   <frameset rows = "20%, 60%, 20%"><frame name = "top" src = "attr1.png" /><frame name = "main" src = "gradient3.png" /><frame name = "bottom" src = "col_last.png" /><noframes><body>The browser you are working does notsupport frames.</body></noframes></frameset><!-- frameset attribute ends here --></html> |

    ```
    `Output:`
    The above example basically used to create three horizontal frames: top, middle, and bottom using row attribute of frameset tag, and the noframe tag is used for that browser that doesn’t support noframe.


    ![](https://media.geeksforgeeks.org/wp-content/uploads/frame-1-2.png)

    `Example 2:`


    ```html
    <!DOCTYPE html><html><head><title>frameset attribute</title></head> <frameset cols = "30%, 40%, 30%"><frame name = "top" src = "attr1.png" /><frame name = "main" src = "gradient3.png" /><frame name = "bottom" src = "col_last.png" /><noframes><body>The browser you are working doesnot support frames.</body></noframes></frameset></html> |

    ```
    `Output:`
    The above example basically used to create three vertical frames: left, center, and right using col attribute of frameset tag.


    ![](https://media.geeksforgeeks.org/wp-content/uploads/frame-2-2.png)

    `Supported Browsers:`

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
            tagName="frameset",
        )


class Head(BaseElement):
    """
    The <head> tag in HTML is used to define the head portion of the document which contains information related to the document.
    The <head> tag contains other head elements such as <title>, <meta>, <link>, <style> <link> etc.
    In HTML 4.01 the <head> element was mandatory but in HTML5, the <head> element can be omitted.
    `Tag Specific Attributes`:
    The below-mentioned layout-attributes of the <hr> tag have been removed from HTML5.

    `Attribute:`

    * `profile:` It is used to specify the URL to a document that contains one or more metadata profiles for browsers to clearly understand the information.

    `Syntax :`



    <head>
    <title>Title of the document</title>
    </head>

    Below program illustrates the <head> element:

    `Program 1:`

    ```html
    <!DOCTYPE html><html lang="en"> <head><title>HTML Head Tag </title></head> <body>  <p>GeeksforGeeks is a portal for geeks.</p>  <hr></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.21.57-AM-300x63.png)

    `Program 2(Using style tag inside head tag)`

    ```html
    <!DOCTYPE html> <html> <head><style>body {background: skyblue;} h1 {color: red;} p {color: blue;}</style></head> <body> <h1>GeeksforGeeks</h1>  <p>It is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.25.44-AM-300x111.png)

    `Program 3(Using link tag inside head tag):`

    ```html
    <!DOCTYPE html> <html> <head><link rel="stylesheet" type="text/css" href="mystyle.css"></head> <body> <h1>GeeksforGeeks</h1>  <p>It is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.28.28-AM-300x121.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <head> tag in HTML is used to define the head portion of the document which contains information related to the document.
    The <head> tag contains other head elements such as <title>, <meta>, <link>, <style> <link> etc.
    In HTML 4.01 the <head> element was mandatory but in HTML5, the <head> element can be omitted.
    `Tag Specific Attributes`:
    The below-mentioned layout-attributes of the <hr> tag have been removed from HTML5.

    `Attribute:`

    * `profile:` It is used to specify the URL to a document that contains one or more metadata profiles for browsers to clearly understand the information.

    `Syntax :`



    <head>
    <title>Title of the document</title>
    </head>

    Below program illustrates the <head> element:

    `Program 1:`

    ```html
    <!DOCTYPE html><html lang="en"> <head><title>HTML Head Tag </title></head> <body>  <p>GeeksforGeeks is a portal for geeks.</p>  <hr></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.21.57-AM-300x63.png)

    `Program 2(Using style tag inside head tag)`

    ```html
    <!DOCTYPE html> <html> <head><style>body {background: skyblue;} h1 {color: red;} p {color: blue;}</style></head> <body> <h1>GeeksforGeeks</h1>  <p>It is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.25.44-AM-300x111.png)

    `Program 3(Using link tag inside head tag):`

    ```html
    <!DOCTYPE html> <html> <head><link rel="stylesheet" type="text/css" href="mystyle.css"></head> <body> <h1>GeeksforGeeks</h1>  <p>It is a portal for geeks.</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-04-at-8.28.28-AM-300x121.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
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
            tagName="head",
        )


class Header(BaseElement):
    """
    The `<header> tag` in HTML is used to define the header for a document or a section as it contains the information related to the title and heading of the related content. The <header> element is intended to usually contain the section’s heading (an h1-h6 element or an <hgroup> element), but this is not required. It can also be used to wrap a section’s table of contents, a search form, or any relevant logos. The <header> tag is a new tag in HTML5 and it is a container tag ie., it contains a starting tag, content & the end tag. There can be several <header> elements in one document. This tag cannot be placed within a <footer>, <address> or another <header> element.

    `Syntax:`



    <header> ...</header>

    `Attributes`: This tag supports all the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) in HTML.

    The below examples illustrate the <header> element in HTML.

    `Example 1:` This example illustrates the use of the <header> tag that makes the container for the head section of the document.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3><hr><article><header><h3>GeeksforGeeks Learning</h3> <p>Posted by GFG</p>   <p>A Computer Science portal for geeks.It contains well written, well thoughtand well explained computer science andprogramming articles.</p>   </header></article></body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921233939/1.jpg)HTML <header> Tag

    `Example 2:` In this example, we have used the <header> tag to contain the surrounding section’s heading, but not required every time.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3> <!--HTML header tag starts here--><header><h1>This is the heading.</h1><h4>This is the sub-heading.</h4> <p>This is the metadata.</p>   </header><!--HTML header tag ends here--></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921235434/2.jpg)HTML <header> Tag

    `Example 3:` In this example, we have represented navigational aids by using the <header> tag.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3> <!--HTML header tag starts here--><header><a href="<https://www.geeksforgeeks.org/fundamentals-of-algorithms/>">Algo</a> |<a href="<https://www.geeksforgeeks.org/data-structures/>">DS</a> |<a href="<https://www.geeksforgeeks.org/category/program-output/>">Languages</a> |<a href="<https://www.geeksforgeeks.org/company-interview-corner/>">Interview</a> |<a href="<https://www.geeksforgeeks.org/student-corner/>">Students</a> |<a href="<https://www.geeksforgeeks.org/gate-cs-notes-gq/>">Gate</a> |<a href="<https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/>">CS Subjects</a> |<a href="<https://www.geeksforgeeks.org/quiz-corner-gq/>">Quizzes</a></header><!--HTML header tag ends here--></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922000359/3.jpg)HTML <header> Tag

    `Supported Browsers:`

    * Google Chrome 5 and above
    * Internet Explorer 9 and above
    * Microsoft Edge 12 and above
    * Firefox 4 and above
    * Opera 11.1 and above
    * Safari 5 and above

    HTML is the foundation of web pages, is used for webpage development by structuring websites and web apps. You can learn HTML from the ground up by following this [HTML Tutorial](https://www.geeksforgeeks.org/html-tutorials/) and [HTML Examples](https://www.geeksforgeeks.org/html-examples/).


    The `<header> tag` in HTML is used to define the header for a document or a section as it contains the information related to the title and heading of the related content. The <header> element is intended to usually contain the section’s heading (an h1-h6 element or an <hgroup> element), but this is not required. It can also be used to wrap a section’s table of contents, a search form, or any relevant logos. The <header> tag is a new tag in HTML5 and it is a container tag ie., it contains a starting tag, content & the end tag. There can be several <header> elements in one document. This tag cannot be placed within a <footer>, <address> or another <header> element.

    `Syntax:`



    <header> ...</header>

    `Attributes`: This tag supports all the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) in HTML.

    The below examples illustrate the <header> element in HTML.

    `Example 1:` This example illustrates the use of the <header> tag that makes the container for the head section of the document.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3><hr><article><header><h3>GeeksforGeeks Learning</h3> <p>Posted by GFG</p>   <p>A Computer Science portal for geeks.It contains well written, well thoughtand well explained computer science andprogramming articles.</p>   </header></article></body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921233939/1.jpg)HTML <header> Tag

    `Example 2:` In this example, we have used the <header> tag to contain the surrounding section’s heading, but not required every time.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3> <!--HTML header tag starts here--><header><h1>This is the heading.</h1><h4>This is the sub-heading.</h4> <p>This is the metadata.</p>   </header><!--HTML header tag ends here--></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921235434/2.jpg)HTML <header> Tag

    `Example 3:` In this example, we have represented navigational aids by using the <header> tag.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML Header Tag</h3> <!--HTML header tag starts here--><header><a href="<https://www.geeksforgeeks.org/fundamentals-of-algorithms/>">Algo</a> |<a href="<https://www.geeksforgeeks.org/data-structures/>">DS</a> |<a href="<https://www.geeksforgeeks.org/category/program-output/>">Languages</a> |<a href="<https://www.geeksforgeeks.org/company-interview-corner/>">Interview</a> |<a href="<https://www.geeksforgeeks.org/student-corner/>">Students</a> |<a href="<https://www.geeksforgeeks.org/gate-cs-notes-gq/>">Gate</a> |<a href="<https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/>">CS Subjects</a> |<a href="<https://www.geeksforgeeks.org/quiz-corner-gq/>">Quizzes</a></header><!--HTML header tag ends here--></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922000359/3.jpg)HTML <header> Tag

    `Supported Browsers:`

    * Google Chrome 5 and above
    * Internet Explorer 9 and above
    * Microsoft Edge 12 and above
    * Firefox 4 and above
    * Opera 11.1 and above
    * Safari 5 and above

    HTML is the foundation of web pages, is used for webpage development by structuring websites and web apps. You can learn HTML from the ground up by following this [HTML Tutorial](https://www.geeksforgeeks.org/html-tutorials/) and [HTML Examples](https://www.geeksforgeeks.org/html-examples/).




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
            tagName="header",
        )


class H1(BaseElement):
    """ """

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
            tagName="h1",
        )


class H2(BaseElement):
    """ """

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
            tagName="h2",
        )


class H3(BaseElement):
    """ """

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
            tagName="h3",
        )


class H4(BaseElement):
    """ """

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
            tagName="h4",
        )


class H5(BaseElement):
    """ """

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
            tagName="h5",
        )


class H6(BaseElement):
    """ """

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
            tagName="h6",
        )


class Hgroup(BaseElement):
    """
    The <hgroup> tag in HTML stands for heading group and is used to group the heading elements. The <hgroup> tag in HTML is used to wrap one or more heading elements from <h1> to <h6>, such as the headings and sub-headings. The <hgroup> tag requires the starting tag as well as ending tag.

    `Note:` <hgroup> is deprecated from HTML5 specification.
    `Syntax :`




    <hgroup> ... </hgroup>

    Below examples illustrate the <hgroup> tag in HTML:
    `Example 1:` This example contains the Title and Sub-Title.


    ```html
    <!DOCTYPE html> <html> <body><!--HTML hgroup tag starts here--><hgroup><h1>This is the title.</h1><h2>This is sub-title.</h2></hgroup><!--HTML hgroup tag ends here--></body>  </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-03-at-7.49.37-AM.png)

    `Example 2:` This example contains Title, Sub-Title, and Metadata.


    ```html
    <!DOCTYPE html> <html> <body><!--HTML hgroup tag starts here--><hgroup><h1>This is the title.</h1><h2>This is sub-title.</h2>  <p>This is the metadata.</p>  </hgroup><!--HTML hgroup tag ends here--></body>  </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-03-at-7.52.36-AM.png)

    `Supported Browsers:`

    * Google Chrome 5.0
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0




    The <hgroup> tag in HTML stands for heading group and is used to group the heading elements. The <hgroup> tag in HTML is used to wrap one or more heading elements from <h1> to <h6>, such as the headings and sub-headings. The <hgroup> tag requires the starting tag as well as ending tag.

    `Note:` <hgroup> is deprecated from HTML5 specification.
    `Syntax :`




    <hgroup> ... </hgroup>

    Below examples illustrate the <hgroup> tag in HTML:
    `Example 1:` This example contains the Title and Sub-Title.


    ```html
    <!DOCTYPE html> <html> <body><!--HTML hgroup tag starts here--><hgroup><h1>This is the title.</h1><h2>This is sub-title.</h2></hgroup><!--HTML hgroup tag ends here--></body>  </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-03-at-7.49.37-AM.png)

    `Example 2:` This example contains Title, Sub-Title, and Metadata.


    ```html
    <!DOCTYPE html> <html> <body><!--HTML hgroup tag starts here--><hgroup><h1>This is the title.</h1><h2>This is sub-title.</h2>  <p>This is the metadata.</p>  </hgroup><!--HTML hgroup tag ends here--></body>  </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-Shot-2018-10-03-at-7.52.36-AM.png)

    `Supported Browsers:`

    * Google Chrome 5.0
    * Internet Explorer 9.0
    * Firefox 4.0
    * Opera 11.1
    * Safari 5.0






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
            tagName="hgroup",
        )


class Hr(BaseVoidElement):
    """ """

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
            tagName="hr",
        )


class Html(BaseElement):
    """
    The <html> tag in HTML is used to define the root of HTML and XHTML documents. The <html> tag tells the browser that it is an HTML document. It is the second outer container for everything that appears in an HTML document followed by the <!DOCTYPE> tag. The <html> tag requires a starting and end tag.
    `Syntax:`




    <html> HTML Contents... </html>

    `Attribute Value:` The <html> tag contains single attribute [*xmlns*](https://www.geeksforgeeks.org/html-html-xmlns-attribute/) whose attribute value is *http://www.w3.org/1999/xhtml*. It is used to define the namespace attributes.
    Below examples illustrate the <html> element in HTML:
    `Example 1:`


    ```html
    <!DOCTYPE html><!-- html tag starts here --><html> <body> <h1>GeeksforGeeks</h1><h2><html> Tag</h2> </body> </html><!-- html tag ends here --> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611152733/html.png)

    `Example 2:` Using the xmlns attribute inside the <html> tag.


    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""<http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>"><html xmlns="<http://www.w3.org/1999/xhtml>"><head><title>html Tag</title><style>h1 {color:green;}body {text-align:center;}</style></head><body><h1>GeeksforGeeks</h1><h2><html> Tag</h2></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/html-tag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox
    * Opera
    * Safari




    The <html> tag in HTML is used to define the root of HTML and XHTML documents. The <html> tag tells the browser that it is an HTML document. It is the second outer container for everything that appears in an HTML document followed by the <!DOCTYPE> tag. The <html> tag requires a starting and end tag.
    `Syntax:`




    <html> HTML Contents... </html>

    `Attribute Value:` The <html> tag contains single attribute [*xmlns*](https://www.geeksforgeeks.org/html-html-xmlns-attribute/) whose attribute value is *http://www.w3.org/1999/xhtml*. It is used to define the namespace attributes.
    Below examples illustrate the <html> element in HTML:
    `Example 1:`


    ```html
    <!DOCTYPE html><!-- html tag starts here --><html> <body> <h1>GeeksforGeeks</h1><h2><html> Tag</h2> </body> </html><!-- html tag ends here --> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611152733/html.png)

    `Example 2:` Using the xmlns attribute inside the <html> tag.


    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""<http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>"><html xmlns="<http://www.w3.org/1999/xhtml>"><head><title>html Tag</title><style>h1 {color:green;}body {text-align:center;}</style></head><body><h1>GeeksforGeeks</h1><h2><html> Tag</h2></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/html-tag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
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
            tagName="html",
        )


class Iframe(BaseElement):
    """ """

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
            tagName="iframe",
        )


class Img(BaseElement):
    """ """

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
            tagName="img",
        )


class Input(BaseVoidElement):
    """ """

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
            tagName="input",
        )


class Ins(BaseElement):
    """
    The <ins> tag in HTML is used to specify a block of inserted text. The <ins> tag is typically used to mark a range of text that has been added to the document. The inserted text is rendered as underlined text by the web browsers although this property can be changed using CSS text-decoration property. The <ins> tag requires a starting and ending tag.


    `Syntax:`



    <ins> Contents... </ins>

    `Attributes:`

    * [`cite:`](https://www.geeksforgeeks.org/html-ins-cite-attribute/) It is used to specify the URL of the document or message which denotes the reason of inserting the text.
    * [`datetime:`](https://www.geeksforgeeks.org/html-ins-datetime-attribute/) It is used to specify the date and time of the inserted text. The datetime is inserted in the format *YYYY-MM-DDThh:mm:ssTZD*.

    `Example 1:` This example describe the use of <ins> tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML ins Tag</h2>  <p>GeeksforGeeks is a <del>mathematical</del><ins>computer</ins> science portal</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205115055/ins1.PNG)

    `Example 2:` This example uses the <ins> tag with the datetime attribute and also use some CSS styles.



    ```html
    <!DOCTYPE html><html> <head><style>del {color: red;} ins {color: green;}</style></head> <body><h1>GeeksforGeeks</h1> <h2>HTML ins Tag</h2>  <p>GeeksforGeeks is a <del>mathematical</del><ins datetime="2018-11-21T15:55:03Z">computer</ins> science portal</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205115426/ins2.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari


    The <ins> tag in HTML is used to specify a block of inserted text. The <ins> tag is typically used to mark a range of text that has been added to the document. The inserted text is rendered as underlined text by the web browsers although this property can be changed using CSS text-decoration property. The <ins> tag requires a starting and ending tag.


    `Syntax:`



    <ins> Contents... </ins>

    `Attributes:`

    * [`cite:`](https://www.geeksforgeeks.org/html-ins-cite-attribute/) It is used to specify the URL of the document or message which denotes the reason of inserting the text.
    * [`datetime:`](https://www.geeksforgeeks.org/html-ins-datetime-attribute/) It is used to specify the date and time of the inserted text. The datetime is inserted in the format *YYYY-MM-DDThh:mm:ssTZD*.

    `Example 1:` This example describe the use of <ins> tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML ins Tag</h2>  <p>GeeksforGeeks is a <del>mathematical</del><ins>computer</ins> science portal</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205115055/ins1.PNG)

    `Example 2:` This example uses the <ins> tag with the datetime attribute and also use some CSS styles.



    ```html
    <!DOCTYPE html><html> <head><style>del {color: red;} ins {color: green;}</style></head> <body><h1>GeeksforGeeks</h1> <h2>HTML ins Tag</h2>  <p>GeeksforGeeks is a <del>mathematical</del><ins datetime="2018-11-21T15:55:03Z">computer</ins> science portal</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205115426/ins2.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="ins",
        )


class Isindex(BaseVoidElement):
    """ """

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
            tagName="isindex",
        )


class I(BaseElement):
    """
    The `<i> tag` in HTML is used to display the content in italic style. This tag is generally used to display the technical term, phrase, the important word in a different language. The *<i> tag* is a container tag that contains the opening tag, content & closing tag.

    `Syntax:`



    <i> Contents</i>

    `Accepted Attributes``:` This is a [Global attribute](https://www.geeksforgeeks.org/html-global-attributes/), and can be used on any HTML element.

    Below code examples illustrate the use of *<i> tag* in HTML.

    `Example 1:` This is a simple example illustrating the *<i> tag* to make the italic text in HTML.

    ```html
    <!DOCTYPE html><html><head><title>HTML i Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3><div>  <p><i>A Computer Science portal for geeks.</i>It contains well written, well thought and wellexplained computer science and programming articles</p>   </div></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921163431/2.jpg)HTML <i> Tag

    `Example 2:` In this example, we have used *<i> tag* & *<p> tag* to illustrate the difference in the text appearance while rendering it.

    ```html
    <!DOCTYPE html><html><head><title>HTML Italic Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3>  <p>This is normal text written inside p tag</p>    <!--HTML <i>(italic) tag is used here--><i>This text is in italic font style</i></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921163829/3.jpg)Italic font-style using HTML <i> Tag

    `Example 3:` A text can be written in italics using CSS also. When the [CSS font-style property](https://www.geeksforgeeks.org/css-font-style-property/) is set to italic, then the text can be seen as follows:

    ```html
    <!DOCTYPE html><html><head><title>HTML Italic Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3> <!--Example for font-style: italic --><p style="font-style: italic;">This text content is in italic font.</p>   <h5>Note:This example is only possible when thefont-style property is kept "italic" in CSS</h5></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921164202/4.jpg)Setting font-style to italic using font-style Property

    `Usage:`

    * Use the *<i> tag* for words that you want to show differently from the normal phrase for readability purposes
    * The tags like *<i>* and *<b>* now define semantics rather than typographic appearance. So to display text in italic type, users can use the CSS font-style property.
    * Use *<i> tag* only when it is not marked up with these elements:
            + [<em>](https://www.geeksforgeeks.org/html-em-tag/)
            + [<strong>](https://www.geeksforgeeks.org/html-strong-tag/)
            + [<mark>](https://www.geeksforgeeks.org/html5-mark-tag/)
            + [<cite>](https://www.geeksforgeeks.org/html-cite-tag/)
            + [<dfn>](https://www.geeksforgeeks.org/html-dfn-tag/)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Internet Explorer
    * Microsoft Edge 12 and above
    * Firefox 1 and above
    * Opera
    * Safari


    The `<i> tag` in HTML is used to display the content in italic style. This tag is generally used to display the technical term, phrase, the important word in a different language. The *<i> tag* is a container tag that contains the opening tag, content & closing tag.

    `Syntax:`



    <i> Contents</i>

    `Accepted Attributes``:` This is a [Global attribute](https://www.geeksforgeeks.org/html-global-attributes/), and can be used on any HTML element.

    Below code examples illustrate the use of *<i> tag* in HTML.

    `Example 1:` This is a simple example illustrating the *<i> tag* to make the italic text in HTML.

    ```html
    <!DOCTYPE html><html><head><title>HTML i Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3><div>  <p><i>A Computer Science portal for geeks.</i>It contains well written, well thought and wellexplained computer science and programming articles</p>   </div></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921163431/2.jpg)HTML <i> Tag

    `Example 2:` In this example, we have used *<i> tag* & *<p> tag* to illustrate the difference in the text appearance while rendering it.

    ```html
    <!DOCTYPE html><html><head><title>HTML Italic Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3>  <p>This is normal text written inside p tag</p>    <!--HTML <i>(italic) tag is used here--><i>This text is in italic font style</i></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921163829/3.jpg)Italic font-style using HTML <i> Tag

    `Example 3:` A text can be written in italics using CSS also. When the [CSS font-style property](https://www.geeksforgeeks.org/css-font-style-property/) is set to italic, then the text can be seen as follows:

    ```html
    <!DOCTYPE html><html><head><title>HTML Italic Tag</title></head> <body><h1>GeeksforGeeks</h1><h3>HTML i tag</h3> <!--Example for font-style: italic --><p style="font-style: italic;">This text content is in italic font.</p>   <h5>Note:This example is only possible when thefont-style property is kept "italic" in CSS</h5></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210921164202/4.jpg)Setting font-style to italic using font-style Property

    `Usage:`

    * Use the *<i> tag* for words that you want to show differently from the normal phrase for readability purposes
    * The tags like *<i>* and *<b>* now define semantics rather than typographic appearance. So to display text in italic type, users can use the CSS font-style property.
    * Use *<i> tag* only when it is not marked up with these elements:
            + [<em>](https://www.geeksforgeeks.org/html-em-tag/)
            + [<strong>](https://www.geeksforgeeks.org/html-strong-tag/)
            + [<mark>](https://www.geeksforgeeks.org/html5-mark-tag/)
            + [<cite>](https://www.geeksforgeeks.org/html-cite-tag/)
            + [<dfn>](https://www.geeksforgeeks.org/html-dfn-tag/)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Internet Explorer
    * Microsoft Edge 12 and above
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
            tagName="i",
        )


class Kbd(BaseElement):
    """
    It is a phrase tag and used to define the keyboard input. The text enclosed within <kbd> tag is typically display in the browser’s default monospace font.

    `Syntax:`



    <kbd> text content ... </kbd>

    `List of all phrase tag:`


    * [`<em>`](https://www.geeksforgeeks.org/html-em-tag/)`:` It is used to emphasize the text.
    * [`<strong>`](https://www.geeksforgeeks.org/html-strong-tag/)`:` It is used to define an important text.
    * [`<code>`](https://www.geeksforgeeks.org/html-code-tag/)`:` It encloses the computer code.
    * [`<samp>`](https://www.geeksforgeeks.org/html-samp-tag/)`:` It defines a sample output text from a computer program.
    * [`<kbd>`](https://www.geeksforgeeks.org/html-kbd-tag/)`:` It defines the text of keyboard input.
    * [`<var>`](https://www.geeksforgeeks.org/html-var-tag/)`:` It defines the variable text.

    `Example 1:` This example describe the use of <kbd> tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h3>HTML kbd Tag</h3>  <p>Open a new window using thekeyboard shortcut<kbd>Ctrl</kbd> + <kbd>N</kbd></p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205120841/kbdTag.PNG)

    `Example 2:` This example using <kbd> tag with some CSS styles.

    ```html
    <!DOCTYPE html><html> <head><style>kbd {border-radius: 2px;padding: 2px;border: 1px solid black;}</style></head> <body><h1>GeeksforGeeks</h1> <h2>HTML kbd Tag</h2>  <p>Open a new window using thekeyboard shortcut<kbd>Ctrl</kbd>+<kbd>N</kbd></p> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205121208/kbdTag1.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera


    It is a phrase tag and used to define the keyboard input. The text enclosed within <kbd> tag is typically display in the browser’s default monospace font.

    `Syntax:`



    <kbd> text content ... </kbd>

    `List of all phrase tag:`


    * [`<em>`](https://www.geeksforgeeks.org/html-em-tag/)`:` It is used to emphasize the text.
    * [`<strong>`](https://www.geeksforgeeks.org/html-strong-tag/)`:` It is used to define an important text.
    * [`<code>`](https://www.geeksforgeeks.org/html-code-tag/)`:` It encloses the computer code.
    * [`<samp>`](https://www.geeksforgeeks.org/html-samp-tag/)`:` It defines a sample output text from a computer program.
    * [`<kbd>`](https://www.geeksforgeeks.org/html-kbd-tag/)`:` It defines the text of keyboard input.
    * [`<var>`](https://www.geeksforgeeks.org/html-var-tag/)`:` It defines the variable text.

    `Example 1:` This example describe the use of <kbd> tag.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h3>HTML kbd Tag</h3>  <p>Open a new window using thekeyboard shortcut<kbd>Ctrl</kbd> + <kbd>N</kbd></p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205120841/kbdTag.PNG)

    `Example 2:` This example using <kbd> tag with some CSS styles.

    ```html
    <!DOCTYPE html><html> <head><style>kbd {border-radius: 2px;padding: 2px;border: 1px solid black;}</style></head> <body><h1>GeeksforGeeks</h1> <h2>HTML kbd Tag</h2>  <p>Open a new window using thekeyboard shortcut<kbd>Ctrl</kbd>+<kbd>N</kbd></p> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205121208/kbdTag1.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera




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
            tagName="kbd",
        )


class Keygen(BaseVoidElement):
    """ """

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
            tagName="keygen",
        )


class Label(BaseElement):
    """
    The <label> tag in HTML is used to provide a usability improvement for mouse users i.e, if a user clicks on the text within the <label> element, it toggles the control. The <label> tag defines the label for <button>, <input>, <meter>, <output>, <progress>, <select>, or <textarea> element.

    `The <label> tag can be used in two ways:`

    * Firstly, use <label> tag by providing the <input> and id attribute. The <label> tag needs a *for* attribute whose value is the same as input id.
    * Alternatively, <input> tag use directly inside the <label> tag. In this case, the *for* and id attributes are not needed because the association is implicit.

    `Syntax:`



    <label> form content... </label>

    `Attribute Value:`

    * [`for`](https://www.geeksforgeeks.org/html-label-for-attribute)`:` It refers to the input control that this label is for. Its value must be the same as the value of the input control’s “id” attribute.
    * [`form`](https://www.geeksforgeeks.org/html-label-form-attribute/)`:` It refers to the form to which the label belongs to.

    `Example 1:` Here we will use the input tag outside the label tag.



    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><strong>HTML label Tag</strong> <form> <!-- Starts label tags from here --><label for="student">Student</label><input type="radio" name="Occupation"id="student" value="student"><br> <label for="business">Business</label><input type="radio" name="Occupation"id="business" value="business"><br> <label for="other">Other</label><!-- Ends label tags here --> <input type="radio" name="Occupation"id="other" value="other"></form></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181659/Screenshot20210215181636.png)

    `Example 2:` Here we will use the input tag inside the label tag.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1> <strong>HTML label Tag </strong> <form><!-- label tag starts from here --><label>Male<input type="radio" name="gender"id="male" value="male" /></label><br/> <label>Female<input type="radio" name="gender"id="female" value="female" /></label><br/> <label>Other<input type="radio" name="gender"id="other" value="other" /></label><!-- label tag ends from here --></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215182532/Screenshot20210215182511.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    The <label> tag in HTML is used to provide a usability improvement for mouse users i.e, if a user clicks on the text within the <label> element, it toggles the control. The <label> tag defines the label for <button>, <input>, <meter>, <output>, <progress>, <select>, or <textarea> element.

    `The <label> tag can be used in two ways:`

    * Firstly, use <label> tag by providing the <input> and id attribute. The <label> tag needs a *for* attribute whose value is the same as input id.
    * Alternatively, <input> tag use directly inside the <label> tag. In this case, the *for* and id attributes are not needed because the association is implicit.

    `Syntax:`



    <label> form content... </label>

    `Attribute Value:`

    * [`for`](https://www.geeksforgeeks.org/html-label-for-attribute)`:` It refers to the input control that this label is for. Its value must be the same as the value of the input control’s “id” attribute.
    * [`form`](https://www.geeksforgeeks.org/html-label-form-attribute/)`:` It refers to the form to which the label belongs to.

    `Example 1:` Here we will use the input tag outside the label tag.



    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><strong>HTML label Tag</strong> <form> <!-- Starts label tags from here --><label for="student">Student</label><input type="radio" name="Occupation"id="student" value="student"><br> <label for="business">Business</label><input type="radio" name="Occupation"id="business" value="business"><br> <label for="other">Other</label><!-- Ends label tags here --> <input type="radio" name="Occupation"id="other" value="other"></form></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181659/Screenshot20210215181636.png)

    `Example 2:` Here we will use the input tag inside the label tag.


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1> <strong>HTML label Tag </strong> <form><!-- label tag starts from here --><label>Male<input type="radio" name="gender"id="male" value="male" /></label><br/> <label>Female<input type="radio" name="gender"id="female" value="female" /></label><br/> <label>Other<input type="radio" name="gender"id="other" value="other" /></label><!-- label tag ends from here --></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215182532/Screenshot20210215182511.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
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
            tagName="label",
        )


class Legend(BaseElement):
    """
    The legend tag is used to define the title for the child contents. The legend elements are the parent element. This tag is used to define the caption for the [<fieldset>](https://www.geeksforgeeks.org/html5-fieldset-tag/) element.

    `Syntax`



    <legend> Text </legend>

    `Attribute :`

    * `align:` It sets the alignment of the legend element.

    `Example 1:`


    ```html
    <!DOCTYPE html><html><head></head><body><h1>GeeksforGeeks</h1><strong>HTML Legend Tag</strong><form><fieldset><!-- Legend tag using --><legend>STUDENT::</legend><label>Name:</label><input type="text"><br><br><label>Email:</label><input type="text"><br><br><label>Date of birth:</label><input type="text"><br><br><label>Address:</label><input type="text"><br><br><label>Enroll No:</label><input type="text"></fieldset></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181030/Screenshot20210215180947.png)

    `Example 2:` Styling the legend tag using CSS properties.



    ```html
    <!DOCTYPE html><html><head><style>form{width: 50%;}legend {display: block;padding-left: 10px;padding-right: 10px;border: 3px solid green;background-color:tomato;color:white;;}label {display: inline-block;float: left;clear: left;width: 90px;margin:5px;text-align: left;}input[type="text"] {width:250px;margin:5px 0px;}.gfg {font-size:40px;color:green;font-weight:bold;}</style></head><body><div class = "gfg">GeeksforGeeks</div><h2>HTML Legend Tag</h2><form><fieldset><!-- Legend tag using --><legend>STUDENT:</legend><label>Name:</label><input type="text"><br><label>Email:</label><input type="text"><br><label>Date of birth:</label><input type="text"><br><label>Address:</label><input type="text"><br><label>Enroll No:</label><input type="text"></fieldset></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181213/Screenshot20210215181156.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer 6 and above
    * Firefox 1 and above
    * Opera 12.1 and above
    * Safari 3 and above


    The legend tag is used to define the title for the child contents. The legend elements are the parent element. This tag is used to define the caption for the [<fieldset>](https://www.geeksforgeeks.org/html5-fieldset-tag/) element.

    `Syntax`



    <legend> Text </legend>

    `Attribute :`

    * `align:` It sets the alignment of the legend element.

    `Example 1:`


    ```html
    <!DOCTYPE html><html><head></head><body><h1>GeeksforGeeks</h1><strong>HTML Legend Tag</strong><form><fieldset><!-- Legend tag using --><legend>STUDENT::</legend><label>Name:</label><input type="text"><br><br><label>Email:</label><input type="text"><br><br><label>Date of birth:</label><input type="text"><br><br><label>Address:</label><input type="text"><br><br><label>Enroll No:</label><input type="text"></fieldset></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181030/Screenshot20210215180947.png)

    `Example 2:` Styling the legend tag using CSS properties.



    ```html
    <!DOCTYPE html><html><head><style>form{width: 50%;}legend {display: block;padding-left: 10px;padding-right: 10px;border: 3px solid green;background-color:tomato;color:white;;}label {display: inline-block;float: left;clear: left;width: 90px;margin:5px;text-align: left;}input[type="text"] {width:250px;margin:5px 0px;}.gfg {font-size:40px;color:green;font-weight:bold;}</style></head><body><div class = "gfg">GeeksforGeeks</div><h2>HTML Legend Tag</h2><form><fieldset><!-- Legend tag using --><legend>STUDENT:</legend><label>Name:</label><input type="text"><br><label>Email:</label><input type="text"><br><label>Date of birth:</label><input type="text"><br><label>Address:</label><input type="text"><br><label>Enroll No:</label><input type="text"></fieldset></form></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210215181213/Screenshot20210215181156.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer 6 and above
    * Firefox 1 and above
    * Opera 12.1 and above
    * Safari 3 and above




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
            tagName="legend",
        )


class Li(BaseElement):
    """
    The <li> tag in HTML is used to define the list item in an HTML document. It is used within an [Ordered List <ol>](https://www.geeksforgeeks.org/html-ol-tag/) or [Unordered List <ul>](https://www.geeksforgeeks.org/html-ul-tag/). The <li> tag requires a starting and end tag.
    `Note:` The end tag can be omitted if the list item is immediately followed by another <li> element, or if there is no more content in its parent element.


    `Syntax:`



    <li> List Items </li>

    `Attribute Value:`

    [`value:`](https://www.geeksforgeeks.org/html-li-value-attribute/) The value attribute is used to specify the starting number of the list item. The list item starts from this number and increments its value with every addition of items to it. The value attribute only works for the ordered lists i.e. <ol> tag.

    `Example 1:` This example using <li> tag inside Ordered Lists.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ol><li>Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ol></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220448/li1.PNG)

    `Example 2:` This example using <li> tag with Unordered Lists.



    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ul><li>Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ul></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220653/li2.PNG)

    `Example 3:` This example using <li> tag with value attribute to create lists.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ol><li value="5">Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ol></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220853/li3.PNG)

    `Applying Styles to <li> Tag:` Some CSS properties can also be used to style the <li> elements that are: [list-style](https://www.geeksforgeeks.org/css-list-style-property/), [list-style-image](https://www.geeksforgeeks.org/css-list-style-image-property/), [list-style-position](https://www.geeksforgeeks.org/css-list-style-position-property/), and [list-style-type](https://www.geeksforgeeks.org/css-list-style-type-property/). These properties can be directly applied to the <li> element although, they are usually applied to the parent element.

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer 5.5
    * Firefox 1
    * Opera 12.1
    * Safari 3


    The <li> tag in HTML is used to define the list item in an HTML document. It is used within an [Ordered List <ol>](https://www.geeksforgeeks.org/html-ol-tag/) or [Unordered List <ul>](https://www.geeksforgeeks.org/html-ul-tag/). The <li> tag requires a starting and end tag.
    `Note:` The end tag can be omitted if the list item is immediately followed by another <li> element, or if there is no more content in its parent element.


    `Syntax:`



    <li> List Items </li>

    `Attribute Value:`

    [`value:`](https://www.geeksforgeeks.org/html-li-value-attribute/) The value attribute is used to specify the starting number of the list item. The list item starts from this number and increments its value with every addition of items to it. The value attribute only works for the ordered lists i.e. <ol> tag.

    `Example 1:` This example using <li> tag inside Ordered Lists.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ol><li>Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ol></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220448/li1.PNG)

    `Example 2:` This example using <li> tag with Unordered Lists.



    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ul><li>Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ul></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220653/li2.PNG)

    `Example 3:` This example using <li> tag with value attribute to create lists.

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2>HTML li Tag</h2> <ol><li value="5">Geeks</li><li>Sudo</li><li>Gfg</li><li>Gate</li><li>Placement</li></ol></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210205220853/li3.PNG)

    `Applying Styles to <li> Tag:` Some CSS properties can also be used to style the <li> elements that are: [list-style](https://www.geeksforgeeks.org/css-list-style-property/), [list-style-image](https://www.geeksforgeeks.org/css-list-style-image-property/), [list-style-position](https://www.geeksforgeeks.org/css-list-style-position-property/), and [list-style-type](https://www.geeksforgeeks.org/css-list-style-type-property/). These properties can be directly applied to the <li> element although, they are usually applied to the parent element.

    `Supported Browsers:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer 5.5
    * Firefox 1
    * Opera 12.1
    * Safari 3




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
            tagName="li",
        )


class Main(BaseElement):
    """
    The `HTML <main> Tag` is used to given the main information of a document. The content inside the `<main>` element should be unique for the document. Which includes the sidebars, navigation links, copyright information, site logos, and search forms.
    `Note:` The document must not contained more than one `<main>` element . The `<main>` element should not be a child elements of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element.
    `Syntax:`




    <main>
        //contents of main Element
    </main>

    `Example:`



    ```html
    <!DOCTYPE html><html> <head> <style>.class {color: green;}</style></head> <body><h1 class="class">&lt;Main&gt; Tag</h1><main><h1>Programming Languages</h1><p>c programming, C++Programming, Java Programming</p> <article><h1>C Programming</h1><p>C is a Procedural language</p></article> <article><h1>C++ Programming</h1><p>C++ programming is aObject oriented Programming.</p></article> <article><h1>Java Programming</h1><p>Java is a pure Objectoriented Programming.</p></article></main> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190618220949/main-tag.png)

    `Supported Browsers:` The browsers supported by `<main> Tag` are listed below:


    * Google Chrome 26
    * Edge 12
    * Firefox 21
    * Apple Safari 7
    * Opera 16




    The `HTML <main> Tag` is used to given the main information of a document. The content inside the `<main>` element should be unique for the document. Which includes the sidebars, navigation links, copyright information, site logos, and search forms.
    `Note:` The document must not contained more than one `<main>` element . The `<main>` element should not be a child elements of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element.
    `Syntax:`




    <main>
        //contents of main Element
    </main>

    `Example:`



    ```html
    <!DOCTYPE html><html> <head> <style>.class {color: green;}</style></head> <body><h1 class="class">&lt;Main&gt; Tag</h1><main><h1>Programming Languages</h1><p>c programming, C++Programming, Java Programming</p> <article><h1>C Programming</h1><p>C is a Procedural language</p></article> <article><h1>C++ Programming</h1><p>C++ programming is aObject oriented Programming.</p></article> <article><h1>Java Programming</h1><p>Java is a pure Objectoriented Programming.</p></article></main> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190618220949/main-tag.png)

    `Supported Browsers:` The browsers supported by `<main> Tag` are listed below:


    * Google Chrome 26
    * Edge 12
    * Firefox 21
    * Apple Safari 7
    * Opera 16






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
            tagName="main",
        )


class Mark(BaseElement):
    """
    The <mark> tag in HTML is used to define the marked text. It is used to highlight the part of the text in a paragraph. The <mark> tag is new in HTML 5.


    `Syntax:`



    <mark> Contents... </mark>

    `Example 1:` This example uses <mark> tag to highlight the text. By default, <mark> tag highlight the text content in yellow color.


    ```html
    <!DOCTYPE html><html> <body><h1 style="color: green;">GeeksforGeeks</h1> <h2>HTML mark Tag</h2>   <p><mark>GeeksforGeeks:</mark> It is a<mark>computer science</mark> portal for geeks</p>  </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204180536/mark.PNG)

    `Example 2:` This example uses <mark> tag with CSS property to change the marked content color and other property.



    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2> HTML mark Tag</h2>   <p><mark>GeeksforGeeks:</mark> It is a<mark style="background-color: green; color: white;">computer science</mark> portal for geeks</p>  </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204180815/markcss.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.0 and above
    * Safari




    The <mark> tag in HTML is used to define the marked text. It is used to highlight the part of the text in a paragraph. The <mark> tag is new in HTML 5.


    `Syntax:`



    <mark> Contents... </mark>

    `Example 1:` This example uses <mark> tag to highlight the text. By default, <mark> tag highlight the text content in yellow color.


    ```html
    <!DOCTYPE html><html> <body><h1 style="color: green;">GeeksforGeeks</h1> <h2>HTML mark Tag</h2>   <p><mark>GeeksforGeeks:</mark> It is a<mark>computer science</mark> portal for geeks</p>  </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204180536/mark.PNG)

    `Example 2:` This example uses <mark> tag with CSS property to change the marked content color and other property.



    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1> <h2> HTML mark Tag</h2>   <p><mark>GeeksforGeeks:</mark> It is a<mark style="background-color: green; color: white;">computer science</mark> portal for geeks</p>  </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210204180815/markcss.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Firefox 4.0 and above
    * Opera 11.0 and above
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
            tagName="mark",
        )


class Marquee(BaseElement):
    """
    The <marquee> tag in HTML is used to create scrolling text or image in a webpages. It scrolls either from horizontally left to right or right to left, or vertically top to bottom or bottom to top.

    `Syntax :`

    The marquee element comes in pairs. It means that the tag has opening and closing elements.



    `<marquee>`
     `<--- contents --->`
    `</marquee>`

    `Attributes`



    | ATTRIBUTES | VALUES | DESCRIPTION |
    | --- | --- ```html
    bgcolor | Color Name | Define the background color of the marquee. |
    | direction | Top, Down, Left, Right | Define the direction of scrolling the content |
    | loop | Number | Specifies how many times content moves. The default value is infinite. |
    | height | px or % | Define the height of marquee |
    | width | px or % | Define the width of marquee |
    | hspace | px | Specify horizontal space around marquee |
    | vspace | px | Specify vertical space around marquee |

    `Methods`

    * `start ():` This method is used to start the scrolling of the Marquee Tag.
    * `stop ():` This method is used to stop the scrolling of the Marquee Tag.

    `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;padding-bottom:10px;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "left" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; padding-bottom:10px; }



    GeeksforGeeks
    A computer science portal for geeks
      `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;font-family:"Times New Roman";}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;text-align:center;}.geek2 {text-align:center;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "up" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; text-align:center; } .geek2 { text-align:center; }



    GeeksforGeeks
    A computer science portal for geeks
      `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;font-family:"Times New Roman";}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;text-align:center;}.geek2 {text-align:center;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "down" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; text-align:center; } .geek2 { text-align:center; }



    GeeksforGeeks
    A computer science portal for geeks
      `Supported Browsers`

    * Google Chrome 1.0
    * Edge 12.0
    * Firefox 65.0
    * Internet Explorer 2.0
    * Opera 7.2
    * Safari 1.2


    The <marquee> tag in HTML is used to create scrolling text or image in a webpages. It scrolls either from horizontally left to right or right to left, or vertically top to bottom or bottom to top.

    `Syntax :`

    The marquee element comes in pairs. It means that the tag has opening and closing elements.



    `<marquee>`
     `<--- contents --->`
    `</marquee>`

    `Attributes`



    | ATTRIBUTES | VALUES | DESCRIPTION |
    | --- | --- ```html
    bgcolor | Color Name | Define the background color of the marquee. |
    | direction | Top, Down, Left, Right | Define the direction of scrolling the content |
    | loop | Number | Specifies how many times content moves. The default value is infinite. |
    | height | px or % | Define the height of marquee |
    | width | px or % | Define the width of marquee |
    | hspace | px | Specify horizontal space around marquee |
    | vspace | px | Specify vertical space around marquee |

    `Methods`

    * `start ():` This method is used to start the scrolling of the Marquee Tag.
    * `stop ():` This method is used to stop the scrolling of the Marquee Tag.

    `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;padding-bottom:10px;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "left" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; padding-bottom:10px; }



    GeeksforGeeks
    A computer science portal for geeks
      `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;font-family:"Times New Roman";}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;text-align:center;}.geek2 {text-align:center;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "up" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; text-align:center; } .geek2 { text-align:center; }



    GeeksforGeeks
    A computer science portal for geeks
      `Example:`



    ```html
    <!DOCTYPE html><html><head><title>Marquee Tag</title><style>.main {text-align:center;font-family:"Times New Roman";}.marq {padding-top:30px;padding-bottom:30px;}.geek1 {font-size:36px;font-weight:bold;color:white;text-align:center;}.geek2 {text-align:center;}</style></head> <body><div class = "main"><marquee class="marq" bgcolor = "Green" direction = "down" loop="" ><div class="geek1">GeeksforGeeks</div><div class="geek2">A computer science portal for geeks</div></marquee></div></body></html> |

    ```
    `Output:`
    Marquee Tag


    .main { text-align:center; font-family:”Times New Roman”; } .marq { padding-top:30px; padding-bottom:30px; } .geek1 { font-size:36px; font-weight:bold; color:white; text-align:center; } .geek2 { text-align:center; }



    GeeksforGeeks
    A computer science portal for geeks
      `Supported Browsers`

    * Google Chrome 1.0
    * Edge 12.0
    * Firefox 65.0
    * Internet Explorer 2.0
    * Opera 7.2
    * Safari 1.2




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
            tagName="marquee",
        )


class Menuitem(BaseElement):
    """
    The `HTML <menuitem> tag` is used to define command or menu that the user can utilize from the popup item. this tag is not supported in HTML5. This tag is support Global Attributes in HTML and Event Attributes in HTML.

    `Syntax:`



    <menuitem label="" icon="" type> </menuitem>

    `Attribute:`

    * `checked:` this attribute defines that the menu item is checked when the page load, works on radio and checkbox type.
    * `default:` This attribute marks the menu item as a default command.
    * `disabled:` This attribute disabled the menu or command.
    * `icon:` This attribute define the menu icon by using url.
    * `label:` This attribute is must required which defines the name of command or menu.
    * `radiogroup:` This attribute defines the group of command.
    * `type:` This attribute defines the type of command or menu is it radio, checkbox or anything else.

    Below example illustrate the `HTML <menuitem> tag:`

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML <menuitem> Tag</title><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>HTML <menuitem> tag</h2><div style="background:green;border:2px solid#black;padding: 10px;" contextmenu="geeks">  <p>A Computer Science Portal for Geeks</p>   <menu type="context" id="geeks"><menu label="Share on..."><menuitem label="Twitter"onclick="window.open('//twitter.com/intent/tweet?text=' + window.location.href);"></menuitem><menuitem label="Pinterest"onclick="window.open('<http://pinterest.com/pin/create/button/?url=>' + window.location.href);"></menuitem></menu><menuitem label="Email This Page"onclick="window.location='mailto:?body='+window.location.href;"></menuitem></menu> </div>   <p>A Computer Science Portal for Geeks</p>  <hr>  <p>Right click on green div and see the menuitem</center></body> </html> |

    ```
    `Output:`
    `Before:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190826193945/Screenshot-from-2019-08-26-19-38-34.png)

    `After:`


    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190827121508/menuitem2.png)

    `Supported Browsers:` The browsers supported by `<menuitem> tag` are listed below:

    * Mozilla Firefox




    The `HTML <menuitem> tag` is used to define command or menu that the user can utilize from the popup item. this tag is not supported in HTML5. This tag is support Global Attributes in HTML and Event Attributes in HTML.

    `Syntax:`



    <menuitem label="" icon="" type> </menuitem>

    `Attribute:`

    * `checked:` this attribute defines that the menu item is checked when the page load, works on radio and checkbox type.
    * `default:` This attribute marks the menu item as a default command.
    * `disabled:` This attribute disabled the menu or command.
    * `icon:` This attribute define the menu icon by using url.
    * `label:` This attribute is must required which defines the name of command or menu.
    * `radiogroup:` This attribute defines the group of command.
    * `type:` This attribute defines the type of command or menu is it radio, checkbox or anything else.

    Below example illustrate the `HTML <menuitem> tag:`

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML <menuitem> Tag</title><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>HTML <menuitem> tag</h2><div style="background:green;border:2px solid#black;padding: 10px;" contextmenu="geeks">  <p>A Computer Science Portal for Geeks</p>   <menu type="context" id="geeks"><menu label="Share on..."><menuitem label="Twitter"onclick="window.open('//twitter.com/intent/tweet?text=' + window.location.href);"></menuitem><menuitem label="Pinterest"onclick="window.open('<http://pinterest.com/pin/create/button/?url=>' + window.location.href);"></menuitem></menu><menuitem label="Email This Page"onclick="window.location='mailto:?body='+window.location.href;"></menuitem></menu> </div>   <p>A Computer Science Portal for Geeks</p>  <hr>  <p>Right click on green div and see the menuitem</center></body> </html> |

    ```
    `Output:`
    `Before:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190826193945/Screenshot-from-2019-08-26-19-38-34.png)

    `After:`


    ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190827121508/menuitem2.png)

    `Supported Browsers:` The browsers supported by `<menuitem> tag` are listed below:

    * Mozilla Firefox






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
            tagName="menuitem",
        )


class Meta(BaseVoidElement):
    """ """

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
            tagName="meta",
        )


class Meter(BaseElement):
    """
    It is used to define the scale for measurement in a well-defined range and also supports a fractional value. It is also known as a gauge. It is used in Disk use, relevance query result, etc.


    `Syntax:`



    <meter attributes...> </meter>

    `Attributes:` This tag contains many attributes which are listed below:

    * [`form`](https://www.geeksforgeeks.org/html-meter-form-attribute/#:~:text=The%20HTML%20form%20Attribute,contain%20one%20or%20more%20forms.&text=Attribute%20Values%3A%20It%20contains%20single,to%20the%20element.)`:` It defines one or more forms that meter tag belongs too.
    * [`max`](https://www.geeksforgeeks.org/html-meter-max-attribute/)`:` It is used to specify the maximum value of a range.
    * [`min`](https://www.geeksforgeeks.org/html-meter-min-attribute/)`:` It is used to specify the minimum value of a range.
    * [`high`](https://www.geeksforgeeks.org/html-meter-high-attribute/)`:` It is used to specify the range considered to be a high value.
    * [`low`](https://www.geeksforgeeks.org/html-meter-low-attribute/)`:` It is used to specify the range value that is considered to be low.
    * [`Optimum`](https://www.geeksforgeeks.org/html-meter-optimum-attribute/#:~:text=HTML%20%7C%20optimum%20Attribute,-Last%20Updated%20%3A%2019&text=The%20HTML%20optimum%20Attribute,the%20range%20is%20considered%20preferable.)`:` It is used to specify the optimum value for the range.
    * [`value`](https://www.geeksforgeeks.org/html-meter-value-attribute/)`:` It is used to specify the required or actual value of the range.

    `Example:`


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1>  <p>Meter Tag:</p>   Sachin's score:<meter value="5" min="0" max="10">5 out of 10</meter><br>Laxma sxore:<meter value="0.5">50% from 100%</meter></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/meter-tag.png)

    `Supported Browsers:`

    * Google Chrome 6
    * Edge 18
    * Firefox 16
    * Opera 11
    * Safari 6

    `Important Note :` The meter tag should not be used to indicate progress (as in a progress bar). For progress bars, use the [progress](https://www.geeksforgeeks.org/html-5-progress-tag/) tag.

    It is used to define the scale for measurement in a well-defined range and also supports a fractional value. It is also known as a gauge. It is used in Disk use, relevance query result, etc.


    `Syntax:`



    <meter attributes...> </meter>

    `Attributes:` This tag contains many attributes which are listed below:

    * [`form`](https://www.geeksforgeeks.org/html-meter-form-attribute/#:~:text=The%20HTML%20form%20Attribute,contain%20one%20or%20more%20forms.&text=Attribute%20Values%3A%20It%20contains%20single,to%20the%20element.)`:` It defines one or more forms that meter tag belongs too.
    * [`max`](https://www.geeksforgeeks.org/html-meter-max-attribute/)`:` It is used to specify the maximum value of a range.
    * [`min`](https://www.geeksforgeeks.org/html-meter-min-attribute/)`:` It is used to specify the minimum value of a range.
    * [`high`](https://www.geeksforgeeks.org/html-meter-high-attribute/)`:` It is used to specify the range considered to be a high value.
    * [`low`](https://www.geeksforgeeks.org/html-meter-low-attribute/)`:` It is used to specify the range value that is considered to be low.
    * [`Optimum`](https://www.geeksforgeeks.org/html-meter-optimum-attribute/#:~:text=HTML%20%7C%20optimum%20Attribute,-Last%20Updated%20%3A%2019&text=The%20HTML%20optimum%20Attribute,the%20range%20is%20considered%20preferable.)`:` It is used to specify the optimum value for the range.
    * [`value`](https://www.geeksforgeeks.org/html-meter-value-attribute/)`:` It is used to specify the required or actual value of the range.

    `Example:`


    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1>  <p>Meter Tag:</p>   Sachin's score:<meter value="5" min="0" max="10">5 out of 10</meter><br>Laxma sxore:<meter value="0.5">50% from 100%</meter></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/meter-tag.png)

    `Supported Browsers:`

    * Google Chrome 6
    * Edge 18
    * Firefox 16
    * Opera 11
    * Safari 6

    `Important Note :` The meter tag should not be used to indicate progress (as in a progress bar). For progress bars, use the [progress](https://www.geeksforgeeks.org/html-5-progress-tag/) tag.



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
            tagName="meter",
        )


class Nav(BaseElement):
    """
    The <nav> tag is used for declaring the navigational section in HTML documents. Websites typically have sections dedicated to navigational links, which enables users to navigate the site. These links can be placed inside a nav tag. In other words, the nav element represents a section of the page whose purpose is to provide navigational links, either in the current document or to another document. The links in the nav element may point to other webpages or to different sections of the same webpage. It is a semantic element. Common examples of the nav elements are menus, tables, contents, and indexes.

    The nav tag is reserved for primary navigation areas, like the main menu across the top of the page or section. A document may have several nav elements, for example, site navigation and one for intra-page navigation. Links within nav tag can be codes within a ul list or simply coded as separate links, without ul element. This element makes it much easier to create a navigation menu, creates a neat horizontal menu of text links, and helps screen reading software to correctly identify primary navigation areas in the document.
      `Syntax:`



    <nav> Links... </nav>

    `Example:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2> HTML nav Tag</h2><!-- nav tag starts --><nav><a href="#">Home</a> |<a href="#">Interview</a> |<a href="#">Languages</a> |<a href="#">Data Structure</a> |<a href="#">Algorithm</a></nav><!-- nav tag ends --></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122253/nav1.PNG)

    `Example:` Styling nav using CSS.


    ```html
    <!DOCTYPE html><html> <head><style>nav {border: 1px;background-color: green;color: white;padding: 6px;} a {text-decoration: none;color: white;font-size: 20px;}</style></head> <body><h1>GeeksforGeeks</h1><h2>HTML nav Tag</h2><!-- nav tag starts --><nav><a href="<https://www.geeksforgeeks.org/>">Home</a> |<a href="<https://www.geeksforgeeks.org/company-interview-corner/>">Interview</a> |<a href="<https://www.geeksforgeeks.org/gate-cs-notes-gq/>">Gate</a> |<a href="<https://www.geeksforgeeks.org/data-structures/>">Data Structure</a> |<a href="<https://www.geeksforgeeks.org/fundamentals-of-algorithms/>">Algorithm</a></nav><!-- nav tag ends --></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212124030/nav2.PNG)

      `Supported Browser:`

    * Google Chrome 5.0 and above
    * Edge 12 and above
    * Internet Explorer 9.0 and above
    * Mozilla 4.0 and above
    * Safari 5.0 and above
    * Opera 11.1 and above


    The <nav> tag is used for declaring the navigational section in HTML documents. Websites typically have sections dedicated to navigational links, which enables users to navigate the site. These links can be placed inside a nav tag. In other words, the nav element represents a section of the page whose purpose is to provide navigational links, either in the current document or to another document. The links in the nav element may point to other webpages or to different sections of the same webpage. It is a semantic element. Common examples of the nav elements are menus, tables, contents, and indexes.

    The nav tag is reserved for primary navigation areas, like the main menu across the top of the page or section. A document may have several nav elements, for example, site navigation and one for intra-page navigation. Links within nav tag can be codes within a ul list or simply coded as separate links, without ul element. This element makes it much easier to create a navigation menu, creates a neat horizontal menu of text links, and helps screen reading software to correctly identify primary navigation areas in the document.
      `Syntax:`



    <nav> Links... </nav>

    `Example:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2> HTML nav Tag</h2><!-- nav tag starts --><nav><a href="#">Home</a> |<a href="#">Interview</a> |<a href="#">Languages</a> |<a href="#">Data Structure</a> |<a href="#">Algorithm</a></nav><!-- nav tag ends --></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122253/nav1.PNG)

    `Example:` Styling nav using CSS.


    ```html
    <!DOCTYPE html><html> <head><style>nav {border: 1px;background-color: green;color: white;padding: 6px;} a {text-decoration: none;color: white;font-size: 20px;}</style></head> <body><h1>GeeksforGeeks</h1><h2>HTML nav Tag</h2><!-- nav tag starts --><nav><a href="<https://www.geeksforgeeks.org/>">Home</a> |<a href="<https://www.geeksforgeeks.org/company-interview-corner/>">Interview</a> |<a href="<https://www.geeksforgeeks.org/gate-cs-notes-gq/>">Gate</a> |<a href="<https://www.geeksforgeeks.org/data-structures/>">Data Structure</a> |<a href="<https://www.geeksforgeeks.org/fundamentals-of-algorithms/>">Algorithm</a></nav><!-- nav tag ends --></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212124030/nav2.PNG)

      `Supported Browser:`

    * Google Chrome 5.0 and above
    * Edge 12 and above
    * Internet Explorer 9.0 and above
    * Mozilla 4.0 and above
    * Safari 5.0 and above
    * Opera 11.1 and above




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
            tagName="nav",
        )


class Nobr(BaseElement):
    """
    The `<nobr>` tag is used to create a single line text, that does not matter how long the statement is, this tag used with [`<wbr>`](https://www.geeksforgeeks.org/html-5-wbr-tag/) tag. The created single line statement bring the horizontal scroll to read the whole line. The `<nobr>` tag is exact opposite of [<br>](https://www.geeksforgeeks.org/html-br-tag/) tag. You can use the CSS white space property as a replacement of this tag.

    `Note:` <nobr> tag is not supported in html5.

    `Syntax:`



    <nobr> Statement </nobr>

    `Attribute:` This tag doesn’t contain any attribute. Below example illustrates the `HTML <nobr> tags:`

    `Example:`


    ```html
    <!Doctype html><html> <head><title>HTML nobr Tag</title><isindex prompt="Search" /><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h4>HTML &lt;nobr&gt; tag</h4><nobr>Articles that need little modification/improvementfrom reviewers are published first. To quickly get yourarticles reviewed, please refer existing articles, theirformating style, coding style, and try to make your closeto them.</nobr></center></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190827102845/Kazam_screencast_00000-1.gif)

    `Supported Browsers:` The browsers supported by `HTML <nobr>` tag are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera
    The `<nobr>` tag is used to create a single line text, that does not matter how long the statement is, this tag used with [`<wbr>`](https://www.geeksforgeeks.org/html-5-wbr-tag/) tag. The created single line statement bring the horizontal scroll to read the whole line. The `<nobr>` tag is exact opposite of [<br>](https://www.geeksforgeeks.org/html-br-tag/) tag. You can use the CSS white space property as a replacement of this tag.

    `Note:` <nobr> tag is not supported in html5.

    `Syntax:`



    <nobr> Statement </nobr>

    `Attribute:` This tag doesn’t contain any attribute. Below example illustrates the `HTML <nobr> tags:`

    `Example:`


    ```html
    <!Doctype html><html> <head><title>HTML nobr Tag</title><isindex prompt="Search" /><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h4>HTML &lt;nobr&gt; tag</h4><nobr>Articles that need little modification/improvementfrom reviewers are published first. To quickly get yourarticles reviewed, please refer existing articles, theirformating style, coding style, and try to make your closeto them.</nobr></center></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190827102845/Kazam_screencast_00000-1.gif)

    `Supported Browsers:` The browsers supported by `HTML <nobr>` tag are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera


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
            tagName="nobr",
        )


class Noembed(BaseElement):
    """
    The `<noembed>` tag is used to show that the browsers is not supported by `<embed>` tag. This `<noembed>` tag will inform the user what is missing in the users browsers.

    `Note: <noembed>` tag is not supported in html5.

    `Syntax:`



    <noembed> Element </noembed>

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>embed Tag</title><style>q {color: #00cc00;font-style: italic;}</style></head> <body><center><br><embed src="<https://media.geeksforgeeks.org/wp-content/uploads/20190825000042/geeks-221.png">><noembed><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20190821123122/gfgsm.png">alt="Alternative Media"></noembed></embed></center></body> </html> |

    ```
    `Output:`

    * IF browsers supported by `<embed>`: ![](https://media.geeksforgeeks.org/wp-content/uploads/20190825000042/geeks-221.png)
    * IF browsers not supported by `<embed>` then `<noembed>` activate: ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821123122/gfgsm.png)

    `Supported Browsers`: The browser supported by `<noembed>` tag are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera
    The `<noembed>` tag is used to show that the browsers is not supported by `<embed>` tag. This `<noembed>` tag will inform the user what is missing in the users browsers.

    `Note: <noembed>` tag is not supported in html5.

    `Syntax:`



    <noembed> Element </noembed>

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>embed Tag</title><style>q {color: #00cc00;font-style: italic;}</style></head> <body><center><br><embed src="<https://media.geeksforgeeks.org/wp-content/uploads/20190825000042/geeks-221.png">><noembed><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20190821123122/gfgsm.png">alt="Alternative Media"></noembed></embed></center></body> </html> |

    ```
    `Output:`

    * IF browsers supported by `<embed>`: ![](https://media.geeksforgeeks.org/wp-content/uploads/20190825000042/geeks-221.png)
    * IF browsers not supported by `<embed>` then `<noembed>` activate: ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821123122/gfgsm.png)

    `Supported Browsers`: The browser supported by `<noembed>` tag are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera


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
            tagName="noembed",
        )


class Noscript(BaseElement):
    """
    The <noscript> tag in HTML is used to display the text for those browsers which does not support script tag or the browsers disable the script by the user. This tag is used in both [<head>](https://www.geeksforgeeks.org/html-head-tag/) and [<body>](https://www.geeksforgeeks.org/html-body-tag/) tag.

    `Note:` This tag is used in those browsers only which does not support scripts.

    `Syntax:`



    <noscript> Contents... </noscript>

    Below example illustrates the <noscript> tag in HTML:

    `Example:`

    ```html
    <html> <body><h1>GeeksforGeeks</h1><h2>HTML noscript Tag</h2><script>document.write("GeeksforGeeks!")</script><!-- noscript tag starts --><noscript>A computer science portal</noscript><!-- noscript tag ends --> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122035/noscript.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari
    The <noscript> tag in HTML is used to display the text for those browsers which does not support script tag or the browsers disable the script by the user. This tag is used in both [<head>](https://www.geeksforgeeks.org/html-head-tag/) and [<body>](https://www.geeksforgeeks.org/html-body-tag/) tag.

    `Note:` This tag is used in those browsers only which does not support scripts.

    `Syntax:`



    <noscript> Contents... </noscript>

    Below example illustrates the <noscript> tag in HTML:

    `Example:`

    ```html
    <html> <body><h1>GeeksforGeeks</h1><h2>HTML noscript Tag</h2><script>document.write("GeeksforGeeks!")</script><!-- noscript tag starts --><noscript>A computer science portal</noscript><!-- noscript tag ends --> </body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122035/noscript.PNG)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="noscript",
        )


class Object(BaseElement):
    """
    The <object> tag is an HTML tag and used to display multimedia like audios, videos, images, PDFs, and Flash in web pages. It can also be used for displaying another webpage inside the HTML page.
    The <param> tag is also used along with this tag to define various parameters. Any text that is written within <object> and </object> tags are considered as an alternative text that appears when the data specified is not supported by the browser.
    This tag supports all Global and Event attributes of HTML.
    `Example:`

    ```html
    <!DOCTYPE html> <html> <body><h1>HTML Object Tag</h1><!--HTML object tag starts here--><object data="<https://media.geeksforgeeks.org/wp-content/cdn-uploads/Geek_logi_-low_res.png>"width="550px" height="150px">GeeksforGeeks<!--HTML object tag ends here--></object></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611142250/object.png)

    The <object> tag has the following attributes:




    | Attribute | Value | Description |
    | --- | --- ```html
    [data](https://www.geeksforgeeks.org/html-object-data-attribute/) | URL | It specifies the URL of data in the object. |
    | [type](https://www.geeksforgeeks.org/html-object-type-attribute/) | media\_type | It specifies the media type of data specified in the data attribute. |
    | typemustmatch | boolean | It indicates that the resource should be embedded only if the value of the type attribute matches with the type of the resource provided on the data attribute. |
    | [align](https://www.geeksforgeeks.org/html-object-align-attribute/) | left, right, top, bottom | It defines the alignment of the objects. |
    | [border](https://www.geeksforgeeks.org/html-object-border-attribute/) | pixels | It specifies the border around the object. |
    | [height](https://www.geeksforgeeks.org/html-height-attribute/) | pixels | It specifies the height of the object. |
    | [hspace](https://www.geeksforgeeks.org/html-object-hspace-attribute/) | pixels | It specifies the whitespace on the left and right side of the object. |
    | [vspace](https://www.geeksforgeeks.org/html-object-vspace-attribute/) | pixels | It specifies the whitespace on the top and bottom of the object. |
    | [height](https://www.geeksforgeeks.org/html-object-height-attribute/) | pixels | It specifies the height of the object. |
    | [width](https://www.geeksforgeeks.org/html-object-width-attribute/) | pixels | It specifies the width of the object. |
    | [name](https://www.geeksforgeeks.org/html-object-name-attribute/) | name | It specifies the name for an object. |
    | [form](https://www.geeksforgeeks.org/html-object-form-attribute/) | form\_id | It specifies the form id to which the object element belongs to. |

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari



    The <object> tag is an HTML tag and used to display multimedia like audios, videos, images, PDFs, and Flash in web pages. It can also be used for displaying another webpage inside the HTML page.
    The <param> tag is also used along with this tag to define various parameters. Any text that is written within <object> and </object> tags are considered as an alternative text that appears when the data specified is not supported by the browser.
    This tag supports all Global and Event attributes of HTML.
    `Example:`

    ```html
    <!DOCTYPE html> <html> <body><h1>HTML Object Tag</h1><!--HTML object tag starts here--><object data="<https://media.geeksforgeeks.org/wp-content/cdn-uploads/Geek_logi_-low_res.png>"width="550px" height="150px">GeeksforGeeks<!--HTML object tag ends here--></object></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611142250/object.png)

    The <object> tag has the following attributes:




    | Attribute | Value | Description |
    | --- | --- ```html
    [data](https://www.geeksforgeeks.org/html-object-data-attribute/) | URL | It specifies the URL of data in the object. |
    | [type](https://www.geeksforgeeks.org/html-object-type-attribute/) | media\_type | It specifies the media type of data specified in the data attribute. |
    | typemustmatch | boolean | It indicates that the resource should be embedded only if the value of the type attribute matches with the type of the resource provided on the data attribute. |
    | [align](https://www.geeksforgeeks.org/html-object-align-attribute/) | left, right, top, bottom | It defines the alignment of the objects. |
    | [border](https://www.geeksforgeeks.org/html-object-border-attribute/) | pixels | It specifies the border around the object. |
    | [height](https://www.geeksforgeeks.org/html-height-attribute/) | pixels | It specifies the height of the object. |
    | [hspace](https://www.geeksforgeeks.org/html-object-hspace-attribute/) | pixels | It specifies the whitespace on the left and right side of the object. |
    | [vspace](https://www.geeksforgeeks.org/html-object-vspace-attribute/) | pixels | It specifies the whitespace on the top and bottom of the object. |
    | [height](https://www.geeksforgeeks.org/html-object-height-attribute/) | pixels | It specifies the height of the object. |
    | [width](https://www.geeksforgeeks.org/html-object-width-attribute/) | pixels | It specifies the width of the object. |
    | [name](https://www.geeksforgeeks.org/html-object-name-attribute/) | name | It specifies the name for an object. |
    | [form](https://www.geeksforgeeks.org/html-object-form-attribute/) | form\_id | It specifies the form id to which the object element belongs to. |

    `Supported Browsers:`

    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="object",
        )


class Optgroup(BaseElement):
    """
    This tag is used to create a group of the same category options in a drop-down list. The <optgroup> tag is required when there is a long list of the item exists.
    `Syntax:`



    <optgroup>
          <option>..</option>
            .
            .
    </optgroup>

    `Attributes:`

    * [`label`](https://www.geeksforgeeks.org/html-optgroup-label-attribute/#:~:text=The%20HTML%20optgroup%20label%20Attribute,for%20an%20Element.&text=Attribute%20Values%3A%20It%20contains%20the,description%20for%20a%20optgroup%20Element.)`:` It is used to specify the label for an optgroup.
    * [`disabled`](https://www.geeksforgeeks.org/html-optgroup-disabled-attribute/#:~:text=HTML%20disabled%20Attribute,-Difficulty%20Level%20%3A%20Basic&text=The%20disabled%20attribute%20for%20%3Coptgroup,It%20is%20a%20boolean%20attribute.)`:` It is used to disable the option-group in a list.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML optgroup Tag</h2><select><!-- optgroup tag starts --><optgroup label="Programming Languages"><option value="C">C</option><option value="C++">C++</option><option value="Java">Java</option></optgroup><optgroup label="Scripting Language"><option value="JavaScript">JavaScript</option><option value="PHP">PHP</option><option value="Shell">Shell</option></optgroup><!-- optgroup tag ends     --></select></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115045/opt1.PNG)

    `Example 2:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML optgroup Tag</h2><select><!-- optgroup tag starts --><optgroup label="Programming Languages"><option value="C">C</option><option value="C++">C++</option><option value="Java">Java</option></optgroup><optgroup label="Scripting Language" disabled><option value="JavaScript">JavaScript</option><option value="PHP">PHP</option><option value="Shell">Shell</option></optgroup><!-- optgroup tag ends --></select></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115216/opt2.PNG)

    `Supported Browser:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer 5.5
    * Firefox 1
    * Opera
    * Safari


    This tag is used to create a group of the same category options in a drop-down list. The <optgroup> tag is required when there is a long list of the item exists.
    `Syntax:`



    <optgroup>
          <option>..</option>
            .
            .
    </optgroup>

    `Attributes:`

    * [`label`](https://www.geeksforgeeks.org/html-optgroup-label-attribute/#:~:text=The%20HTML%20optgroup%20label%20Attribute,for%20an%20Element.&text=Attribute%20Values%3A%20It%20contains%20the,description%20for%20a%20optgroup%20Element.)`:` It is used to specify the label for an optgroup.
    * [`disabled`](https://www.geeksforgeeks.org/html-optgroup-disabled-attribute/#:~:text=HTML%20disabled%20Attribute,-Difficulty%20Level%20%3A%20Basic&text=The%20disabled%20attribute%20for%20%3Coptgroup,It%20is%20a%20boolean%20attribute.)`:` It is used to disable the option-group in a list.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML optgroup Tag</h2><select><!-- optgroup tag starts --><optgroup label="Programming Languages"><option value="C">C</option><option value="C++">C++</option><option value="Java">Java</option></optgroup><optgroup label="Scripting Language"><option value="JavaScript">JavaScript</option><option value="PHP">PHP</option><option value="Shell">Shell</option></optgroup><!-- optgroup tag ends     --></select></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115045/opt1.PNG)

    `Example 2:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML optgroup Tag</h2><select><!-- optgroup tag starts --><optgroup label="Programming Languages"><option value="C">C</option><option value="C++">C++</option><option value="Java">Java</option></optgroup><optgroup label="Scripting Language" disabled><option value="JavaScript">JavaScript</option><option value="PHP">PHP</option><option value="Shell">Shell</option></optgroup><!-- optgroup tag ends --></select></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115216/opt2.PNG)

    `Supported Browser:`

    * Google Chrome 1
    * Edge 12
    * Internet Explorer 5.5
    * Firefox 1
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
            tagName="optgroup",
        )


class Option(BaseElement):
    """
    The <option> tag in HTML is used to choose an option from a Drop-Down menu. This tag can be used with or without any attributes and needed value can be sent to the server. The group of options can be created using [<optgroup> Tag](https://www.geeksforgeeks.org/html-optgroup-tag/). It creates a group of related menu items.

    `Syntax:`



    <option> Contents... </option>

    `Attributes:` The <option> tag contains four attributes which are listed below:

    * [`disabled`](https://www.w3schools.com/tags/att_option_disabled.asp#:~:text=The%20disabled%20attribute%20is%20a,a%20checkbox%2C%20etc.).)`:` This attribute contains the value disabled which represents the option is disabled.
    * [`label`](https://www.geeksforgeeks.org/html-option-label-attribute/#:~:text=The%20HTML%20option%20label%20Attribute,in%20the%20drop%2Ddown%20list.&text=Attribute%20Values%3A%20It%20contains%20single,shorter%20version%20for%20an%20option.)`:` This attribute contains the text value which represents the shorted label for the option.
    * [`selected`](https://www.w3schools.com/tags/att_option_selected.asp)`:` This attribute contains the value selected which represents the item that is pre-selected when the browser loaded.
    * [`value`](https://www.w3schools.com/tags/att_option_value.asp)`:` This attribute contains the value text sent to the server.

    `Example 1:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML option Tag</h2><select><!-- option tag starts --><option>Choose an option</option><option value="html">HTML</option><option value="java">JAVA</option><option value="C++">C++</option><option value="php">PHP</option><option value="perl">PERL</option><!-- option tag ends --></select></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122714/option1.PNG)

    `Example 2:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML option Tag</h2><strong>Select City<br></strong><select><!-- option tag starts --><option>Allahabad</option><option>Pryagraj</option><option>Jaipur</option><option>Noida</option><!-- option tag ends     --></select></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212123648/opt2.PNG)

    `Supported Browsers:`

    * Google Chrome 1+
    * Edge 12+
    * Firefox 1+
    * Safari
    * Opera


    The <option> tag in HTML is used to choose an option from a Drop-Down menu. This tag can be used with or without any attributes and needed value can be sent to the server. The group of options can be created using [<optgroup> Tag](https://www.geeksforgeeks.org/html-optgroup-tag/). It creates a group of related menu items.

    `Syntax:`



    <option> Contents... </option>

    `Attributes:` The <option> tag contains four attributes which are listed below:

    * [`disabled`](https://www.w3schools.com/tags/att_option_disabled.asp#:~:text=The%20disabled%20attribute%20is%20a,a%20checkbox%2C%20etc.).)`:` This attribute contains the value disabled which represents the option is disabled.
    * [`label`](https://www.geeksforgeeks.org/html-option-label-attribute/#:~:text=The%20HTML%20option%20label%20Attribute,in%20the%20drop%2Ddown%20list.&text=Attribute%20Values%3A%20It%20contains%20single,shorter%20version%20for%20an%20option.)`:` This attribute contains the text value which represents the shorted label for the option.
    * [`selected`](https://www.w3schools.com/tags/att_option_selected.asp)`:` This attribute contains the value selected which represents the item that is pre-selected when the browser loaded.
    * [`value`](https://www.w3schools.com/tags/att_option_value.asp)`:` This attribute contains the value text sent to the server.

    `Example 1:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML option Tag</h2><select><!-- option tag starts --><option>Choose an option</option><option value="html">HTML</option><option value="java">JAVA</option><option value="C++">C++</option><option value="php">PHP</option><option value="perl">PERL</option><!-- option tag ends --></select></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212122714/option1.PNG)

    `Example 2:`

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h2>HTML option Tag</h2><strong>Select City<br></strong><select><!-- option tag starts --><option>Allahabad</option><option>Pryagraj</option><option>Jaipur</option><option>Noida</option><!-- option tag ends     --></select></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212123648/opt2.PNG)

    `Supported Browsers:`

    * Google Chrome 1+
    * Edge 12+
    * Firefox 1+
    * Safari
    * Opera




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
            tagName="option",
        )


class Output(BaseElement):
    """
    The <output> tag in HTML is used to represent the result of a calculation performed by the client-side script such as JavaScript. The <output> tag is a new tag in HTML 5, and it requires a starting and ends tag.


    `Syntax:`



    <output> Results... </output>

    `Attributes:` The output tag accepts three attributes which are listed below:

    * [`for`](https://www.geeksforgeeks.org/html-output-for-attribute/#:~:text=The%20HTML%20for%20Attribute,the%20result%20and%20the%20calculation.&text=Attribute%20Values%3A%20It%20contains%20a,the%20result%20and%20the%20calculation.)`:` This attribute contains an attribute value *element\_id* which is used to specify the relation between result and calculations.
    * [`form`](https://www.geeksforgeeks.org/html-output-form-attribute/)`:` This attribute contains an attribute value *form\_id* which is used to specify one or more forms of output elements.
    * [`name`](https://www.geeksforgeeks.org/html-output-name-attribute/)`:` This attribute contains an attribute value *name* that is used to specify the name of the output element.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML output Tag</h2><form oninput="sumresult.value = parseInt(A.value)+ parseInt(B.value) + parseInt(C.value)"><input type="number" name="A" value="50" /> +<input type="range" name="B" value="0" /> +<input type="number" name="C" value="30" /><br><!-- output tag -->Result: <output name="sumresult"></output></form></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115934/output1.PNG)

    `Example 2:` In this example, <output> tag is used with for and form attribute.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML output Tag</h2><form oninput="sumresult.value = parseInt(A.value)+ parseInt(B.value) + parseInt(C.value)"><input type="number" name="A" value="50" /> +<input type="range" name="B" value="0" /> +<input type="number" name="C" value="50" /><br /> Submit Result:<!-- output tag --><output name="sumresult" for="A B C"></output><br><input type="submit"></form></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212120119/output2.PNG)

    `Supported Browsers:`

    * Google Chrome 10.0 and above
    * Edge 18 and above
    * Firefox 4.0 and above
    * Opera 11.0 and above
    * Apple Safari 7 and above
    * Internet Explorer not supported


    The <output> tag in HTML is used to represent the result of a calculation performed by the client-side script such as JavaScript. The <output> tag is a new tag in HTML 5, and it requires a starting and ends tag.


    `Syntax:`



    <output> Results... </output>

    `Attributes:` The output tag accepts three attributes which are listed below:

    * [`for`](https://www.geeksforgeeks.org/html-output-for-attribute/#:~:text=The%20HTML%20for%20Attribute,the%20result%20and%20the%20calculation.&text=Attribute%20Values%3A%20It%20contains%20a,the%20result%20and%20the%20calculation.)`:` This attribute contains an attribute value *element\_id* which is used to specify the relation between result and calculations.
    * [`form`](https://www.geeksforgeeks.org/html-output-form-attribute/)`:` This attribute contains an attribute value *form\_id* which is used to specify one or more forms of output elements.
    * [`name`](https://www.geeksforgeeks.org/html-output-name-attribute/)`:` This attribute contains an attribute value *name* that is used to specify the name of the output element.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML output Tag</h2><form oninput="sumresult.value = parseInt(A.value)+ parseInt(B.value) + parseInt(C.value)"><input type="number" name="A" value="50" /> +<input type="range" name="B" value="0" /> +<input type="number" name="C" value="30" /><br><!-- output tag -->Result: <output name="sumresult"></output></form></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212115934/output1.PNG)

    `Example 2:` In this example, <output> tag is used with for and form attribute.


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2>HTML output Tag</h2><form oninput="sumresult.value = parseInt(A.value)+ parseInt(B.value) + parseInt(C.value)"><input type="number" name="A" value="50" /> +<input type="range" name="B" value="0" /> +<input type="number" name="C" value="50" /><br /> Submit Result:<!-- output tag --><output name="sumresult" for="A B C"></output><br><input type="submit"></form></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210212120119/output2.PNG)

    `Supported Browsers:`

    * Google Chrome 10.0 and above
    * Edge 18 and above
    * Firefox 4.0 and above
    * Opera 11.0 and above
    * Apple Safari 7 and above
    * Internet Explorer not supported




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
            tagName="output",
        )


class P(BaseElement):
    """ """

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
            tagName="p",
        )


class Param(BaseVoidElement):
    """ """

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
            tagName="param",
        )


class Em(BaseElement):
    """ """

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
            tagName="em",
        )


class Pre(BaseElement):
    """
    The <pre> tag in HTML is used to define the `block of preformatted text` which preserves the text spaces, line breaks, tabs, and other formatting characters which are ignored by web browsers. Text in the <pre> element is displayed in a fixed-width font, but it can be changed using CSS. The <pre> tag requires a starting and end tag.
    `Syntax:`




    <pre> Contents... </pre>

    Below examples illustrate the <pre> tag in HTML:
    `Example 1:`


    ```html
    <html><body><!-- html pre tag starts here --><pre>GeeksforGeeksA Computer   Science Portal   For Geeks</pre><!-- html pre tag ends here --></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/pre-1.png)

    `Example 2:`


    ```html
    <html><head><title>pre tag with CSS</title><style>pre {font-family: Arial;color: #009900;margin: 25px;}</style></head><body><!-- html pre tag starts here --><pre>GeeksforGeeksA Computer   Science Portal   For Geeks</pre><!-- html pre tag ends here --></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/pre1-1.png)

    `Supported Browsers:`


    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
    * Opera
    * Safari




    The <pre> tag in HTML is used to define the `block of preformatted text` which preserves the text spaces, line breaks, tabs, and other formatting characters which are ignored by web browsers. Text in the <pre> element is displayed in a fixed-width font, but it can be changed using CSS. The <pre> tag requires a starting and end tag.
    `Syntax:`




    <pre> Contents... </pre>

    Below examples illustrate the <pre> tag in HTML:
    `Example 1:`


    ```html
    <html><body><!-- html pre tag starts here --><pre>GeeksforGeeksA Computer   Science Portal   For Geeks</pre><!-- html pre tag ends here --></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/pre-1.png)

    `Example 2:`


    ```html
    <html><head><title>pre tag with CSS</title><style>pre {font-family: Arial;color: #009900;margin: 25px;}</style></head><body><!-- html pre tag starts here --><pre>GeeksforGeeksA Computer   Science Portal   For Geeks</pre><!-- html pre tag ends here --></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/pre1-1.png)

    `Supported Browsers:`


    * Google Chrome
    * Edge 12
    * Internet Explorer
    * Firefox 1
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
            tagName="pre",
        )


class Progress(BaseElement):
    """
    It is used to represent the progress of a task. It is also defined how much work is done and how much is left to download a thing. It is not used to represent the disk space or relevant query.

    ``Syntax:``



    <progress attributes...> </progress>

    ``Attributes:`` The <progress> tag consists of two attributes which are listed below:

    * [``max``](https://www.geeksforgeeks.org/html-progress-max-attribute/)``:`` It represents the total work is to be done for completing a task.
    * [``value``](https://www.geeksforgeeks.org/html-progress-value-attribute/)``:`` It represents the amount of work is already completed.

    ``Note:`` This tag is used in conjunction with JavaScript to display the progress of a task. It is not used for gauging purposes.

    ``Example:``

    ```html
    <!DOCTYPE html> <html> <body><h1>GeeksforGeeks</h1>Downloading progress for a song:<!--HTML progress tag starts here--><progress value="57"max="100"></progress><!--HTML progress tag ends here--></body> </html> |

    ````
    `Output:``


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611143947/progress.png)

    ``Supported Browsers:``


    * Google Chrome and above
    * Edge and above
    * Firefox
    * Opera
    * Safari
    It is used to represent the progress of a task. It is also defined how much work is done and how much is left to download a thing. It is not used to represent the disk space or relevant query.

    ``Syntax:``



    <progress attributes...> </progress>

    ``Attributes:`` The <progress> tag consists of two attributes which are listed below:

    * [``max``](https://www.geeksforgeeks.org/html-progress-max-attribute/)``:`` It represents the total work is to be done for completing a task.
    * [``value``](https://www.geeksforgeeks.org/html-progress-value-attribute/)``:`` It represents the amount of work is already completed.

    ``Note:`` This tag is used in conjunction with JavaScript to display the progress of a task. It is not used for gauging purposes.

    ``Example:``

    ```html
    <!DOCTYPE html> <html> <body><h1>GeeksforGeeks</h1>Downloading progress for a song:<!--HTML progress tag starts here--><progress value="57"max="100"></progress><!--HTML progress tag ends here--></body> </html> |

    ````
    `Output:``


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611143947/progress.png)

    ``Supported Browsers:``


    * Google Chrome and above
    * Edge and above
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
            tagName="progress",
        )


class Q(BaseElement):
    """
    The <q> tag is a standard quotation tag and is used for short quotations. The browser normally inserts a quotation mark around the quotation. For longer quotations, the <blockquote> tag must be used since it is a block-level element. The <q> tag requires a starting as well as an end tag.

    `Syntax:`



    <q> Contents... </q>

    `Attributes:`

    [`cite`](https://www.geeksforgeeks.org/html-cite-tag/)`:` It contains the value i.e `URL` which specifies the source URL of the Quote.

    `Example 1:` The below example illustrates the <q> tag in HTML:

    ```html
    <html><body><p><!-- html q tag is used here --><q>GeeksforGeeks</q>A computer science portal for geeks</p></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/q-4.png)

    `Example 2(Use CSS in q tag):` The below example illustrates the <q> tag in HTML:

    ```html
    <html><head><title>q tag</title><style>q {color: #00cc00;font-style: italic;}</style></head> <body><p><!-- html q tag is used here --><q>GeeksforGeeks</q>A computer science portal for geeks</p></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/q1-6.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari


    The <q> tag is a standard quotation tag and is used for short quotations. The browser normally inserts a quotation mark around the quotation. For longer quotations, the <blockquote> tag must be used since it is a block-level element. The <q> tag requires a starting as well as an end tag.

    `Syntax:`



    <q> Contents... </q>

    `Attributes:`

    [`cite`](https://www.geeksforgeeks.org/html-cite-tag/)`:` It contains the value i.e `URL` which specifies the source URL of the Quote.

    `Example 1:` The below example illustrates the <q> tag in HTML:

    ```html
    <html><body><p><!-- html q tag is used here --><q>GeeksforGeeks</q>A computer science portal for geeks</p></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/q-4.png)

    `Example 2(Use CSS in q tag):` The below example illustrates the <q> tag in HTML:

    ```html
    <html><head><title>q tag</title><style>q {color: #00cc00;font-style: italic;}</style></head> <body><p><!-- html q tag is used here --><q>GeeksforGeeks</q>A computer science portal for geeks</p></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/q1-6.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="q",
        )


class Rp(BaseElement):
    """
    The <rp> tag in HTML is used to provide parentheses around a ruby main text which defines the information. This tag is used when the browser does not support ruby annotations. Such kind of annotation is used in Japanese publications. It is an optional tag. This tag is used within the <ruby> tag. This tag is new in HTML5.
    `Syntax:`




    <rt><rp>[</rp> Explanation... <rp>]</rp></rt>

    `Example:`


    ```html
    <!DOCTYPE html> <html> <body><h1>GeeksforGeeks</h1><h2><rp> Tag</h2><ruby>GFG:<rt><!-- HTML rp tag starts here --><rp>[</rp>GeeksforGeeks<rp>]</rp><!-- HTML rp tag starts here --></rt></ruby></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154229/rpnew.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 79.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0



    The <rp> tag in HTML is used to provide parentheses around a ruby main text which defines the information. This tag is used when the browser does not support ruby annotations. Such kind of annotation is used in Japanese publications. It is an optional tag. This tag is used within the <ruby> tag. This tag is new in HTML5.
    `Syntax:`




    <rt><rp>[</rp> Explanation... <rp>]</rp></rt>

    `Example:`


    ```html
    <!DOCTYPE html> <html> <body><h1>GeeksforGeeks</h1><h2><rp> Tag</h2><ruby>GFG:<rt><!-- HTML rp tag starts here --><rp>[</rp>GeeksforGeeks<rp>]</rp><!-- HTML rp tag starts here --></rt></ruby></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154229/rpnew.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 79.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0





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
            tagName="rp",
        )


class Rt(BaseElement):
    """
    The <rt> tag in HTML is used to define the explanation of the ruby annotation which is a small text, attached with the main text. Such kind of annotation is used in Japanese publications. This tag is new in HTML5.

    `Syntax:`



    <rt> Explanation... </rt>

    `Example 1:` This example describes <rt> tag within <ruby> tag.


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><rt> Tag</h2><ruby><!-- html rt tag is used here -->GFG<rt>GeeksforGeeks</rt></ruby> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154022/rt.png)

    `Example 2:` This example does not contain <ruby> tag.


    ```html
    <!DOCTYPE html><html><head><title>rt tag</title><style>body {text-align:center;}h1 {color:green;}</style></head><body><h1>GeeksforGeeks</h1><h2><rt> Tag</h2><rt>GeeksforGeeks Contents</rt></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/rt2.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 79.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0




    The <rt> tag in HTML is used to define the explanation of the ruby annotation which is a small text, attached with the main text. Such kind of annotation is used in Japanese publications. This tag is new in HTML5.

    `Syntax:`



    <rt> Explanation... </rt>

    `Example 1:` This example describes <rt> tag within <ruby> tag.


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><rt> Tag</h2><ruby><!-- html rt tag is used here -->GFG<rt>GeeksforGeeks</rt></ruby> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154022/rt.png)

    `Example 2:` This example does not contain <ruby> tag.


    ```html
    <!DOCTYPE html><html><head><title>rt tag</title><style>body {text-align:center;}h1 {color:green;}</style></head><body><h1>GeeksforGeeks</h1><h2><rt> Tag</h2><rt>GeeksforGeeks Contents</rt></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/rt2.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 79.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0






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
            tagName="rt",
        )


class Ruby(BaseElement):
    """
    The <ruby> tag in HTML is used to specify the ruby annotation which is a small text, attached with the main text to specify the meaning of the main text. This kind of annotation is used in Japanese publications.
    `Syntax:`




    <ruby attributes> Contents... </ruby>

    `Note:` <ruby> tag contains two other tags which are listed below:


    * [`<rt> tag`](https://www.geeksforgeeks.org/html5-rt-tag/)`:` It is used to describe the explanation of main text on top of the main text.
    * [`<rp> tag`](https://www.geeksforgeeks.org/html5-rp-tag/)`:` It is optional which is used to specify the information which need to show when browsers are not supported ruby annotations.

    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><ruby> Tag</h2><!-- html ruby tag is used here --><ruby>GFG<rt>GeeksforGeeks</rt></ruby> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154803/ruby.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 12.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0



    The <ruby> tag in HTML is used to specify the ruby annotation which is a small text, attached with the main text to specify the meaning of the main text. This kind of annotation is used in Japanese publications.
    `Syntax:`




    <ruby attributes> Contents... </ruby>

    `Note:` <ruby> tag contains two other tags which are listed below:


    * [`<rt> tag`](https://www.geeksforgeeks.org/html5-rt-tag/)`:` It is used to describe the explanation of main text on top of the main text.
    * [`<rp> tag`](https://www.geeksforgeeks.org/html5-rp-tag/)`:` It is optional which is used to specify the information which need to show when browsers are not supported ruby annotations.

    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><ruby> Tag</h2><!-- html ruby tag is used here --><ruby>GFG<rt>GeeksforGeeks</rt></ruby> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611154803/ruby.png)

    `Supported Browsers:`


    * Google Chrome 5.0
    * Edge 12.0
    * Internet Explorer 5.0
    * Firefox 38.0
    * Opera 15.0
    * Safari 5.0





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
            tagName="ruby",
        )


class S(BaseElement):
    """
    This tag is used to specify that the text content is no longer correct or accurate. This tag is similar but slightly different from [<del> tag](https://www.geeksforgeeks.org/html-del-tag/). It is not used to replaced or deletes text but <del> tag is used to replaced or delete the text.
    `Syntax:`




    <s> Contents... </s>

    `Note:` This tag is depreciated from HTML 4.1, but it is redefined in HTML 5 using CSS text-decoration property instead. It is used to define the text is no longer correct.
    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><s> Tag</h2>  <p>GeeksforGeeks is a<!-- html <s> tag is used here --><s>computer science</s>portal for geeks</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611155523/stag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari



    This tag is used to specify that the text content is no longer correct or accurate. This tag is similar but slightly different from [<del> tag](https://www.geeksforgeeks.org/html-del-tag/). It is not used to replaced or deletes text but <del> tag is used to replaced or delete the text.
    `Syntax:`




    <s> Contents... </s>

    `Note:` This tag is depreciated from HTML 4.1, but it is redefined in HTML 5 using CSS text-decoration property instead. It is used to define the text is no longer correct.
    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><s> Tag</h2>  <p>GeeksforGeeks is a<!-- html <s> tag is used here --><s>computer science</s>portal for geeks</p>   </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611155523/stag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="s",
        )


class Samp(BaseElement):
    """
    It is a phrase tag and used to define the sample output text from a computer program.
    `Syntax:`




    <samp> Contents... </samp>

    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><samp> Tag</h2><!-- html <samp> tag is used here --><samp>A computer science portal for Geeks</samp> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611160227/samp.png)

    `Supported Browsers:`


    * Apple Safari
    * Google Chrome
    * Edge 12 and above
    * Firefox 1 and above
    * Opera
    * Internet Explorer



    It is a phrase tag and used to define the sample output text from a computer program.
    `Syntax:`




    <samp> Contents... </samp>

    `Example:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><samp> Tag</h2><!-- html <samp> tag is used here --><samp>A computer science portal for Geeks</samp> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210611160227/samp.png)

    `Supported Browsers:`


    * Apple Safari
    * Google Chrome
    * Edge 12 and above
    * Firefox 1 and above
    * Opera
    * Internet Explorer





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
            tagName="samp",
        )


class Script(BaseElement):
    """
    The <script> tag in HTML is used to define the client-side script. The <script> tag contains the scripting statements, or it points to an external script file. The JavaScript is mainly used in form validation, dynamic changes of content, image manipulation, etc.
    `Syntax:`




    <script> Script Contents... </script>

    `Attributes:` Many attribute associated with script tag.


    * [`async`](https://www.geeksforgeeks.org/html-script-async-attribute/)`:` It is used to specify the script is executed asynchronously.
    * [`charset`](https://www.geeksforgeeks.org/html-script-charset-attribute/)`:` It is used to specify the character encoding used in an external script file.
    * [`defer`](https://www.geeksforgeeks.org/html-script-defer-attribute/)`:` It is used to specify that the script is executed when the page has finished parsing.
    * [`src`](https://www.geeksforgeeks.org/html-script-src-attribute/)`:` It is used to specify the URL of an external script file.
    * [`type`](https://www.geeksforgeeks.org/html-script-type-attribute/)`:` It is used to specify the media type of the script.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><script> Tag</h2><p id="Geeks"></p>  <!-- html script tag starts here --><script>document.getElementById("Geeks").innerHTML ="Hello GeeksforGeeks!";</script><!-- html script tag ends here --> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210615133553/script1.png)

    `Example 2(script outside body tag):`

    ```html
    <!DOCTYPE html><html><head><title>script tag</title><style>body {text-align:center;}h1 {color:green;}</style><script>function Geeks() {alert('Welcome to GeeksforGeeks!');}</script></head><body><h1>GeeksforGeeks</h1><h2><script> Tag</h2><button type="button" onclick="Geeks()">Hello GeeksforGeeks</button></body></html> |

    ```
    `Output:`


    ![script tag](https://media.geeksforgeeks.org/wp-content/uploads/script.png)

    `Supported Browsers:`


    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <script> tag in HTML is used to define the client-side script. The <script> tag contains the scripting statements, or it points to an external script file. The JavaScript is mainly used in form validation, dynamic changes of content, image manipulation, etc.
    `Syntax:`




    <script> Script Contents... </script>

    `Attributes:` Many attribute associated with script tag.


    * [`async`](https://www.geeksforgeeks.org/html-script-async-attribute/)`:` It is used to specify the script is executed asynchronously.
    * [`charset`](https://www.geeksforgeeks.org/html-script-charset-attribute/)`:` It is used to specify the character encoding used in an external script file.
    * [`defer`](https://www.geeksforgeeks.org/html-script-defer-attribute/)`:` It is used to specify that the script is executed when the page has finished parsing.
    * [`src`](https://www.geeksforgeeks.org/html-script-src-attribute/)`:` It is used to specify the URL of an external script file.
    * [`type`](https://www.geeksforgeeks.org/html-script-type-attribute/)`:` It is used to specify the media type of the script.

    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body> <h1>GeeksforGeeks</h1><h2><script> Tag</h2><p id="Geeks"></p>  <!-- html script tag starts here --><script>document.getElementById("Geeks").innerHTML ="Hello GeeksforGeeks!";</script><!-- html script tag ends here --> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210615133553/script1.png)

    `Example 2(script outside body tag):`

    ```html
    <!DOCTYPE html><html><head><title>script tag</title><style>body {text-align:center;}h1 {color:green;}</style><script>function Geeks() {alert('Welcome to GeeksforGeeks!');}</script></head><body><h1>GeeksforGeeks</h1><h2><script> Tag</h2><button type="button" onclick="Geeks()">Hello GeeksforGeeks</button></body></html> |

    ```
    `Output:`


    ![script tag](https://media.geeksforgeeks.org/wp-content/uploads/script.png)

    `Supported Browsers:`


    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
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
            tagName="script",
        )


class Section(BaseElement):
    """
    Section tag defines the section of documents such as chapters, headers, footers or any other sections. The section tag divides the content into section and subsections. The section tag is used when requirements of two headers or footers or any other section of documents needed. Section tag grouped the generic block of related contents. The main advantage of the section tag is, it is a semantic element, which describes its meaning to both browser and developer.
    `Syntax:`




    <section> Section Contents </section>

    Section tag is used to distribute the content i.e, it distributes the sections and subsections.
    `Example:`


    ```html
    <!DOCTYPE html><html><body><!-- html section tag is used here --><section><h1>Geeksforgeeek: Section 1</h1>  <p>Content of section 1</p>  </section><section><h1>GeeksforGeeks: Section 2</h1>  <p>Content of section 2</p>  </section><section><h1>GeeksforGeeks: Section 3</h1>  <p>Content of section 3</p>  </section></body></html> |

    ```
    `Output:`


    ![section tag](https://media.geeksforgeeks.org/wp-content/uploads/section1.png)

    `Nested Section tag:` The section tag can be nested. The font size of subsection is smaller than section tag if the text contains the same font property. The subsection tag is used for organizing complex documents. A rule of thumb is that section should logically appear in outline of the document.
    `Example:`


    ```html
    <!DOCTYPE html><html><body><!-- html section tag is used here --><section><h1>Geeksforgeeek: Section 1</h1>  <p>Content of section 1</p>  <section><h1>Subsection</h1><h1>Subsection</h1></section></section><section><h1>GeeksforGeeks: Section 2</h1>  <p>Content of section 2</p>  <section><h1>Subsection</h1><h1>Subsection</h1></section></section></body></html> |

    ```
    `Output:`


    ![nested section tag](https://media.geeksforgeeks.org/wp-content/uploads/section2.png)

    `Supported Browsers:`


    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Mozilla 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above




    Section tag defines the section of documents such as chapters, headers, footers or any other sections. The section tag divides the content into section and subsections. The section tag is used when requirements of two headers or footers or any other section of documents needed. Section tag grouped the generic block of related contents. The main advantage of the section tag is, it is a semantic element, which describes its meaning to both browser and developer.
    `Syntax:`




    <section> Section Contents </section>

    Section tag is used to distribute the content i.e, it distributes the sections and subsections.
    `Example:`


    ```html
    <!DOCTYPE html><html><body><!-- html section tag is used here --><section><h1>Geeksforgeeek: Section 1</h1>  <p>Content of section 1</p>  </section><section><h1>GeeksforGeeks: Section 2</h1>  <p>Content of section 2</p>  </section><section><h1>GeeksforGeeks: Section 3</h1>  <p>Content of section 3</p>  </section></body></html> |

    ```
    `Output:`


    ![section tag](https://media.geeksforgeeks.org/wp-content/uploads/section1.png)

    `Nested Section tag:` The section tag can be nested. The font size of subsection is smaller than section tag if the text contains the same font property. The subsection tag is used for organizing complex documents. A rule of thumb is that section should logically appear in outline of the document.
    `Example:`


    ```html
    <!DOCTYPE html><html><body><!-- html section tag is used here --><section><h1>Geeksforgeeek: Section 1</h1>  <p>Content of section 1</p>  <section><h1>Subsection</h1><h1>Subsection</h1></section></section><section><h1>GeeksforGeeks: Section 2</h1>  <p>Content of section 2</p>  <section><h1>Subsection</h1><h1>Subsection</h1></section></section></body></html> |

    ```
    `Output:`


    ![nested section tag](https://media.geeksforgeeks.org/wp-content/uploads/section2.png)

    `Supported Browsers:`


    * Google Chrome 5.0 and above
    * Edge 12.0 and above
    * Internet Explorer 9.0 and above
    * Mozilla 4.0 and above
    * Opera 11.1 and above
    * Safari 5.0 and above






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
            tagName="section",
        )


class Small(BaseElement):
    """
    The <small> tag in HTML is used to set small font size. It decreases the font size by one size (from medium to small, from x-large to large). It has a [display](https://www.geeksforgeeks.org/css-display-property/https://www.geeksforgeeks.org/css-display-property/) property of inline.
    `Syntax:`




    <small> Contents... </small>

    `Example 1:`


    ```html
    <html><body><h1>GeeksforGeeks</h1><h2><small> Tag</h2> <!-- html small tag is used here --><small>Welcome to GeeksforGeeks!</small> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210618172007/small.png)

    `There are basically two ways in which you could use this <small> tag.`

    `i)` `In a nested form`: When you use the <small> tag in a nested form then the <small> tag will going to change the font size of the text in between it with respect to the parent element’s font size which means changing text with respect to its surroundings.

    Example:

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 18px;">Geeks For Geeks <small>krlo ho jayega!</small></p>  </body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602170029/gfgsmalltag2-300x95.jpg)<small> tag in nested form

    But when we increase the font size of the parent element, the <small> tag will automatically increase the font size of its text as well.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 32px">Geeks for Geeks <small>krlo ho jayega</small></p>  </body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602170029/gfgsmalltag2-300x95.jpg)<small> tag in nested form



    It means that the ratio between the font size of the nested <small> tag text and the parent element's text is same.

    `ii) In a non-nested form:` If the <small> tag is used as a separate element in the HTML document, then changing the font size of any element will not going to affect the font size of the <small>tag text.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 18px">Geeks For Geeks</p>  <small>Krlo ho jayega!</small></body></html> |



    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602172919/gfgsmalltag3-200x125.jpg)<small> tag in a non-nested form

    But if we change the font size of the paragraph, it will not affect the font size of the <small> tag text.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 32px">Geeks For Geeks</p>  <small>Krlo ho jayega!</small></body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602173336/gfgsmalltag4-200x136.jpg)<small> tag in non-nested form

    `Example 2:` Use CSS property to set the font size smaller.


    ```html
    <!DOCTYPE html><html><head><title>small Tag</title><style>body {text-align:center;}h1 {color:green;}.gfg {font-size:smaller;}</style></head><body><h1>GeeksforGeeks</h1><h2>font-size: smaller;</h2><div class = "gfg">Welcome to GeeksforGeeks!</div></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/small2.png)

    `Supported Browsers:`


    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera




    The <small> tag in HTML is used to set small font size. It decreases the font size by one size (from medium to small, from x-large to large). It has a [display](https://www.geeksforgeeks.org/css-display-property/https://www.geeksforgeeks.org/css-display-property/) property of inline.
    `Syntax:`




    <small> Contents... </small>

    `Example 1:`


    ```html
    <html><body><h1>GeeksforGeeks</h1><h2><small> Tag</h2> <!-- html small tag is used here --><small>Welcome to GeeksforGeeks!</small> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210618172007/small.png)

    `There are basically two ways in which you could use this <small> tag.`

    `i)` `In a nested form`: When you use the <small> tag in a nested form then the <small> tag will going to change the font size of the text in between it with respect to the parent element’s font size which means changing text with respect to its surroundings.

    Example:

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 18px;">Geeks For Geeks <small>krlo ho jayega!</small></p>  </body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602170029/gfgsmalltag2-300x95.jpg)<small> tag in nested form

    But when we increase the font size of the parent element, the <small> tag will automatically increase the font size of its text as well.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 32px">Geeks for Geeks <small>krlo ho jayega</small></p>  </body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602170029/gfgsmalltag2-300x95.jpg)<small> tag in nested form



    It means that the ratio between the font size of the nested <small> tag text and the parent element's text is same.

    `ii) In a non-nested form:` If the <small> tag is used as a separate element in the HTML document, then changing the font size of any element will not going to affect the font size of the <small>tag text.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 18px">Geeks For Geeks</p>  <small>Krlo ho jayega!</small></body></html> |



    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602172919/gfgsmalltag3-200x125.jpg)<small> tag in a non-nested form

    But if we change the font size of the paragraph, it will not affect the font size of the <small> tag text.

    ```html
    <!DOCTYPE html><html><head><title>GeeksForGeeks</title></head><body><h2>Welcome To GFG</h2><p style="font-size: 32px">Geeks For Geeks</p>  <small>Krlo ho jayega!</small></body></html> |


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20220602173336/gfgsmalltag4-200x136.jpg)<small> tag in non-nested form

    `Example 2:` Use CSS property to set the font size smaller.


    ```html
    <!DOCTYPE html><html><head><title>small Tag</title><style>body {text-align:center;}h1 {color:green;}.gfg {font-size:smaller;}</style></head><body><h1>GeeksforGeeks</h1><h2>font-size: smaller;</h2><div class = "gfg">Welcome to GeeksforGeeks!</div></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/small2.png)

    `Supported Browsers:`


    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera






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
            tagName="small",
        )


class Source(BaseElement):
    """
    The <source> tag in HTML is used to attach multimedia files like audio, video and pictures. The <audio>, <video> and <picture> elements contain the <source> element.

    `Syntax:`



    <source src="" type="">
        // Statements
    </source>

    `Attributes:` This tag contains five attributes as mentioned above and described below:

    * [`src`](https://www.geeksforgeeks.org/html-source-srcset-attribute/?ref=rp)`:` It is used to hold the path of media content.
    * `media:` It is used to define the type of the media content.
    * [`srcset`](https://www.geeksforgeeks.org/html-source-srcset-attribute/?ref=rp)`:` It is used to specify the URL of image used in different situations.
    * `sizes:` It is used to specify the sizes of image in different page layout.
    * `type:` It is used to specify the MIME-type resource.

    Below examples illustrate the <source> tag in HTML:

    `Example 1:` This example uses <source> tag with the video media file.


    ```html
    <!DOCTYPE html><html> <head><title>HTML source Tag</title></head> <body><h1 style="color:green;">GeeksforGeeks</h1> <h2>HTML &lt;source&gt; Tag</h2> <video width="400" height="350" controls><source src="video.mp4" type="video/mp4"><source src="video.ogg" type="video/ogg"></video></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821121240/source11.png)

    `Example 2:` This example uses <source> tag with the audio media files.


    ```html
    <!DOCTYPE html><html> <head><title>HTML source Tag</title></head> <body><h1 style="color:green;">GeeksforGeeks</h1> <h2>HTML &lt;source&gt; Tag</h2> <audio controls><source src="audio.mp3" type="audio/mp3"></audio></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821121242/source21.png)

    `Supported Browsers:` The browsers supported by `HTML <source> Tag` are listed below:

    * Google Chrome
    * Edge 12
    * Internet Explorer 9.0
    * Firefox 3.5
    * Safari
    * Opera


    The <source> tag in HTML is used to attach multimedia files like audio, video and pictures. The <audio>, <video> and <picture> elements contain the <source> element.

    `Syntax:`



    <source src="" type="">
        // Statements
    </source>

    `Attributes:` This tag contains five attributes as mentioned above and described below:

    * [`src`](https://www.geeksforgeeks.org/html-source-srcset-attribute/?ref=rp)`:` It is used to hold the path of media content.
    * `media:` It is used to define the type of the media content.
    * [`srcset`](https://www.geeksforgeeks.org/html-source-srcset-attribute/?ref=rp)`:` It is used to specify the URL of image used in different situations.
    * `sizes:` It is used to specify the sizes of image in different page layout.
    * `type:` It is used to specify the MIME-type resource.

    Below examples illustrate the <source> tag in HTML:

    `Example 1:` This example uses <source> tag with the video media file.


    ```html
    <!DOCTYPE html><html> <head><title>HTML source Tag</title></head> <body><h1 style="color:green;">GeeksforGeeks</h1> <h2>HTML &lt;source&gt; Tag</h2> <video width="400" height="350" controls><source src="video.mp4" type="video/mp4"><source src="video.ogg" type="video/ogg"></video></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821121240/source11.png)

    `Example 2:` This example uses <source> tag with the audio media files.


    ```html
    <!DOCTYPE html><html> <head><title>HTML source Tag</title></head> <body><h1 style="color:green;">GeeksforGeeks</h1> <h2>HTML &lt;source&gt; Tag</h2> <audio controls><source src="audio.mp3" type="audio/mp3"></audio></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190821121242/source21.png)

    `Supported Browsers:` The browsers supported by `HTML <source> Tag` are listed below:

    * Google Chrome
    * Edge 12
    * Internet Explorer 9.0
    * Firefox 3.5
    * Safari
    * Opera




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
            tagName="source",
        )


class Spacer(BaseVoidElement):
    """ """

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
            tagName="spacer",
        )


class Span(BaseElement):
    """ """

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
            tagName="span",
        )


class Strike(BaseElement):
    """
    In this article, we will know the `HTML <strike> tag`, along with understanding its implementation through the example. The <strike> tag defines a strike or line through Text.  This tag creates a cut line in the text. This tag is depreciated from HTML 5. Now, the [<del> tag](https://www.geeksforgeeks.org/html-del-tag/#:~:text=The%20tag%20in%20HTML,a%20starting%20and%20ending%20tag.) is used instead of this tag.

    `Syntax:`



    <strike> Contents </strike>

    `Note:` This tag is not supported in HTML5, instead of this tag, we can use [HTML del Tag](https://www.geeksforgeeks.org/html-del-tag/) or [HTML ins Tag](https://www.geeksforgeeks.org/html-ins-tag/) or use CSS [text-decoration](https://www.geeksforgeeks.org/css-text-decoration-property/#:~:text=The%20text%2Ddecoration%20property%20is,and%20text%2Ddecoration%2Dstyle.) property.

    `Example:` In this example, we simply use strike tag on text `Hi Geeks!`

    ```html
    <!DOCTYPE html><html> <body> <!-- Strike Tag --><h2>Welcome To GeeksforGeeks</h2><strike>Hi Geeks!</strike></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210920130309/2010.png)HTML <strike> tag

    `Example:` Below example illustrates the <strike> tag in HTML.

    ```html
    <!DOCTYPE html><html> <body><h1>Welcome to GeeksforGeeks</h1><h2>strike Tag</h2> <!-- Html strike tag --><strike>GeeksforGeeks</strike></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210920115346/209.png)HTML <strike> Tag

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari
    * Microsoft Edge 12 and above


    In this article, we will know the `HTML <strike> tag`, along with understanding its implementation through the example. The <strike> tag defines a strike or line through Text.  This tag creates a cut line in the text. This tag is depreciated from HTML 5. Now, the [<del> tag](https://www.geeksforgeeks.org/html-del-tag/#:~:text=The%20tag%20in%20HTML,a%20starting%20and%20ending%20tag.) is used instead of this tag.

    `Syntax:`



    <strike> Contents </strike>

    `Note:` This tag is not supported in HTML5, instead of this tag, we can use [HTML del Tag](https://www.geeksforgeeks.org/html-del-tag/) or [HTML ins Tag](https://www.geeksforgeeks.org/html-ins-tag/) or use CSS [text-decoration](https://www.geeksforgeeks.org/css-text-decoration-property/#:~:text=The%20text%2Ddecoration%20property%20is,and%20text%2Ddecoration%2Dstyle.) property.

    `Example:` In this example, we simply use strike tag on text `Hi Geeks!`

    ```html
    <!DOCTYPE html><html> <body> <!-- Strike Tag --><h2>Welcome To GeeksforGeeks</h2><strike>Hi Geeks!</strike></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210920130309/2010.png)HTML <strike> tag

    `Example:` Below example illustrates the <strike> tag in HTML.

    ```html
    <!DOCTYPE html><html> <body><h1>Welcome to GeeksforGeeks</h1><h2>strike Tag</h2> <!-- Html strike tag --><strike>GeeksforGeeks</strike></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210920115346/209.png)HTML <strike> Tag

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
            tagName="strike",
        )


class Strong(BaseElement):
    """
    The <strong> tag in HTML is the parsed tag and used to show the importance of the text. Make that text bold.

    This tag also supports the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) and [event attributes](https://www.geeksforgeeks.org/html-event-attributes-complete-reference/) in HTML.
    `Syntax:`



    <strong> Contents... </strong>

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><strong> Tag</h2><!-- html strong tag used here --><strong>Welcome to geeksforGeeks!</strong></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625183309/strong.png)

    `Example 2:` Use CSS property to set bold font weight.

    ```html
    <!DOCTYPE html><html><head><title>strong Tag</title><style>body {text-align:center;}h1 {color:green;}.gfg {font-weight:bold;}</style></head><body><h1>GeeksforGeeks</h1><h2>font-weight: bold;</h2><div class = "gfg">Welcome to geeksforGeeks!</div></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/strong2.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <strong> tag in HTML is the parsed tag and used to show the importance of the text. Make that text bold.

    This tag also supports the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) and [event attributes](https://www.geeksforgeeks.org/html-event-attributes-complete-reference/) in HTML.
    `Syntax:`



    <strong> Contents... </strong>

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><strong> Tag</h2><!-- html strong tag used here --><strong>Welcome to geeksforGeeks!</strong></body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625183309/strong.png)

    `Example 2:` Use CSS property to set bold font weight.

    ```html
    <!DOCTYPE html><html><head><title>strong Tag</title><style>body {text-align:center;}h1 {color:green;}.gfg {font-weight:bold;}</style></head><body><h1>GeeksforGeeks</h1><h2>font-weight: bold;</h2><div class = "gfg">Welcome to geeksforGeeks!</div></body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/strong2.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
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
            tagName="strong",
        )


class Style(BaseElement):
    """
    The <style> tag in HTML helps us to modify our text, viewed in the page. This modification includes changing font size, font family, font color etc. Not only the texts but also we can change the style of a body or part of a page. Now let’s look at various attributes of style and what else the tag supports.

    `Syntax:`



    <tagname style="property:value;">

    * The tagname includes [<p>](https://www.geeksforgeeks.org/html-paragraph/), [<body>](https://www.geeksforgeeks.org/html-body-tag/), from [<h1>](https://www.geeksforgeeks.org/html-heading/) to [<h6>](https://www.geeksforgeeks.org/html-heading/) etc.
    * The property is borrowed from CSS like color, font-size, font-family etc.
    * The value is also borrowed from CSS.

    `1. HTML Font Family:` The [font family](https://www.geeksforgeeks.org/css-font-family-property/) changes the font style of a text and can be used in any text writing tag like <p> or heading tag. These font families include all the names that you find in Microsoft Office or any other writing-based software.



    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Family</title></head> <body><h1 style="font-family:commanders;">Hello GeeksforGeeks.</h1><h2 style="font-family:Chaparral Pro Light;">Hello GeeksforGeeks.</h2><h3 style="font-family:algerian;">Hello GeeksforGeeks.</h3><p style="font-family:Castellar;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/ff.jpg)

    `2. HTML Font Size:` The [font size](https://www.geeksforgeeks.org/css-font-size-property/) changes the size of a text and this can also be used in any text writing tag like <p> or heading tag. The units can be given in “%” or pixels or other units can also be included.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Size</title></head> <body><h1 style="font-size:80%;">Hello GeeksforGeeks.</h1><h2 style="font-size:150%;">Hello GeeksforGeeks.</h2><h3 style="font-size:20px;">Hello GeeksforGeeks.</h3><p style="font-size:30px;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/fs.jpg)

    `3. HTML Font Color:` The font color tag changes the color of a text and can be used in any text writing tag like <p> or heading tag. We can use both name of the colors or also the color codes that is mainly used in Photoshop. For various color codes or to pick from various color ranges refer [HTML Color Codes](http://htmlcolorcodes.com/).

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Color</title></head> <body><h1 style="color:red;">Hello GeeksforGeeks.</h1><h2 style="color:#8CCEF9;">Hello GeeksforGeeks.</h2><h3 style="color:green;">Hello GeeksforGeeks.</h3><p style="color:#810CA6;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/fc.jpg)

    `4. HTML Text Align:` The [text alignment](https://www.geeksforgeeks.org/how-to-align-text-in-html/) tag is used to change the alignment of a text including centre, left or right alignment.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Text Align</title></head> <body><h1 style="text-align:left;">Hello GeeksforGeeks.</h1><h2 style="text-align:center;">Hello GeeksforGeeks.</h2><p style="text-align:right;">Hello GeeksforGeeks.</h2></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/ta.jpg)

    `5. HTML Background Color:` Using this attribute we can change the color of the background page or web page. This attribute is used along with the body tag to change the whole color of the body. It can also be used along with the text tags to change the text block’s color.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set background color</title></head> <body style="background-color:#616A6B;"><h1 style="font-family:commanders;background-color:yellow;">Hello GeeksforGeeks.</h1><h2 style="font-family:algerian;background-color:cyan;">Hello GeeksforGeeks.</h2><p style="font-family:Castellar;background-color:green;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/bc.jpg)

    Now we also learn a new thing that within a single <style> tag we can add various attributes by using a semicolon as shown in the previous example.

    `Application of Style Tag:`

    Since we have learned how to use the style attribute in providing the CSS properties to HTML elements, let’s see how to use them in CSS. CSS properties can be mentioned inside style tags which are inside the head tag. Each element can be provided unique properties by mentioning there unique tags like h1 or p and if there are more than one elements, we can assign each element with an unique id or class, to differentiate them from the rest.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>CSS</title> <!--CSS properties applied insidethis style tag--><style>body {background-color: #616A6B;} h1 {font-family: commanders;background-color: yellow;} h2 {font-family: algerian;background-color: cyan;} #first {font-family: Castellar;background-color: green;color: blue;} .second {text-align: right;background-color: white;font-size: 30px;color: red;}</style></head> <body><h1>Hello GeeksforGeeks.</h1><h2>Hello GeeksforGeeks.</h2><p id="first">Hello GeeksforGeeks.</p><p class="second">Welcome Geeks</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20221103160922/22.jpg)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari


    The <style> tag in HTML helps us to modify our text, viewed in the page. This modification includes changing font size, font family, font color etc. Not only the texts but also we can change the style of a body or part of a page. Now let’s look at various attributes of style and what else the tag supports.

    `Syntax:`



    <tagname style="property:value;">

    * The tagname includes [<p>](https://www.geeksforgeeks.org/html-paragraph/), [<body>](https://www.geeksforgeeks.org/html-body-tag/), from [<h1>](https://www.geeksforgeeks.org/html-heading/) to [<h6>](https://www.geeksforgeeks.org/html-heading/) etc.
    * The property is borrowed from CSS like color, font-size, font-family etc.
    * The value is also borrowed from CSS.

    `1. HTML Font Family:` The [font family](https://www.geeksforgeeks.org/css-font-family-property/) changes the font style of a text and can be used in any text writing tag like <p> or heading tag. These font families include all the names that you find in Microsoft Office or any other writing-based software.



    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Family</title></head> <body><h1 style="font-family:commanders;">Hello GeeksforGeeks.</h1><h2 style="font-family:Chaparral Pro Light;">Hello GeeksforGeeks.</h2><h3 style="font-family:algerian;">Hello GeeksforGeeks.</h3><p style="font-family:Castellar;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/ff.jpg)

    `2. HTML Font Size:` The [font size](https://www.geeksforgeeks.org/css-font-size-property/) changes the size of a text and this can also be used in any text writing tag like <p> or heading tag. The units can be given in “%” or pixels or other units can also be included.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Size</title></head> <body><h1 style="font-size:80%;">Hello GeeksforGeeks.</h1><h2 style="font-size:150%;">Hello GeeksforGeeks.</h2><h3 style="font-size:20px;">Hello GeeksforGeeks.</h3><p style="font-size:30px;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/fs.jpg)

    `3. HTML Font Color:` The font color tag changes the color of a text and can be used in any text writing tag like <p> or heading tag. We can use both name of the colors or also the color codes that is mainly used in Photoshop. For various color codes or to pick from various color ranges refer [HTML Color Codes](http://htmlcolorcodes.com/).

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Font Color</title></head> <body><h1 style="color:red;">Hello GeeksforGeeks.</h1><h2 style="color:#8CCEF9;">Hello GeeksforGeeks.</h2><h3 style="color:green;">Hello GeeksforGeeks.</h3><p style="color:#810CA6;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/fc.jpg)

    `4. HTML Text Align:` The [text alignment](https://www.geeksforgeeks.org/how-to-align-text-in-html/) tag is used to change the alignment of a text including centre, left or right alignment.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set Text Align</title></head> <body><h1 style="text-align:left;">Hello GeeksforGeeks.</h1><h2 style="text-align:center;">Hello GeeksforGeeks.</h2><p style="text-align:right;">Hello GeeksforGeeks.</h2></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/ta.jpg)

    `5. HTML Background Color:` Using this attribute we can change the color of the background page or web page. This attribute is used along with the body tag to change the whole color of the body. It can also be used along with the text tags to change the text block’s color.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>HTML Style Tag | Set background color</title></head> <body style="background-color:#616A6B;"><h1 style="font-family:commanders;background-color:yellow;">Hello GeeksforGeeks.</h1><h2 style="font-family:algerian;background-color:cyan;">Hello GeeksforGeeks.</h2><p style="font-family:Castellar;background-color:green;">Hello GeeksforGeeks.</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/bc.jpg)

    Now we also learn a new thing that within a single <style> tag we can add various attributes by using a semicolon as shown in the previous example.

    `Application of Style Tag:`

    Since we have learned how to use the style attribute in providing the CSS properties to HTML elements, let’s see how to use them in CSS. CSS properties can be mentioned inside style tags which are inside the head tag. Each element can be provided unique properties by mentioning there unique tags like h1 or p and if there are more than one elements, we can assign each element with an unique id or class, to differentiate them from the rest.

    `Example:`

    ```html
    <!DOCTYPE html><html> <head><title>CSS</title> <!--CSS properties applied insidethis style tag--><style>body {background-color: #616A6B;} h1 {font-family: commanders;background-color: yellow;} h2 {font-family: algerian;background-color: cyan;} #first {font-family: Castellar;background-color: green;color: blue;} .second {text-align: right;background-color: white;font-size: 30px;color: red;}</style></head> <body><h1>Hello GeeksforGeeks.</h1><h2>Hello GeeksforGeeks.</h2><p id="first">Hello GeeksforGeeks.</p><p class="second">Welcome Geeks</p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20221103160922/22.jpg)

    `Supported Browsers:`

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
            tagName="style",
        )


class Sub(BaseElement):
    """ """

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
            tagName="sub",
        )


class Sup(BaseElement):
    """ """

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
            tagName="sup",
        )


class Summary(BaseElement):
    """
    The <summary> tag in HTML is used to define a summary for the <details> element.

    * The <summary> element is used along with the <details> element and provides a summary visible to the user.
    * When the summary is clicked by the user, the content placed inside the <details> element becomes visible which was previously hidden.
    * The <summary> tag was added in HTML 5.
    * The <summary> tag requires both starting and ending tag.

    `Note:` The <summary> element should be the first child element of the <details> element.

    `Syntax:`



    <summary> Content </summary>

    Below program illustrates the <summary> element:
    `Input :`


    ```html
    <!DOCTYPE html><html><body> <details><!-- html summary tag is used here --><summary>GeeksforGeeks.</summary>   <p> It is a portal for geeks.</p>   </details> </body></html> |

    `Output :`


    <https://media.geeksforgeeks.org/wp-content/uploads/summary-tag-1.mp4>`Supported Browsers:`

    * Google Chrome 12.0 and above
    * Edge 79 and above
    * Firefox 49.0 and above
    * Opera 15.0 and above
    * Safari 8.0 and above
    * Internet Explorer not supported



    The <summary> tag in HTML is used to define a summary for the <details> element.

    * The <summary> element is used along with the <details> element and provides a summary visible to the user.
    * When the summary is clicked by the user, the content placed inside the <details> element becomes visible which was previously hidden.
    * The <summary> tag was added in HTML 5.
    * The <summary> tag requires both starting and ending tag.

    `Note:` The <summary> element should be the first child element of the <details> element.

    `Syntax:`



    <summary> Content </summary>

    Below program illustrates the <summary> element:
    `Input :`


    ```html
    <!DOCTYPE html><html><body> <details><!-- html summary tag is used here --><summary>GeeksforGeeks.</summary>   <p> It is a portal for geeks.</p>   </details> </body></html> |

    `Output :`


    <https://media.geeksforgeeks.org/wp-content/uploads/summary-tag-1.mp4>`Supported Browsers:`

    * Google Chrome 12.0 and above
    * Edge 79 and above
    * Firefox 49.0 and above
    * Opera 15.0 and above
    * Safari 8.0 and above
    * Internet Explorer not supported





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
            tagName="summary",
        )


class Svg(BaseElement):
    """ """

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
            tagName="svg",
        )


class Table(BaseElement):
    """ """

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
            tagName="table",
        )


class Tbody(BaseElement):
    """
    The <tbody> tag in HTML is used to make a group of the same type of content of body element. This tag is used in HTML table with header and footer which is known as “thead” and “tfoot”. <tbody> tag is child tag of table tag and parent tag of <tr> and <td> tags.

    `Syntax:`



    <tbody> // Table contents   </tbody>

    `Attributes:` Some attributes are supported by <tbody> tag in HTML4.1 but not supported in HTML5. The list of attributes is given below:

    * [`align`](https://www.geeksforgeeks.org/html-tbody-align-attribute/)`:` Set the alignment of the content.
    * [`valign`](https://www.geeksforgeeks.org/html-tbody-valign-attribute/)`:` Set the vertical alignment of the content.
    * [`char`](https://www.geeksforgeeks.org/html-tbody-char-attribute/)`:` Set the alignment of content inside <thead> tag to a character.
    * [`charoff`](https://www.geeksforgeeks.org/html-tbody-charoff-attribute/)`:` It is used to set the characters the content inside the <thead> tag aligned from the character specified by the char attribute.

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>tbody Tag</h2><table><thead><tr><th>Name</th><th>User Id</th></tr></thead> <!-- tbody tag starts from here --><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody><!-- tbody tag ends here --></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625185357/tbo.png)

    `Supported Browsers:`

    * Google Chrome 1+
    * Internet Explorer
    * Firefox 1+
    * Opera
    * Safari
    * Edge 12+


    The <tbody> tag in HTML is used to make a group of the same type of content of body element. This tag is used in HTML table with header and footer which is known as “thead” and “tfoot”. <tbody> tag is child tag of table tag and parent tag of <tr> and <td> tags.

    `Syntax:`



    <tbody> // Table contents   </tbody>

    `Attributes:` Some attributes are supported by <tbody> tag in HTML4.1 but not supported in HTML5. The list of attributes is given below:

    * [`align`](https://www.geeksforgeeks.org/html-tbody-align-attribute/)`:` Set the alignment of the content.
    * [`valign`](https://www.geeksforgeeks.org/html-tbody-valign-attribute/)`:` Set the vertical alignment of the content.
    * [`char`](https://www.geeksforgeeks.org/html-tbody-char-attribute/)`:` Set the alignment of content inside <thead> tag to a character.
    * [`charoff`](https://www.geeksforgeeks.org/html-tbody-charoff-attribute/)`:` It is used to set the characters the content inside the <thead> tag aligned from the character specified by the char attribute.

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>tbody Tag</h2><table><thead><tr><th>Name</th><th>User Id</th></tr></thead> <!-- tbody tag starts from here --><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody><!-- tbody tag ends here --></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625185357/tbo.png)

    `Supported Browsers:`

    * Google Chrome 1+
    * Internet Explorer
    * Firefox 1+
    * Opera
    * Safari
    * Edge 12+




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
            tagName="tbody",
        )


class Td(BaseElement):
    """
    The `<td> tag` is used to define a standard cell in an HTML table.

    `Syntax:`



    <td>........</td>

    `Types of cells:`

    * `Header cells`: contains header information(<th>)
    * `Standard cells:` contains data(<td>)

    The text in `<th>` elements are bold and centered for heading by default.
    The text in `<td>` elements are regular and left-aligned for data by default.

    `Attributes:` There are many attributes supported by HTML4.1 but removed from HTML5 are listed below:

    * `abbr:` This attribute is used as abbreviated version of the text content in a header cell.
    * `align:` Set the alignment the text content.
    * `axis:` Categorizes header cells.
    * `bgcolor:` Set the background color of a header cell.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes are in numeric form.
    * `colspan:` Number of columns a header cell should span.
    * `headers:` Specifies multiple header cells a cell is related to.
    * `height:` Set the height of a header cell.
    * `nowrap:` It specifies that the content inside a header cell should not wrap.
    * `rowspan:` Set the number of rows a header cell should span.
    * `scope:` It is used to specify the score of header content.
    * `sorted:` It is used to sort the direction of a column.
    * `valign:` It is used to set the vertical alignment of text content.
    * `width:` It is used to set the width of a header cell

    `Example:`


    ```html
    <!DOCTYPE html><html><head><title>td tag</title><style>body {text-align:center;}h1 {color:green;}th {color:blue;}table, tbody, td {border: 1px solid black;border-collapse: collapse;}</style></head><body><center><h1>GeeksforGeeks</h1><h2>td Tag</h2><table><thead><tr><th>Name</th><th>User Id</th></tr></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190913124521/td.png)

    `Supported Browsers:` The browser supported by `td tag` are listed below

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera


    The `<td> tag` is used to define a standard cell in an HTML table.

    `Syntax:`



    <td>........</td>

    `Types of cells:`

    * `Header cells`: contains header information(<th>)
    * `Standard cells:` contains data(<td>)

    The text in `<th>` elements are bold and centered for heading by default.
    The text in `<td>` elements are regular and left-aligned for data by default.

    `Attributes:` There are many attributes supported by HTML4.1 but removed from HTML5 are listed below:

    * `abbr:` This attribute is used as abbreviated version of the text content in a header cell.
    * `align:` Set the alignment the text content.
    * `axis:` Categorizes header cells.
    * `bgcolor:` Set the background color of a header cell.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes are in numeric form.
    * `colspan:` Number of columns a header cell should span.
    * `headers:` Specifies multiple header cells a cell is related to.
    * `height:` Set the height of a header cell.
    * `nowrap:` It specifies that the content inside a header cell should not wrap.
    * `rowspan:` Set the number of rows a header cell should span.
    * `scope:` It is used to specify the score of header content.
    * `sorted:` It is used to sort the direction of a column.
    * `valign:` It is used to set the vertical alignment of text content.
    * `width:` It is used to set the width of a header cell

    `Example:`


    ```html
    <!DOCTYPE html><html><head><title>td tag</title><style>body {text-align:center;}h1 {color:green;}th {color:blue;}table, tbody, td {border: 1px solid black;border-collapse: collapse;}</style></head><body><center><h1>GeeksforGeeks</h1><h2>td Tag</h2><table><thead><tr><th>Name</th><th>User Id</th></tr></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190913124521/td.png)

    `Supported Browsers:` The browser supported by `td tag` are listed below

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera




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
            tagName="td",
        )


class Template(BaseElement):
    """
    The `<template> tag` in HTML is used to store the HTML code fragments, which can be cloned and inserted in an HTML document. The content of the tag is hidden from clients being stored on the client-side. It is inserted until activated using JavaScript. Use JavaScript to get the content from a template, and add it to the web page.

    `Syntax:`



    <template> Contents </template>

    `Note:` The <template> tag is new in HTML 5.

    `Attributes:` This tag supports the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) in HTML.

    `Example 1:` In this example, we have an unordered list of the courses that we have hidden to display using the <template> tag in HTML.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Content inside a template tag willbe hidden from the client.</p>    <!-- Html script tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><h4>GeeksforGeeks Offline Courses</h4><ul><li>DSA</li><li>Placement & Interview Preparation</li><li>Web Development</li><li>Algorithms & basic programming</li></ul></template><!-- Html template tag ends here --> <p>End of the example of template tag</p> </body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922103742/1.jpg)HTML template tag

    `Example 2:` This example uses a template tag, and it hides the content within the template tag.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Content inside a template tagis hidden from the client.</p>    <!-- html script tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20210922100958/gfg3-300x300.png>">Content Writer:<input type="text"placeholder="author name"></template><!-- html template tag ends here -->  <p>End of the example of template tag</p>   </body></html> |

    ```
    `Output:`

    ![template1](https://media.geeksforgeeks.org/wp-content/uploads/20190311164616/template11.png)HTML template tag

    `Example 3:` This example illustrates the uses of JavaScript to display the template tag content.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Click the button to get the content from a template,and display it in the web page.</p>   <button onclick="myGeeks()"> Show content </button> <!-- Html template tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20210922100958/gfg3-300x300.png>"><br>Content Writer:<input type="text"placeholder="author name"></template><!-- Html template tag ends here --> <!-- Script to display the content of template tag --><script>function myGeeks() {var t = document.getElementsByTagName("template")[0];var clone = t.content.cloneNode(true);document.body.appendChild(clone);}</script></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922101615/20210922101437.gif)HTML template tag

    `Supported Browsers:`

    * Google Chrome 26.0 & above
    * Microsoft Edge 13.0 & above
    * Firefox 22.0 & above
    * Safari 8.0 & above
    * Opera 15.0 & above


    The `<template> tag` in HTML is used to store the HTML code fragments, which can be cloned and inserted in an HTML document. The content of the tag is hidden from clients being stored on the client-side. It is inserted until activated using JavaScript. Use JavaScript to get the content from a template, and add it to the web page.

    `Syntax:`



    <template> Contents </template>

    `Note:` The <template> tag is new in HTML 5.

    `Attributes:` This tag supports the [global attributes](https://www.geeksforgeeks.org/html-global-attributes/) in HTML.

    `Example 1:` In this example, we have an unordered list of the courses that we have hidden to display using the <template> tag in HTML.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Content inside a template tag willbe hidden from the client.</p>    <!-- Html script tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><h4>GeeksforGeeks Offline Courses</h4><ul><li>DSA</li><li>Placement & Interview Preparation</li><li>Web Development</li><li>Algorithms & basic programming</li></ul></template><!-- Html template tag ends here --> <p>End of the example of template tag</p> </body></html> |

      ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922103742/1.jpg)HTML template tag

    `Example 2:` This example uses a template tag, and it hides the content within the template tag.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Content inside a template tagis hidden from the client.</p>    <!-- html script tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20210922100958/gfg3-300x300.png>">Content Writer:<input type="text"placeholder="author name"></template><!-- html template tag ends here -->  <p>End of the example of template tag</p>   </body></html> |

    ```
    `Output:`

    ![template1](https://media.geeksforgeeks.org/wp-content/uploads/20190311164616/template11.png)HTML template tag

    `Example 3:` This example illustrates the uses of JavaScript to display the template tag content.

    ```html
    <!DOCTYPE html><html><body><h1>GeeksforGeeks</h1><h3>HTML template tag</h3> <p>Click the button to get the content from a template,and display it in the web page.</p>   <button onclick="myGeeks()"> Show content </button> <!-- Html template tag starts here --><template><h2>GeeksforGeeks: A computer science portal</h2><img src="<https://media.geeksforgeeks.org/wp-content/uploads/20210922100958/gfg3-300x300.png>"><br>Content Writer:<input type="text"placeholder="author name"></template><!-- Html template tag ends here --> <!-- Script to display the content of template tag --><script>function myGeeks() {var t = document.getElementsByTagName("template")[0];var clone = t.content.cloneNode(true);document.body.appendChild(clone);}</script></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210922101615/20210922101437.gif)HTML template tag

    `Supported Browsers:`

    * Google Chrome 26.0 & above
    * Microsoft Edge 13.0 & above
    * Firefox 22.0 & above
    * Safari 8.0 & above
    * Opera 15.0 & above




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
            tagName="template",
        )


class Tfoot(BaseElement):
    """
      The <tfoot> tag in HTML is used to give footer group of content. This tag is used in HTML table with header and body which is known as “thead” and “tbody”. <tfoot> tag is child tag of table and parent tag of <tr> and <td>.

    `Syntax:`



    <tfoot> // Table footer contents... </tfoot>

    `Attributes:` The <tfoot> tag contains many attributes which are supported by HTML4.1 but not supported by HTML5.

    * [`align`](https://www.geeksforgeeks.org/html-tfoot-align-attribute/)`:` Set the alignment of the text content.
    * [`valign`](https://www.geeksforgeeks.org/html-tfoot-valign-attribute/)`:` It is used to set the vertical alignment of text content.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><center><h1>GeeksforGeeks</h1><h2>tfoot Tag</h2><table ><thead><tr><th>Name</th><th>User Id</th></tr></thead><tbody><tr><td>Ram</td><td>@ram_b</td></tr><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>Rahman</td><td>@rahamD</td></tr></tbody> <!-- tfoot tag starts from here --><tfoot><tr><td>Total user</td><td>4</td></tr></tfoot><!-- tfoot tag ends here --> </table></center></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625190013/tfoot.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera


      The <tfoot> tag in HTML is used to give footer group of content. This tag is used in HTML table with header and body which is known as “thead” and “tbody”. <tfoot> tag is child tag of table and parent tag of <tr> and <td>.

    `Syntax:`



    <tfoot> // Table footer contents... </tfoot>

    `Attributes:` The <tfoot> tag contains many attributes which are supported by HTML4.1 but not supported by HTML5.

    * [`align`](https://www.geeksforgeeks.org/html-tfoot-align-attribute/)`:` Set the alignment of the text content.
    * [`valign`](https://www.geeksforgeeks.org/html-tfoot-valign-attribute/)`:` It is used to set the vertical alignment of text content.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><center><h1>GeeksforGeeks</h1><h2>tfoot Tag</h2><table ><thead><tr><th>Name</th><th>User Id</th></tr></thead><tbody><tr><td>Ram</td><td>@ram_b</td></tr><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>Rahman</td><td>@rahamD</td></tr></tbody> <!-- tfoot tag starts from here --><tfoot><tr><td>Total user</td><td>4</td></tr></tfoot><!-- tfoot tag ends here --> </table></center></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210625190013/tfoot.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Safari
    * Opera




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
            tagName="tfoot",
        )


class Th(BaseElement):
    """
    The <th> tag in HTML is used to set the header cell of a table. Two types of cells in the HTML table.

    * `Header Cell:` It is used to hold the header information.
    * `Standard Cell:` It is used to hold the body of data.

    The working of both tags (<th> and <td>) are the same, but the text properties are different. In <th> text is bold and centered, and in <td> text is regular and left align by default.

    `Syntax:`



    <th> Contents... </th>

    `Attributes:` There are many attributes supported by HTML5 are listed below:

    * [`abbr`](https://www.geeksforgeeks.org/html-th-abbr-attribute/)`:` This attribute is used as an abbreviated version of the text content in a header cell.
    * [`colspan`](https://www.geeksforgeeks.org/html-th-colspan-attribute/)`:` Number of columns a header cell should span.
    * [`headers`](https://www.geeksforgeeks.org/html-th-headers-attribute/)`:` Specifies one or more header cells a cell is related to.
    * [`rowspan`](https://www.geeksforgeeks.org/html-th-rowspan-attribute/)`:` Set the number of rows a header cell should span.
    * [`scope`](https://www.geeksforgeeks.org/html-th-scope-attribute/)`:` It is used to specify the score of header content.

    `Attributes:` There are many attributes supported by HTML4.1 but removed from HTML5 are listed below:

    * [`align:`](https://www.geeksforgeeks.org/html-th-align-attribute/) Set the alignment of the text content.
    * [`axis`](https://www.geeksforgeeks.org/html-th-axis-attribute/)`:` Categories header cells.
    * [`bgcolor:`](https://www.geeksforgeeks.org/html-th-bgcolor-attribute/) Set the background color of a header cell.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.
    * [`height:`](https://www.geeksforgeeks.org/html-th-height-attribute/) Set the height of a header cell.
    * [`valign:`](https://www.geeksforgeeks.org/html-th-valign-attribute/) It is used to set the vertical alignment of text content.
    * [`width:`](https://www.geeksforgeeks.org/html-th-width-attribute/) It is used to set the width of a header cell

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>th Tag</h2><table><thead><tr><!-- th tag starts here --><th>Name</th><th>User Id</th><!-- th tag end here --></tr></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701164501/th.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera


    The <th> tag in HTML is used to set the header cell of a table. Two types of cells in the HTML table.

    * `Header Cell:` It is used to hold the header information.
    * `Standard Cell:` It is used to hold the body of data.

    The working of both tags (<th> and <td>) are the same, but the text properties are different. In <th> text is bold and centered, and in <td> text is regular and left align by default.

    `Syntax:`



    <th> Contents... </th>

    `Attributes:` There are many attributes supported by HTML5 are listed below:

    * [`abbr`](https://www.geeksforgeeks.org/html-th-abbr-attribute/)`:` This attribute is used as an abbreviated version of the text content in a header cell.
    * [`colspan`](https://www.geeksforgeeks.org/html-th-colspan-attribute/)`:` Number of columns a header cell should span.
    * [`headers`](https://www.geeksforgeeks.org/html-th-headers-attribute/)`:` Specifies one or more header cells a cell is related to.
    * [`rowspan`](https://www.geeksforgeeks.org/html-th-rowspan-attribute/)`:` Set the number of rows a header cell should span.
    * [`scope`](https://www.geeksforgeeks.org/html-th-scope-attribute/)`:` It is used to specify the score of header content.

    `Attributes:` There are many attributes supported by HTML4.1 but removed from HTML5 are listed below:

    * [`align:`](https://www.geeksforgeeks.org/html-th-align-attribute/) Set the alignment of the text content.
    * [`axis`](https://www.geeksforgeeks.org/html-th-axis-attribute/)`:` Categories header cells.
    * [`bgcolor:`](https://www.geeksforgeeks.org/html-th-bgcolor-attribute/) Set the background color of a header cell.
    * `char:` Aligns the content in a header cell to a character.
    * `charoff:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.
    * [`height:`](https://www.geeksforgeeks.org/html-th-height-attribute/) Set the height of a header cell.
    * [`valign:`](https://www.geeksforgeeks.org/html-th-valign-attribute/) It is used to set the vertical alignment of text content.
    * [`width:`](https://www.geeksforgeeks.org/html-th-width-attribute/) It is used to set the width of a header cell

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>th Tag</h2><table><thead><tr><!-- th tag starts here --><th>Name</th><th>User Id</th><!-- th tag end here --></tr></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701164501/th.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera




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
            tagName="th",
        )


class Thead(BaseElement):
    """
    The <thead> tag in HTML is used to give a header to the group of content of the body. This tag is used in HTML tables as head and body which is known as `thead` and `tbody`.

    `Syntax:`



    <thead>
    // Table head Contents...
    </thead>

    `Attributes:`

    * [`align`](https://www.geeksforgeeks.org/html-thead-align-attribute/)`:` Set the alignment of the text content.
    * [`valign`](https://www.geeksforgeeks.org/html-thead-valign-attribute/)`:` Set the vertical alignment of the text content.
    * [`char`](https://www.geeksforgeeks.org/html-thead-char-attribute/)`:` Set the alignment of content inside the <thead> element to a character.
    * [`charoff`](https://www.geeksforgeeks.org/html-thead-charoff-attribute/)`:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>thead Tag</h2><table> <!-- thead tag starts from here --><thead><tr><th>Name</th><th>User Id</th></tr></thead><!-- thead tag ends here --> <tbody><tr><td>Ram</td><td>@ram_b</td></tr><tr><td>Shashank</td><td>@shashankla</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701164945/thead.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera


    The <thead> tag in HTML is used to give a header to the group of content of the body. This tag is used in HTML tables as head and body which is known as `thead` and `tbody`.

    `Syntax:`



    <thead>
    // Table head Contents...
    </thead>

    `Attributes:`

    * [`align`](https://www.geeksforgeeks.org/html-thead-align-attribute/)`:` Set the alignment of the text content.
    * [`valign`](https://www.geeksforgeeks.org/html-thead-valign-attribute/)`:` Set the vertical alignment of the text content.
    * [`char`](https://www.geeksforgeeks.org/html-thead-char-attribute/)`:` Set the alignment of content inside the <thead> element to a character.
    * [`charoff`](https://www.geeksforgeeks.org/html-thead-charoff-attribute/)`:` It is used to sets the number of characters that will be aligned from the character specified by the char attribute. The value of these attributes is in numeric form.

    `Example:`

    ```html
    <!DOCTYPE html><html><body><center><h1>GeeksforGeeks</h1><h2>thead Tag</h2><table> <!-- thead tag starts from here --><thead><tr><th>Name</th><th>User Id</th></tr></thead><!-- thead tag ends here --> <tbody><tr><td>Ram</td><td>@ram_b</td></tr><tr><td>Shashank</td><td>@shashankla</td></tr></tbody></table></center></body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701164945/thead.png)

    `Supported Browsers:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Firefox 1 and above
    * Internet Explorer
    * Safari
    * Opera




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
            tagName="thead",
        )


class Time(BaseElement):
    """
    The <time> tag is used to display the human-readable date/time. It can also be used to encode dates and times in a machine-readable form. The main advantage for users is that they can offer to add birthday reminders or scheduled events to their calendars and search engines can produce smarter search results.

    `Syntax:`



    <time attribute> Time... </time>

    `Attributes:` This tag contains an optional attribute [*datetime*](https://www.geeksforgeeks.org/html-time-datetime-attribute/) which is used to define the date/time in a machine-readable form of the <time> element.



    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><time> Tag</h2> <p>I Wake up at <time>6.00</time>in every morning.</p> <p>Jawahar lal Nehru birthday is celebratedon <time datetime="2018--11-14 12:00">children's day.</time></p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701165439/timen.png)

    `Supported Browsers:`

    * Google Chrome 62.0 and above
    * Edge 18.0 and above
    * Internet Explorer not supported
    * Firefox 22.0 and above
    * Opera 49.0 and above
    * Safari 7.0 and above
    The <time> tag is used to display the human-readable date/time. It can also be used to encode dates and times in a machine-readable form. The main advantage for users is that they can offer to add birthday reminders or scheduled events to their calendars and search engines can produce smarter search results.

    `Syntax:`



    <time attribute> Time... </time>

    `Attributes:` This tag contains an optional attribute [*datetime*](https://www.geeksforgeeks.org/html-time-datetime-attribute/) which is used to define the date/time in a machine-readable form of the <time> element.



    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><time> Tag</h2> <p>I Wake up at <time>6.00</time>in every morning.</p> <p>Jawahar lal Nehru birthday is celebratedon <time datetime="2018--11-14 12:00">children's day.</time></p></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701165439/timen.png)

    `Supported Browsers:`

    * Google Chrome 62.0 and above
    * Edge 18.0 and above
    * Internet Explorer not supported
    * Firefox 22.0 and above
    * Opera 49.0 and above
    * Safari 7.0 and above


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
            tagName="time",
        )


class Title(BaseElement):
    """
    The <title> tag in HTML is used to define the title of HTML document. It sets the title in the browser toolbar. It provides the title for the web page when it is added to favorites. It displays the title for the page in search engine results.

    `Note:` You can NOT have more than one <title> element in an HTML document.

    `Syntax:`



    <title> Title name </title>

    `Example:`

    ```html
    <!DOCTYPE html><html><head><title>title Tag</title></head><body><h1>GeeksforGeeks</h1><h2><title> Tag</h2>   <p>Welcome to GeeksforGeeks!</p>   </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701183208/title.png)

    `Supported Browser:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer 1 and above
    * Firefox 1 and above
    * Opera
    * Safari 1 and above
    The <title> tag in HTML is used to define the title of HTML document. It sets the title in the browser toolbar. It provides the title for the web page when it is added to favorites. It displays the title for the page in search engine results.

    `Note:` You can NOT have more than one <title> element in an HTML document.

    `Syntax:`



    <title> Title name </title>

    `Example:`

    ```html
    <!DOCTYPE html><html><head><title>title Tag</title></head><body><h1>GeeksforGeeks</h1><h2><title> Tag</h2>   <p>Welcome to GeeksforGeeks!</p>   </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701183208/title.png)

    `Supported Browser:`

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer 1 and above
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
            tagName="title",
        )


class Tr(BaseElement):
    """
    The `<tr> tag` is used to define a row in an HTML table. The `<tr>` element contains multiple <th> or <td> elements.

    `Syntax:`



    <tr>.....</tr>

    `Attributes:`

    * `align:` Align the content.
    * `bgcolor:` Specify background of row
    * `char:` Align the content to a character
    * `charoff:` Set the number of character
    * `valign:` Vertical align the content

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>tr tag</title><style>body {text-align: center;} h1 {color: green;} th {color: blue;} table,tbody,td {border: 1px solid black;border-collapse: collapse;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>tr Tag</h2><table><thead><!-- tr tag starts here --><tr><th>Name</th><th>User Id</th></tr><!-- tr tag end here --></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190913121025/tr7.png)

    `Supported Browsers:` The browsers supported by `HTML <tr> Tag` are listed below:

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Apple Safari
    * Opera


    The `<tr> tag` is used to define a row in an HTML table. The `<tr>` element contains multiple <th> or <td> elements.

    `Syntax:`



    <tr>.....</tr>

    `Attributes:`

    * `align:` Align the content.
    * `bgcolor:` Specify background of row
    * `char:` Align the content to a character
    * `charoff:` Set the number of character
    * `valign:` Vertical align the content

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>tr tag</title><style>body {text-align: center;} h1 {color: green;} th {color: blue;} table,tbody,td {border: 1px solid black;border-collapse: collapse;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>tr Tag</h2><table><thead><!-- tr tag starts here --><tr><th>Name</th><th>User Id</th></tr><!-- tr tag end here --></thead><tbody><tr><td>Shashank</td><td>@shashankla</td></tr><tr><td>GeeksforGeeks</td><td>@geeks</td></tr></tbody></table></center></body> </html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190913121025/tr7.png)

    `Supported Browsers:` The browsers supported by `HTML <tr> Tag` are listed below:

    * Google Chrome 1 and above
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Apple Safari
    * Opera




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
            tagName="tr",
        )


class Track(BaseElement):
    """
    The `<track> tag` specifies text tracks for media components audio and video This part is employed to specify subtitles, caption files or different files containing text, that ought to be visible once the media is taking part in.

    `Syntax:`



    <track Attribute>

    `Attribute:`

    * `default:` Specifies to that track to enabled if the user want to change the track
    * `kind:` Specifies the kind of text track
    * `label:` the title of the text track
    * `src:` It is for URL of the track file
    * `srclang:` It tell the language of the track text data (required if kind=”subtitles”)

    `Example:`


    ```html
    <html> <head></head> <body style="text-align: center"><h1 style="color: green">GeeksforGeeks</h1><h2>HTML Track srclang Attribute</h2> <video width="600" height="400" controls> <track src="CSS-animation-duration02.mp4"id="myTrack1"kind="subtitles"srclang="en"label="English"> <source id="myTrack"src="CSS-animation-duration02.mp4"type="video/mp4"></video></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190610143516/track-srclang.png)

    `Supported Browsers:` The browsers supported by `HTML <track> tag` are listed below:

    * Google Chrome 23
    * Edge 12
    * Internet Explorer 10
    * Firefox 31
    * Apple Safari 6
    * Opera 12.1
    The `<track> tag` specifies text tracks for media components audio and video This part is employed to specify subtitles, caption files or different files containing text, that ought to be visible once the media is taking part in.

    `Syntax:`



    <track Attribute>

    `Attribute:`

    * `default:` Specifies to that track to enabled if the user want to change the track
    * `kind:` Specifies the kind of text track
    * `label:` the title of the text track
    * `src:` It is for URL of the track file
    * `srclang:` It tell the language of the track text data (required if kind=”subtitles”)

    `Example:`


    ```html
    <html> <head></head> <body style="text-align: center"><h1 style="color: green">GeeksforGeeks</h1><h2>HTML Track srclang Attribute</h2> <video width="600" height="400" controls> <track src="CSS-animation-duration02.mp4"id="myTrack1"kind="subtitles"srclang="en"label="English"> <source id="myTrack"src="CSS-animation-duration02.mp4"type="video/mp4"></video></body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190610143516/track-srclang.png)

    `Supported Browsers:` The browsers supported by `HTML <track> tag` are listed below:

    * Google Chrome 23
    * Edge 12
    * Internet Explorer 10
    * Firefox 31
    * Apple Safari 6
    * Opera 12.1


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
            tagName="track",
        )


class Tt(BaseElement):
    """
    The <tt> tag is the abbreviation of teletype text. This tag is depreciated from HTML 5. It was used for marking Keyboard input. It was mainly used for formatting purposes. This tag was used in HTML 4 (Not Supported in HTML5).
    `Syntax:`



    <tt> Contents... </tt>

    `Example:` The below example illustrates the <tt> tag in HTML:

    ```html
    <html><body><h1>GeeksforGeeks</h1><h2>tt Tag</h2> <!-- HTML tt Tag is used here--><tt>GfG stands for GeeksforGeeks</tt> <p><tt>It is a computer science portal for geeks</tt></p> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701220408/ttupdate.JPG)

    `Supported Browsers:`

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Opera
    * Safari
    The <tt> tag is the abbreviation of teletype text. This tag is depreciated from HTML 5. It was used for marking Keyboard input. It was mainly used for formatting purposes. This tag was used in HTML 4 (Not Supported in HTML5).
    `Syntax:`



    <tt> Contents... </tt>

    `Example:` The below example illustrates the <tt> tag in HTML:

    ```html
    <html><body><h1>GeeksforGeeks</h1><h2>tt Tag</h2> <!-- HTML tt Tag is used here--><tt>GfG stands for GeeksforGeeks</tt> <p><tt>It is a computer science portal for geeks</tt></p> </body></html> |

    ```
    `Output:`

    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701220408/ttupdate.JPG)

    `Supported Browsers:`

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
            tagName="tt",
        )


class U(BaseElement):
    """
    The <u> tag in HTML stands for underline, and it’s used to underline the text enclosed within the <u> tag. This tag is generally used to underline misspelled words. This tag requires a starting as well as ending tag.

    `Syntax:`



    <u> Contents... </u>

    `Note:` This tag is depreciated from HTML 4.1 and redefined in HTML 5 using CSS text-decoration property instead.
    Below examples illustrates the <u> tag in HTML:
    `Example 1:`

    ```html
    <html> <body><h1>GeeksforGeeks</h1><h2><u> Tag</h2>  <p>GeeksforGeeks: A <u>computer science</u>portal for geeks</p>  </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702122128/u.png)

    `Example 2:` Alternate way of <u> tag to underline the text.

    ```html
    <html><head><title>u Tag</title><style>body {text-align:center;}.gfg {font-size:40px;font-weight:bold;color:green;}.geeks {font-size:25px;font-weight:bold;}p {font-size:20px;}span {text-decoration:underline;}</style></head><body><div class = "gfg">GeeksforGeeks</div><div class = "geeks"><u> Tag</div>  <p>GeeksforGeeks: A <span>computer science</span>portal for geeks</p>  </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/u-tag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari




    The <u> tag in HTML stands for underline, and it’s used to underline the text enclosed within the <u> tag. This tag is generally used to underline misspelled words. This tag requires a starting as well as ending tag.

    `Syntax:`



    <u> Contents... </u>

    `Note:` This tag is depreciated from HTML 4.1 and redefined in HTML 5 using CSS text-decoration property instead.
    Below examples illustrates the <u> tag in HTML:
    `Example 1:`

    ```html
    <html> <body><h1>GeeksforGeeks</h1><h2><u> Tag</h2>  <p>GeeksforGeeks: A <u>computer science</u>portal for geeks</p>  </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702122128/u.png)

    `Example 2:` Alternate way of <u> tag to underline the text.

    ```html
    <html><head><title>u Tag</title><style>body {text-align:center;}.gfg {font-size:40px;font-weight:bold;color:green;}.geeks {font-size:25px;font-weight:bold;}p {font-size:20px;}span {text-decoration:underline;}</style></head><body><div class = "gfg">GeeksforGeeks</div><div class = "geeks"><u> Tag</div>  <p>GeeksforGeeks: A <span>computer science</span>portal for geeks</p>  </body></html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/u-tag.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="u",
        )


class Var(BaseElement):
    """
    It is a phrase tag and used to specify the variable in a mathematical equation or in a computer program. The content of this tag is displayed in an italic format in most browsers.

    `Syntax:`



    <var> Contents... </var>

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksForGeeks</h1><h2><var> Tag</h2> <!-- HTML var Tag is used here--><var>GeeksforGeeks Variable</var> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701184711/var.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
    * Firefox 1 and above
    * Opera
    * Safari
    It is a phrase tag and used to specify the variable in a mathematical equation or in a computer program. The content of this tag is displayed in an italic format in most browsers.

    `Syntax:`



    <var> Contents... </var>

    `Example:`

    ```html
    <!DOCTYPE html><html> <body><h1>GeeksForGeeks</h1><h2><var> Tag</h2> <!-- HTML var Tag is used here--><var>GeeksforGeeks Variable</var> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210701184711/var.png)

    `Supported Browsers:`

    * Google Chrome
    * Edge 12 and above
    * Internet Explorer
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
            tagName="var",
        )


class Video(BaseElement):
    """ """

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
            tagName="video",
        )


class Wbr(BaseElement):
    """
    The <wbr> tag in HTML stands for word break opportunity and is used to define the position within the text which is treated as a line break by the browser. It is mostly used when the used word is too long and there are chances that the browser may break lines at the wrong place for fitting the text.
    `Syntax:`




    <wbr>

    `Note:` The <wbr> tag is new in HTML5 and it does not require end tag.
    Below examples illustrate the <wbr> tag in HTML 5:
    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><wbr> Tag</h2><!--  It is mostly used when the used word is too long andthere are chances that the browser may break lines atthe wrong place --> <p>GFGstandsforGeeksforGeeksanditis<wbr>acomputerscienceportalforgeeks.</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702115325/wbr.png)

    `Supported Browsers:`


    * Google Chrome 1
    * Edge 79.0
    * Firefox 1
    * Opera 11.6
    * Safari 4
    The <wbr> tag in HTML stands for word break opportunity and is used to define the position within the text which is treated as a line break by the browser. It is mostly used when the used word is too long and there are chances that the browser may break lines at the wrong place for fitting the text.
    `Syntax:`




    <wbr>

    `Note:` The <wbr> tag is new in HTML5 and it does not require end tag.
    Below examples illustrate the <wbr> tag in HTML 5:
    `Example 1:`


    ```html
    <!DOCTYPE html><html> <body><h1>GeeksforGeeks</h1><h2><wbr> Tag</h2><!--  It is mostly used when the used word is too long andthere are chances that the browser may break lines atthe wrong place --> <p>GFGstandsforGeeksforGeeksanditis<wbr>acomputerscienceportalforgeeks.</p> </body> </html> |

    ```
    `Output:`


    ![](https://media.geeksforgeeks.org/wp-content/uploads/20210702115325/wbr.png)

    `Supported Browsers:`


    * Google Chrome 1
    * Edge 79.0
    * Firefox 1
    * Opera 11.6
    * Safari 4


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
            tagName="wbr",
        )


class Xmp(BaseElement):
    """
    The `<xmp>` tag is used to create any content as letter format. Any text content between this <xmp> tag will display as the user type in the code section, same width, same position ending everything will be displayed as a replica of typed format or style.

    `Note:` It is not supported in html5.

    `Syntax:`



    <xmp> statement </xmp>

    `Attribute:` This tag does not contain any attribute.

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>HTML &lt;xmp&gt; Tag</title><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>HTML &lt;xmp&gt; tag</h2></center><xmp>HTML tags are hidden keywords and used to create web pages in different format.Most of the tags contain two parts, opening tags and closing tags.</xmp> </body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190827123607/xmp1.png)

    `Supported Browsers:` The browsers supported by `HTML <xmp> tag` are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera
    The `<xmp>` tag is used to create any content as letter format. Any text content between this <xmp> tag will display as the user type in the code section, same width, same position ending everything will be displayed as a replica of typed format or style.

    `Note:` It is not supported in html5.

    `Syntax:`



    <xmp> statement </xmp>

    `Attribute:` This tag does not contain any attribute.

    `Example:`


    ```html
    <!DOCTYPE html><html> <head><title>HTML &lt;xmp&gt; Tag</title><style>h1 {color: green;}</style></head> <body><center><h1>GeeksforGeeks</h1><h2>HTML &lt;xmp&gt; tag</h2></center><xmp>HTML tags are hidden keywords and used to create web pages in different format.Most of the tags contain two parts, opening tags and closing tags.</xmp> </body> </html> |

    ```
    `Output:`

      ![](https://media.geeksforgeeks.org/wp-content/uploads/20190827123607/xmp1.png)

    `Supported Browsers:` The browsers supported by `HTML <xmp> tag` are listed below:

    * Google Chrome
    * Internet Explorer
    * Firefox
    * Safari
    * Opera


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
            tagName="xmp",
        )


class Ol(BaseElement):
    """ """

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
            tagName="ol",
        )
