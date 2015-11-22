from domain.client import Client

class ClientController:
    """
    Controller for clients.
    """
    def __init__(self, client_rep, rental_rep):
        self._client_rep = client_rep

    """
    Executes the given command.
    """
    def executeCommand(self, command):
        if command.getType() == "add":
            if len(command.getParams()) == 2:
                self._add_client(command.getParams()[0], command.getParams()[1])
            else:
                raise ValueError("Invalid parameters")
        elif command.getType() == "remove":
            if len(command.getParams()) == 1:
                self._remove_client(command.getParams()[0])
            else:
                raise ValueError("Invalid parameters")
        elif command.getType() == "update":
            if len(command.getParams()) == 3:
                self._update_client(command.getParams()[0], command.getParams()[1], command.getParams()[2])
            else:
                raise ValueError("Invalid parameters")
        elif command.getType() == "search":
            if len(command.getParams()) == 1:
                return(self.search_client(command.getParams()[0]))
            else:
                raise ValueError("Invalid parameters")
        elif command.getType() == "list":
            return str(self._client_rep)
    """
    Adds client with given name and CNP.
    """
    def _add_client(self, name, CNP):
        self._client_rep.add(Client(name, CNP))

    """
    Removes client with id client_id.
    """
    def _remove_client(self, client_id):
        self._client_rep.remove_id(client_id)

    """
    Returns a client by client_data.
    If data is an id, then it searches by id, otherwise, by name.
    """
    def search_client(self, client_data):
        result = self._client_rep.search_id(client_data)
        if result == None:
            result = self._client_rep.search_title(client_data)
        return result

    """
    Updates a client by client_id.
    """
    def _update_client(self, client_id, newName, newCNP):
        self._client_rep.update_client(client_id, newName, newCNP)
