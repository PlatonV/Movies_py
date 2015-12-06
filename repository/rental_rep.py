from repository.repository_base import *

class RentalRep(Repository):
    """
    Repository for rentals.
    """
    def __init__(self):
        Repository.__init__(self)

    """
    Returns the state of rental by movieID
    """
    def get_movie_state(self, movieID):
        try:
            for x in self._data:
                if x.movie.getID() == int(movieID):
                    return x.state
            return "Not rented"
        except:
            raise ValueError("Invalid id!")

    def __str__(self):
        s = ""
        for x in self.data:
            if x.valid == 1:
                s += str(x)
        return s
