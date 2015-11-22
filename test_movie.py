#!/usr/bin/python3

from test.test_utils import *
from domain.movie import Movie

def test_movie():
	movie = Movie("Title", "Description bla bla", "Action")
	print("###################### Testing Movie class:")
	custom_assert("getTitle() for valid movie.", movie.getTitle() == "Title")
	custom_assert("getDescription() for valid movie.", movie.getDescription() == "Description bla bla")
	custom_assert("getType() for valid movie.", movie.getType() == "Action")

if __name__ == "__main__":
	test_movie()
