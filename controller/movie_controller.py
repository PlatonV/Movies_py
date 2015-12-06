from copy import deepcopy
from domain.movie import Movie

class MovieController:
    """
    Controller for movies.
    """
    def __init__(self, movie_rep, rental_controller, undo_controller):
        self._movie_rep = movie_rep
        self._rental_controller = rental_controller
        self._undo_controller = undo_controller

    """
    Executes the given command.
    """
    def executeCommand(self, command):
        if command.getType() == "add":
            if len(command.getParams()) == 3:
                command.setObj(self.add_movie(command.getParams()[0], command.getParams()[1], command.getParams()[2]))
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "remove":
            if len(command.getParams()) == 1:
                command.setObj(self.remove_movie(command.getParams()[0]))
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "search":
            if len(command.getParams()) == 1:
                return(self.search_movie(command.getParams()[0]))
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "update":
            if len(command.getParams()) == 4:
                self.update_movie(command.getParams()[0], command.getParams()[1], command.getParams()[2], command.getParams()[3])
            else:
                raise ValueError("Invalid parameters!")
        elif command.getType() == "list":
            return str(self._movie_rep)
        # If execution reaches this point, the command was succesfull
        if command.getType() in ["add", "remove", "update"]:
            self._undo_controller.recordCommand(command)

    """
    Adds movie with given title, description and movie_type.
    Returns added movie.
    """
    def add_movie(self, title, description, movie_type):
        movie = Movie(title, description, movie_type)
        self._movie_rep.add(movie)
        self._rental_controller.update()
        return movie

    """
    Changes id of a movie.
    """
    def change_id(self, oldID, newID):
        self._movie_rep.change_id(oldID, newID)
        self._rental_controller.update()

    """
    Removes movie with id movie_id.
    Returns removed movie.
    """
    def remove_movie(self, movie_id):
        movie = deepcopy(self.search_movie(movie_id))
        self._movie_rep.remove_id(movie_id)
        self._rental_controller.update()
        return movie

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
    Returns updated movie.
    """
    def update_movie(self, movie_id, newTitle, newDescription, newType):
        self._movie_rep.update_movie(movie_id, newTitle, newDescription, newType)
