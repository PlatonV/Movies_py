class Rental:
    """
    Domain for rental.
    """

    # Counts instances of Client. Used for id auto-gen.
    ___counter = 0

    """
    Rental constructor.
    """
    def __init__(self, client, movie):
        self._ID = Rental.___counter
        self.movie = movie
        self.client = client
        self._status = "Rented"
        self.valid = 1
        Rental.___counter += 1

    """
    Sets rental as invalid.
    """
    def setInvalid(self):
        self.valid = 0

    """
    Sets rental as valid.
    """
    def setValid(self):
        self._valid = 1

    """
    Sets status as "Rented".
    """
    def setRented(self):
        self._status = "Rented"

    """
    Sets status as "Returned".
    """
    def setReturned(self):
        self._status = "Returned"

    """
    String representation of a rental.
    """
    def __str__(self):
        s = ""
        s += "ID: " + str(self._ID) + '\n'
        s += "MovieID: " + str(self.movie.getID()) + '\n'
        s += "ClientID: " + str(self.client.getID()) + '\n'
        s += "Status: " + self._status + '\n'
        return s
