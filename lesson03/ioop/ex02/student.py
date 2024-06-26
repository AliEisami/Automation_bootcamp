class Student:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return f"{self._name}_S"

    @id.setter
    def id(self, id):
        self._id = id

    @name.setter
    def name(self, name):
        self._name = name

    def get_help(self):
        with open("get_help.txt", 'a+') as file:
            file.write(f"{self._name} need help!\n")

    def other_get_help(self,other):
        with open("get_help.txt", 'a+') as file:
            file.write(f"{other._name} need help!\n")