from domain.client import Client
from copy import deepcopy

class ClientController:
	"""
	Controller for clients.
	"""
	def __init__(self, client_rep, rental_controller, undo_controller):
		self._client_rep = client_rep
		self._rental_controller = rental_controller
		self._undo_controller = undo_controller

	"""
	Executes the given command.
	"""
	def executeCommand(self, command):
		if command.getType() == "add":
			if len(command.getParams()) == 2:
				command.setObj(self._add_client(command.getParams()[0], command.getParams()[1]))
			else:
				raise ValueError("Invalid parameters")
		elif command.getType() == "remove":
			if len(command.getParams()) == 1:
				command.setObj(self._remove_client(command.getParams()[0]))
			else:
				raise ValueError("Invalid parameters")
		elif command.getType() == "update":
			if len(command.getParams()) == 3:
				command.setPrevObj(self._update_client(command.getParams()[0], command.getParams()[1], command.getParams()[2]))
				command.setObj(self.search_client(int(command.getParams()[0])))
			else:
				raise ValueError("Invalid parameters")
		elif command.getType() == "search":
			if len(command.getParams()) == 1:
				return(self.search_client(command.getParams()[0]))
			else:
				raise ValueError("Invalid parameters")
		elif command.getType() == "list":
			return str(self._client_rep)
		if command.getType() in ["add", "remove", "update"]:
			self._undo_controller.recordCommand(command)

	"""
	Adds client with given name and CNP.
	"""
	def _add_client(self, name, CNP):
		client = Client(name, CNP)
		self._client_rep.add(client)
		self._rental_controller.update()
		return client

	def sadd_client(self, client):
		self._client_rep.add(client)
		self._rental_controller.update()
		return client

	"""
	Changes id of a client.
	"""
	def change_id(self, oldID, newID):
		self._client_rep.change_id(oldID, newID)
		self._rental_controller.update()

	"""
	Removes client with id client_id.
	"""
	def _remove_client(self, client_id):
		client = deepcopy(self.search_client(client_id))
		self._client_rep.remove_id(client_id)
		self._rental_controller.update()
		return client

	"""
	Returns a client by client_data.
	If data is an id, then it searches by id, otherwise, by name.
	"""
	def search_client(self, client_data):
		result = self._client_rep.search_id(client_data)
		if result == None:
			result = self._client_rep.search_name(client_data)
		return result

	"""
	Updates a client by client_id.
	"""
	def _update_client(self, client_id, newName, newCNP):
		client = deepcopy(self.search_client(client_id))
		self._client_rep.update_client(client_id, newName, newCNP)
		return client
