from repository.client_rep import ClientRep
from repository.movie_rep import MovieRep
from repository.rental_rep import RentalRep
from controller.command import Command
from controller.movie_controller import MovieController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController

def parse_command(command_str):
    split_cmd = command_str.split(' ')
    cmd_type = split_cmd[0]
    cmd_params = split_cmd[2:len(split_cmd)]
    return Command(cmd_type, cmd_params)

def run():
    movie_rep = MovieRep()
    client_rep = ClientRep()
    rental_rep = RentalRep()
    movie_controller = MovieController(movie_rep, rental_rep)
    client_controller = ClientController(client_rep, rental_rep)
    rental_controller = RentalController(rental_rep, movie_controller, client_controller)
    while True:
        try:
            print("> ", end='')
            command_str = input()
            if command_str == 'quit':
                break
            split_cmd = command_str.split(' ')
            command_destination = split_cmd[1]
            command = parse_command(command_str)
            if command.getType() == "search" or command.getType() == "list":
                if command_destination == "movies" or command_destination == "movie":
                    print(str(movie_controller.executeCommand(command)))
                elif command_destination == "clients" or command_destination == "client":
                    print(str(client_controller.executeCommand(command)))
                elif command_destination == "rentals" or command_destination == "rental":
                    print(str(rental_controller.executeCommand(command)))
            elif command.getType() == "add" or command.getType() == "remove" or command.getType() == "update":
                if command_destination == "movie":
                    movie_controller.executeCommand(command)
                elif command_destination == "client":
                    client_controller.executeCommand(command)
            elif command.getType() == "rent" or command.getType() == "return":
                if command_destination == "movie":
                    rental_controller.executeCommand(command)
        except ValueError as e:
            print(e)
        except IndexError:
            print("Invalid parameters!")
