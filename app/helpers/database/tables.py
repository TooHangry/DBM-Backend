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
                    password BLOB NOT NULL,
                    UUID_token BLOB NOT NULL,

                    UNIQUE(email),
                    UNIQUE(UUID_token)
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
                    nickname VARCHAR(128),
                    GUID VARCHAR(128) UNIQUE
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
                    category VARCHAR(64) NOT NULL,
                    UNIQUE(category)
                )
                ''')


def populate_tables(db, connection):
    try:
        db.execute('''
            INSERT INTO categories (category) 
            VALUES
            ('Food'),
            ('Media'),
            ('Clothing'),
            ('Stationary'),
            ('Toys'),
            ('Tools'),
            ('Books'),
            ('Beverages'),
            ('Electronics'),
            ('Furniture'),
            ('Games'),
            ('Vehicles'),
            ('Kitchenware')
        ''')
        connection.commit()
    except:
        print('Categories already added')

    connection.commit()