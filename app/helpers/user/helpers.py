from hashlib import pbkdf2_hmac
from config import HASH_KEY

def get_hashed_password(password):
    return pbkdf2_hmac(
        'sha256',  # Hashing Algorithm
        password.encode(),  # Convert password to bytes
        HASH_KEY,  # Salt
        100000,  # 100,000 iterations of SHA-256
        dklen=32  # Get a 32 byte key
    )
