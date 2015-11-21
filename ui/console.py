from repository.client_rep import ClientRep
from repository.movie_rep import MovieRep
from controller.movie_controller import MovieController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController

def run():
    movie_rep = MovieRep()
    client_rep = ClientRep()
    movie_controller = MovieController(movie_rep, rental_rep)
    client_controller = ClientController(client_rep, rental_rep)
    rental_controller = RentalController(rental_rep, movie_rep, client_rep)
    command = [""]
    while command[0] != "quit":
        try:
            print("> ", end='')
            command = input().split(' ')
            if command[0] == "add":
                if command[1] == "movie":
                    movie_controller.add_movie(command[2:5])
                elif command[1] == "client":
                    client_controller.add_client(command[2:4])
                else:
                    print("Invalid command!")
            elif command[0] == "remove":
                if command[1] == "movie":
                    movie_controller.remove_movie(command[2])
                elif command[1] == "client":
                    client_controller.remove_client(command[2])
                else:
                    print("Invalid command!")
            elif command[0] == "update":
                if command[1] == "movie":
                    movie_controller.update_movie(command[2:6])
                elif command[1] == "client":
                    client_controller.remove_client(command[2:5])
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
