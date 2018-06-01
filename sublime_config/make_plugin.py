import sublime
import sublime_plugin
import tempfile
import re
import os
import subprocess

#@ need to add build system: for ctrl+space
#@ check out to get ctrl+space output to sublime
#@ check out to get ctrl+enter output to sublime
#@ find a way to clean temp file

cmder_path = r'C:\Users\nessisbr\Desktop\cmder\vendor\conemu-maximus5\ConEmu\ConEmuC64.exe'
cmder_send = cmder_path + ' -GuiMacro:0 Paste(2, "exec(open(r\\"{}\\",\\"r\\").read())")'
cmder_enter = cmder_path + ' -GuiMacro:0 Keys("Return")'

class MakeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		selection = ''
		for region in view.sel():  
			if not region.empty():
				selection += view.substr(region) + '\n'

		path = tempfile.NamedTemporaryFile('w').name + '_'

		if not selection:
			selection = view.substr(view.line(view.sel()[0]))

		selection = trim(selection)
		open(path, 'w').write(selection)
		send_to_python(path)

		#@ find a way to clean temp file

def send_to_python(path):
	platform = sublime.platform()
	if platform == 'linux':
		send_to_tmux(path)
	else:
		send_to_cmder(path)

def send_to_tmux(path):
	pass

def send_to_cmder(path):
	path = path.replace('\\', '\\\\')
	cmd = cmder_send.format(path)
	print(cmd)

	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

	subprocess.check_call(cmd, startupinfo=startupinfo)
	subprocess.check_call(cmder_enter, startupinfo=startupinfo)

# trim
newline = '\n'
leading_space = re.compile('\s*')

def trim(s):
	lines = s.splitlines()

	# determine minimum indentation 
	maxindent = 1e9
	indent = maxindent
	for line in lines:
		if line.strip():
			current_indent = len(leading_space.findall(line)[0])
			indent = min(indent, current_indent)

	# remove indentation
	if indent < maxindent:
		trimmed = []
		for line in lines:
			if line.strip():
					trimmed.append(line[indent:])
			else:
					trimmed.append('')
	else:
		trimmed = lines

	# return a single string
	return '\n'.join(trimmed)
