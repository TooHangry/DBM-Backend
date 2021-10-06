import sqlite3
import app.helpers.database.serializers as serializers

# Running on a single thread
connection = sqlite3.connect('db.sqlite3', timeout=10, check_same_thread=False)
db = connection.cursor()


# SELECT home_items.item_name, home_items.quantity, categories.category
# from home_items
# Join categories on categories.id = home_items.category
# WHERE home = 1 AND home_items.category = 1

################
# USER QUERIES #
################

def login_current_user(email, password):
    db.execute('''
                SELECT *
                FROM users
                WHERE email = '{}' AND password = '{}';
                '''.format(email, password))
    users = serializers.serialize_users(db.fetchall())
    return users[0] if len(users) > 0 else {}    
    

def get_user_homes(id):
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

def get_user_by_id(id):
    db.execute('''
                SELECT * 
                FROM users
                WHERE id = {}
                '''.format(id))
    users = serializers.serialize_users(db.fetchall())
    return users[0] if len(users) > 0 else {}


def get_all_users():
    db.execute('''
                SELECT * 
                FROM users
                ''')
    users = serializers.serialize_users(db.fetchall())
    return users

###########################
# DATABASE INITIALIZATION #
###########################
def initialize_database():
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
    db.execute('''
                CREATE TABLE IF NOT EXISTS user_to_homes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user INTEGER NOT NULL,
                    home INTEGER NOT NULL,
                    is_admin CHAR(1) NOT NULL DEFAULT('F'),

                    FOREIGN KEY(user) REFERENCES user(id),
                    FOREIGN KEY(home) REFERENCES home(id),
                    UNIQUE(user, home)
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

    # Home Items table
    db.execute('''
                CREATE TABLE IF NOT EXISTS home_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    home INTEGER NOT NULL,
                    quantity INTEGER,
                    item_name VARCHAR(64),
                    category INTEGER NOT NULL,

                    FOREIGN KEY(home) REFERENCES homes(id)
                    FOREIGN KEY(category) REFERENCES categories(id)
                )
                ''')

    # Home Items table
    db.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category VARCHAR(64),
                    UNIQUE(category)
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
            ('Brendon''s Barndemenium'),
            ('Tyler''s Townhome')
        ''')
        connection.commit()
    except:
        print('Homes already added')

    try:
        db.execute('''
            INSERT INTO user_to_homes (user, home, is_admin) 
            VALUES
            (1, 1, 'T'),
            (1, 3, 'F'),
            (1, 2, 'F'),
            (2, 2, 'T'),
            (2, 3, 'F'),
            (3, 3, 'T')
        ''')
        connection.commit()
    except:
        print('User To Homes already added')

    try:
        db.execute('''
            INSERT INTO categories (category) 
            VALUES
            ('Food'),
            ('Media'),
            ('Clothing'),
            ('Stationary'),
            ('Toys'),
            ('Kitchenware')
        ''')
        connection.commit()
    except:
        print('Categories already added')

    # try:
    db.execute('''
        INSERT INTO home_items (home, quantity, item_name, category) 
        VALUES
        (1, 5, 'Apple', 1),
        (1, 2, 'Peach', 1),
        (1, 1, 'Bread', 1),
        (1, 69, 'Brendon', 1),
    ''')
    connection.commit()
    # except:
    #     print('Items already added')

    connection.commit()        