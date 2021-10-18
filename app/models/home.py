class UserToHome:
    id: int
    is_admin: bool
    nickname: str

    def __init__(self, home):
        self.id = home[0] 
        self.is_admin = False if home[1] != 'T' else True
        self.nickname = home[2]  
    
    def serialize(self):
        return {
            'id': self.id,
            'isAdmin': self.is_admin,
            'nickname': self.nickname,
        }

class Home:
    id: int
    nickname: str
    GUID: str

    def __init__(self, home):
        self.id = home[0] 
        self.nickname = home[1]
    
    def serialize(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
        }