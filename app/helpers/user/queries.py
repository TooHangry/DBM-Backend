from app.helpers.user import serializers

def login_current_user(db, email, password):
    db.execute('''
                SELECT *
                FROM users
                WHERE email = '{}' AND password = '{}';
                '''.format(email, password))
    users = serializers.serialize_users(db.fetchall())
    return users[0] if len(users) > 0 else {}    
    
def get_user_homes(db, id):
    db.execute('''
                SELECT home, is_admin, nickname, users.id
                FROM users
                INNER JOIN (SELECT *
                            FROM user_to_homes
                            INNER JOIN homes
                            ON user_to_homes.home = homes.id) merged_homes
                ON users.id = merged_homes.user
                WHERE users.id = {}
                '''.format(id))
    return serializers.serialize_homes(db.fetchall())

def get_user_by_id(db, id):
    db.execute('''
                SELECT * 
                FROM users
                WHERE id = {}
                '''.format(id))
    users = serializers.serialize_users(db.fetchall())
    return users[0] if len(users) > 0 else {}


def get_all_users(db):
    db.execute('''
                SELECT * 
                FROM users
                ''')
    users = serializers.serialize_users(db.fetchall())
    return users