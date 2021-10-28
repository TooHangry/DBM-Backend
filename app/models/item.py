class Item:
    id: int
    home_id: int
    quantity: int
    item_name: str
    category_id: int

    def __init__(self, item):
        self.id = item[0]
        self.home_id = item[1]
        self.quantity = item[2]  
        self.item_name = item[3]  
        self.category_id = item[4]  
    
    def serialize(self):
        return {
            'id': self.id,
            'homeID': self.home_id,
            'quantity': self.quantity,
            'itemName': self.item_name,
            'categoryID': self.category_id
        }

class HomeItem:
    id: int
    item_name: str
    quantity: int
    category: str
    alert_threshold: int

    def __init__(self, item):
        self.id = item[0]
        self.item_name = item[1]
        self.quantity = item[2]  
        self.category = item[3]  
        self.alert_threshold = item[4]

    def serialize(self):
        return {
            'id': self.id,
            'item': self.item_name,
            'quantity': self.quantity,
            'category': self.category,
            'alertThreshold': self.alert_threshold
        }