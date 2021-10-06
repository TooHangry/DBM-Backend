from app.helpers.home import serializers

def get_all_homes(db):
    db.execute('''
                SELECT *
                FROM homes
                ''')
    return serializers.serialize_homes(db.fetchall())