class DataDict(dict):
	def __getattr__(s, name):
		if name in s:
			return s[name]
		else:
			raise AttributeError("No such attribute: " + name)

	def __setattr__(s, name, value):
		s[name] = value

	def __delattr__(s, name):
		if name in s:
			del s[name]
		else:
			raise AttributeError("No such attribute: " + name)
