from domain.movie import *
from repository.repository_base import *

class MovieRep:
    """
    Repository for movie.
    """
    def __init__(self):
        Repository.__init__(self)

    def update_movie(self, ID, title, description, movie_type):
        for x in self.data:
            if x.ID == ID:
                x.title = title
                x.description = description
                x.movie_type = movie_type
