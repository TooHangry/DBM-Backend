from flask import Blueprint

list_routes = Blueprint('list', __name__, url_prefix='')

@list_routes.route('/lists', methods=['GET'])
def get_default():
    return {
        'lists': []
    }

# /lists/mine/id
#   Gets user lists (pass userID as query param) test

# /lists/home/id
#   Gets lists in a home (pass in homeIDas query param)

# /lists/add
#   Create a new list (pass in formdata with name, homeID, adminID, etc.)

# /lists/remove/id
#   Delete home with id from query param

# /lists/update/id
#   Update the list at 'id' with passed-in form data