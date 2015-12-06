class Command:
    """
    Class for defining a command.
    """

    """
    Command class constructor.
    Contains a type and a parameter list.
    Raises exception for invalid command type.
    """
    def __init__(self, cmd_type, params, destination):
        self._destination = destination
        if cmd_type in ['add', 'remove', 'update', 'list', 'rent', 'return']:
            self._type = cmd_type
        else:
            raise ValueError("Unrecognized command!")
        self._params = params
        self._obj = None
        self._prevObj = None

    """
    Returns command type.
    """
    def getType(self):
        return self._type

    """
    Returns the parameters.
    """
    def getParams(self):
        return self._params

    """
    Returns the destination.
    """
    def getDest(self):
        return self._destination

    """
    Returns the object.
    """
    def getObj(self):
        return self._obj

    """
    Returns the previous object(for updates).
    """
    def getPrevObj(self):
        return self._prevObj

    """
    Sets the object.
    """
    def setObj(self, obj):
        self._obj = obj

    """
    Sets the previous object.
    """
    def setPrevObj(self, obj):
        self._prevObj = obj


