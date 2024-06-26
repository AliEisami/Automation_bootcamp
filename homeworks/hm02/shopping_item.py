class ShoppingItem:
    def __init__(self, name):
        self._name = name
        self._purchased = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def purchased(self):
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        self._purchased = purchased