class Command:
    """
    Class for defining a command.
    """

    """
    Command class constructor.
    Contains a type and a parameter list.
    Raises exception for invalid command type.
    """
    def __init__(self, cmd_type, params):
        self._type = cmd_type
        self._params = params

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
