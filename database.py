import sqlite3
# Base database class
class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
    
    def __del__(self):
        self.conn.close()

    def __str__(self):
        return 'Initialize an object to start a connection with a database'

    def __repr__(self):
        return f'Database({self.db})'
    
    # Create new id
    def create_id(self, table, prefix):
        self.c.execute(f'SELECT id FROM {table} ORDER BY id DESC LIMIT 1')
        rows = self.c.fetchall()
        item = rows[0]
        temp_id = int(item[0].strip(prefix))
        return f'{prefix}{"0"*(7-len(str(temp_id)))}{temp_id+1}'

    # Select all table entries
    def fetch(self, table):
        self.c.execute(f'SELECT * FROM {table}')
        rows = self.c.fetchall()
        return rows

    # Insert new item to table
    def insert_master(self, table, prefix, first, last, address, city, state, zipcode, email):
        user_id = self.create_id(table, prefix)
        self.c.execute(
            f'INSERT INTO {table} VALUES (?,?,?,?,?,?,?,?)', (user_id, first, last, address, city, state, zipcode, email))
        self.conn.commit()

# Student class that is instance of Database
class Student(Database):
    # Initialization
    def __init__(self, db):
        super(Student, self).__init__(db)
        self.table = 'student_master'
        self.prefix = 'ST'
        self.c.execute(
            f'CREATE TABLE IF NOT EXISTS {self.table} (id VARCHAR(9) PRIMARY KEY , first_name VARCHAR(50), last_name VARCHAR(50), Address TEXT, city VARCHAR(50), state VARCHAR(50), zip_code VARCHAR(9), email VARCHAR(50))')
        self.conn.commit()

    def __del__(self):
        super(Student, self).__del__()
    
    def __str__(self):
        return 'An instance of the Database class for students'
    
    def __repr__(self):
        return f'Student({self.db})'
    

