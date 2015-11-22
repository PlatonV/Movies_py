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
        self.state = "Rented"
        Rental.___counter += 1

    """
    String representation of a rental.
    """
    def __str__(self):
        s = ""
        s += "ID: " + str(self._ID) + '\n'
        s += "MovieID: " + str(self.movie.getID()) + '\n'
        s += "ClientID: " + str(self.client.getID()) + '\n'
        s += "State: " + self.state + '\n'
        return s
