# Copy the path of the current file to the clipboard.
# http://blog.codeclimate.com/blog/2012/06/21/sublime-text-2-for-ruby/

import sublime, sublime_plugin
import os

class CopyPathToClipboard(sublime_plugin.TextCommand):
  def run(self, edit):
    line_number, column = self.view.rowcol(self.view.sel()[0].begin())
    line_number += 1
    sublime.set_clipboard(self.view.file_name() + ":" + str(line_number))
