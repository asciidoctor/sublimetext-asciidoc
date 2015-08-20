# AsciiDoc Package for SublimeText 3

This package provides more complete and up-to-date syntax highlighting, snippets and other goodies for AsciiDoc editing in [SublimeText 3](http://www.sublimetext.com/3).

TODO

## Features

### Keymaps

* Asterisks (strong), underscores (emphasis), backticks (monospaced), English quotation marks, and Czech quotation marks are autopaired and will wrap selected text.
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

| Name               | Trigger       |
| ------------------ | ------------- |
| Button             | btn⇥         |
| Comment Block      | //⇥          |
| Document Title     | h0⇥          |
| Example Block      |               |
| Footnote Reference | fnr⇥         |
| Footnote           | fn⇥          |
| Image              | img⇥         |
| Keyboard Shortcut  | kbd⇥         |
| Listing Block      | --⇥          |
| Passthrough Block  |               |
| Quote Block        | __⇥          |
| Section Title 1–5  | h1⇥, …, h5⇥ |
| Sidebar block      |               |
| Table              | |=⇥          |

### Others

* Displays document and section titles in the local symbol list (<kbd>Ctrl</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>R</kbd>) and the global symbol list (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>R</kbd>).
    - In the local symbol list, titles are nicely indented.
    - In the global symbol list, titles will start with `=`, so you will know they belong to AsciiDoc files at a glance. Also they will be on top of the list because of the presedence of `=`.
* Defines [comment markers](http://docs.sublimetext.info/en/latest/reference/comments.html), so you can use [default commands](http://docs.sublimetext.info/en/latest/reference/comments.html#related-keyboard-shortcuts) to comment and uncomment lines of text.
* Provides completions for attributes (built-in and locally defined) and cross references (local anchors and titles).


## Installation

Note: If you have installed the [AsciiDoc](https://packagecontrol.io/packages/AsciiDoc) package, then you should remove it, or manually assign `.adoc` extension to the Asciidoctor plugin.

### Package Control

The easiest way to install this plugin is to use the [Package Control](https://packagecontrol.io/installation) plugin.

1. [Install Package Control](https://packagecontrol.io/installation), if you don’t have it already.
2. Open the Command Palette (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>P</kbd>, or <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd>), type “Install package” and hit Enter.
3. Search for “Asciidoctor” and hit Enter.

### Manually

You can also install this plugin manually from GitHub if you want, although Package Control automates just that.

1. Go to your Packages subdirectory under the ST3’s data directory:
    * OS X: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`
    * Linux: `~/.config/sublime-text-3/Packages/`
    * Windows: `%APPDATA%\Sublime Text 3\Packages\`
2. Clone this repository here into subdirectory Asciidoctor:

        git clone https://github.com/asciidoctor/sublimetext-asciidoc.git Asciidoctor
3. Restart SublimeText.


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
