from client import *

class ClientRep:
    """
    Repositoy for clients.
    """
    def __init__(self):
        self.clients = []
    
    def add_client(self, c):
        self.clients.append(c)
    
    def remove_client(self, i):
        self.clients = list(filter(lambda x: x.id != i, self.clients))

    def update_client(self, i, name, cnp):
        for x in self.clients:
            if x.id == i:
                x.name = name
                if len(cnp) > 0:
                    x.cnp = cnp

    def __str__(self):
        s = ""
        for c in self.clients:
                s += "\nid: " + str(c.id) + '\n'
                s += "name: " + c.name + '\n'
                s += "CNP: " + c.cnp + '\n'
        return s
