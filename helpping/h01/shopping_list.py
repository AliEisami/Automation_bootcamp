class ShoppingList:
    def __init__(self, name):
        self._name = name
        self._items = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def mark_item_as_purchased(self, item_name):
        for item in self._items:
            if item.name == item_name:
                item.set_as_purchased()

    def display_the_list(self):
        print(self._name)
        for item in self._items:
            print(item)