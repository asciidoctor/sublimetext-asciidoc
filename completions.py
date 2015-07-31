import sublime
from sublime_plugin import EventListener

# String that must be found in the syntax setting of the current view
# to active this plugin.
SYNTAX = 'Asciidoc'

# Selector that specifies the scope in which completions may be activated.
ADOC_SCOPE = 'text.asciidoc - source'

# Selector that specifies the scope in which attribute completions may
# be activated.
ATTR_SCOPE = 'variable.other'

# Name of the plugin's settings file.
SETTINGS_NAME = 'Asciidoctor.sublime-settings'

# Global list of built-in attributes to display in the completion list.
builtin_attrs = []


def plugin_loaded():
    """ Called by SublimeText when the plugin is loaded. """
    global builtin_attrs
    settings = sublime.load_settings(SETTINGS_NAME)
    builtin_attrs = sorted(settings.get('built_in_attributes'))


class AsciidocAttributeCompletions(EventListener):

    def on_query_completions(self, view, prefix, locations):
        """ Called by SublimeText when auto-complete pop-up box appears. """

        if SYNTAX not in view.settings().get('syntax'):
            return None
        if not all(self.should_trigger(view, loc) for loc in locations):
            return None

        local_attrs = (
            attr for attr, lno in self.declared_attrs(view)
            if attr not in builtin_attrs and min(cursors_line_num(view)) > lno)

        completions = completions_list(search(local_attrs, prefix), 'local')
        completions += completions_list(search(builtin_attrs, prefix), 'built-in')

        return (completions, sublime.INHIBIT_WORD_COMPLETIONS)

    def should_trigger(self, view, point):
        """ Return True if completions should be triggered at the given point. """
        return (view.match_selector(point, ADOC_SCOPE) and (
                view.match_selector(point, ATTR_SCOPE) or
                lsubstr(view, point) in [':', '{']))

    def declared_attrs(self, view):
        """ Get attributes declared in the document.

        Yields:
            Tuple of attribute name and line number where it's first declared.
        """
        regions = view.find_by_selector('support.variable.attribute.asciidoc')
        return sorted(
            {view.substr(region): view.rowcol(region.end())[0]
                for region in reversed(regions)}.items())


def completions_list(entries, hint):
    return [("%s\t%s" % (entry, hint), entry) for entry in entries]


def cursors_line_num(view):
    """ Return list of 0-based line numbers of the cursor(s). """
    return [view.rowcol(region.b)[0] for region in view.sel()]


def lsubstr(view, point):
    """ Return the character to the left of the point. """
    row, col = view.rowcol(point)
    return view.substr(point - 1) if col != 0 else ''


def search(collection, substring):
    return (item for item in collection if item.startswith(substring))
