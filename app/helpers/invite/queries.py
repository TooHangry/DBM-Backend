from app.helpers.invite import serializers

def create_invite(db, connection, email, home_id):
    db.execute('''
        INSERT INTO invite (email, home)
        VALUES (?, ?);
    ''', (email, home_id))

    connection.commit()

def get_home_invites(db, home_id):
    db.execute('''
                SELECT *
                FROM invite
                WHERE home = ?
                ''', (home_id, ))
    return serializers.serialize_invites(db.fetchall())


def remove_invite(db, connection, id):
    db.execute('''
                DELETE FROM invite
                WHERE id = ?;
                ''', (id, ))

    connection.commit()