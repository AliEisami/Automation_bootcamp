from shopping_list import ShoppingList

class ShoppingListApp(ShoppingList):
    def __init__(self):
        super().__init__()

    def shopping_main(self):
        select = input("wellcome to Shopping App:\nwhat would you like to do?\n1. Add item\n2. display list\n")
        while select != 'x':
            if select == '1':
                item_name = input("Enter the item name:\n")
                self.add_item(item_name)
            if select == '2':
                self.display_list()
                buy_item = input("do you want to buy item?(enter yes to buy)\n")
                if buy_item == 'yes':
                    item_index = input("enter the number of the item:\n")
                    try:
                        self.mark_purchased(int(item_index))
                    except ValueError:
                        print("invalid input (Enter only numbers)")
            select = input("anything else? press x to exit\n")
        print("Good Bye!!")
