from app.models.user import User
from app.models.home import UserToHome

def serialize_users(users):
    return [User(user).serialize() for user in users]

def serialize_home_members(users):
    return [User(user).serialize_as_member() for user in users]

def serialize_homes(homes):
    return [UserToHome(home).serialize() for home in homes]