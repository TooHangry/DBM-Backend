class Item:
    id: int
    home_id: int
    quantity: int
    item_name: str
    category_id: int
    alert_threshold: int 
    list_id: int
    needed: int

    def __init__(self, item):
        self.id = item[0]
        self.home_id = item[1]
        self.quantity = item[2]  
        self.item_name = item[3]  
        self.category_id = item[4]  
        self.alert_threshold = item[5]  
        self.list_id = item[6]  
        self.needed = item[7]  
    
    def serialize(self):
        return {
            'id': self.id,
            'homeID': self.home_id,
            'quantity': self.quantity,
            'item': self.item_name,
            'categoryID': self.category_id,
            'alertThreshold': self.alert_threshold,
            'isInAList': self.list_id != 0,
            'needed': self.needed
        }



class HomeItem:
    id: int
    item_name: str
    quantity: int
    category: str
    alert_threshold: int
    is_in_a_list: bool
    needed: int

    def __init__(self, item):
        self.id = item[0]
        self.item_name = item[1]
        self.quantity = item[2]  
        self.category = item[3]  
        self.alert_threshold = item[4]
        self.is_in_a_list = item[5]
        self.needed = item[6]

    def serialize(self):
        return {
            'id': self.id,
            'item': self.item_name,
            'quantity': self.quantity,
            'category': self.category,
            'alertThreshold': self.alert_threshold,
            'isInAList': self.is_in_a_list,
            'needed': self.needed
        }