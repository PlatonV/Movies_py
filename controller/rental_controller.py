from copy import deepcopy
from domain.rental import Rental

class RentalController:
	"""
	Controller for rentals.
	"""
	def __init__(self, rental_rep, undo_controller):
		self._rental_rep = rental_rep
		self._undo_controller = undo_controller

	def setMC(self, movie_controller):
		self._movie_controller = movie_controller

	def setCC(self, client_controller):
		self._client_controller = client_controller

	"""
	Executes the given command.
	May return something or not depending on command type.
	"""
	def executeCommand(self, command):
		if command.getType() == "rent":
			command.setObj(self._add_rental(command.getParams()[0], command.getParams()[1]))
		if command.getType() == "return":
			command.setObj(self._remove_rental(command.getParams()[0]))
		if command.getType() == "search":
			return self.search_rental(command.getParams()[0])
		if command.getType() == "list":
			return str(self._rental_rep)
		if command.getType() in ["rent", "return"]:
			self._undo_controller.recordCommand(command)


	"""
	Updates rentals according to changes in client rep and movie repo.
	"""
	def update(self):
		for x in self._rental_rep:
			if (self._movie_controller.search_movie(x.movieID) == None) or (self._client_controller.search_client(x.clientID) == None):
				x.setInvalid()
			else:
				x.setValid()

	"""
	Adds rental with given client and movie.
	"""
	def _add_rental(self, clientID, movieID):
		rental = Rental(clientID, movieID)
		self._rental_rep.add(rental)
		return rental

	"""
	Removes rental with id rental_id.
	"""
	def _remove_rental(self, rental_id):
		rental = deepcopy(self.search_rental(rental_id))
		self._rental_rep.search_id(rental_id).setReturned()
		return rental

	"""
	Sets a rental as rented.
	"""
	def rerent_rental(self, rental_id):
		self._rental_rep.search_id(rental_id).setRented()

	"""
	Returns a rental by rental_id.
	"""
	def search_rental(self, rental_id):
		result = self._rental_rep.search_id(rental_id)
		return result

	"""
	Returns most rented movies.
	"""
	def most_rented(self):
		m = [0 for x in range(1000)]
		if len(self._rental_rep) == 0:
			return "No rented movies!"
		result = []
		maxID = -1
		for x in self._rental_rep:
			m[int(x.movieID)] += 1
		mi = -1
		mx = -1
		for i in range(1000):
			if m[i] > mx:
				mx = m[i]
				mi = i
		return self._movie_controller.search_movie(mi)
