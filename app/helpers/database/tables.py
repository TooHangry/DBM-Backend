def create_tables(db):
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
                    user INTEGER NOT NULL,
                    home INTEGER NOT NULL,
                    is_admin CHAR(1) NOT NULL DEFAULT('F'),

                    FOREIGN KEY(user) REFERENCES user(id),
                    FOREIGN KEY(home) REFERENCES home(id),
                    PRIMARY KEY (user, home)
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
                    home INTEGER NOT NULL,
                    quantity INTEGER,
                    item_name VARCHAR(64),
                    category INTEGER NOT NULL,
                    alert_threshold INTEGER,

                    PRIMARY KEY (home, item_name),
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


def populate_tables(db, connection):
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

    try:
        db.execute('''
            INSERT INTO home_items (home, quantity, item_name, category, alert_threshold) 
            VALUES
            (1, 5, 'Apple', 1, 2),
            (1, 2, 'Peach', 1, 2),
            (1, 1, 'Bread', 1, 0),
            (1, 1, 'Lord of the Rings', 2, 0),
            (1, 1, 'Star Wars', 2, 0),
            (1, 15, 'Pencil', 4, 0),
            (1, 300, 'Paper', 4, 20)
        ''')
        connection.commit()
    except:
        print('Items already added')

    connection.commit()      