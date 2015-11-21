class Repository:
    """
    Base class for all repositories in this project.
    All data objects must have a getID function.
    """
    def __init__(self):
        self.data = []

    def add(self, new):
        self.data.append(new)

    def remove(self, removeID):
        self.data = list(filter(lambda x: x.ID != removeID, self.data))

    def __str__(self):
        s = ""
        for x in self.data:
            s += str(x) + '\n'
        return s

