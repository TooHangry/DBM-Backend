
DEBUG = True

# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Application threads
THREADS_PER_PAGE = 4

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "6e!a4^2@ed09ocp)@=sryko%=5hw$1q*3ykk5!(1z21!9+90x^"

# Secret key for cookies
SECRET_KEY = "e#c6464=_mlpc5isu0=ce_8vp5ftefs3yyltz6p-a1ljn*jx)@"

HASH_KEY = b'\x8a\xcdB\xe3?+\x92x3,\xbb\x9e\xf2\xed\xc1a\xb0\x9f\xb1\xfax\xfa\xc4\x94f\x06\x93\xe0jPMQ'

# Folders for user uploads
UPLOAD_FOLDER = '{}/uploads/'.format(BASE_DIR)

# Email config values
EMAIL_ADDRESS  = 'homemanagementdbm2021@gmail.com'
EMAIL_PASSWORD = 'TableFlippers2021!'