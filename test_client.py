#!/usr/bin/python3

from test.test_utils import *
from domain.client import Client

def test_client():
	client = Client("Name", "1234567891")
	print("###################### Testing Client class:")
	custom_assert("getName() for valid client.", client.getName() == "Name")
	custom_assert("getCNP() for valid client.", client.getCNP() == "1234567891")

if __name__ == "__main__":
	test_client()
