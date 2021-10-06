from app.models.item import Item, HomeItem

def serialize_items(items):
    return [Item(item).serialize() for item in items]

def serialize_home_items(items):
    return [HomeItem(item).serialize() for item in items]