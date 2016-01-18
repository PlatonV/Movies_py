from domain.rental import *
from repository.repository_base import *

class RentalRep(Repository):
	"""
	Repository for rentals.
	"""
	def __init__(self):
		Repository.__init__(self)

	"""
	Loads the data from a file called rentals.rep
	"""
	def loadData(self):
		with open("rentals.rep") as f:
			content = f.readlines()
		i = 0
		while i < len(content):
			movieid = int(content[i])
			clientid = int(content[i + 1])
			self._data.append(Rental(clientid, movieid))
			i += 2

	"""
	Saves the data to a file called rentals.rep
	"""
	def saveData(self):
		with open("rentals.rep", 'w') as f:
			for rental in self._data:
				if rental.valid:
					f.write(str(rental.clientID) + '\n')
					f.write(str(rental.movieID) + '\n')

	"""
	Returns the state of rental by movieID
	"""
	def get_movie_state(self, movieID):
		try:
			for x in self.__data:
				if x.movie.getID() == int(movieID):
					return x.state
			return "Not rented"
		except:
			raise ValueError("Invalid id!")

	def __str__(self):
		s = ""
		for x in self._data:
			if x.valid == 1:
				s += str(x)
		return s
