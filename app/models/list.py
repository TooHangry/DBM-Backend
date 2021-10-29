class ListItems:
    list_id: int
    item_id: int
    quantity: int
    is_complete: bool

    def __init__(self, shopping_list):
        self.list_id     = shopping_list[0]
        self.item_id     = shopping_list[1]
        self.quantity    = shopping_list[2]
        self.is_complete = False if shopping_list[3] != 'T' else True
    
    def serialize(self):
        return {
            'listID': self.list_id,
            'itemID': self.item_id,
            'quantity': self.quantity,
            'isComplete': self.is_complete
        }

class ShoppingList:
    id: int
    tasked_to: int
    home_tasked: int
    tasked_on: str

    def __init__(self, shopping_list):
        self.id = shopping_list[0] 
        self.tasked_to = shopping_list[1]
        self.home_tasked = shopping_list[2]
        self.tasked_on = shopping_list[3]
    
    def serialize(self):
        return {
            'id': self.id,
            'taskedTo': self.tasked_to,
            'homeTasked': self.home_tasked,
            'taskedOn': str(self.tasked_on)
        }