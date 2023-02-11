# style-print

style-print is a utility CLI for formatting and printing text in different styles. It uses the ``printy`` library for color and formatting options.

## Installation

- Install the package using pip:

    ```bash
    pip install style-print
    ```

- Pre-commit hook:

    ```yaml
    repos:
      - repo: local
        hooks:
          - id: style-print
            name: style-print
            entry: style-print "This is a test" "r>UBI{b}"
            language: python
            additional_dependencies: ["style-print"]
    ```

## Usage

### Command line usage

style-print can be used from the command line using the ``style-print`` command. The script takes three arguments:
- *positional* ``text``: The text to be printed, or the ``?gimme`` command
- *optional* ``options``: The options for formatting the text
- *info* ``?gimme``: A special text that prints the available colors and formats
- *optional* ``-d`` or ``--disable-gimme``: A flag that disables the default behavior when the ``text`` is equal to ``"?gimme"``.

#### *Text*

The text argument is the text to be printed. If the text is equal to ``"?gimme"``, then the available colors and formats are printed. This behavior can be disabled by passing the ``-d`` or ``--disable-gimme`` flag. You must use double quotes if you want to print a string that contains spaces.

#### *Options*

The options argument is used to pass the formatting options to ``printy``. The options are passed in a string format. You must use double quotes if you want to use background colors or colors with greater than or smaller than signs. For example, to set the text color to light red and background color to blue and underlined-bold-italic, you can pass the option ``"r>UBI{b}"``.

For more information on the options available, see the ``printy`` library documentation: https://github.com/edraobdu/printy#list-1-flags

### In code usage

Just use the ``printy`` library itself. The ``style-print`` package is just a wrapper around the ``printy`` library for command line usage.

## Issues

If you run into any issues, please open an issue on the GitHub repository: https://github.com/egeakman/style-print/issues

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details
