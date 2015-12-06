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
            self._add_rental(command.getParams()[0], command.getParams()[1])
        if command.getType() == "return":
            self._remove_rental(command.getParams()[0])
        if command.getType() == "search":
            return self.search_rental(command.getParams()[0])
        if command.getType() == "list":
            return str(self._rental_rep)

    """
    Updates rentals according to changes in client rep and movie repo.
    """
    def update(self):
        for x in self._rental_rep.data:
            print(str(x.valid))
            if self._movie_controller.search_movie(x.movieID) == None or self._client_controller.search_client(x.clientID) == None:
                x.setInvalid()
            else:
                x.setValid()

    """
    Adds rental with given client and movie.
    """
    def _add_rental(self, clientID, movieID):
        self._rental_rep.add(Rental(clientID, movieID))

    """
    Removes rental with id rental_id.
    """
    def _remove_rental(self, rental_id):
        self._rental_rep.search_id(rental_id).setReturned()

    """
    Returns a rental by rental_id.
    """
    def search_rental(self, rental_id):
        result = self._rental_rep.search_id(rental_id)
        return result
