def _find_quote(string: str):
    if '"' in string and '"' in string:
        string = string.replace('"', '\\"')
        string = string.replace("'", "\\'")
        return f'"{string}"'
    elif "'" in string:
        return f'"{string}"'

    elif '"' in string:
        return f"'{string}'"
    else:
        return f'"{string}"'
