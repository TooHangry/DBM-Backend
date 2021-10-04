class Home:
    id: int
    is_admin: str
    nickname: str

    def __init__(self, home):
        self.id = home[0] 
        self.is_admin = home[1]
        self.nickname = home[2]  
    
    def serialize(self):
        return {
            'id': self.id,
            'isAdmin': self.is_admin,
            'nickname': self.nickname,
        }