from animal import Animal

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)
        # self._specific_name = specific_name

    @property
    def name(self):
        return f"{self._name}_Cat"
    #
    # @specific_name.setter
    # def specific_name(self, specific_name):
    #     self._specific_name = specific_name

    def speak(self):
        print("The cat meows")