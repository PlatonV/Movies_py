class Movie:
    """
    Movie domain.
    """
    ___counter = 0
    def __init__(self, title, description, t):
        self.id = Movie.___counter
        Movie.___counter += 1
        self.title = title
        self.description = description
        self.t = t
