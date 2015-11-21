from repository.repository_base import *

class ClientRep(Repository):
    """
    Repository for clients.
    """
    def __init__(self):
        Repository.__init__(self)
    
    def update_client(self, ID, name, CNP):
        for x in self.data:
            if x.ID == ID:
                x.name = name
                if len(CNP) > 0:
                    x.CNP = CNP
