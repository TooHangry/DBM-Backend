from app.models.home import Home

def serialize_homes(homes):
    return [Home(home).serialize() for home in homes]