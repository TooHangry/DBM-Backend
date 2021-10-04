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

Structure: \
. \
|__ run.py \
|__ db \
|__ app \
    &emsp;|__ init.py (entry point) \
    &emsp;|__ helpers \
    &emsp;|&emsp;|__ database helpers (all data actions) \
    &emsp;| &emsp;|__ auth helpers (all auth) \
    &emsp;|__ routes \
        &emsp;&emsp;|__ default \
        &emsp;&emsp;|__ auth \
        &emsp;&emsp;|__ items \
        &emsp;&emsp;|__ homes \
        &emsp;&emsp;|... \
        &emsp;&emsp;.... \
        &emsp;&emsp;.... \
        &emsp;&emsp;....