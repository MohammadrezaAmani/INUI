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

    def toHtml(self, prettify:bool=True):
        starttag = ''
        endtag = ''
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
            if self.__dict__[i] != None and i not in ["data", "attributes", "startTagName", "tagname", 'endTagName']:
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

    def save(self, filePath:str='./out.html', prettify:bool=True):
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(self.toHtml(prettify=prettify))

    def __str__(self):
        return self.toHtml()

    def __repr__(self):
        return self.toHtml()
