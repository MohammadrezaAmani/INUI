replaceDict = {
    "classs": "class",
    "forr": "for",
    "accessskey": "accesskey",
    "aria_lable": "aria-label",
    "aria_describedby": "aria-describedby",
    "iss": "is",
    "doctype": "!DOCTYPE HTML",
    "typee": "type",
    "aria_expanded": "aria-expanded",
    "asyncc": "async",
    "data_expandable": "data-expandable",
    "data_parent": "data-parent",
    "data_child": "data-child",
    "data_nl": "data-nl",
    "data_sm": "data-sm",
    "data_mode": "data-mode",
    "data_gfg_action": "data-gfg-action",
    "data_expanded": "data-expanded",
    "data_show": "data-show",
    "data_article_slider": "data-article-slider",
    "data_bookmark_value": "data-bookmark-value",
    "data_type": "data-type",
    "aria_hidden": "aria-hidden",
    "data_icon": "data-icon",
    "data_rating": "data-rating",
    "fromm": "from",
    "inn": "in",
}


def replace(string: str):
    if string in replaceDict:
        return replaceDict[string]
    string = string.replace("_", "-", string.count("-"))
    string = string.replace("___", " ", string.count(" "))
    string = string.replace("__", ":", string.count(":"))
    string = string.replace("_____", "*", string.count("*"))
    return string


def reverse_replace(string: str):
    for i in replaceDict:
        if string == replaceDict[i]:
            return i
    string = string.replace("-", "_", string.count("-"))
    string = string.replace(" ", "___", string.count(" "))
    string = string.replace(":", "__", string.count(":"))
    string = string.replace("*", "_____", string.count("*"))
    return string
