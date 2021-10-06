class Item:
    home_id: int
    quantity: int
    item_name: str
    category_id: int

    def __init__(self, item):
        self.home_id = item[0]
        self.quantity = item[1]  
        self.item_name = item[2]  
        self.category_id = item[3]  
    
    def serialize(self):
        return {
            'homeID': self.home_id,
            'quantity': self.quantity,
            'itemName': self.item_name,
            'categoryID': self.category_id
        }

class HomeItem:
    item_name: str
    quantity: int
    category: str
    alert_threshold: int

    def __init__(self, item):
        self.item_name = item[0]
        self.quantity = item[1]  
        self.category = item[2]  
        self.alert_threshold = item[3]  
    
    def serialize(self):
        return {
            'item': self.item_name,
            'quantity': self.quantity,
            'category': self.category,
            'alertThreshold': self.alert_threshold
        }