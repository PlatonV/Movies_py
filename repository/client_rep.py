from repository.repository_base import *

class ClientRep(Repository):
    """
    Repository for clients.
    """
    def __init__(self):
        Repository.__init__(self)
    
    """
	Searches a client by name.
	"""
    def search_name(self, name):
        for x in self.data:
            if x.name == name:
                return x
        return None

    def update_client(self, ID, name, CNP):
        try:
            for x in self.data:
                if x.getID() == int(ID):
                    x.setName(name)
                    if len(CNP) > 0:
                        x.setCNP(CNP)
        except:
            raise ValueError("Invalid id!")
