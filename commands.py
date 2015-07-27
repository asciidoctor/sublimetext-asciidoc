from sublime_plugin import TextCommand

class ReplaceFollowingCharacterCommand(TextCommand):
    """ Replace the following character after the cursor with the replacement. """

    def run(self, edit, replacement=' '):
        self.view.run_command('right_delete')
        self.view.run_command('insert', { 'characters': replacement })
