from argparse import ArgumentParser
from pprint import pprint
import printy


def style_print(text: str, options: str, disable_gimme: bool = False):
    if text == "?gimme" and not disable_gimme:
        pprint({"COLORS": printy.COLORS, "FORMATS": printy.FORMATS})
    else:
        printy.printy(text, options)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "text",
        help="Text to print. Use double quotes if you want to print a string with spaces",
    )
    parser.add_argument(
        "options",
        nargs="?",
        help=r"""Options to pass to printy. Use double quotes if you want to use background colors
        or colors with greater than or smaller than signs. Example: light red on blue -> 'r>{b}'. Also see:
        https://github.com/egeakman/style-print#usage""",
    )
    parser.add_argument(
        "-d",
        "--disable-gimme",
        action="store_true",
        help="If you are planning to print '?gimme', use this flag to disable the default behavior",
    )
    args = parser.parse_args()

    style_print(args.text, args.options, args.disable_gimme)


if __name__ == "__main__":
    raise NotImplementedError("This module is not meant to be run directly")
