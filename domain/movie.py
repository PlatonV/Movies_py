class Movie:
    """
    Movie domain.
    """

    # Counts instances of Client. Used for id auto-gen.
    ___counter = 0

    """
    Movie constructor.
    Raises ValueError for invalid parameters.
    """
    def __init__(self, title, description, movie_type):
        self.ID = Movie.___counter
        self._title = title
        self._description = description
        self._movie_type = movie_type
        Movie.___counter += 1

    """
    Returns the ID.
    """
    def getID(self):
        return self._ID

    """
    Returns the title.
    """
    def getTitle(self):
        return self._title

    """
    Returns the description.
    """
    def getDescription(self):
        return self._description

    """
    Returns the type.
    """
    def getType(self):
        return self.movie_type

    """
    Returns string representation of movie.
    """
    def __str__(self):
        s = ""
        s += "ID: " + self._ID
        s += "Title: " + self._title
        s += "Description: " + self._description
        s += "Type: " + self._movie_type + '\n'
