from controller.movie_controller import MovieController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController

class UndoController:
    """
    Undo controller class.
    """

    """
    Undo controller constructor takes a reference to all controllers.
    """
    def __init__(self):
        self.history_index = -1
        self.command_history = []

    def setMovieController(self, ctrl):
        self._movie_controller = ctrl

    def setClientController(self, ctrl):
        self._client_controller = ctrl

    def setRentalController(self, ctrl):
        self._rental_controller = ctrl

    def recordCommand(self, command):
        self.command_history.append(command)
        self.history_index += 1
        self.command_history = self.command_history[:self.history_index + 1]


    def undo(self):
        if self.history_index >= 0:
            cmd = self.command_history[self.history_index]
            if cmd.getDest() == "movie":
                if cmd.getType() == "add":
                    self._movie_controller.remove_movie(cmd.getObj().getID())
                if cmd.getType() == "remove":
                    movie = self._movie_controller.add_movie(cmd.getObj().getTitle(), cmd.getObj().getDescription(), cmd.getObj().getType())
                    self._movie_controller.change_id(movie.getID(), cmd.getObj().getID())
            if cmd.getDest() == "client":
                if cmd.getType() == "add":
                    self._client_controller.remove_client(cmd.getObj().getID())
                if cmd.getType() == "remove":
                    client = self._client_controller.add_movie(cmd.getObj().getName(), cmd.getObj().getCNP())
                    self._client_controller.change_id(client.getID(), cmd.getObj().getID())
                self.history_index -= 1
        else:
            raise ValueError("Nothing to undo!")

    def redo(self):
        if self.history_index < len(self.command_history) - 1:
            self.history_index += 1
            cmd = self.command_history[self.history_index]
            if cmd.getDest() == "movie":
                if cmd.getType() == "add":
                    movie = self._movie_controller.add_movie(cmd.getObj().getTitle(), cmd.getObj().getDescription(), cmd.getObj().getType())
                    self._movie_controller.change_id(movie.getID(), cmd.getObj().getID())
                if cmd.getType() == "remove":
                    self._movie_controller.remove_movie(cmd.getObj().getID())
        else:
            raise ValueError("Nothing to redo!")
