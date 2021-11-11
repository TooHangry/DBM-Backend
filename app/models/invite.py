class Invite:
    email: str
    home: int

    def __init__(self, invite):
        self.email = invite[0]
        self.home = invite[1]
    
    def serialize(self):
        return {
            'email': self.email,
            'home': self.home
        }
