# DBM-Backend
Database Management Backend Application

Virtual Enviornment: 
1. Create a Python 3 Virtual Environment: \
    macOS / Linux: `virtualenv env` \
    Windows: `python3 -m venv env` 
2. Activate virtual environment \
    macOS / Linux: `source env/bin/activate` \
    Windows: `\env\Scripts\activate` 
3. Install required dependencies \
    `pip3 install -r reqs.txt` 

App:
1. Ensure virtual environment is activated 
2. Run `python3 run.py` to launch the dev server 

Structure:
.
|__ run.py
|__ db
|__ app
    |__ init.py (entry point)
    |__ helpers
    |   |__ database helpers (all data actions)
    |   |__ auth helpers (all auth)
    |__ routes
        |__ default
        |__ auth
        |__ items
        |__ homes
        |...
        ....
        ....
        ....