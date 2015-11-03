from movie import *
from client import *
from movie_rep import *
from client_rep import *
from controller import *

movie_rep = MovieRep()
client_rep = ClientRep()
movie_controller = MovieController(movie_rep, client_rep)
command = [""]
while command[0] != "quit":
    try:
        print("> ", end='')
        command = input().split(' ')
        if command[0] == "add":
            if command[1] == "movie":
                movie_controller.add_movie(command[2:5])
            elif command[1] == "client":
                movie_controller.add_client(command[2:4])
            else:
                print("Invalid command!")
        elif command[0] == "remove":
            if command[1] == "movie":
                movie_controller.remove_movie(command[2])
            elif command[1] == "client":
                movie_controller.remove_client(command[2])
            else:
                print("Invalid command!")
        elif command[0] == "update":
            if command[1] == "movie":
                movie_controller.update_movie(command[2:6])
            elif command[1] == "client":
                movie_controller.remove_client(command[2:5])
            else:
                print("Invalid command!")
        elif command[0] == "list":
            if command[1] == "movies":
                print(str(movie_rep))
            elif command[1] == "clients":
                print(str(client_rep))
            else:
                print("Invalid command!")
        else:
            if command[0] != "quit":
                print("Invalid command!")
    except ValueError as e:
        print(e)
    except:
        print("Please enter valid input!")
