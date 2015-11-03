from movie import *
from client import *
from movie_rep import *
from client_rep import *

class MovieController:
    """
    Controls movie and client repos.
    """
    def __init__(self, movie_rep, client_rep):
        self.movie_rep = movie_rep
        self.client_rep = client_rep

    def add_movie(self, command_str):
        """
        Adds a movie to the repo.
        command_str: string with movie title, description and type.
        """
        if len(command_str) == 3:
            self.movie_rep.add_movie(Movie(command_str[0], command_str[1], command_str[2]))
        else:
            raise ValueError("Please provide title, description and type!")

    def remove_movie(self, command_str):
        """
        Removes a movie from the repo.
        command_str: string with movie id.
        """
        if str(command_str).isdigit():
            self.movie_rep.remove_movie(int(command_str))
        else:
            raise ValueError("Please enter valid id!")

    def update_movie(self, command_str):
        """
        Updates a movie from the repo.
        command_str: string with movie id, title, description and type.
        """
        if command_str[0].isdigit() and len(command_str) == 4:
            self.movie_rep.update_movie(int(command_str[0]), command_str[1], command_str[2], command_str[3])
        else:
            raise ValueError("Please insert valid id, title, description and type")

    def add_client(self, command_str):
        """
        Adds a client to the repo.
        command_str: string with client name and cnp.
        """
        if len(command_str) == 2:
            self.client_rep.add_client(Client(command_str[0], command_str[1]))
        else:
            raise ValueError("Please provide title, description and type!")

    def remove_client(self, command_str):
        """
        Removes a client from the repo.
        command_str: string with client id.
        """
        if str(command_str).isdigit():
            self.client_rep.remove_client(int(command_str))
        else:
            raise ValueError("Please enter valid id!")
	
    def update_client(self, command_str):
        """
        Updates a client from the repo.
        command_str: string with client id, name and optionally cnp.
        """
        if command_str[0].is_digit():
            self.client_rep.update_client(command_str[0], command_str[1], command_str[2])
        else:
            raise ValueError("Please enter valid id, name and maybe CNP!")
