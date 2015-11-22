from repository.repository_base import *

class MovieRep(Repository):
    """
    Repository for movie.
    """
    def __init__(self):
        Repository.__init__(self)

    """
    Searches a movie by title.
    """
    def search_title(self, title):
        for x in self.data:
            if x.getTitle() == title:
                return x
        return None

    """
    Updates a movie by id.
    """
    def update_movie(self, ID, title, description, movie_type):
        try:
            for x in self.data:
                if x.getID() == int(ID):
                    x.setTitle(title)
                    x.setDescription(description)
                    x.setType(movie_type)
        except:
            raise ValueError("Invalid id!")
