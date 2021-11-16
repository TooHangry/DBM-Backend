from app.models.list import ListItem

def serialize_lists(lists):
    return [ListItem(list_item).serialize() for list_item in lists]
