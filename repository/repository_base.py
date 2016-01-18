class Repository:
	"""
	Base class for all repositories in this project.
	All _data objects must have a getID function.
	"""

	"""
	Repository constructor.
	"""
	def __init__(self):
		self._data = []

	"""
	Adds new item to the repo.
	"""
	def add(self, new):
		self._data.append(new)

	"""
	Removes an item by id.
	"""
	def remove_id(self, removeID):
		try:
			self._data = list(filter(lambda x: x.getID() != int(removeID), self._data))
		except:
			raise ValueError("Invalid id!")

	"""
	Changes id of an element.
	"""
	def change_id(self, oldID, newID):
		x = self.search_id(oldID)
		x.setID(newID)

	"""
	Returns the element with searchID.
	"""
	def search_id(self, searchID):
		try:
			return list(filter(lambda x: x.getID() == int(searchID), self._data))[0]
		except:
			return None

	"""
	String representation of the repository.
	"""
	def __str__(self):
		s = ""
		for x in self._data:
			s += str(x)
		return s

	"""
	Returns number of elements in data from repository.
	"""
	def __len__(self):
		return len(self._data)

	def __iter__(self):
		self._index = 0
		return list.__iter__(self._data)

	def next(self):
		self._index += 1
		if self._index == len(self):
			raise StopIteration
		return self._data[self._index]
