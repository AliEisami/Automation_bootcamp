from helpping.h01.shopping_list import ShoppingList
from helpping.h01.shpping_item import ShoppingItem


class ShoppingListApp:
    def __init__(self):
        self._lists = {}

    @property
    def lists(self):
        return self._lists

    @lists.setter
    def lists(self, lists):
        self._lists = lists

    def create_shopping_list(self, name):
        self._lists[name] = ShoppingList(name)

    def add_item_to_list(self, list_name, item_name):
        item = ShoppingItem(item_name)
        self._lists[list_name].add_item(item)

    def mark_items_as_purchased(self, list_name, item_name):
        self._lists[list_name].mark_item_as_purchased(item_name)

    def display_all_lists(self):
        for shop_list in self._lists.values():
            shop_list.display_the_list()