from shopping_item import ShoppingItem

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_item(self, name):
        item = ShoppingItem(name)
        exists = False
        for list_item in self._items:
            if(item.name == list_item.name):
                exists = True
        if not exists:
            self._items.append(item)
        else:
            print("item already in the list")

    def mark_purchased(self, index):
        if index-1 < len(self._items):
            self._items[index-1].purchased = True
        else:
            print("incorrect input!!!")

    def display_list(self):
        print("items list:\n")
        index = 1
        for item in self._items:
            print(f"{index}. {item.name} - {item.purchased}\n")
            index = index + 1