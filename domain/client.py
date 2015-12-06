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
        self._ID = Client.___counter
        self.setName(name)
        self.setCNP(CNP)
        Client.___counter += 1

    """
    Sets the ID.
    """
    def setID(self, newID):
        self._ID = newID

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
    Sets the name.
    """
    def setName(self, name):
        self._name = name

    """
    Sets the cnp.
    """
    def setCNP(self, CNP):
        if len(CNP) == 10:
            self._CNP = CNP
        else:
            raise ValueError("Invalid CNP!")

    """
    Returns string representation of client.
    """
    def __str__(self):
        s = ""
        s += "ID: " + str(self._ID) + '\n'
        s += "Name: " + self._name + '\n'
        s += "CNP: " + self._CNP + '\n'
        return s
