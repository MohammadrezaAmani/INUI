import argparse
import logging
import os
import sys

from inui.bases.utils import build
from inui.hotreload import hot_reload
from inui.toinui import convert

INUI_PATH = os.path.dirname(os.path.realpath(__file__))


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
COMMANDS = {
    "run": {
        "aliases": ["r"],
        "help": "Run Code.",
        "args": [
            {
                "name": "file",
                "help": "Target file in the format module:content or path.to.module:content",
            },
            {"name": "--host", "default": "127.0.0.1", "help": "Host to bind to"},
            {"name": "--port", "type": int, "default": 8000, "help": "Port to bind to"},
            {
                "name": "--reload",
                "type": bool,
                "default": True,
                "help": "Use Hot Reload",
            },
            {
                "name": "--time",
                "type": float,
                "default": 0.5,
                "help": "HotReload sleep time.",
            },
            {
                "name": "--static-dir",
                "type": str,
                "default": ".",
                "help": "Static files directory",
            },
        ],
    },
    "build": {
        "aliases": ["b"],
        "help": "Build the application",
        "args": [
            {"name": "file", "help": "Target file in the format module:content"},
            {
                "name": "--out",
                "required": False,
                "default": None,
                "help": "Output path",
            },
        ],
    },
    "convert": {
        "aliases": ["c"],
        "help": "Convert HTML to INUI.",
        "args": [
            {"name": "--html", "required": False, "help": "HTML content as a string"},
            {
                "name": "--url",
                "required": False,
                "help": "URL to fetch HTML content from",
            },
            {"name": "--file_name", "required": False, "help": "Path to the HTML file"},
            {
                "name": "--out",
                "required": False,
                "help": "Path to save the output file",
            },
            {
                "name": "--indent",
                "type": int,
                "required": False,
                "default": 4,
                "help": "Indentation level for output",
            },
        ],
    },
    "version": {"aliases": ["v"], "help": "Version of INUI.", "args": []},
}


def create_parser():
    parser = argparse.ArgumentParser(
        prog="inui",
        description="CLI for INUI: A Powerful and Highly Customizable Python Library for UI",
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available subcommands"
    )

    alias_map = {}
    for cmd, config in COMMANDS.items():
        alias_list = ", ".join(config["aliases"])
        subparser = subparsers.add_parser(
            cmd,
            help=f"{config['help']} (aliases: {alias_list})",
            description=f"{config['help']} (aliases: {alias_list})",
        )
        for arg in config["args"]:
            subparser.add_argument(arg.pop("name"), **arg)
        for alias in config["aliases"]:
            alias_map[alias] = cmd

    return parser, alias_map


def main():
    parser, alias_map = create_parser()

    if len(sys.argv) > 1 and sys.argv[1] in alias_map:
        sys.argv[1] = alias_map[sys.argv[1]]

    args = parser.parse_args()

    if args.command == "run":
        module_name, variable_name = args.file.split(":")

        hot_reload(
            host=args.host,
            port=args.port,
            module=module_name,
            variable_name=variable_name,
            sleep_time=args.time,
            static_dir=args.static_dir,
        )
    if args.command == "build":
        module_name, variable_name = args.file.split(":")
        build(
            module=module_name,
            variable=variable_name,
            out=args.out,
        )

    if args.command == "convert":
        convert(
            html=args.html,
            url=args.url,
            file_name=args.file_name,
            save_to=args.out,
            indent=args.indent,
        )
    if args.command == "version":
        print(__version__())


def __version__() -> str:
    config_path = os.path.join(INUI_PATH, "__version__")
    with open(config_path, encoding="utf-8") as f:
        text = f.read()
    return text.strip()


if __name__ == "__main__":
    main()
