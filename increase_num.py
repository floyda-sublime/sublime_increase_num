
import sublime
import sublime_plugin


class IncreaseNumEditCommand(sublime_plugin.TextCommand):
	def run(self, edit, index):
		for region in self.view.sel():
			pos = region.begin()
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
				print("It's not number")
				return

			window.run_command("increase_num_edit", {"index" : index})
			
		window.show_input_panel("Floyda", "1", on_done, None, None)
