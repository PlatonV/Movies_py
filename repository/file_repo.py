class FileRepository(Repository):
	"""
	Repository with added functionality.
	"""

	"""
	FileRepository constructor.
	"""
	def __init__(self, store):
		super.__init__(self)
		self._store_to_file = store

	"""
	Saves the data to a file.
	"""
	def saveToFile(self, filename):
		pass

	"""
	Loads the data from a file.
	"""
	def loadFromFile(self, filename):
		pass
