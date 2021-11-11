from app.helpers.invite import serializers
from flask import abort

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

def get_invites_for_user(db, email):
    db.execute('''
                SELECT * 
                FROM invite
                WHERE email = ?
                ''', (email, ))
    return serializers.serialize_invites(db.fetchall())

def remove_invite(db, connection, home, user):
    db.execute('''
                DELETE FROM invite
                WHERE email = ? AND home = ?;
                ''', (user, home, ))

    connection.commit()

def get_invite(db, email, home_id):
    db.execute('''
                SELECT * 
                FROM invite
                WHERE email = ? AND home = ?
                ''', (email, home_id))
    invites = serializers.serialize_invites(db.fetchall())
    return invites[0] if len(invites) > 0 else abort(404)