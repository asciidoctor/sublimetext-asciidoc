from sublime_plugin import TextCommand
import re


class ReplaceFollowingCharacterCommand(TextCommand):
    """ Replace the following character after the cursor with the replacement. """

    def run(self, edit, replacement=' '):
        self.view.run_command('right_delete')
        self.view.run_command('insert', {'characters': replacement})


class AsciidocIndentListItemCommand(TextCommand):
    """ (Un)indent an item or selected items of ordered and unordered list. """

    def run(self, edit, reverse=False):
        view = self.view
        indent_str = self._indent_str()

        # \1: single indentation (optional)
        # \2: remaining indentation followed by markers (except the last one)
        # \3: the last marker
        pattern = re.compile(r'^((?:%s)?)(\s*[*.-]*)([*.-])' % indent_str)

        def indent_line(line_region):
            if line_region.empty(): return ''
            replacement = r'\2' if reverse else indent_str + r'\1\2\3\3'
            return re.sub(pattern, replacement, view.substr(line_region))

        changes = [
            (region, indent_line(region))
            for regions in view.sel()
            for region in view.split_by_newlines(view.line(regions))]

        for item in reversed(changes):
            view.replace(edit, *item)

    def _indent_str(self):
        """ Get indentation string. """
        setting = self.view.settings().get

        if not setting('indent_lists', True):
            return ''
        elif setting('translate_tabs_to_spaces'):
            return setting('tab_size', 2) * ' '
        else:
            return '\t'


class AsciidocExtendCalloutsListCommand(TextCommand):

    def run(self, edit):
        view = self.view

        for selection in view.sel():
            line = view.substr(view.line(selection))
            indent, num = re.findall(r'^(\s*)<(\d+)>', line)[0]
            new_line = "\n%s<%d> " % (indent, int(num) + 1)

            view.insert(edit, selection.begin(), new_line)


class AsciidocRunCommandsCommand(TextCommand):
    """ Run multiple commands in chain. """

    def run(self, edit, commands):
        for command in commands:
            if isinstance(command, str):
                self.view.run_command(command)
            else:
                self.view.run_command(command[0], *command[1:])
