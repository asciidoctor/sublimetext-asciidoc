#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re
from sublimedsl.keymap import *


def asciidoc_macro(name):
    return "res://Packages/Asciidoctor/Macros/%s.sublime-macro" % name


def builtin_macro(name):
    return "res://Packages/Default/%s.sublime-macro" % name


def escape(string):
    """ Escape regex special characters (``re.escape`` escapes all non-ASCII). """
    return re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\|\:\-])', r'\\\1', string)


def paired_chars(left, right):
    """ Create common key bindings for paired characters. """
    return Keymap(
        # When you type the left char, then the right char is automatically
        # inserted after the cursor.
        bind(left)
            .to('insert_snippet', contents="%s$0%s" % (left, right))
            .when('selection_empty').true()
            .also('following_text').regex_contains('^(?:$|\\s|\\)|\\]|\\}|\\*|_|\\`)')
            .also('preceding_text').regex_contains('(?:^|\\s|\\(|\\[|\\]|\\*|_|\\`)$')
            .also('eol_selector').not_equal('string.quoted.single'),

        # When you select some text and type the left char, then the selection
        # is wrapped in the pair of chars.
        bind(left)
            .to('insert_snippet', contents="%s${0:$SELECTION}%s" % (left, right))
            .when('selection_empty').false(),

        # When the cursor is before the right char and you type the right char,
        # then the cursor is just moved beyond the right char.
        bind(right)
            .to('move', by='characters', forward=True)
            .when('selection_empty').true()
            .also('following_text').regex_contains("^%s" % escape(right)),

        # When the cursor is between the left and the right char and you hit
        # backspace, then both chars are deleted.
        bind('backspace')
            .to('run_macro_file', file=builtin_macro('Delete Left Right'))
            .when('selection_empty').true()
            .also('preceding_text').regex_contains("%s$" % escape(left))
            .also('following_text').regex_contains("^%s" % escape(right)),

        common_context=[
            context('setting.auto_match_enabled').true()
        ]
    )  # nopep8


def delete_paired_chars(left, right):
    """
    When the cursor is between the left and the right char and you hit
    backspace, then both chars are deleted and auto complete list closed.
    """
    return [
        bind('backspace')
            .to('asciidoc_run_commands', commands=[
                ['run_macro_file', {'file': builtin_macro('Delete Left Right')}],
                ['hide_auto_complete']])
            .when('setting.auto_match_enabled').true()
            .also('selection_empty').true()
            .also('preceding_text').regex_contains("%s$" % escape(left))
            .also('following_text').regex_contains("^%s" % escape(right))
    ]  # nopep8


def replace_following_asterisk(key, replacement):
    """
    When the line contains just two asterisks, possibly preceded by whitespaces,
    the cursor is between them, and space or tab is pressed, then the following
    asterisk is replaced with space, or tab.

    The goal is to remove undesirably paired asterisk when creating a list
    instead of a strong text.
    """
    return [
        bind(key)
            .to('replace_following_character', replacement=replacement)
            .when('setting.auto_match_enabled').true()
            .also('selection_empty').true()
            .also('preceding_text').regex_match('^\\s*\\*$')
            .also('following_text').regex_match('^\\*$')
    ]  # nopep8


def indent_list_items(key, reverse=False):
    """ Indent or unindent (un)ordered list item(s). """
    return [
        # When the cursor is at EOL with an empty list item and the *key* is
        # pressed, then the list item is (un)indented by one level.
        bind(key)
            .to('asciidoc_indent_list_item', reverse=reverse)
            .when('selection_empty').true()
            .also('preceding_text').regex_match('^\\s*[*.-]+\\s+$')
            .also('following_text').regex_match('^$'),

        # When you select one or more list items and press the *key*, then the
        # selected items are (un)indented.
        bind(key)
            .to('asciidoc_indent_list_item', reverse=reverse)
            .when('selection_empty').false()
            .also('text').regex_contains('^\\s*[*.-]+\\s+')
    ]  # nopep8


Keymap(
    paired_chars('*', '*'),
    paired_chars('_', '_'),
    paired_chars('`', '`'),

    # English single and double quotes.
    paired_chars('‘', '’'),
    paired_chars('“', '”'),

    # Czech single and double quotes.
    paired_chars('„', '“'),
    paired_chars('‚', '‘'),

    # When you type "{", then "}" is automatically inserted after the cursor
    # and auto complete list is opened.
    # This is workaround to get both auto-pairing and auto-completion working.
    bind('{')
        .to('asciidoc_run_commands', commands=[
            ['insert_snippet', {'contents': '{$0}'}],
            ['auto_complete']])
        .when('setting.auto_match_enabled').true()
        .also('setting.auto_complete').true()
        .also('selection_empty').true(),

    delete_paired_chars('{', '}'),

    # When you type "<<", then ">>" is automatically inserted after the cursor
    # and auto complete list is opened.
    bind('<')
        .to('asciidoc_run_commands', commands=[
            ['insert_snippet', {'contents': '<$0>>'}],
            ['auto_complete']])
        .when('setting.auto_match_enabled').true()
        .also('setting.auto_complete').true()
        .also('selection_empty').true()
        .also('preceding_text').regex_contains('<$'),

    delete_paired_chars('<', '>'),

    replace_following_asterisk(' ', ' '),
    replace_following_asterisk('tab', '\t'),

    indent_list_items('tab'),
    indent_list_items('shift+tab', reverse=True),

    # When the cursor is at EOL with an (un)ordered list item and you hit
    # Enter, then the next item is added (with the same nesting level).
    bind('enter')
        .to('insert_snippet', contents='${TM_CURRENT_LINE/^(\\s*([*.\\-]+)(\\s+)).*/\n$2$3/}')
        .when('auto_complete_visible').false()
        .also('preceding_text').regex_contains('^\\s*([*.-]+)\\s+\\S'),

    # When the cursor is at EOL with a callout list item and you hit Enter,
    # then the next item is added (with incremented number).
    bind('enter')
        .to('asciidoc_extend_callouts_list')
        .when('selection_empty').true()
        .also('auto_complete_visible').false()
        .also('preceding_text').regex_contains('^\\s*<\\d+>\\s+\\S'),

    # When the cursor is at EOL with an empty list item (ordered, unordered or
    # callout) and you hit Enter, then the list item is removed.
    bind('enter')
        .to('asciidoc_run_commands', commands=[
            ['run_macro_file', {'file': builtin_macro('Delete Line')}],
            ['insert', {'characters': '\n'}],
            ['move', {'by': 'characters', 'forward': False}]])
        .when('auto_complete_visible').false()
        .also('preceding_text').regex_match('^\\s*(?:[*.-]+|<\\d+>)\\s+$')
        .also('following_text').regex_match('^\\s*$'),

    common_context=[
        context('selector').equal('text.asciidoc'),
        context('selector').not_equal('markup.raw')
    ],
    default_match_all=True

).dump()  # nopep8
