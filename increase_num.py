
import sublime
import sublime_plugin


class InsertIncreaseNumCommand(sublime_plugin.TextCommand):
	def run(self, edit, index):
		for region in self.view.sel():
			pos = region.end()
			self.view.insert(edit, pos, str(index))
			index += 1


class IncreaseNumCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		index = 1
		window = sublime.active_window()

		def on_done(x):
			window = sublime.active_window()
			edit
			try:
				index = int(x)
			except:
				index = 1
			window.run_command("insert_increase_num", {"index" : index})
			
		window.show_input_panel("Beginning Index ", "", on_done, None, None)
