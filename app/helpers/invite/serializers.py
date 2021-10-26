from app.models.invite import Invite

def serialize_invites(invites):
    return [Invite(invite).serialize() for invite in invites]