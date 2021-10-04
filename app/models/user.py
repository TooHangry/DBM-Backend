from datetime import datetime

class User:
    id: int
    fname: str
    lname: str
    email: str
    dateJoined: datetime

    def __init__(self, user):
        self.id = user[0] 
        self.fname = user[1]
        self.lname = user[2]
        self.email = user[3]
        self.dateJoined = user[4]  
    
    def serialize(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
            'dateJoined': str(self.dateJoined)
        }