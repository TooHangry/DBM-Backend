from datetime import datetime

class User:
    id: int
    fname: str
    lname: str
    email: str
    dateJoined: datetime
    token: str
    homes: object

    def __init__(self, user):
        self.id = user[0] 
        self.fname = user[1]
        self.lname = user[2]
        self.email = user[3]
        self.dateJoined = user[4]  
        self.token = user[5]  
    
    def serialize(self, homes = list()):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
            'dateJoined': str(self.dateJoined),
            'token': self.token,
            'homes': homes
        }

    def serialize_as_member(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
        }
    
    def set_homes(self, homes):
        self.homes = homes