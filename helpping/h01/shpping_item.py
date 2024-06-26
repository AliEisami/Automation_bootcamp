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

    def set_as_purchased(self):
        self._purchased = True