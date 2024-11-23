replaceDict = {
    "classs": "class",
    "class_": "class",
    "forr": "for",
    "for_": "for",
    "accessskey": "accesskey",
    "access_key": "accesskey",
    "aria_lable": "aria-label",
    "arialable": "aria-label",
    "aria_describedby": "aria-describedby",
    "ariadescribedby": "aria-describedby",
    "iss": "is",
    "is_": "is",
    "doctype": "!DOCTYPE HTML",
    "typee": "type",
    "type_": "type",
    "aria_expanded": "aria-expanded",
    "ariaexpanded": "aria-expanded",
    "asyncc": "async",
    "async_": "async",
    "data_expandable": "data-expandable",
    "dataexpandable": "data-expandable",
    "data_parent": "data-parent",
    "dataparent": "data-parent",
    "data_child": "data-child",
    "datachild": "data-child",
    "data_nl": "data-nl",
    "datanl": "data-nl",
    "data_sm": "data-sm",
    "datasm": "data-sm",
    "data_mode": "data-mode",
    "datamode": "data-mode",
    "data_gfg_action": "data-gfg-action",
    "data_expanded": "data-expanded",
    "data_show": "data-show",
    "data_article_slider": "data-article-slider",
    "data_bookmark_value": "data-bookmark-value",
    "data_type": "data-type",
    "aria_hidden": "aria-hidden",
    "data_icon": "data-icon",
    "data_rating": "data-rating",
    "datagfg_action": "data-gfg-action",
    "dataexpanded": "data-expanded",
    "datashow": "data-show",
    "dataarticle_slider": "data-article-slider",
    "databookmark_value": "data-bookmark-value",
    "datatype": "data-type",
    "ariahidden": "aria-hidden",
    "dataicon": "data-icon",
    "datarating": "data-rating",
    "fromm": "from",
    "from_": "from",
    "inn": "in",
    "in_": "in",
    "as_": "as",
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
