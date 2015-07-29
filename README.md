# AsciiDoc Package for SublimeText

This package provides more complete and up-to-date syntax highlighting and snippets for [SublimeText 3](http://www.sublimetext.com/3).

TODO

## Features

### Keymaps

* Asterisks (strong), underscores (emphasis) and backticks (monospaced) are autopaired and will wrap selected text.
  - If you start an empty pair and hit backspace, both elements are deleted.
  - If you start an empty asterisks pair and hit <kbd>Space</kbd> or <kbd>Tab</kbd>, the right element is deleted (because you probably wanted to start a list, not a strong text).
* At the end of a (un)ordered list item, pressing <kbd>Enter</kbd> will automatically insert the new list item “bullet.”
  - Pressing <kbd>Enter</kbd> on the blank list item will remove it.
  - Pressing <kbd>Tab</kbd> on the blank list item, or selected item(s), will increase nesting level and indent it.
  - Pressing <kbd>Shift</kbd> <kbd>Tab</kbd> on the blank list item, or selected item(s), will decrease nesting level and unindent it.
  - You can disable indentation of list items in your settings file.
* At the end of a callouts list item, pressing <kbd>Enter</kbd> will automatically insert the new list item with incremented number.
  - Pressing <kbd>Enter</kbd> on the blank list item will remove it.

### Snippets

TODO

### Others

* Displays document and section titles in the local symbol list (<kbd>Ctrl</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>R</kbd>) and the global symbol list (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>R</kbd>).
  - In the local symbol list, titles are nicely indented.
  - In the global symbol list, titles will start with `=`, so you will know they belong to AsciiDoc files at a glance. Also they will be on top of the list because of the presedence of `=`.
* Defines [comment markers](http://docs.sublimetext.info/en/latest/reference/comments.html), so you can use [default commands](http://docs.sublimetext.info/en/latest/reference/comments.html#related-keyboard-shortcuts) to comment and uncomment lines of text.

## Acknowledgement

The syntax definition is based on [AsciiDoc-TextMate-2.tmbundle](https://github.com/mattneub/AsciiDoc-TextMate-2.tmbundle) by [Matt Neuburg](https://github.com/mattneub).

Most of the commands, keymaps and some text in this readme are based on (or inspired by) [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) package.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

This project is licensed under [MIT License](http://opensource.org/licenses/MIT/).
For the full text of the license, see the [LICENSE](LICENSE) file.
