from movie import *

class MovieRep:
    """
    Repository for movie.
    """
    def __init__(self):
        self.movies = []

    def add_movie(self, m):
        self.movies.append(m)
    
    def remove_movie(self, i):
        self.movies = list(filter(lambda x: x.id != i, self.movies))

    def update_movie(self, i, title, description, t):
        for x in self.movies:
            if x.id == i:
                x.title = title
                x.description = description
                x.t = t
    
    def __str__(self):
        s = ""
        for m in self.movies:
            s += "\nid: " + str(m.id) + '\n'
            s += "title: " + m.title + '\n'
            s += "description: " + m.description + '\n'
            s += "type: " + m.t + '\n'
        return s
