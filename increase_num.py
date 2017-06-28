import sublime
import sublime_plugin


class InsertIncreaseNumberCommand(sublime_plugin.TextCommand):
    def run(self, edit, index):
        for region in self.view.sel():
            pos = region.end()
            self.view.insert(edit, pos, str(index))
            index += 1


class InsertIncreaseStringCommand(sublime_plugin.TextCommand):
    def run(self, edit, index):
        for region in self.view.sel():
            pos = region.end()
            self.view.insert(edit, pos, chr(index))
            index += 1


# ----------------------------------------------------------
def deal_input_str(input_str):
    try:
        return True, int(input_str)
    except:
        pass
    if len(input_str) != 1: return True, 1
    # a..z, A..Z
    ord_num = ord(input_str)
    if (ord_num >= 65 and ord_num <= 90) or (ord_num >= 97 and ord_num <= 122):
        return False, ord_num

    return (True, 1)


class IncreaseNumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()

        def on_done(input_str):
            status, index = deal_input_str(input_str)
            if status:
                window.run_command("insert_increase_number", {"index": index})
            else:
                window.run_command("insert_increase_string", {"index": index})

        window.show_input_panel("Beginning Index ", "", on_done, None, None)
