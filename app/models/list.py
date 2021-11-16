from datetime import datetime

class ListItem:
    id: int
    title: str
    tasked_user_id: int
    home_id: str
    date_tasked: datetime
    date_due: datetime
    is_complete: bool

    def __init__(self, item):
        self.id = item[0]
        self.title = item[1]
        self.tasked_user_id = item[2]  
        self.home_id = item[3]  
        self.date_tasked = item[4]
        self.date_due = item[5]
        self.is_complete = False if item[6] != 'T' else True

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'taskedUser': self.tasked_user_id,
            'homeID': self.home_id,
            'dateTasked': str(self.date_tasked),
            'dateDue': str(self.date_due),
            'isComplete': str(self.is_complete),
            'items': []
        }