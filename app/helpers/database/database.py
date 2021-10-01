from os import path
import sqlite3

connection = sqlite3.connect('db.sqlite3', timeout=10)
db = connection.cursor()


def initData():
    ###########################
    # DATABASE INITIALIZATION #
    ###########################

    # User table
    # You do not need to specify the primary key or a timestamp when inserting
    db.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name VARCHAR(128) NOT NULL,
                    last_name VARCHAR(128) NOT NULL,
                    email VARCHAR(128) NOT NULL,
                    date_joined DATETIME DEFAULT(CURRENT_TIMESTAMP),
                    password VARCHAR(256) NOT NULL,

                    UNIQUE(email)
                )
                ''')

    # Users to Home Table
    #   Relates a user to a home with admin information
    # REMOVE THE UNIQUE CONSTRAINT FOR HOME (just so test data is only entered once)
    db.execute('''
                CREATE TABLE IF NOT EXISTS user_to_homes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user INTEGER NOT NULL,
                    home INTEGER NOT NULL,
                    is_admin CHAR(1) NOT NULL DEFAULT('F'),

                    UNIQUE(home),
                    FOREIGN KEY(user) REFERENCES user(id),
                    FOREIGN KEY(home) REFERENCES home(id)
                )
                ''')


    # Home table
    # REMOVE THE UNIQUE CONSTRAINT FOR NICKNAME (just so test data is only entered once)
    db.execute('''
                CREATE TABLE IF NOT EXISTS homes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nickname VARCHAR(128) UNIQUE
                )
                ''')
    

    # Insert Dummy Data
    try:
        db.execute('''
            INSERT INTO users (first_name, last_name, email, password) 
            VALUES
            ('Robert', 'Connolly', 'rec73@uakron.edu', 'password1'),
            ('Brendon', 'Lovejoy', 'bjl66@uakron.edu', 'password2'),
            ('Tyler', 'Moff', 'tdm105@uakron.edu', 'password3')
        ''')
        connection.commit()
    except:
        print('Users already added')

    try:
        db.execute('''
            INSERT INTO homes (nickname) 
            VALUES
            ('Robert''s Residence'),
            ('Tyler''s Townhome'),
            ('Brendon''s Barndemenium')
        ''')
        connection.commit()
    except:
        print('Homes already added')

    try:
        db.execute('''
            INSERT INTO user_to_homes (user, home) 
            VALUES
            (1, 1),
            (2, 2),
            (3, 3)
        ''')
        connection.commit()
    except:
        print('User To Homes already added')

    connection.commit()        

    