import sqlite3

def connect_to_db(db_name):
    """
    Connect to an SQLite database.
    """
    conn = sqlite3.connect(db_name)
    return conn

def create_tables(cursor):
    """
    Create necessary tables for the car parts database.
    """
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Parts (
        part_id INTEGER PRIMARY KEY AUTOINCREMENT,
        part_name TEXT NOT NULL,
        part_description TEXT,
        part_price REAL NOT NULL,
        part_stock INTEGER NOT NULL,
        supplier_id INTEGER,
        FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suppliers (
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_name TEXT NOT NULL,
        supplier_contact TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        customer_contact TEXT,
        customer_vehicle TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date DATE NOT NULL,
        customer_id INTEGER,
        total_amount REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderDetails (
        order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        part_id INTEGER,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (part_id) REFERENCES Parts(part_id)
    )
    ''')

def main():
    """
    Main function to create the database and tables.
    """
    conn = connect_to_db('car_parts.db')
    cursor = conn.cursor()
    create_tables(cursor)
    conn.close()

if __name__ == "__main__":
    main()
