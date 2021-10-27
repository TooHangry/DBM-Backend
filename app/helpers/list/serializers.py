from app.models.list import List

def serialize_lists(lists):
    return [List(shopping_list).serialize() for shopping_list in lists]

def serialize_list_items(lists):
    return [str(item[0]) for item in list]  #TODO: no idea if this is right, uncertain of what these serializers do
                                            #      (used in queries)