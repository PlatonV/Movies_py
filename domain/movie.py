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
        self._ID = Movie.___counter
        self._title = title
        self._description = description
        self._movie_type = movie_type
        Movie.___counter += 1

    """
    Sets the ID.
    """
    def setID(self, newID):
        self._ID = newID

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
        return self._movie_type

    """
    Sets the title.
    """
    def setTitle(self, title):
        self._title = title

    """
    Sets the description.
    """
    def setDescription(self, description):
        self._description = description

    """
    Sets the type.
    """
    def setType(self, movie_type):
        self._movie_type = movie_type

    """
    Returns string representation of movie.
    """
    def __str__(self):
        s = ""
        s += "ID: " + str(self._ID) + '\n'
        s += "Title: " + self._title + '\n'
        s += "Description: " + self._description + '\n'
        s += "Type: " + self._movie_type + '\n'
        return s
