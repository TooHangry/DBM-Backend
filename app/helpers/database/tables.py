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
                    UNIQUE(UUID_token),
                    CHECK(email LIKE '%@%.%')
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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    home INTEGER NOT NULL,
                    quantity INTEGER,
                    item_name VARCHAR(64),
                    category INTEGER NOT NULL,
                    alert_threshold INTEGER,

                    FOREIGN KEY(home) REFERENCES homes(id)
                    FOREIGN KEY(category) REFERENCES categories(id)
                )
                ''')

    # Home categories table
    db.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category VARCHAR(64) NOT NULL,
                    UNIQUE(category)
                )
                ''')
    
    # Invite table
    db.execute('''
                CREATE TABLE IF NOT EXISTS invite (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(128) NOT NULL,
                    home INTEGER NOT NULL,

                    FOREIGN KEY (home) REFERENCES homes(id),
                    CHECK(email LIKE '%@%.%')
                );
                ''')
    
    # Shopping List Table
    db.execute('''
               CREATE TABLE IF NOT EXISTS shopping_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tasked_to INTEGER NOT NULL,
                    home_tasked INTEGER NOT NULL,
                    tasked_on DATETIME DEFAULT(CURRENT_TIMESTAMP),

                    FOREIGN KEY (tasked_to) REFERENCES user(id),
                    FOREIGN KEY (home_tasked) REFERENCES home(id)
                );
                ''')


    # Shopping List Items Table
    db.execute('''
               CREATE TABLE IF NOT EXISTS list_items (
                    list_id INTEGER NOT NULL,
                    item_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    is_complete CHAR(1) NOT NULL,

                    PRIMARY KEY (list_id, item_id)
                    FOREIGN KEY (list_id) REFERENCES shopping_list(id),
                    FOREIGN KEY (item_id) REFERENCES home_items(id)
                    CHECK (quantity > 0)
                );
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