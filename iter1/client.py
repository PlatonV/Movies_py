class Client:
    """
    Domain for client.
    """
    ___counter = 0
    def __init__(self, name, cnp):
        self.id = Client.___counter
        Client.___counter += 1
        self.name = name
        self.cnp = cnp
