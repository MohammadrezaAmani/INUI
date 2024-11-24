import importlib
import logging
import os


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


def get_module_content(module: str, variable_name: str):
    file_name = f"{module.replace('.', '/')}.py"
    try:
        module_name = os.path.splitext(os.path.basename(file_name))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return str(getattr(module, variable_name))
    except Exception as err:
        logging.error(f"Error getting file contents: {err}")
        return f"<h1>{err}</h1>"


def build(module, variable, out: str | None, _print: bool = True):
    rendered = get_module_content(module, variable)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(rendered)
            return rendered
    else:
        if _print:
            print(rendered)
        return rendered
