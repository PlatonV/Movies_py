#!/usr/bin/python3

from movie import *
from movie_rep import *

def test_movie_repo():
	rep = MovieRep()
	rep.add_movie("Name", "asd", "asd")
	custom_assert("getTitle():", movie.getTitle() == "Name")
	custom_assert("getDescription():", movie.getDescription() == "asd")
	custom_assert("getType():", client.getType() == "asd")

if __name__ == "__main__":
	test_movie_repo()
