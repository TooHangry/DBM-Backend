from app.models.home import Home

def serialize_homes(homes):
    return [Home(home).serialize() for home in homes]

def serialize_categories(categories):
    return [str(cat[0]) for cat in categories]