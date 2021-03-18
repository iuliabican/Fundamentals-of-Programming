
class Player:
    def __init__(self, id, name, strength):
        self._id = id
        self._name = name
        self._strength = strength

    @property
    def ID(self):
        return self._id

    @ID.setter
    def ID(self, newId):
        self._id = newId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, newName):
        self._name = newName

    @property
    def Strength(self):
        return self._strength

    @Strength.setter
    def Strength(self, newStrength):
        self._strength = newStrength

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return "ID: " + str(self._id) + ", Name:" + str(self._name) + ", Strength:" + str(self._strength)
