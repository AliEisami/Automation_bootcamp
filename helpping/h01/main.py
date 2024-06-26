from helpping.h01.shopping_list_app import ShoppingListApp


def main():
    shopping_app = ShoppingListApp()
    shopping_app.create_shopping_list("food")
    shopping_app.add_item_to_list('food','meat')
    shopping_app.mark_items_as_purchased('food', 'meat')
    shopping_app.display_all_lists()

main()