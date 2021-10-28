from app.models.list import List

def serialize_lists(shopping_lists):
    return [List(shopping_list).serialize() for shopping_list in shopping_lists]

def serialize_list_items(shopping_lists):
    return [str(item[0]) for item in shopping_lists]  #TODO: no idea if this is right, uncertain of what these serializers do
                                                      #      (used in queries)