import sqlite3
from db_setup import connect_to_db

def insert_sample_data():
    """
    Insert sample data into the database.
    """
    conn = connect_to_db('car_parts.db')
    cursor = conn.cursor()
    
    # Insert sample suppliers
    cursor.execute('''
    INSERT INTO Suppliers (supplier_name, supplier_contact)
    VALUES 
        ('Supplier A', 'contactA@example.com'),
        ('Supplier B', 'contactB@example.com')
    ''')
    
    # Insert sample parts
    cursor.execute('''
    INSERT INTO Parts (part_name, part_description, part_price, part_stock, supplier_id)
    VALUES 
        ('Right-side mirror', 'Honda Civic right hand side mirror', 50.0, 100, 1),
        ('Brake pad', 'High quality brake pad', 25.0, 200, 2),
        ('Air filter', 'Engine air filter for various models', 15.0, 150, 1)
    ''')
    
    # Insert sample customers
    cursor.execute('''
    INSERT INTO Customers (customer_name, customer_contact, customer_vehicle)
    VALUES 
        ('John Doe', 'john@example.com', 'Toyota Camry 2015'),
        ('Jane Smith', 'jane@example.com', 'Honda Accord 2018')
    ''')
    
    # Insert sample orders
    cursor.execute('''
    INSERT INTO Orders (order_date, customer_id, total_amount)
    VALUES 
        ('2024-01-10', 1, 75.0),
        ('2024-02-15', 2, 50.0)
    ''')
    
    # Insert sample order details
    cursor.execute('''
    INSERT INTO OrderDetails (order_id, part_id, quantity, price)
    VALUES 
        (1, 1, 1, 50.0),
        (1, 3, 1, 15.0),
        (2, 2, 2, 25.0)
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()
