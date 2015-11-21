class Client:
    """
    Domain for client.
    """

    # Counts instances of Client. Used for id auto-gen.
    ___counter = 0

    """
    Client constructor.
    Raises ValueError for invalid parameters.
    """
    def __init__(self, name, CNP):
        self.ID = Client.___counter
        self._name = name
        self._CNP = CNP
        Client.___counter += 1

    """
    Returns the ID.
    """
    def getID(self):
        return self._ID

    """
    Returns the name.
    """
    def getName(self):
        return self._name

    """
    Returns the cnp.
    """
    def getCNP(self):
        return self._CNP

    """
    Returns string representation of client.
    """
    def __str__(self):
        s = ""
        s += "ID: " + self._ID
        s += "Name: " + self._name
        s += "CNP: " + self._CNP

