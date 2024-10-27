def class_to_lower(name: str):
    if len(name) < 2:
        return name.lower()

    result = name[0].lower()
    for i in name[1:]:
        if i.isupper():
            result += "-" + i.lower()
        else:
            result += i

    return result


def lower_to_class(name: str):
    name = name.replace(".", "")
    name = name.replace("-", " ")
    name = name.title()
    name = name.replace(" ", "")
    return name
