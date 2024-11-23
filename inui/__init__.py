import logging
import importlib

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def build(module, variable, out: str | None, _print: bool = True):
    lib = importlib.import_module(module)

    rendered = str(getattr(lib, variable))
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(rendered)
            return rendered
    else:
        if _print:
            print(rendered)
        return rendered
