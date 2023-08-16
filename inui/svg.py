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

        

class Ellipse(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<ellipse>
=========

The **`<ellipse>`** element is an SVG basic shape, used to create ellipses based on a center coordinate, and both their x and y radius.



**Note:** Ellipses are unable to specify the exact orientation of the ellipse (if, for example, you wanted to draw an ellipse tilted at a 45 degree angle), but it can be rotated by using the `[transform](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/transform)` attribute.


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
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="50" rx="100" ry="50" />
</svg>

```
[Attributes](#attributes)
-------------------------


`[cx](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cx)`


 The x position of the center of the ellipse.
 *Value type*: [**<length>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)|[**<percentage>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage) ; *Default value*: `0`; *Animatable*: **yes**




`[cy](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/cy)`


 The y position of the center of the ellipse.
 *Value type*: [**<length>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)|[**<percentage>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage) ; *Default value*: `0`; *Animatable*: **yes**




`[rx](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/rx)`


 The radius of the ellipse on the x axis.
 *Value type*: `auto`|[**<length>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)|[**<percentage>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage) ; *Default value*: `auto`; *Animatable*: **yes**




`[ry](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/ry)`


 The radius of the ellipse on the y axis.
 *Value type*: `auto`|[**<length>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#length)|[**<percentage>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#percentage) ; *Default value*: `auto`; *Animatable*: **yes**




`[pathLength](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/pathLength)`


 This attribute lets specify the total length for the path, in user units.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number) ; *Default value*: *none*; *Animatable*: **yes**






**Note:** Starting with SVG2 `cx`, `cy`, `rx` and `ry` are *Geometry Properties*, meaning those attributes can also be used as CSS properties for that element.


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
| [Scalable Vector Graphics (SVG) 2](https://svgwg.org/svg2-draft/shapes.html#EllipseElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* Other SVG basic shapes: **[`<circle>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/circle)**, [`<line>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/line), [`<polygon>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/polygon), [`<polyline>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/polyline), [`<rect>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/rect)


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
            tagName="ellipse",
        )

        

class Feblend(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feBlend>
=========

The **`<feBlend>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive composes two objects together ruled by a certain blending mode. This is similar to what is known from image editing software when blending two layers. The mode is defined by the `[mode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mode)` attribute.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`
* `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)`
* `[mode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/mode)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEBlendElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEBlendElement) interface.

[Example](#example)
-------------------

### [SVG](#svg)

html


```
<svg
 width="200"
 height="200"
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <filter id="spotlight">
      <feFlood
 result="floodFill"
 x="0"
 y="0"
 width="100%"
 height="100%"
 flood-color="green"
 flood-opacity="1" />
      <feBlend in="SourceGraphic" in2="floodFill" mode="multiply" />
    </filter>
  </defs>

  <image
 href="mdn\_logo\_only\_color.png"
 x="10%"
 y="10%"
 width="80%"
 height="80%"
 style="filter:url(#spotlight);" />
</svg>

```
### [Result](#result)

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feBlendElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feBlend",
        )

        

class Fecolormatrix(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feColorMatrix>
===============

The **`<feColorMatrix>`** SVG filter element changes colors based on a transformation matrix. Every pixel's color value `[R,G,B,A]` is [matrix multiplied](https://en.wikipedia.org/wiki/Matrix_multiplication) by a 5 by 5 color matrix to create new color `[R',G',B',A']`.



**Note:** The prime symbol **`'`** is used in mathematics indicate the result of a transformation.




```
| R' |     | r1 r2 r3 r4 r5 |   | R |
| G' |     | g1 g2 g3 g4 g5 |   | G |
| B' |  =  | b1 b2 b3 b4 b5 | * | B |
| A' |     | a1 a2 a3 a4 a5 |   | A |
| 1  |     | 0  0  0  0  1  |   | 1 |

```

In simplified terms, below is how each color channel in the new pixel is calculated. The last row is ignored because its values are constant.



```
R' = r1*R + r2*G + r3*B + r4*A + r5
G' = g1*R + g2*G + g3*B + g4*A + g5
B' = b1*R + b2*G + b3*B + b4*A + b5
A' = a1*R + a2*G + a3*B + a4*A + a5

```

Take the amount of red in the new pixel, or `R'`:


It is the sum of:


* `r1` times the old pixel's red `R`,
* `r2` times the old pixel's green `G`,
* `r3` times of the old pixel's blue `B`,
* `r4` times the old pixel's alpha `A`,
* plus a shift `r5`.


These specified amounts can be any real number, though the final **R'** will be clamped between 0 and 1. The same goes for **G'**, **B'**, and **A'**.



```
R'      =      r1 * R      +        r2 * G      +       r3 * B      +       r4 * A       +       r5
New red = [ r1 * old red ] + [ r2 * old green ] + [ r3 * old Blue ] + [ r4 * old Alpha ] + [ shift of r5 ]

```

If, say, we want to make a completely black image redder, we can make the `r5` a positive real number *x*, boosting the redness on every pixel of the new image by *x*.


An **identity matrix** looks like this:



```
     R G B A W
R' | 1 0 0 0 0 |
G' | 0 1 0 0 0 |
B' | 0 0 1 0 0 |
A' | 0 0 0 1 0 |

```

In it, every new value is exactly 1 times its old value, with nothing else added. It is recommended to start manipulating the matrix from here.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes), including the `x`, `y`, `width`, `height`, and `result` attributes.
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`: Values include `SourceGraphic`, `SourceAlpha`, `BackgroundImage`, `BackgroundAlpha`, `FillPaint`, `StrokePaint`, or a reference to another filter primitive.
* `[type](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/type)`: Values include `matrix`, `saturate`, `hueRotate`, and `luminanceToAlpha`.
* `[values](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/values)`: The value for the matrix type set in the `type` attribute.
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEColorMatrixElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEColorMatrixElement) interface.

[Example](#example)
-------------------

### [SVG](#svg)

html


```
<svg
 width="100%"
 height="100%"
 viewBox="0 0 150 500"
 preserveAspectRatio="xMidYMid meet"
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
  <!-- ref -->
  <defs>
    <g id="circles">
      <circle cx="30" cy="30" r="20" fill="blue" fill-opacity="0.5" />
      <circle cx="20" cy="50" r="20" fill="green" fill-opacity="0.5" />
      <circle cx="40" cy="50" r="20" fill="red" fill-opacity="0.5" />
    </g>
  </defs>
  <use href="#circles" />
  <text x="70" y="50">Reference</text>

  <!-- identity matrix -->
  <filter id="colorMeTheSame">
    <feColorMatrix
 in="SourceGraphic"
 type="matrix"
 values="1 0 0 0 0
 0 1 0 0 0
 0 0 1 0 0
 0 0 0 1 0" />
  </filter>
  <use
 href="#circles"
 transform="translate(0 70)"
 filter="url(#colorMeTheSame)" />
  <text x="70" y="120">Identity matrix</text>

  <!-- Combine RGB into green matrix -->
  <filter id="colorMeGreen">
    <feColorMatrix
 in="SourceGraphic"
 type="matrix"
 values="0 0 0 0 0
 1 1 1 1 0
 0 0 0 0 0
 0 0 0 1 0" />
  </filter>
  <use
 href="#circles"
 transform="translate(0 140)"
 filter="url(#colorMeGreen)" />
  <text x="70" y="190">rgbToGreen</text>

  <!-- saturate -->
  <filter id="colorMeSaturate">
    <feColorMatrix in="SourceGraphic" type="saturate" values="0.2" />
  </filter>
  <use
 href="#circles"
 transform="translate(0 210)"
 filter="url(#colorMeSaturate)" />
  <text x="70" y="260">saturate</text>

  <!-- hueRotate -->
  <filter id="colorMeHueRotate">
    <feColorMatrix in="SourceGraphic" type="hueRotate" values="180" />
  </filter>
  <use
 href="#circles"
 transform="translate(0 280)"
 filter="url(#colorMeHueRotate)" />
  <text x="70" y="330">hueRotate</text>

  <!-- luminanceToAlpha -->
  <filter id="colorMeLTA">
    <feColorMatrix in="SourceGraphic" type="luminanceToAlpha" />
  </filter>
  <use href="#circles" transform="translate(0 350)" filter="url(#colorMeLTA)" />
  <text x="70" y="400">luminanceToAlpha</text>
</svg>

```
### [Result](#result)



| Screenshot | Live sample |
| --- | --- |
|  |  |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feColorMatrixElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feColorMatrix",
        )

        

class Fecomponenttransfer(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feComponentTransfer>
=====================

The **`<feComponentTransfer>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive performs color-component-wise remapping of data for each pixel. It allows operations like brightness adjustment, contrast adjustment, color balance or thresholding.


The calculations are performed on non-premultiplied color values. The colors are modified by changing each channel (R, G, B, and A) to the result of what the children [`<feFuncR>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncR), [`<feFuncB>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncB), [`<feFuncG>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncG), and [`<feFuncA>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncA) return. If more than one of the same element is provided, the last one specified is used, and if no element is supplied to modify one of the channels, the effect is the same is if an identity transformation had been given for that channel.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<feFuncA>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncA), [`<feFuncR>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncR), [`<feFuncB>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncB), [`<feFuncG>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncG) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEComponentTransferElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEComponentTransferElement) interface.

[Example](#example)
-------------------

### [SVG](#svg)

html


```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300">
  <defs>
    <linearGradient
 id="rainbow"
 gradientUnits="userSpaceOnUse"
 x1="0"
 y1="0"
 x2="100%"
 y2="0">
      <stop offset="0" stop-color="#ff0000"></stop>
      <stop offset="0.2" stop-color="#ffff00"></stop>
      <stop offset="0.4" stop-color="#00ff00"></stop>
      <stop offset="0.6" stop-color="#00ffff"></stop>
      <stop offset="0.8" stop-color="#0000ff"></stop>
      <stop offset="1" stop-color="#800080"></stop>
    </linearGradient>
    <filter id="identity" x="0" y="0" width="100%" height="100%">
      <feComponentTransfer>
        <feFuncR type="identity"></feFuncR>
        <feFuncG type="identity"></feFuncG>
        <feFuncB type="identity"></feFuncB>
        <feFuncA type="identity"></feFuncA>
      </feComponentTransfer>
    </filter>
    <filter id="table" x="0" y="0" width="100%" height="100%">
      <feComponentTransfer>
        <feFuncR type="table" tableValues="0 0 1 1"></feFuncR>
        <feFuncG type="table" tableValues="1 1 0 0"></feFuncG>
        <feFuncB type="table" tableValues="0 1 1 0"></feFuncB>
      </feComponentTransfer>
    </filter>
    <filter id="discrete" x="0" y="0" width="100%" height="100%">
      <feComponentTransfer>
        <feFuncR type="discrete" tableValues="0 0 1 1"></feFuncR>
        <feFuncG type="discrete" tableValues="1 1 0 0"></feFuncG>
        <feFuncB type="discrete" tableValues="0 1 1 0"></feFuncB>
      </feComponentTransfer>
    </filter>
    <filter id="linear" x="0" y="0" width="100%" height="100%">
      <feComponentTransfer>
        <feFuncR type="linear" slope="0.5" intercept="0"></feFuncR>
        <feFuncG type="linear" slope="0.5" intercept="0.25"></feFuncG>
        <feFuncB type="linear" slope="0.5" intercept="0.5"></feFuncB>
      </feComponentTransfer>
    </filter>
    <filter id="gamma" x="0" y="0" width="100%" height="100%">
      <feComponentTransfer>
        <feFuncR type="gamma" amplitude="4" exponent="7" offset="0"></feFuncR>
        <feFuncG type="gamma" amplitude="4" exponent="4" offset="0"></feFuncG>
        <feFuncB type="gamma" amplitude="4" exponent="1" offset="0"></feFuncB>
      </feComponentTransfer>
    </filter>
  </defs>
  <g font-weight="bold">
    <text x="0" y="20">Default</text>
    <rect x="0" y="30" width="100%" height="20"></rect>
    <text x="0" y="70">Identity</text>
    <rect
 x="0"
 y="80"
 width="100%"
 height="20"
 style="filter:url(#identity)"></rect>
    <text x="0" y="120">Table lookup</text>
    <rect
 x="0"
 y="130"
 width="100%"
 height="20"
 style="filter:url(#table)"></rect>
    <text x="0" y="170">Discrete table lookup</text>
    <rect
 x="0"
 y="180"
 width="100%"
 height="20"
 style="filter:url(#discrete)"></rect>
    <text x="0" y="220">Linear function</text>
    <rect
 x="0"
 y="230"
 width="100%"
 height="20"
 style="filter:url(#linear)"></rect>
    <text x="0" y="270">Gamma function</text>
    <rect
 x="0"
 y="280"
 width="100%"
 height="20"
 style="filter:url(#gamma)"></rect>
  </g>
</svg>

```
### [CSS](#css)

css


```
rect {
  fill: url(#rainbow);
}

```
### [Result](#result)

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feComponentTransferElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feFuncA>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncA)
* [`<feFuncB>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncB)
* [`<feFuncG>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncG)
* [`<feFuncR>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncR)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feComponentTransfer",
        )

        

class Fecomposite(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feComposite>
=============

The **`<feComposite>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive performs the combination of two input images pixel-wise in image space using one of the Porter-Duff compositing operations: `over`, `in`, `atop`, `out`, `xor`, `lighter`, or `arithmetic`.


The table below shows each of these operations using an image of the MDN logo composited with a red circle:




| Operation | Description |
| --- | --- |
| over 
 over operator
 | 
 The source graphic defined by the `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)` attribute
 (the MDN logo) is placed over the destination graphic defined by the
 `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)` attribute (the circle).
 
 This is the *default operation*, which will be used if no
 operation or an unsupported operation is specified.
  |
| in 
 in operator
 | 
 The parts of the source graphic defined by the `in` attribute
 that overlap the destination graphic defined in the
 `in2` attribute, replace the destination graphic.
  |
| out 
 out operator
 | 
 The parts of the source graphic defined by the `in` attribute
 that fall outside the destination graphic defined in the
 `in2` attribute, are displayed.
  |
| atop 
 atop operator
 | 
 The parts of the source graphic defined in the
 `in` attribute, which overlap the destination graphic defined
 in the `in2` attribute, replace the destination graphic. The
 parts of the destination graphic that do not overlap with the source
 graphic stay untouched.
  |
| xor 
 xor operator
 | 
 The non-overlapping regions of the source graphic defined in the
 `in` attribute and the destination graphic defined in the
 `in2` attribute are combined.
  |
| lighter 
 lighter operator
 | 
 The sum of the source graphic defined in the `in` attribute
 and the destination graphic defined in the `in2` attribute is
 displayed.
  |
| 
 arithmetic
 
 arithmetic operator
 | 
 The `arithmetic` operation is useful for combining the
 output from the [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting) and
 [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting) filters with texture
 data. If the `arithmetic` operation is chosen, each result
 pixel is computed using the following formula:
 

```
result = k1*i1*i2 + k2*i1 + k3*i2 + k4
```

where:* `i1` and `i2` indicate the corresponding pixel
 channel values of the input image, which map to
 `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)` and `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)` respectively
* `[k1](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k1)`, `[k2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k2)`,
 `[k3](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k3)`, and `[k4](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k4)` indicate the
 values of the attributes with the same name.
 |

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`: First input for the given filter primitive.
* `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)`: Second input for the given filter primitive (works the same as the `in` attribute).
* `[operator](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/operator)`: `over` | `in` | `out` | `atop` | `xor` | `lighter` | `arithmetic`
* `[k1](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k1)`, `[k2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k2)`, `[k3](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k3)`, `[k4](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/k4)`: Values used for calculating the result pixel in `arithmetic` `[operator](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/operator)` filter primitives.
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFECompositeElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFECompositeElement) interface.

[Example](#example)
-------------------

This example defines filters for each of the supported operations (`over`, `atop`, `lighter`, etc.), which composite an input `SourceGraphic` with an image of the MDN logo. The filters are each applied to a circle element, which is then used as the `SourceGraphic`.



**Note:** `BackgroundImage` cannot be used as a compositing source on modern browsers, so we can't define a filter that composites using whatever pixels happen to be under the filter as one of the sources. The approach taken here is a [workaround because we can't use `BackgroundImage`](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in#workaround_for_backgroundimage).


### [SVG](#svg)

html


```
<svg
 style="width:800px; height:400px; display: inline;"
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <filter id="imageOver">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="over" />
    </filter>
    <filter id="imageIn">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="in" />
    </filter>
    <filter id="imageOut">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="out" />
    </filter>
    <filter id="imageAtop">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="atop" />
    </filter>
    <filter id="imageXor">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="xor" />
    </filter>
    <filter id="imageArithmetic">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite
 in2="SourceGraphic"
 operator="arithmetic"
 k1="0.1"
 k2="0.2"
 k3="0.3"
 k4="0.4" />
    </filter>
    <filter id="imageLighter">
      <feImage
 xlink:href="mdn\_logo\_only\_color.png"
 x="10px"
 y="10px"
 width="160px" />
      <feComposite in2="SourceGraphic" operator="lighter" />
    </filter>
  </defs>
  <g transform="translate(0,25)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageOver)" />
    <text x="80" y="-5">over</text>
  </g>
  <g transform="translate(200,25)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageIn)" />
    <text x="80" y="-5">in</text>
  </g>
  <g transform="translate(400,25)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageOut)" />
    <text x="80" y="-5">out</text>
  </g>
  <g transform="translate(600,25)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageAtop)" />
    <text x="80" y="-5">atop</text>
  </g>
  <g transform="translate(0,240)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageXor)" />
    <text x="80" y="-5">xor</text>
  </g>
  <g transform="translate(200,240)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageArithmetic)" />
    <text x="70" y="-5">arithmetic</text>
  </g>
  <g transform="translate(400,240)">
    <circle
 cx="90px"
 cy="80px"
 r="70px"
 fill="#c00"
 style="filter:url(#imageLighter)" />
    <text x="80" y="-5">lighter</text>
  </g>
</svg>

```
### [Result](#result)

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feCompositeElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feComposite",
        )

        

class Feconvolvematrix(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feConvolveMatrix>
==================

The **`<feConvolveMatrix>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive applies a matrix convolution filter effect. A convolution combines pixels in the input image with neighboring pixels to produce a resulting image. A wide variety of imaging operations can be achieved through convolutions, including blurring, edge detection, sharpening, embossing and beveling.


A matrix convolution is based on an n-by-m matrix (the convolution kernel) which describes how a given pixel value in the input image is combined with its neighboring pixel values to produce a resulting pixel value. Each result pixel is determined by applying the kernel matrix to the corresponding source pixel and its neighboring pixels. The basic convolution formula which is applied to each color value for a given pixel is:



 COLORX,Y = (
 SUM I=0 to [[orderY](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-1] {
 SUM J=0 to [[orderX](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-1] {
 SOURCE X-[targetX](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetXAttribute)+J, Y-[targetY](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetYAttribute)+I \* [kernelMatrix](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementKernelMatrixAttribute)[orderX](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-J-1, [orderY](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-I-1
 }
 }
 ) / [divisor](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementDivisorAttribute) + [bias](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementBiasAttribute) \* ALPHAX,Y



where "orderX" and "orderY" represent the X and Y values for the ['order'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute) attribute, "targetX" represents the value of the ['targetX'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetXAttribute) attribute, "targetY" represents the value of the ['targetY'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetYAttribute) attribute, "kernelMatrix" represents the value of the ['kernelMatrix'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementKernelMatrixAttribute) attribute, "divisor" represents the value of the ['divisor'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementDivisorAttribute) attribute, and "bias" represents the value of the ['bias'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementBiasAttribute) attribute.


Note in the above formulas that the values in the kernel matrix are applied such that the kernel matrix is rotated 180 degrees relative to the source and destination images in order to match convolution theory as described in many computer graphics textbooks.


To illustrate, suppose you have an input image which is 5 pixels by 5 pixels, whose color values for one of the color channels are as follows:



```
0    20  40 235 235
100 120 140 235 235
200 220 240 235 235
225 225 255 255 255
225 225 255 255 255

```

and you define a 3-by-3 convolution kernel as follows:



```
1 2 3
4 5 6
7 8 9

```

Let's focus on the color value at the second row and second column of the image (source pixel value is 120). Assuming the simplest case (where the input image's pixel grid aligns perfectly with the kernel's pixel grid) and assuming default values for attributes ['divisor'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementDivisorAttribute), ['targetX'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetXAttribute) and ['targetY'](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetYAttribute), then resulting color value will be:



```
(9*0   + 8*20  + 7*40 +
 6*100 + 5*120 + 4*140 +
 3*200 + 2*220 + 1*240) / (9+8+7+6+5+4+3+2+1)

```
[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`
* `[order](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/order)`
* `[kernelMatrix](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/kernelMatrix)`
* `[divisor](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/divisor)`
* `[bias](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/bias)`
* `[targetX](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/targetX)`
* `[targetY](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/targetY)`
* `[edgeMode](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/edgeMode)`
* `[kernelUnitLength](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/kernelUnitLength)`
* `[preserveAlpha](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/preserveAlpha)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEConvolveMatrixElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEConvolveMatrixElement) interface.

[Example](#example)
-------------------

### [SVG](#svg)

html


```
<svg
 width="200"
 height="200"
 viewBox="0 0 200 200"
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <filter id="emboss">
      <feConvolveMatrix
 kernelMatrix="3 0 0
 0 0 0
 0 0 -3" />
    </filter>
  </defs>

  <image
 href="mdn.svg"
 x="0"
 y="0"
 height="200"
 width="200"
 style="filter:url(#emboss);" />
</svg>

```
### [Result](#result)

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feConvolveMatrixElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feConvolveMatrix",
        )

        

class Fediffuselighting(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feDiffuseLighting>
===================

The **`<feDiffuseLighting>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive lights an image using the alpha channel as a bump map. The resulting image, which is an RGBA opaque image, depends on the light color, light position and surface geometry of the input bump map.


The light map produced by this filter primitive can be combined with a texture image using the multiply term of the `arithmetic` operator of the [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite) filter primitive. Multiple light sources can be simulated by adding several of these light maps together before applying it to the texture image.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of [descriptive elements](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#descriptive) and exactly one [light source element](https://developer.mozilla.org//en-US/docs/Web/SVG/Element#lightsource), in any order. |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`
* `[surfaceScale](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/surfaceScale)`
* `[diffuseConstant](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/diffuseConstant)`
* `[kernelUnitLength](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/kernelUnitLength)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEDiffuseLightingElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEDiffuseLightingElement) interface.

[Example](#example)
-------------------

The following example show the effect of the `<feDiffuseLighting>` element on a circle with each light source available. Each time, the light comes from the upper left corner.


html


```
<svg width="440" height="140" xmlns="http://www.w3.org/2000/svg">
  <!-- No light is applied -->
  <text text-anchor="middle" x="60" y="22">No Light</text>
  <circle cx="60" cy="80" r="50" fill="green" />

  <!-- the light source is a fePointLight element -->
  <text text-anchor="middle" x="170" y="22">fePointLight</text>
  <filter id="lightMe1">
    <feDiffuseLighting in="SourceGraphic" result="light" lighting-color="white">
      <fePointLight x="150" y="60" z="20" />
    </feDiffuseLighting>

    <feComposite
 in="SourceGraphic"
 in2="light"
 operator="arithmetic"
 k1="1"
 k2="0"
 k3="0"
 k4="0" />
  </filter>

  <circle cx="170" cy="80" r="50" fill="green" filter="url(#lightMe1)" />

  <!-- the light source is a feDistantLight element -->
  <text text-anchor="middle" x="280" y="22">feDistantLight</text>
  <filter id="lightMe2">
    <feDiffuseLighting in="SourceGraphic" result="light" lighting-color="white">
      <feDistantLight azimuth="240" elevation="20" />
    </feDiffuseLighting>

    <feComposite
 in="SourceGraphic"
 in2="light"
 operator="arithmetic"
 k1="1"
 k2="0"
 k3="0"
 k4="0" />
  </filter>

  <circle cx="280" cy="80" r="50" fill="green" filter="url(#lightMe2)" />

  <!-- the light source is a feSpotLight source -->
  <text text-anchor="middle" x="390" y="22">feSpotLight</text>
  <filter id="lightMe3">
    <feDiffuseLighting in="SourceGraphic" result="light" lighting-color="white">
      <feSpotLight
 x="360"
 y="5"
 z="30"
 limitingConeAngle="20"
 pointsAtX="390"
 pointsAtY="80"
 pointsAtZ="0" />
    </feDiffuseLighting>

    <feComposite
 in="SourceGraphic"
 in2="light"
 operator="arithmetic"
 k1="1"
 k2="0"
 k3="0"
 k4="0" />
  </filter>

  <circle cx="390" cy="80" r="50" fill="green" filter="url(#lightMe3)" />
</svg>

```

Expected rendering:



![Expected rendering for the example](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting/fediffuselighting.png)



Live rendering:

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1 # feDiffuseLightingElement](https://drafts.fxtf.org/filter-effects/#feDiffuseLightingElement) |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feDistantLight>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDistantLight)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<fePointLight>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/fePointLight)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feSpotLight>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpotLight)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feDiffuseLighting",
        )

        

class Fedisplacementmap(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feDisplacementMap>
===================

The **`<feDisplacementMap>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive uses the pixel values from the image from `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)` to spatially displace the image from `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`.


The formula for the transformation looks like this:


`P'(x,y) â P(x + scale * (XC(x,y) - 0.5), y + scale * (YC(x,y) - 0.5))`


where `P(x,y)` is the input image, `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`, and `P'(x,y)` is the destination. `XC(x,y)` and `YC(x,y)` are the component values of the channel designated by `[xChannelSelector](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/xChannelSelector)` and `[yChannelSelector](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/yChannelSelector)`.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`
* `[in2](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in2)`
* `[scale](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/scale)`
* `[xChannelSelector](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/xChannelSelector)`
* `[yChannelSelector](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/yChannelSelector)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEDisplacementMapElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEDisplacementMapElement) interface.

[Example](#example)
-------------------

html


```
<svg
 width="200"
 height="200"
 viewBox="0 0 220 220"
 xmlns="http://www.w3.org/2000/svg">
  <filter id="displacementFilter">
    <feTurbulence
 type="turbulence"
 baseFrequency="0.05"
 numOctaves="2"
 result="turbulence" />
    <feDisplacementMap
 in2="turbulence"
 in="SourceGraphic"
 scale="50"
 xChannelSelector="R"
 yChannelSelector="G" />
  </filter>

  <circle cx="100" cy="100" r="100" style="filter: url(#displacementFilter)" />
</svg>

```
[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feDisplacementMapElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feFlood>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFlood)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feDisplacementMap",
        )

        

class Fedistantlight(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feDistantLight>
================

The **`<feDistantLight>`** filter primitive defines a distant light source that can be used within a lighting filter primitive: [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting) or [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting).

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Light source element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
### [Specific attributes](#specific_attributes)

* `[azimuth](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/azimuth)`
* `[elevation](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/elevation)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEDistantLightElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEDistantLightElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feDistantLightElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<fePointLight>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/fePointLight)
* [`<feSpotLight>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpotLight)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feDistantLight",
        )

        

class Fedropshadow(SVG):
    """



In this article
---------------

* [Example](#example)
* [Attributes](#attributes)
* [Usage notes](#usage_notes)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
<feDropShadow>
==============

The SVG **`<feDropShadow>`** filter primitive creates a drop shadow of the input image. It can only be used inside a [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter) element.



**Note:** The drop shadow color and opacity can be changed by using the `[flood-color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-color)` and `[flood-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-opacity)` presentation attributes.


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
<svg viewBox="0 0 30 10" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow">
      <feDropShadow dx="0.2" dy="0.4" stdDeviation="0.2" />
    </filter>
    <filter id="shadow2">
      <feDropShadow dx="0" dy="0" stdDeviation="0.5" flood-color="cyan" />
    </filter>
    <filter id="shadow3">
      <feDropShadow
 dx="-0.8"
 dy="-0.8"
 stdDeviation="0"
 flood-color="pink"
 flood-opacity="0.5" />
    </filter>
  </defs>

  <circle cx="5" cy="50%" r="4" style="fill:pink; filter:url(#shadow);" />

  <circle cx="15" cy="50%" r="4" style="fill:pink; filter:url(#shadow2);" />

  <circle cx="25" cy="50%" r="4" style="fill:pink; filter:url(#shadow3);" />
</svg>

```
[Attributes](#attributes)
-------------------------


`[dx](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/dx)`


 This attribute defines the x offset of the drop shadow.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number); *Default value*: `2`; *Animatable*: **yes**




`[dy](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/dy)`


 This attribute defines the y offset of the drop shadow.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number); *Default value*: `2`; *Animatable*: **yes**




`[stdDeviation](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/stdDeviation)`


 This attribute defines the standard deviation for the blur operation in the drop shadow.
 *Value type*: [**<number>**](https://developer.mozilla.org//en-US/docs/Web/SVG/Content_type#number); *Default value*: `2`; *Animatable*: **yes**




### [Global attributes](#global_attributes)


[Core Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Core)

Most notably: `[id](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/id)`



[Styling Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Styling)
`[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`, `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
[Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filters_attributes)
`[height](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/height)`, `[in](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/in)`, `[result](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/result)`, `[x](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/x)`, `[y](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/y)`, `[width](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/width)`
[Presentation Attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/Presentation)

Most notably: `[flood-color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-color)`, `[flood-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-opacity)`



[Usage notes](#usage_notes)
---------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<script>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/script), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feDropShadowElement)  |

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
            tagName="feDropShadow",
        )

        

class Feflood(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Example](#example)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feFlood>
=========

The **`<feFlood>`** SVG filter primitive fills the filter subregion with the color and opacity defined by `[flood-color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-color)` and `[flood-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-opacity)`.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | Filter primitive element |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Presentation attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#presentation_attributes)
* [Filter primitive attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#filter_primitive_attributes)
* `[class](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/class)`
* `[style](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/style)`
### [Specific attributes](#specific_attributes)

* `[flood-color](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-color)`
* `[flood-opacity](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute/flood-opacity)`
[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEFloodElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEFloodElement) interface.

[Example](#example)
-------------------

### [HTML](#html)

html


```
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <defs>
    <filter id="floodFilter" filterUnits="userSpaceOnUse">
      <feFlood
 x="50"
 y="50"
 width="100"
 height="100"
 flood-color="green"
 flood-opacity="0.5" />
    </filter>
  </defs>

  <use style="filter: url(#floodFilter);" />
</svg>

```
### [Result](#result)

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feFloodElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feBlend>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feBlend)
* [`<feColorMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feColorMatrix)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feComposite>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComposite)
* [`<feConvolveMatrix>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feConvolveMatrix)
* [`<feDiffuseLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDiffuseLighting)
* [`<feDisplacementMap>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feDisplacementMap)
* [`<feGaussianBlur>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feGaussianBlur)
* [`<feImage>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feImage)
* [`<feMerge>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMerge)
* [`<feMorphology>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feMorphology)
* [`<feOffset>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feOffset)
* [`<feSpecularLighting>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feSpecularLighting)
* [`<feTile>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTile)
* [`<feTurbulence>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feTurbulence)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feFlood",
        )

        

class Fefunca(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feFuncA>
=========

The **`<feFuncA>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive defines the transfer function for the alpha component of the input graphic of its parent [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer) element.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | None |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Transfer function attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#transfer_function_attributes)
### [Specific attributes](#specific_attributes)

None.

[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEFuncAElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEFuncAElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feFuncAElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feFuncR>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncR)
* [`<feFuncB>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncB)
* [`<feFuncG>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncG)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feFuncA",
        )

        

class Fefuncb(SVG):
    """



In this article
---------------

* [Usage context](#usage_context)
* [Attributes](#attributes)
* [DOM Interface](#dom_interface)
* [Specifications](#specifications)
* [Browser compatibility](#browser_compatibility)
* [See also](#see_also)
<feFuncB>
=========

The **`<feFuncB>`** [SVG](https://developer.mozilla.org//en-US/docs/Web/SVG) filter primitive defines the transfer function for the blue component of the input graphic of its parent [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer) element.

[Usage context](#usage_context)
-------------------------------



|  |  |
| --- | --- |
| Categories | None |
| Permitted content | Any number of the following elements, in any order:[`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate), [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set) |

[Attributes](#attributes)
-------------------------

### [Global attributes](#global_attributes)

* [Core attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#core_attributes)
* [Transfer function attributes](https://developer.mozilla.org//en-US/docs/Web/SVG/Attribute#transfer_function_attributes)
### [Specific attributes](#specific_attributes)

None.

[DOM Interface](#dom_interface)
-------------------------------

This element implements the [`SVGFEFuncBElement`](https://developer.mozilla.org//en-US/docs/Web/API/SVGFEFuncBElement) interface.

[Specifications](#specifications)
---------------------------------



| Specification |
| --- |
| [Filter Effects Module Level 1](https://drafts.fxtf.org/filter-effects/#feFuncBElement)  |

[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser with JavaScript enabled. Enable JavaScript to view data.

[See also](#see_also)
---------------------

* [`<filter>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/filter)
* [`<animate>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/animate)
* [`<set>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/set)
* [`<feComponentTransfer>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feComponentTransfer)
* [`<feFuncA>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncA)
* [`<feFuncR>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncR)
* [`<feFuncG>`](https://developer.mozilla.org//en-US/docs/Web/SVG/Element/feFuncG)
* [SVG tutorial: Filter effects](https://developer.mozilla.org//en-US/docs/Web/SVG/Tutorial/Filter_effects)


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
            tagName="feFuncB",
        )

        

