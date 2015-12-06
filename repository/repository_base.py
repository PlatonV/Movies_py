class Repository:
    """
    Base class for all repositories in this project.
    All data objects must have a getID function.
    """

    """
    Repository constructor.
    """
    def __init__(self):
        self.data = []

    """
    Adds new item to the repo.
    """
    def add(self, new):
        self.data.append(new)

    """
    Removes an item by id.
    """
    def remove_id(self, removeID):
        try:
            self.data = list(filter(lambda x: x.getID() != int(removeID), self.data))
        except:
            raise ValueError("Invalid id!")

    """
    Changes id of an element.
    """
    def change_id(self, oldID, newID):
        x = self.search_id(oldID)
        x.setID(newID)

    """
    Returns the element with searchID.
    """
    def search_id(self, searchID):
        try:
            return list(filter(lambda x: x.getID() == int(searchID), self.data))[0]
        except:
            return None

    """
    String representation of the repository.
    """
    def __str__(self):
        s = ""
        for x in self.data:
            s += str(x)
        return s

