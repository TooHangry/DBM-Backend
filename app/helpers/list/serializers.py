from app.models.list import ShoppingList, ListItems

def serialize_lists(shopping_lists):
    return [ShoppingList(shopping_list).serialize() for shopping_list in shopping_lists]

def serialize_list_items(shopping_lists):
    return [str(item[0]) for item in shopping_lists]