from domain.client import *
from repository.repository_base import *

class ClientRep(Repository):
	"""
	Repository for clients.
	"""
	def __init__(self):
		Repository.__init__(self)

	"""
	Loads the data from a file called clients.rep
	"""
	def loadData(self):
		with open("clients.rep") as f:
			content = f.readlines()
		i = 0
		while i < len(content):
			name = content[i][:len(content[i]) - 1]
			cnp = content[i + 1][:len(content[i + 1]) - 1]
			self._data.append(Client(name, cnp))
			i += 2

	"""
	Saves the data to a file called clients.rep
	"""
	def saveData(self):
		with open("clients.rep", 'w') as f:
			for client in self._data:
				f.write(client.getName() + '\n')
				f.write(client.getCNP() + '\n')
	"""
	Searches a client by name.
	"""
	def search_name(self, name):
		for x in self._data:
			if x.name == name:
				return x
		return None

	def update_client(self, ID, name, CNP):
		try:
			for x in self._data:
				if x.getID() == int(ID):
					x.setName(name)
					if len(CNP) > 0:
						x.setCNP(CNP)
		except:
			raise ValueError("Invalid id!")
