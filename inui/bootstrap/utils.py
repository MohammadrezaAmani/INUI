def bs_class_to_lower(name: str):
    name = name.replace("_", "-")
    return name


def bs_lower_to_class(name: str):
    name = name.replace(".", "")
    name = name.replace("-", "_")
    name = name.replace("/", "_")
    name = name.replace(":", "_")
    return name
