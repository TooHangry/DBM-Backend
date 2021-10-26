class Invite:
    id: int
    email: str
    home: int

    def __init__(self, invite):
        self.id = invite[0] 
        self.email = invite[1]
        self.home = invite[2]
    
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'home': self.home
        }
