from domain.movie import Movie

class MovieController:
    """
    Controller for movies.
    """
    def __init__(self, movie_rep, rental_rep):
        self._movie_rep = movie_rep

    """
    Executes the given command.
    """
    def executeCommand(self, command):
        if command.getType() == "add":
            if len(command.getParams()) == 3:
                self._add_movie(command.getParams()[0], command.getParams()[1], command.getParams()[2])
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "remove":
            if len(command.getParams()) == 1:
                self._remove_movie(command.getParams()[0])
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "search":
            if len(command.getParams()) == 1:
                return(self.search_movie(command.getParams()[0]))
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "update":
            if len(command.getParams()) == 4:
                self._update_movie(command.getParams()[0], command.getParams()[1], command.getParams()[2], command.getParams()[3])
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "list":
            return str(self._movie_rep)

    """
    Adds movie with given title, description and movie_type.
    """
    def _add_movie(self, title, description, movie_type):
        self._movie_rep.add(Movie(title, description, movie_type))

    """
    Removes movie with id movie_id.
    """
    def _remove_movie(self, movie_id):
        self._movie_rep.remove_id(movie_id)

    """
    Returns a movie by movie_data.
    If data is an id, then it searches by id, otherwise, by title.
    """
    def search_movie(self, movie_data):
        result = self._movie_rep.search_id(movie_data)
        if result == None:
            result = self._movie_rep.search_title(movie_data)
        return result

    """
    Updates a movie by movie_id.
    """
    def _update_movie(self, movie_id, newTitle, newDescription, newType):
        self._movie_rep.update_movie(movie_id, newTitle, newDescription, newType)
