import sublime, sublime_plugin, Queue

class CustomElementsImporterCommand(sublime_plugin.TextCommand):

	def integrity_test(self, settings):

		for part in ["prefix_paths", "tag_paths", "tag_dependencies"]:
			if not settings.get(part):
				if sublime.ok_cancel_dialog("Settings file is corrupted!\nDo you want to revert it to default? (all changes in settings file will be lost!)"):
					pass
				else:
					return 1

		default_path = settings.get("default_path")
		if not default_path:
			sublime.error_message("Default path for custom elements is not defined. \nPlease define \"default_path\" in CustomElementsImporter's settings file.")
			return 1

		return 0


	def run(self, edit):
		settings = sublime.load_settings('CustomElementsImporter.sublime-settings')

		if self.integrity_test(settings) == 1:
			return

		default_path = settings.get("default_path")
		all_dependencies = settings.get("tag_dependencies")
		line_padding = self.view.sel()[0].a - self.view.line(self.view.sel()[0]).a
		line_bonus = " "*line_padding

		import_pattern = """{0}<link rel="import" href="{1}">{2}\n"""

		custom_elements = []
		already_imported = []
		self.view.find_all("<([^\-\s\/\>\<\!]+\-[^\s\/\>\<\!]+)", sublime.IGNORECASE, "$1", custom_elements)
		self.view.find_all("<link.+import.+?([^\-\s\/\>\<\!]+\-[^\s\/\>\<\!]+)\.html", sublime.IGNORECASE, "$1", already_imported)
		custom_elements = set(custom_elements)

		queue = Queue.Queue()

		for element in custom_elements:
			queue.put(element)

		custom_elements = []

		while not queue.empty():
			element = queue.get()
			custom_elements.append(element)
			dependencies = all_dependencies.get(element, [])
			for dependency in dependencies:
				queue.put(dependency)

		custom_elements = set(custom_elements)
		custom_elements = custom_elements.difference(set(already_imported))


		if len(custom_elements) == 0:
			sublime.status_message("All tags already imported!")

		string_to_insert = ""
		
		for element in custom_elements:
			print element
			prefix = element.split("-")[0]
			prefix_path = settings.get("tag_paths", {}).get(element)
			if prefix_path:
				string_to_insert += import_pattern.format(line_bonus, prefix_path)
			else:
				prefix_path = settings.get("prefix_paths", {}).get(prefix)
				real_path = (prefix_path if prefix_path else default_path)+"/{0}/{0}.html".format(element)
				string_to_insert += import_pattern.format(line_bonus, real_path, " <!-- based on default path -->" if not prefix_path else "")



		self.view.insert(edit, self.view.sel()[0].a - line_padding, string_to_insert)


		# for element_name in custom_elements:
		# 	string_to_insert += import_pattern.format(" "*line_padding, element_name)
		# 	print element_name
