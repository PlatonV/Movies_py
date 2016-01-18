from repository.client_rep import ClientRep
from repository.movie_rep import MovieRep
from repository.rental_rep import RentalRep
from controller.command import Command
from controller.movie_controller import MovieController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController
from controller.undo_controller import UndoController

def parse_command(command_str):
	split_cmd = command_str.split(' ')
	cmd_type = split_cmd[0]
	cmd_params = split_cmd[2:len(split_cmd)]
	return Command(cmd_type, cmd_params, split_cmd[1])

def run():
	movie_rep = MovieRep()
	movie_rep.loadData()
	client_rep = ClientRep()
	client_rep.loadData()
	rental_rep = RentalRep()
	rental_rep.loadData()
	undo_controller = UndoController()
	rental_controller = RentalController(rental_rep, undo_controller)
	movie_controller = MovieController(movie_rep, rental_controller, undo_controller)
	client_controller = ClientController(client_rep, rental_controller, undo_controller)
	rental_controller.setMC(movie_controller)
	rental_controller.setCC(client_controller)
	undo_controller.setMovieController(movie_controller)
	undo_controller.setClientController(client_controller)
	undo_controller.setRentalController(rental_controller)
	while True:
		try:
			print("> ", end='')
			command_str = input()
			if command_str == 'quit':
				break
			elif command_str == 'most rented':
				print(rental_controller.most_rented())
				continue
			elif command_str == "undo":
				undo_controller.undo()
				continue
			elif command_str == "redo":
				undo_controller.redo()
				continue
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
				if command_destination in ["movie", "rental"]:
					rental_controller.executeCommand(command)
		except ValueError as e:
			print(e)
	movie_rep.saveData()
	client_rep.saveData()
	rental_rep.saveData()
