from app.models.user import User
from app.models.home import Home

####################
# USER SERIALIZERS #
####################
def serialize_users(users):
    return [User(user).serialize() for user in users]

####################
# HOME SERIALIZERS #
####################
def serialize_homes(homes):
    return [Home(home).serialize() for home in homes]