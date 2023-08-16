from inui.config.replaces import replace
from inui.prettify import Pretiffy


class BaseSVG:
    def __init__(
            self,
            data=(),
            attributes={},
            accent_height = None,
            accumulate = None,
            additive = None,
            alignment_baseline = None,
            alphabetic = None,
            amplitude = None,
            arabic_form = None,
            ascent = None,
            attributeName = None,
            attributeType = None,
            azimuth = None,
            baseFrequency = None,
            baseline_shift = None,
            baseProfile = None,
            bbox = None,
            begin = None,
            bias = None,
            by = None,
            calcMode = None,
            cap_height = None,
            classs = None,
            clip = None,
            clip_path = None,
            clip_rule = None,
            clipPathUnits = None,
            color = None,
            color_interpolation = None,
            color_interpolation_filters = None,
            color_profile = None,
            contentScriptType = None,
            contentStyleType = None,
            cursor = None,
            cx = None,
            cy = None,
            d = None,
            data______ = None,
            decoding = None,
            descent = None,
            diffuseConstant = None,
            direction = None,
            display = None,
            divisor = None,
            dominant_baseline = None,
            dur = None,
            dx = None,
            dy = None,
            edgeMode = None,
            elevation = None,
            enable_background = None,
            end = None,
            exponent = None,
            fill = None,
            fill_opacity = None,
            fill_rule = None,
            filter = None,
            filterRes = None,
            filterUnits = None,
            flood_color = None,
            flood_opacity = None,
            font_family = None,
            font_size = None,
            font_size_adjust = None,
            font_stretch = None,
            font_style = None,
            font_variant = None,
            font_weight = None,
            fr = None,
            fromm = None,
            fx = None,
            fy = None,
            g1 = None,
            g2 = None,
            glyph_name = None,
            glyph_orientation_horizontal = None,
            glyph_orientation_vertical = None,
            gradientTransform = None,
            gradientUnits = None,
            hanging = None,
            height = None,
            horiz_adv_x = None,
            horiz_origin_x = None,
            horiz_origin_y = None,
            href = None,
            id = None,
            ideographic = None,
            image_rendering = None,
            inn = None,
            in2 = None,
            intercept = None,
            k = None,
            k1 = None,
            k2 = None,
            k3 = None,
            k4 = None,
            kernelMatrix = None,
            kernelUnitLength = None,
            kerning = None,
            keyPoints = None,
            keySplines = None,
            keyTimes = None,
            lang = None,
            lengthAdjust = None,
            letter_spacing = None,
            lighting_color = None,
            limitingConeAngle = None,
            marker_end = None,
            marker_mid = None,
            marker_start = None,
            markerHeight = None,
            markerUnits = None,
            markerWidth = None,
            mask = None,
            maskContentUnits = None,
            maskUnits = None,
            mathematical = None,
            max = None,
            media = None,
            method = None,
            min = None,
            mode = None,
            name = None,
            numOctaves = None,
            onclick = None,
            opacity = None,
            operator = None,
            order = None,
            orient = None,
            orientation = None,
            origin = None,
            overflow = None,
            overline_position = None,
            overline_thickness = None,
            paint_order = None,
            panose_1 = None,
            path = None,
            pathLength = None,
            patternContentUnits = None,
            patternTransform = None,
            patternUnits = None,
            pointer_events = None,
            points = None,
            pointsAtX = None,
            pointsAtY = None,
            pointsAtZ = None,
            preserveAlpha = None,
            preserveAspectRatio = None,
            primitiveUnits = None,
            r = None,
            radius = None,
            refX = None,
            refY = None,
            repeatCount = None,
            repeatDur = None,
            requiredFeatures = None,
            restart = None,
            result = None,
            rotate = None,
            rx = None,
            ry = None,
            scale = None,
            seed = None,
            shape_rendering = None,
            side = None,
            slope = None,
            spacing = None,
            specularConstant = None,
            specularExponent = None,
            spreadMethod = None,
            startOffset = None,
            stdDeviation = None,
            stemh = None,
            stemv = None,
            stitchTiles = None,
            stop_color = None,
            stop_opacity = None,
            strikethrough_position = None,
            strikethrough_thickness = None,
            string = None,
            stroke = None,
            stroke_dasharray = None,
            stroke_dashoffset = None,
            stroke_linecap = None,
            stroke_linejoin = None,
            stroke_miterlimit = None,
            stroke_opacity = None,
            stroke_width = None,
            style = None,
            surfaceScale = None,
            SVG___attribute_____crossorigin = None,
            SVG___Conditional___Processing___Attributes = None,
            SVG___Core___Attributes = None,
            SVG___Event___Attributes = None,
            SVG___Presentation___Attributes = None,
            SVG___Styling___Attributes = None,
            systemLanguage = None,
            tabindex = None,
            tableValues = None,
            target = None,
            targetX = None,
            targetY = None,
            text_anchor = None,
            text_decoration = None,
            text_rendering = None,
            textLength = None,
            to = None,
            transform = None,
            transform_origin = None,
            typee= None,
            u1 = None,
            u2 = None,
            underline_position = None,
            underline_thickness = None,
            unicode = None,
            unicode_bidi = None,
            unicode_range = None,
            units_per_em = None,
            v_alphabetic = None,
            v_hanging = None,
            v_ideographic = None,
            v_mathematical = None,
            values = None,
            vector_effect = None,
            version = None,
            vert_adv_y = None,
            vert_origin_x = None,
            vert_origin_y = None,
            viewBox = None,
            viewTarget = None,
            visibility = None,
            width = None,
            widths = None,
            word_spacing = None,
            writing_mode = None,
            x = None,
            x_height = None,
            x1 = None,
            x2 = None,
            xChannelSelector = None,
            xlink__arcrole = None,
            xlink__href = None,
            xlink__show = None,
            xlink__title = None,
            xlink__type = None,
            xml__base = None,
            xml__lang = None,
            xml__space = None,
            y = None,
            y1 = None,
            y2 = None,
            yChannelSelector = None,
            z = None,
            zoomAndPan = None,
            startTagName=None,
            endTagName=None,
            tagName=None,
        ):
        self.accent_height = accent_height
        self.accumulate = accumulate
        self.additive = additive
        self.alignment_baseline = alignment_baseline
        self.alphabetic = alphabetic
        self.amplitude = amplitude
        self.arabic_form = arabic_form
        self.ascent = ascent
        self.attributeName = attributeName
        self.attributeType = attributeType
        self.azimuth = azimuth
        self.baseFrequency = baseFrequency
        self.baseline_shift = baseline_shift
        self.baseProfile = baseProfile
        self.bbox = bbox
        self.begin = begin
        self.bias = bias
        self.by = by
        self.calcMode = calcMode
        self.cap_height = cap_height
        self.classs = classs
        self.clip = clip
        self.clip_path = clip_path
        self.clip_rule = clip_rule
        self.clipPathUnits = clipPathUnits
        self.color = color
        self.color_interpolation = color_interpolation
        self.color_interpolation_filters = color_interpolation_filters
        self.color_profile = color_profile
        self.contentScriptType = contentScriptType
        self.contentStyleType = contentStyleType
        self.cursor = cursor
        self.cx = cx
        self.cy = cy
        self.d = d
        self.data______ = data______
        self.decoding = decoding
        self.descent = descent
        self.diffuseConstant = diffuseConstant
        self.direction = direction
        self.display = display
        self.divisor = divisor
        self.dominant_baseline = dominant_baseline
        self.dur = dur
        self.dx = dx
        self.dy = dy
        self.edgeMode = edgeMode
        self.elevation = elevation
        self.enable_background = enable_background
        self.end = end
        self.exponent = exponent
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.fill_rule = fill_rule
        self.filter = filter
        self.filterRes = filterRes
        self.filterUnits = filterUnits
        self.flood_color = flood_color
        self.flood_opacity = flood_opacity
        self.font_family = font_family
        self.font_size = font_size
        self.font_size_adjust = font_size_adjust
        self.font_stretch = font_stretch
        self.font_style = font_style
        self.font_variant = font_variant
        self.font_weight = font_weight
        self.fr = fr
        self.fromm = fromm
        self.fx = fx
        self.fy = fy
        self.g1 = g1
        self.g2 = g2
        self.glyph_name = glyph_name
        self.glyph_orientation_horizontal = glyph_orientation_horizontal
        self.glyph_orientation_vertical = glyph_orientation_vertical
        self.gradientTransform = gradientTransform
        self.gradientUnits = gradientUnits
        self.hanging = hanging
        self.height = height
        self.horiz_adv_x = horiz_adv_x
        self.horiz_origin_x = horiz_origin_x
        self.horiz_origin_y = horiz_origin_y
        self.href = href
        self.id = id
        self.ideographic = ideographic
        self.image_rendering = image_rendering
        self.inn = inn
        self.in2 = in2
        self.intercept = intercept
        self.k = k
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.kernelMatrix = kernelMatrix
        self.kernelUnitLength = kernelUnitLength
        self.kerning = kerning
        self.keyPoints = keyPoints
        self.keySplines = keySplines
        self.keyTimes = keyTimes
        self.lang = lang
        self.lengthAdjust = lengthAdjust
        self.letter_spacing = letter_spacing
        self.lighting_color = lighting_color
        self.limitingConeAngle = limitingConeAngle
        self.marker_end = marker_end
        self.marker_mid = marker_mid
        self.marker_start = marker_start
        self.markerHeight = markerHeight
        self.markerUnits = markerUnits
        self.markerWidth = markerWidth
        self.mask = mask
        self.maskContentUnits = maskContentUnits
        self.maskUnits = maskUnits
        self.mathematical = mathematical
        self.max = max
        self.media = media
        self.method = method
        self.min = min
        self.mode = mode
        self.name = name
        self.numOctaves = numOctaves
        self.onclick = onclick
        self.opacity = opacity
        self.operator = operator
        self.order = order
        self.orient = orient
        self.orientation = orientation
        self.origin = origin
        self.overflow = overflow
        self.overline_position = overline_position
        self.overline_thickness = overline_thickness
        self.paint_order = paint_order
        self.panose_1 = panose_1
        self.path = path
        self.pathLength = pathLength
        self.patternContentUnits = patternContentUnits
        self.patternTransform = patternTransform
        self.patternUnits = patternUnits
        self.pointer_events = pointer_events
        self.points = points
        self.pointsAtX = pointsAtX
        self.pointsAtY = pointsAtY
        self.pointsAtZ = pointsAtZ
        self.preserveAlpha = preserveAlpha
        self.preserveAspectRatio = preserveAspectRatio
        self.primitiveUnits = primitiveUnits
        self.r = r
        self.radius = radius
        self.refX = refX
        self.refY = refY
        self.repeatCount = repeatCount
        self.repeatDur = repeatDur
        self.requiredFeatures = requiredFeatures
        self.restart = restart
        self.result = result
        self.rotate = rotate
        self.rx = rx
        self.ry = ry
        self.scale = scale
        self.seed = seed
        self.shape_rendering = shape_rendering
        self.side = side
        self.slope = slope
        self.spacing = spacing
        self.specularConstant = specularConstant
        self.specularExponent = specularExponent
        self.spreadMethod = spreadMethod
        self.startOffset = startOffset
        self.stdDeviation = stdDeviation
        self.stemh = stemh
        self.stemv = stemv
        self.stitchTiles = stitchTiles
        self.stop_color = stop_color
        self.stop_opacity = stop_opacity
        self.strikethrough_position = strikethrough_position
        self.strikethrough_thickness = strikethrough_thickness
        self.string = string
        self.stroke = stroke
        self.stroke_dasharray = stroke_dasharray
        self.stroke_dashoffset = stroke_dashoffset
        self.stroke_linecap = stroke_linecap
        self.stroke_linejoin = stroke_linejoin
        self.stroke_miterlimit = stroke_miterlimit
        self.stroke_opacity = stroke_opacity
        self.stroke_width = stroke_width
        self.style = style
        self.surfaceScale = surfaceScale
        self.SVG___attribute_____crossorigin = SVG___attribute_____crossorigin
        self.SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes
        self.SVG___Core___Attributes = SVG___Core___Attributes
        self.SVG___Event___Attributes = SVG___Event___Attributes
        self.SVG___Presentation___Attributes = SVG___Presentation___Attributes
        self.SVG___Styling___Attributes = SVG___Styling___Attributes
        self.systemLanguage = systemLanguage
        self.tabindex = tabindex
        self.tableValues = tableValues
        self.target = target
        self.targetX = targetX
        self.targetY = targetY
        self.text_anchor = text_anchor
        self.text_decoration = text_decoration
        self.text_rendering = text_rendering
        self.textLength = textLength
        self.to = to
        self.transform = transform
        self.transform_origin = transform_origin
        self.typee = typee
        self.u1 = u1
        self.u2 = u2
        self.underline_position = underline_position
        self.underline_thickness = underline_thickness
        self.unicode = unicode
        self.unicode_bidi = unicode_bidi
        self.unicode_range = unicode_range
        self.units_per_em = units_per_em
        self.v_alphabetic = v_alphabetic
        self.v_hanging = v_hanging
        self.v_ideographic = v_ideographic
        self.v_mathematical = v_mathematical
        self.values = values
        self.vector_effect = vector_effect
        self.version = version
        self.vert_adv_y = vert_adv_y
        self.vert_origin_x = vert_origin_x
        self.vert_origin_y = vert_origin_y
        self.viewBox = viewBox
        self.viewTarget = viewTarget
        self.visibility = visibility
        self.width = width
        self.widths = widths
        self.word_spacing = word_spacing
        self.writing_mode = writing_mode
        self.x = x
        self.x_height = x_height
        self.x1 = x1
        self.x2 = x2
        self.xChannelSelector = xChannelSelector
        self.xlink__arcrole = xlink__arcrole
        self.xlink__href = xlink__href
        self.xlink__show = xlink__show
        self.xlink__title = xlink__title
        self.xlink__type = xlink__type
        self.xml__base = xml__base
        self.xml__lang = xml__lang
        self.xml__space = xml__space
        self.y = y
        self.y1 = y1
        self.y2 = y2
        self.yChannelSelector = yChannelSelector
        self.z = z
        self.zoomAndPan = zoomAndPan
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
                "laststate",
            ]:
                self.attributes[i] = self.__dict__[i]
        for attribute in self.attributes:
            name = replace(attribute)
            if type(self.attributes[attribute]) == str:
                text += '%s="%s" ' % (name, self.attributes[attribute])

            if type(self.attributes[attribute]) in [list, set, tuple]:
                text += '%s="%s" ' % (name, " ".join(self.attributes[attribute]))
        return text

    def save(self, filePath: str = "./out.svg", prettify: bool = True):
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(self.toHtml(prettify=prettify))
            
class A(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<a>
===

The **<a>** SVG element creates a hyperlink to other web pages, files, locations in the same page, email addresses, or any other URL. It is very similar to HTML's [`<a>`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a) element.


SVG's `<a>` element is a container, which means you can create a link around text (like in HTML) but also around any shape.

[Example](#example)
-------------------


```
@namespace svg url(http://www.w3.org/2000/svg);
html,
body,
svg {
  height: 100%;
}

```

html


```
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- A link around a shape -->
  <a href="/docs/Web/SVG/Element/circle">
    <circle cx="50" cy="40" r="35" />
  </a>

  <!-- A link around a text -->
  <a href="/docs/Web/SVG/Element/text">
    <text x="50" y="90" text-anchor="middle">&lt;circle&gt;</text>
  </a>
</svg>

```

css


```
/\* As SVG does not provide a default visual style for links,
 it's considered best practice to add some \*/

@namespace svg url(http://www.w3.org/2000/svg);
/\* Necessary to select only SVG <a> elements, and not also HTML's.
 See warning below \*/

svg|a:link,
svg|a:visited {
  cursor: pointer;
}

svg|a text,
text svg|a {
  fill: blue; /\* Even for text, SVG uses fill over color \*/
  text-decoration: underline;
}

svg|a:hover,
svg|a:active {
  outline: dotted 1px blue;
}

```


**Warning:** Since this element shares its tag name with [HTML's `<a>` element](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a), selecting `a` with CSS or [`querySelector`](https://developer.mozilla.org//en-US/docs/Web/API/Document/querySelector "querySelector") may apply to the wrong kind of element. Try [the `@namespace` rule](https://developer.mozilla.org//en-US/docs/Web/CSS/@namespace) to distinguish the two.


[Attributes](#attributes)
-------------------------


[`download`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#download)


 Instructs browsers to download a [URL](https://developer.mozilla.org//en-US/docs/Glossary/URL) instead of navigating to it, so the user will be prompted to save it as a local file.
 *Value type*: **<string>** ; *Default value*: *none*; *Animatable*: **no**




`[href](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/href)`


 The [URL](https://developer.mozilla.org//en-US/docs/Glossary/URL) or URL fragment the hyperlink points to.
 *Value type*: **[<URL>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#url)** ; *Default value*: *none*; *Animatable*: **yes**




[`hreflang`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#hreflang)


 The human language of the URL or URL fragment that the hyperlink points to.
 *Value type*: **<string>** ; *Default value*: *none*; *Animatable*: **yes**




[`ping`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#ping) 
Experimental



 A space-separated list of URLs to which, when the hyperlink is followed, [`POST`](https://developer.mozilla.org//en-US/docs/Web/HTTP/Methods/POST) requests with the body `PING` will be sent by the browser (in the background). Typically used for tracking. For a more widely-supported feature addressing the same use cases, see [`Navigator.sendBeacon()`](https://developer.mozilla.org//en-US/docs/Web/API/Navigator/sendBeacon).
 *Value type*: **[<list-of-URLs>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#list-of-ts)** ; *Default value*: *none*; *Animatable*: **no**




[`referrerpolicy`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#referrerpolicy)


 Which [referrer](https://developer.mozilla.org//en-US/docs/Web/HTTP/Headers/Referer) to send when fetching the [URL](https://developer.mozilla.org//en-US/docs/Glossary/URL).
 *Value type*: `no-referrer`|`no-referrer-when-downgrade`|`same-origin`|`origin`|`strict-origin`|`origin-when-cross-origin`|`strict-origin-when-cross-origin`|`unsafe-url` ; *Default value*: *none*; *Animatable*: **no**




[`rel`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#rel)


 The relationship of the target object to the link object.
 *Value type*: **[<list-of-Link-Types>](https://developer.mozilla.org//en-US/docs/Web/HTML/Attributes/rel)** ; *Default value*: *none*; *Animatable*: **yes**




`[target](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/target)`


 Where to display the linked [URL](https://developer.mozilla.org//en-US/docs/Glossary/URL).
 *Value type*: `_self`|`_parent`|`_top`|`_blank`|**<name>** ; *Default value*: `_self`; *Animatable*: **yes**




[`type`](https://developer.mozilla.org//en-US/docs/Web/HTML/Element/a#type)


 A [MIME type](https://developer.mozilla.org//en-US/docs/Glossary/MIME_type) for the linked URL.
 *Value type*: **<string>** ; *Default value*: *none*; *Animatable*: **yes**




`[xlink:href](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/xlink:href)` 
Deprecated



 The URL or URL fragment that the hyperlink points to. May be required for backwards compatibility for older browsers.
 *Value type*: **[<URL>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#url)** ; *Default value*: *none*; *Animatable*: **yes**




### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`, `[lang](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/lang)`, `[tabindex](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/tabindex)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
[Conditional Processing Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Conditional_Processing)

Most notably: `[requiredExtensions](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/requiredExtensions "This is a link to an unwritten page")`, `[systemLanguage](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/systemLanguage)`



Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Document element event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#document_element_event_attributes), [Graphical event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#graphical_event_attributes)



[Presentation Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Presentation)

Most notably: `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)`, `[clip-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-rule)`, `[color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color)`, `[color-interpolation](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-interpolation)`, `[color-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-rendering "This is a link to an unwritten page")`, `[cursor](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cursor)`, `[display](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/display)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`, `[fill-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-opacity)`, `[fill-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-rule)`, `[filter](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/filter)`, `[mask](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mask)`, `[opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/opacity)`, `[pointer-events](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/pointer-events)`, `[shape-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/shape-rendering)`, `[stroke](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke)`, `[stroke-dasharray](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dasharray)`, `[stroke-dashoffset](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dashoffset)`, `[stroke-linecap](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linecap)`, `[stroke-linejoin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linejoin)`, `[stroke-miterlimit](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-miterlimit)`, `[stroke-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-opacity)`, `[stroke-width](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-width)`, `[transform](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/transform)`, `[vector-effect](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/vector-effect)`, `[visibility](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/visibility)`



XLink Attributes

Most notably: `[xlink:title](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/xlink:title)`



ARIA Attributes

`aria-activedescendant`, `aria-atomic`, `aria-autocomplete`, `aria-busy`, `aria-checked`, `aria-colcount`, `aria-colindex`, `aria-colspan`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-grabbed`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-level`, `aria-live`, `aria-modal`, `aria-multiline`, `aria-multiselectable`, `aria-orientation`, `aria-owns`, `aria-placeholder`, `aria-posinset`, `aria-pressed`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`, `aria-rowcount`, `aria-rowindex`, `aria-rowspan`, `aria-selected`, `aria-setsize`, `aria-sort`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext`, `role`



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | Container element |
| Permitted content | Any number of the following elements, in any order:[Animation elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#animation_elements)[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements)[Shape elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#shape_elements)[Structural elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#structural_elements)[Gradient elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#gradient_elements)[`<a>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/a), [`<clipPath>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/clipPath), `<color-profile>`, [`<cursor>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/cursor), [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter), [`<font>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/font), [`<font-face>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/font-face), [`<foreignObject>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/foreignObject), [`<image>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/image), [`<marker>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/marker), [`<mask>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mask), [`<pattern>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/pattern), [`<script>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/script), [`<style>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/style), [`<switch>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/switch), [`<text>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/text), [`<view>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/view) |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2](https://svgwg.org/svg2-draft/linking.html#Links)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.



ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="a",
        )

        

class Animate(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Accessibility concerns](#accessibility_concerns)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<animate>
=========

The SVG **`<animate>`** element provides a way to animate an attribute of an element over time.

[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
  margin: 0;
  padding: 0;
}

```

html


```
<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
  <rect width="10" height="10">
    <animate
 attributeName="rx"
 values="0;5;0"
 dur="10s"
 repeatCount="indefinite" />
  </rect>
</svg>

```
[Attributes](#attributes)
-------------------------

### [Animation Attributes](#animation_attributes)


[Animation timing attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_timing_attributes)
`[begin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/begin)`, `[dur](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/dur)`, `[end](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/end)`, `[min](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/min)`, `[max](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/max)`, `[restart](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/restart)`, `[repeatCount](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/repeatCount)`, `[repeatDur](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/repeatDur)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`
[Animation value attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_value_attributes)
`[calcMode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/calcMode)`, `[values](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/values)`, `[keyTimes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keyTimes)`, `[keySplines](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keySplines)`, `[from](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/From)`, `[to](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/To)`, `[by](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/by)`
[Other Animation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_attributes)

Most notably: `[attributeName](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/attributeName)`, `[additive](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/additive)`, `[accumulate](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/accumulate)`



[Animation event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#animation_event_attributes)

Most notably: `[onbegin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onbegin "This is a link to an unwritten page")`, `[onend](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onend "This is a link to an unwritten page")`, `[onrepeat](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onrepeat "This is a link to an unwritten page")`



### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Document element event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#document_element_event_attributes)



[Usage notes](#usage_notes)
---------------------------

This element implements the [`SVGAnimateElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGAnimateElement) interface.

[Accessibility concerns](#accessibility_concerns)
-------------------------------------------------

Blinking and flashing animation can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD). Additionally, certain kinds of motion can be a trigger for Vestibular disorders, epilepsy, and migraine and Scotopic sensitivity.


Consider providing a mechanism for pausing or disabling animation, as well as using the [Reduced Motion Media Query](https://developer.mozilla.org//en-US/docs/Web/CSS/@media/prefers-reduced-motion) or equivalent [User Agent client hint](https://developer.mozilla.org//en-US/docs/Web/HTTP/Client_hints#user-agent_client_hints) [`Sec-CH-Prefers-Reduced-Motion`](https://developer.mozilla.org//en-US/docs/Web/HTTP/Headers/Sec-CH-Prefers-Reduced-Motion) to create a complimentary experience for users who have expressed a preference for no animated experiences.


* [Designing Safer Web Animation For Motion Sensitivity Â· An A List Apart Article](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/)
* [An Introduction to the Reduced Motion Media Query | CSS-Tricks](https://css-tricks.com/introduction-reduced-motion-media-query/)
* [Responsive Design for Motion | WebKit](https://webkit.org/blog/7551/responsive-design-for-motion/)
* [MDN Understanding WCAG, Guideline 2.2 explanations](https://developer.mozilla.org//en-US/docs/Web/Accessibility/Understanding_WCAG/Operable#guideline_2.2_%e2%80%94_enough_time_provide_users_enough_time_to_read_and_use_content)
* [Understanding Success Criterion 2.2.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/time-limits-pause.html)
[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [SVG Animations Level 2 # AnimateElement](https://svgwg.org/specs/animations/#AnimateElement) |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.



ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="animate",
        )

        

class Animatemotion(SVG):
    """



In this article
---------------

* [Example](#example)
* [Usage context](#usage_context)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<animateMotion>
===============

The SVG **`<animateMotion>`** element provides a way to define how an element moves along a motion path.



**Note:** To reuse an existing path, it will be necessary to use an [`<mpath>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mpath) element inside the `<animateMotion>` element instead of the `[path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/path)` attribute.


[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
  margin: 0;
  padding: 0;
  display: block;
}

```

html


```
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <path
 fill="none"
 stroke="lightgrey"
 d="M20,50 C20,-50 180,150 180,50 C180-50 20,150 20,50 z" />

  <circle r="5" fill="red">
    <animateMotion
 dur="10s"
 repeatCount="indefinite"
 path="M20,50 C20,-50 180,150 180,50 C180-50 20,150 20,50 z" />
  </circle>
</svg>

```
[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Animation element |
| Permitted content | Any number of the following elements, in any order:[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements)[`<mpath>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mpath) |

[Attributes](#attributes)
-------------------------


`[keyPoints](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keyPoints)`


 This attribute indicate, in the range [0,1], how far is the object along the path for each `[keyTimes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keyTimes)` associated values.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number)\*; *Default value*: none; *Animatable*: **no**




`[path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/path)`


 This attribute defines the path of the motion, using the same syntax as the `[d](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/d)` attribute.
 *Value type*: **<string>**; *Default value*: none; *Animatable*: **no**




`[rotate](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/rotate)`


 This attribute defines a rotation applied to the element animated along a path, usually to make it pointing in the direction of the animation.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number)|`auto`|`auto-reverse`; *Default value*: `0`; *Animatable*: **no**






**Note:** For `<animateMotion>`, the default value for the `[calcMode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/calcMode)` attribute is `paced`.


### [Animation Attributes](#animation_attributes)


[Animation timing attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_timing_attributes)
`[begin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/begin)`, `[dur](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/dur)`, `[end](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/end)`, `[min](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/min)`, `[max](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/max)`, `[restart](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/restart)`, `[repeatCount](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/repeatCount)`, `[repeatDur](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/repeatDur)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`
[Animation value attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_value_attributes)
`[calcMode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/calcMode)`, `[values](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/values)`, `[keyTimes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keyTimes)`, `[keySplines](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/keySplines)`, `[from](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/From)`, `[to](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/To)`, `[by](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/by)`
[Other Animation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_attributes)

Most notably: `[attributeName](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/attributeName)`, `[additive](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/additive)`, `[accumulate](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/accumulate)`



[Animation event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#animation_event_attributes)

Most notably: `[onbegin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onbegin "This is a link to an unwritten page")`, `[onend](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onend "This is a link to an unwritten page")`, `[onrepeat](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/onrepeat "This is a link to an unwritten page")`



### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Document element event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#document_element_event_attributes)



[Usage notes](#usage_notes)
---------------------------

This element implements the [`SVGAnimateMotionElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGAnimateMotionElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [SVG Animations Level 2](https://svgwg.org/specs/animations/#AnimateMotionElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<mpath>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mpath)


ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="animateMotion",
        )

        

class Animatetransform(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Example](#example)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<animateTransform>
==================

The `animateTransform` element animates a transformation attribute on its target element, thereby allowing animations to control translation, scaling, rotation, and/or skewing.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Animation element |
| Permitted content | Any number of the following elements, in any order:[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements) |

[Example](#example)
-------------------

html


```
<svg
 width="120"
 height="120"
 viewBox="0 0 120 120"
 xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,30 90,90 30,90">
    <animateTransform
 attributeName="transform"
 attributeType="XML"
 type="rotate"
 from="0 60 70"
 to="360 60 70"
 dur="10s"
 repeatCount="indefinite" />
  </polygon>
</svg>

```
[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Conditional processing attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#conditional_processing_attributes)
* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Animation event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_event_attributes)
* [Xlink attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#xlink_attributes)
* [Animation attribute target attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_attribute_target_attributes)
* [Animation timing attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_timing_attributes)
* [Animation value attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_value_attributes)
* [Animation addition attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#animation_addition_attributes)
### [Specific attributes](#specific_attributes)

* `[by](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/by)`
* `[from](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/From)`
* `[to](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/To)`
* `[type](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/type)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGAnimateTransformElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGAnimateTransformElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [SVG Animations Level 2](https://svgwg.org/specs/animations/#AnimateTransformElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.



ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="animateTransform",
        )

        

class Circle(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<circle>
========

The **`<circle>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) element is an [SVG basic shape](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Basic_Shapes), used to draw circles based on a center point and a radius.

[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
}

```

html


```
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="50" />
</svg>

```
[Attributes](#attributes)
-------------------------


`[cx](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cx)`


 The x-axis coordinate of the center of the circle.
 *Value type*: **[<length>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)**|**[<percentage>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage)** ; *Default value*: `0`; *Animatable*: **yes**




`[cy](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cy)`


 The y-axis coordinate of the center of the circle.
 *Value type*: **[<length>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)**|**[<percentage>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage)** ; *Default value*: `0`; *Animatable*: **yes**




`[r](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/r)`


 The radius of the circle. A value lower or equal to zero disables rendering of the circle.
 *Value type*: **[<length>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)**|**[<percentage>](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage)** ; *Default value*: `0`; *Animatable*: **yes**




`[pathLength](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/pathLength)`


 The total length for the circle's circumference, in user units.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number) ; *Default value*: *none*; *Animatable*: **yes**






**Note:** Starting with SVG2, `cx`, `cy`, and `r` are *Geometry Properties*, meaning those attributes can also be used as CSS properties for that element.


### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`, `[tabindex](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/tabindex)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
[Conditional Processing Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Conditional_Processing)

Most notably: `[requiredExtensions](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/requiredExtensions "This is a link to an unwritten page")`, `[systemLanguage](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/systemLanguage)`



Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Graphical event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#graphical_event_attributes)



[Presentation Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Presentation)

Most notably: `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)`, `[clip-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-rule)`, `[color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color)`, `[color-interpolation](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-interpolation)`, `[color-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-rendering "This is a link to an unwritten page")`, `[cursor](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cursor)`, `[display](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/display)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`, `[fill-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-opacity)`, `[fill-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-rule)`, `[filter](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/filter)`, `[mask](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mask)`, `[opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/opacity)`, `[pointer-events](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/pointer-events)`, `[shape-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/shape-rendering)`, `[stroke](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke)`, `[stroke-dasharray](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dasharray)`, `[stroke-dashoffset](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dashoffset)`, `[stroke-linecap](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linecap)`, `[stroke-linejoin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linejoin)`, `[stroke-miterlimit](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-miterlimit)`, `[stroke-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-opacity)`, `[stroke-width](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-width)`, `[transform](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/transform)`, `[vector-effect](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/vector-effect)`, `[visibility](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/visibility)`



ARIA Attributes

`aria-activedescendant`, `aria-atomic`, `aria-autocomplete`, `aria-busy`, `aria-checked`, `aria-colcount`, `aria-colindex`, `aria-colspan`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-grabbed`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-level`, `aria-live`, `aria-modal`, `aria-multiline`, `aria-multiselectable`, `aria-orientation`, `aria-owns`, `aria-placeholder`, `aria-posinset`, `aria-pressed`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`, `aria-rowcount`, `aria-rowindex`, `aria-rowspan`, `aria-selected`, `aria-setsize`, `aria-sort`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext`, `role`



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | Basic shape element, Graphics element, Shape element |
| Permitted content | Any number of the following elements, in any order:[Animation elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#animation_elements)[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements) |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2](https://svgwg.org/svg2-draft/shapes.html#CircleElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* Other SVG basic shapes: **[`<ellipse>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/ellipse)**, [`<line>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/line), [`<polygon>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/polygon), [`<polyline>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/polyline), [`<rect>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/rect)


ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="circle",
        )

        

class Clippath(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [Related](#related)
<clipPath>
==========

The **`<clipPath>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) element defines a clipping path, to be used by the `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)` property.


A clipping path restricts the region to which paint can be applied. Conceptually, parts of the drawing that lie outside of the region bounded by the clipping path are not drawn.

[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
}

```

html


```
<svg viewBox="0 0 100 100">
  <clipPath id="myClip">
    <!--
 Everything outside the circle will be
 clipped and therefore invisible.
 -->
    <circle cx="40" cy="35" r="35" />
  </clipPath>

  <!-- The original black heart, for reference -->
  <path
 id="heart"
 d="M10,30 A20,20,0,0,1,50,30 A20,20,0,0,1,90,30 Q90,60,50,90 Q10,60,10,30 Z" />

  <!--
 Only the portion of the red heart
 inside the clip circle is visible.
 -->
  <use clip-path="url(#myClip)" href="#heart" fill="red" />
</svg>

```

css


```
/\* With a touch of CSS for browsers who \*
 \* implemented the r Geometry Property. \*/

@keyframes openYourHeart {
  from {
    r: 0;
  }
  to {
    r: 60px;
  }
}

#myClip circle {
  animation: openYourHeart 15s infinite;
}

```

A clipping path is conceptually equivalent to a custom viewport for the referencing element. Thus, it affects the *rendering* of an element, but not the element's *inherent geometry*. The bounding box of a clipped element (meaning, an element which references a `<clipPath>` element via a `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)` property, or a child of the referencing element) must remain the same as if it were not clipped.


By default, [`pointer-events`](https://developer.mozilla.org//en-US/docs/Web/CSS/pointer-events) are not dispatched on clipped regions. For example, a circle with a radius of `10` which is clipped to a circle with a radius of `5` will not receive "click" events outside the smaller radius.

[Attributes](#attributes)
-------------------------


`[clipPathUnits](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clipPathUnits)`


 Defines the coordinate system for the contents of the `<clipPath>` element.
 *Value type*: `userSpaceOnUse`|`objectBoundingBox` ; *Default value*: `userSpaceOnUse`; *Animatable*: **yes**




### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
[Conditional Processing Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Conditional_Processing)

Most notably: `[requiredExtensions](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/requiredExtensions "This is a link to an unwritten page")`, `[systemLanguage](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/systemLanguage)`



[Presentation Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Presentation)

Most notably: `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)`, `[clip-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-rule)`, `[color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color)`, `[display](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/display)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`, `[fill-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-opacity)`, `[fill-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-rule)`, `[filter](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/filter)`, `[mask](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mask)`, `[opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/opacity)`, `[shape-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/shape-rendering)`, `[stroke](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke)`, `[stroke-dasharray](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dasharray)`, `[stroke-dashoffset](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dashoffset)`, `[stroke-linecap](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linecap)`, `[stroke-linejoin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linejoin)`, `[stroke-miterlimit](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-miterlimit)`, `[stroke-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-opacity)`, `[stroke-width](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-width)`, `[transform](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/transform)`, `[vector-effect](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/vector-effect)`, `[visibility](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/visibility)`



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | None |
| Permitted content | Any number of the following elements, in any order:[Animation elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#animation_elements)[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements)[Shape elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#shape_elements)[`<text>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/text), [`<use>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/use) |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [CSS Masking Module Level 1](https://drafts.fxtf.org/css-masking/#ClipPathElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[Related](#related)
-------------------

* Other clipping and masking SVG elements: [`<mask>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mask)
* Some CSS properties: [`clip-path`](https://developer.mozilla.org//en-US/docs/Web/CSS/clip-path), [`pointer-events`](https://developer.mozilla.org//en-US/docs/Web/CSS/pointer-events)


ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="clipPath",
        )

        

class Cursor(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<cursor>
========

**Deprecated:** This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.



**Note:** The CSS [`cursor`](https://developer.mozilla.org//en-US/docs/Web/CSS/cursor) property should be used instead of this element.



The **`<cursor>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) element can be used to define a platform-independent custom cursor. A recommended approach for defining a platform-independent custom cursor is to create a PNG image and define a `cursor` element that references the PNG image and identifies the exact position within the image which is the pointer position (i.e., the hot spot).


The PNG format is recommended because it supports the ability to define a transparency mask via an alpha channel. If a different image format is used, this format should support the definition of a transparency mask (two options: provide an explicit alpha channel or use a particular pixel color to indicate transparency). If the transparency mask can be determined, the mask defines the shape of the cursor; otherwise, the cursor is an opaque rectangle. Typically, the other pixel information (e.g., the R, G and B channels) defines the colors for those parts of the cursor which are not masked out. Note that cursors usually contain at least two colors so that the cursor can be visible over most backgrounds.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | None |
| Permitted content | Any number of the following elements, in any order:[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Conditional processing attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#conditional_processing_attributes)
* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Xlink attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#xlink_attributes)
### [Specific attributes](#specific_attributes)

* `[x](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/x)` 
Deprecated
* `[y](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/y)` 
Deprecated
* `[xlink:href](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/xlink:href)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGCursorElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGCursorElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 1.1 (Second Edition)](https://www.w3.org/TR/SVG11/interact.html#CursorElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.



ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="cursor",
        )

        

class Defs(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<defs>
======

The **`<defs>`** element is used to store graphical objects that will be used at a later time. Objects created inside a `<defs>` element are not rendered directly. To display them you have to reference them (with a [`<use>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/use) element for example).


Graphical objects can be referenced from anywhere, however, defining these objects inside of a `<defs>` element promotes understandability of the SVG content and is beneficial to the overall accessibility of the document.

[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
}

```

html


```
<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
  <!-- Some graphical objects to use -->
  <defs>
    <circle id="myCircle" cx="0" cy="0" r="5" />

    <linearGradient id="myGradient" gradientTransform="rotate(90)">
      <stop offset="20%" stop-color="gold" />
      <stop offset="90%" stop-color="red" />
    </linearGradient>
  </defs>

  <!-- using my graphical objects -->
  <use x="5" y="5" href="#myCircle" fill="url('#myGradient')" />
</svg>

```
[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)` `[lang](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/lang)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Document element event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#document_element_event_attributes), [Graphical event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#graphical_event_attributes)



[Presentation Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Presentation)

Most notably: `[clip-path](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-path)`, `[clip-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/clip-rule)`, `[color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color)`, `[color-interpolation](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-interpolation)`, `[color-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/color-rendering "This is a link to an unwritten page")`, `[cursor](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cursor)`, `[display](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/display)`, `[fill](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill)`, `[fill-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-opacity)`, `[fill-rule](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/fill-rule)`, `[filter](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/filter)`, `[mask](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mask)`, `[opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/opacity)`, `[pointer-events](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/pointer-events)`, `[shape-rendering](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/shape-rendering)`, `[stroke](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke)`, `[stroke-dasharray](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dasharray)`, `[stroke-dashoffset](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-dashoffset)`, `[stroke-linecap](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linecap)`, `[stroke-linejoin](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-linejoin)`, `[stroke-miterlimit](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-miterlimit)`, `[stroke-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-opacity)`, `[stroke-width](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stroke-width)`, `[transform](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/transform)`, `[vector-effect](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/vector-effect)`, `[visibility](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/visibility)`



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | Container element, Structural element |
| Permitted content | Any number of the following elements, in any order:[Animation elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#animation_elements)[Descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive_elements)[Shape elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#shape_elements)[Structural elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#structural_elements)[Gradient elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#gradient_elements)[`<a>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/a), [`<clipPath>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/clipPath), `<color-profile>`, [`<cursor>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/cursor), [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter), [`<font>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/font), [`<font-face>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/font-face), [`<foreignObject>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/foreignObject), [`<image>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/image), [`<marker>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/marker), [`<mask>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/mask), [`<pattern>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/pattern), [`<script>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/script), [`<style>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/style), [`<switch>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/switch), [`<text>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/text), [`<view>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/view) |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2](https://svgwg.org/svg2-draft/struct.html#Head)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.



ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="defs",
        )

        

class Desc(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<desc>
======

The **`<desc>`** element provides an accessible, long-text description of any SVG [container element](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#container_elements) or [graphics element](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#graphics_elements).


Text in a `<desc>` element is not rendered as part of the graphic. If the element can be described by visible text, it is possible to reference that text with the [`aria-describedby`](https://developer.mozilla.org//en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby) attribute. If `aria-describedby` is used, it will take precedence over `<desc>`.


The hidden text of a `<desc>` element can also be concatenated with the visible text of other elements using multiple IDs in an `aria-describedby` value. In that case, the `<desc>` element must provide an ID for reference.

[Example](#example)
-------------------


```
html,
body,
svg {
  height: 100%;
}

```

html


```
<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
  <circle cx="5" cy="5" r="4">
    <desc>
      I'm a circle and that description is here to demonstrate how I can be
      described, but is it really necessary to describe a simple circle like me?
    </desc>
  </circle>
</svg>

```
[Attributes](#attributes)
-------------------------

This element only includes global attributes

### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
Event Attributes

[Global event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#global_event_attributes), [Document element event attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Events#document_element_event_attributes)



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | Descriptive element |
| Permitted content | Any elements or character data |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2 # DescriptionAndTitleElements](https://svgwg.org/svg2-draft/struct.html#DescriptionAndTitleElements) |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<title>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/title)


ref = [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
"""

    def __init__(
        self,
        data=(),
        attributes={},
        accent_height = None,
        accumulate = None,
        additive = None,
        alignment_baseline = None,
        alphabetic = None,
        amplitude = None,
        arabic_form = None,
        ascent = None,
        attributeName = None,
        attributeType = None,
        azimuth = None,
        baseFrequency = None,
        baseline_shift = None,
        baseProfile = None,
        bbox = None,
        begin = None,
        bias = None,
        by = None,
        calcMode = None,
        cap_height = None,
        classs = None,
        clip = None,
        clip_path = None,
        clip_rule = None,
        clipPathUnits = None,
        color = None,
        color_interpolation = None,
        color_interpolation_filters = None,
        color_profile = None,
        contentScriptType = None,
        contentStyleType = None,
        cursor = None,
        cx = None,
        cy = None,
        d = None,
        data______ = None,
        decoding = None,
        descent = None,
        diffuseConstant = None,
        direction = None,
        display = None,
        divisor = None,
        dominant_baseline = None,
        dur = None,
        dx = None,
        dy = None,
        edgeMode = None,
        elevation = None,
        enable_background = None,
        end = None,
        exponent = None,
        fill = None,
        fill_opacity = None,
        fill_rule = None,
        filter = None,
        filterRes = None,
        filterUnits = None,
        flood_color = None,
        flood_opacity = None,
        font_family = None,
        font_size = None,
        font_size_adjust = None,
        font_stretch = None,
        font_style = None,
        font_variant = None,
        font_weight = None,
        fr = None,
        fromm = None,
        fx = None,
        fy = None,
        g1 = None,
        g2 = None,
        glyph_name = None,
        glyph_orientation_horizontal = None,
        glyph_orientation_vertical = None,
        gradientTransform = None,
        gradientUnits = None,
        hanging = None,
        height = None,
        horiz_adv_x = None,
        horiz_origin_x = None,
        horiz_origin_y = None,
        href = None,
        id = None,
        ideographic = None,
        image_rendering = None,
        inn = None,
        in2 = None,
        intercept = None,
        k = None,
        k1 = None,
        k2 = None,
        k3 = None,
        k4 = None,
        kernelMatrix = None,
        kernelUnitLength = None,
        kerning = None,
        keyPoints = None,
        keySplines = None,
        keyTimes = None,
        lang = None,
        lengthAdjust = None,
        letter_spacing = None,
        lighting_color = None,
        limitingConeAngle = None,
        marker_end = None,
        marker_mid = None,
        marker_start = None,
        markerHeight = None,
        markerUnits = None,
        markerWidth = None,
        mask = None,
        maskContentUnits = None,
        maskUnits = None,
        mathematical = None,
        max = None,
        media = None,
        method = None,
        min = None,
        mode = None,
        name = None,
        numOctaves = None,
        onclick = None,
        opacity = None,
        operator = None,
        order = None,
        orient = None,
        orientation = None,
        origin = None,
        overflow = None,
        overline_position = None,
        overline_thickness = None,
        paint_order = None,
        panose_1 = None,
        path = None,
        pathLength = None,
        patternContentUnits = None,
        patternTransform = None,
        patternUnits = None,
        pointer_events = None,
        points = None,
        pointsAtX = None,
        pointsAtY = None,
        pointsAtZ = None,
        preserveAlpha = None,
        preserveAspectRatio = None,
        primitiveUnits = None,
        r = None,
        radius = None,
        refX = None,
        refY = None,
        repeatCount = None,
        repeatDur = None,
        requiredFeatures = None,
        restart = None,
        result = None,
        rotate = None,
        rx = None,
        ry = None,
        scale = None,
        seed = None,
        shape_rendering = None,
        side = None,
        slope = None,
        spacing = None,
        specularConstant = None,
        specularExponent = None,
        spreadMethod = None,
        startOffset = None,
        stdDeviation = None,
        stemh = None,
        stemv = None,
        stitchTiles = None,
        stop_color = None,
        stop_opacity = None,
        strikethrough_position = None,
        strikethrough_thickness = None,
        string = None,
        stroke = None,
        stroke_dasharray = None,
        stroke_dashoffset = None,
        stroke_linecap = None,
        stroke_linejoin = None,
        stroke_miterlimit = None,
        stroke_opacity = None,
        stroke_width = None,
        style = None,
        surfaceScale = None,
        SVG___attribute_____crossorigin = None,
        SVG___Conditional___Processing___Attributes = None,
        SVG___Core___Attributes = None,
        SVG___Event___Attributes = None,
        SVG___Presentation___Attributes = None,
        SVG___Styling___Attributes = None,
        systemLanguage = None,
        tabindex = None,
        tableValues = None,
        target = None,
        targetX = None,
        targetY = None,
        text_anchor = None,
        text_decoration = None,
        text_rendering = None,
        textLength = None,
        to = None,
        transform = None,
        transform_origin = None,
        typee = None,
        u1 = None,
        u2 = None,
        underline_position = None,
        underline_thickness = None,
        unicode = None,
        unicode_bidi = None,
        unicode_range = None,
        units_per_em = None,
        v_alphabetic = None,
        v_hanging = None,
        v_ideographic = None,
        v_mathematical = None,
        values = None,
        vector_effect = None,
        version = None,
        vert_adv_y = None,
        vert_origin_x = None,
        vert_origin_y = None,
        viewBox = None,
        viewTarget = None,
        visibility = None,
        width = None,
        widths = None,
        word_spacing = None,
        writing_mode = None,
        x = None,
        x_height = None,
        x1 = None,
        x2 = None,
        xChannelSelector = None,
        xlink__arcrole = None,
        xlink__href = None,
        xlink__show = None,
        xlink__title = None,
        xlink__type = None,
        xml__base = None,
        xml__lang = None,
        xml__space = None,
        y = None,
        y1 = None,
        y2 = None,
        yChannelSelector = None,
        z = None,
        zoomAndPan = None,
    ):
        super().__init__(
            data=data,
            attributes=attributes,
            accent_height = accent_height,
            accumulate = accumulate,
            additive = additive,
            alignment_baseline = alignment_baseline,
            alphabetic = alphabetic,
            amplitude = amplitude,
            arabic_form = arabic_form,
            ascent = ascent,
            attributeName = attributeName,
            attributeType = attributeType,
            azimuth = azimuth,
            baseFrequency = baseFrequency,
            baseline_shift = baseline_shift,
            baseProfile = baseProfile,
            bbox = bbox,
            begin = begin,
            bias = bias,
            by = by,
            calcMode = calcMode,
            cap_height = cap_height,
            classs = classs,
            clip = clip,
            clip_path = clip_path,
            clip_rule = clip_rule,
            clipPathUnits = clipPathUnits,
            color = color,
            color_interpolation = color_interpolation,
            color_interpolation_filters = color_interpolation_filters,
            color_profile = color_profile,
            contentScriptType = contentScriptType,
            contentStyleType = contentStyleType,
            cursor = cursor,
            cx = cx,
            cy = cy,
            d = d,
            data______ = data______,
            decoding = decoding,
            descent = descent,
            diffuseConstant = diffuseConstant,
            direction = direction,
            display = display,
            divisor = divisor,
            dominant_baseline = dominant_baseline,
            dur = dur,
            dx = dx,
            dy = dy,
            edgeMode = edgeMode,
            elevation = elevation,
            enable_background = enable_background,
            end = end,
            exponent = exponent,
            fill = fill,
            fill_opacity = fill_opacity,
            fill_rule = fill_rule,
            filter = filter,
            filterRes = filterRes,
            filterUnits = filterUnits,
            flood_color = flood_color,
            flood_opacity = flood_opacity,
            font_family = font_family,
            font_size = font_size,
            font_size_adjust = font_size_adjust,
            font_stretch = font_stretch,
            font_style = font_style,
            font_variant = font_variant,
            font_weight = font_weight,
            fr = fr,
            fromm = fromm,
            fx = fx,
            fy = fy,
            g1 = g1,
            g2 = g2,
            glyph_name = glyph_name,
            glyph_orientation_horizontal = glyph_orientation_horizontal,
            glyph_orientation_vertical = glyph_orientation_vertical,
            gradientTransform = gradientTransform,
            gradientUnits = gradientUnits,
            hanging = hanging,
            height = height,
            horiz_adv_x = horiz_adv_x,
            horiz_origin_x = horiz_origin_x,
            horiz_origin_y = horiz_origin_y,
            href = href,
            id = id,
            ideographic = ideographic,
            image_rendering = image_rendering,
            inn = inn,
            in2 = in2,
            intercept = intercept,
            k = k,
            k1 = k1,
            k2 = k2,
            k3 = k3,
            k4 = k4,
            kernelMatrix = kernelMatrix,
            kernelUnitLength = kernelUnitLength,
            kerning = kerning,
            keyPoints = keyPoints,
            keySplines = keySplines,
            keyTimes = keyTimes,
            lang = lang,
            lengthAdjust = lengthAdjust,
            letter_spacing = letter_spacing,
            lighting_color = lighting_color,
            limitingConeAngle = limitingConeAngle,
            marker_end = marker_end,
            marker_mid = marker_mid,
            marker_start = marker_start,
            markerHeight = markerHeight,
            markerUnits = markerUnits,
            markerWidth = markerWidth,
            mask = mask,
            maskContentUnits = maskContentUnits,
            maskUnits = maskUnits,
            mathematical = mathematical,
            max = max,
            media = media,
            method = method,
            min = min,
            mode = mode,
            name = name,
            numOctaves = numOctaves,
            onclick = onclick,
            opacity = opacity,
            operator = operator,
            order = order,
            orient = orient,
            orientation = orientation,
            origin = origin,
            overflow = overflow,
            overline_position = overline_position,
            overline_thickness = overline_thickness,
            paint_order = paint_order,
            panose_1 = panose_1,
            path = path,
            pathLength = pathLength,
            patternContentUnits = patternContentUnits,
            patternTransform = patternTransform,
            patternUnits = patternUnits,
            pointer_events = pointer_events,
            points = points,
            pointsAtX = pointsAtX,
            pointsAtY = pointsAtY,
            pointsAtZ = pointsAtZ,
            preserveAlpha = preserveAlpha,
            preserveAspectRatio = preserveAspectRatio,
            primitiveUnits = primitiveUnits,
            r = r,
            radius = radius,
            refX = refX,
            refY = refY,
            repeatCount = repeatCount,
            repeatDur = repeatDur,
            requiredFeatures = requiredFeatures,
            restart = restart,
            result = result,
            rotate = rotate,
            rx = rx,
            ry = ry,
            scale = scale,
            seed = seed,
            shape_rendering = shape_rendering,
            side = side,
            slope = slope,
            spacing = spacing,
            specularConstant = specularConstant,
            specularExponent = specularExponent,
            spreadMethod = spreadMethod,
            startOffset = startOffset,
            stdDeviation = stdDeviation,
            stemh = stemh,
            stemv = stemv,
            stitchTiles = stitchTiles,
            stop_color = stop_color,
            stop_opacity = stop_opacity,
            strikethrough_position = strikethrough_position,
            strikethrough_thickness = strikethrough_thickness,
            string = string,
            stroke = stroke,
            stroke_dasharray = stroke_dasharray,
            stroke_dashoffset = stroke_dashoffset,
            stroke_linecap = stroke_linecap,
            stroke_linejoin = stroke_linejoin,
            stroke_miterlimit = stroke_miterlimit,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            style = style,
            surfaceScale = surfaceScale,
            SVG___attribute_____crossorigin = SVG___attribute_____crossorigin,
            SVG___Conditional___Processing___Attributes = SVG___Conditional___Processing___Attributes,
            SVG___Core___Attributes = SVG___Core___Attributes,
            SVG___Event___Attributes = SVG___Event___Attributes,
            SVG___Presentation___Attributes = SVG___Presentation___Attributes,
            SVG___Styling___Attributes = SVG___Styling___Attributes,
            systemLanguage = systemLanguage,
            tabindex = tabindex,
            tableValues = tableValues,
            target = target,
            targetX = targetX,
            targetY = targetY,
            text_anchor = text_anchor,
            text_decoration = text_decoration,
            text_rendering = text_rendering,
            textLength = textLength,
            to = to,
            transform = transform,
            transform_origin = transform_origin,
            typee = typee,
            u1 = u1,
            u2 = u2,
            underline_position = underline_position,
            underline_thickness = underline_thickness,
            unicode = unicode,
            unicode_bidi = unicode_bidi,
            unicode_range = unicode_range,
            units_per_em = units_per_em,
            v_alphabetic = v_alphabetic,
            v_hanging = v_hanging,
            v_ideographic = v_ideographic,
            v_mathematical = v_mathematical,
            values = values,
            vector_effect = vector_effect,
            version = version,
            vert_adv_y = vert_adv_y,
            vert_origin_x = vert_origin_x,
            vert_origin_y = vert_origin_y,
            viewBox = viewBox,
            viewTarget = viewTarget,
            visibility = visibility,
            width = width,
            widths = widths,
            word_spacing = word_spacing,
            writing_mode = writing_mode,
            x = x,
            x_height = x_height,
            x1 = x1,
            x2 = x2,
            xChannelSelector = xChannelSelector,
            xlink__arcrole = xlink__arcrole,
            xlink__href = xlink__href,
            xlink__show = xlink__show,
            xlink__title = xlink__title,
            xlink__type = xlink__type,
            xml__base = xml__base,
            xml__lang = xml__lang,
            xml__space = xml__space,
            y = y,
            y1 = y1,
            y2 = y2,
            yChannelSelector = yChannelSelector,
            z = z,
            zoomAndPan = zoomAndPan,
            startTagName=None,
            endTagName=None,
            tagName="desc",
        )

        

