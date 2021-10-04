from app.models.user import User
from app.models.home import Home
import json

def serialize_users(users):
    return [User(user).serialize() for user in users]

def serialize_homes(homes):
    return [Home(home).serialize() for home in homes]