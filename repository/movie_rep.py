from domain.movie import *
from repository.repository_base import *

class MovieRep(Repository):
	"""
	Repository for movie.
	"""
	def __init__(self):
		Repository.__init__(self)

	"""
	Loads the data from a file called movies.rep
	"""
	def loadData(self):
		with open("movies.rep") as f:
			content = f.readlines()
		i = 0
		while i < len(content):
			title = content[i][:len(content[i]) - 1]
			description = content[i + 1][:len(content[i + 1]) - 1]
			tp = content[i + 2][:len(content[i + 2]) - 1]
			self._data.append(Movie(title, description, tp))
			i += 3

	"""
	Saves the data to a file called movies.rep
	"""
	def saveData(self):
		with open("movies.rep", 'w') as f:
			for movie in self._data:
				f.write(movie.getTitle() + '\n')
				f.write(movie.getDescription() + '\n')
				f.write(movie.getType() + '\n')

		"""
	Searches a movie by title.
	"""
	def search_title(self, title):
		for x in self._data:
			if x.getTitle() == title:
				return x
		return None

	"""
	Updates a movie by id.
	"""
	def update_movie(self, ID, title, description, movie_type):
		try:
			for x in self._data:
				if x.getID() == int(ID):
					x.setTitle(title)
					x.setDescription(description)
					x.setType(movie_type)
		except:
			raise ValueError("Invalid id!")
