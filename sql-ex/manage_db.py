import sqlite3
from db_setup import connect_to_db

def insert_part(cursor, part_name, part_description, part_price, part_stock, supplier_id):
    """
    Insert a new part into the Parts table.
    """
    cursor.execute('''
    INSERT INTO Parts (part_name, part_description, part_price, part_stock, supplier_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (part_name, part_description, part_price, part_stock, supplier_id))
    cursor.connection.commit()

def insert_supplier(cursor, supplier_name, supplier_contact):
    """
    Insert a new supplier into the Suppliers table.
    """
    cursor.execute('''
    INSERT INTO Suppliers (supplier_name, supplier_contact)
    VALUES (?, ?)
    ''', (supplier_name, supplier_contact))
    cursor.connection.commit()

def insert_customer(cursor, customer_name, customer_contact, customer_vehicle):
    """
    Insert a new customer into the Customers table.
    """
    cursor.execute('''
    INSERT INTO Customers (customer_name, customer_contact, customer_vehicle)
    VALUES (?, ?, ?)
    ''', (customer_name, customer_contact, customer_vehicle))
    cursor.connection.commit()

def insert_order(cursor, order_date, customer_id, total_amount):
    """
    Insert a new order into the Orders table.
    """
    cursor.execute('''
    INSERT INTO Orders (order_date, customer_id, total_amount)
    VALUES (?, ?, ?)
    ''', (order_date, customer_id, total_amount))
    cursor.connection.commit()

def insert_order_detail(cursor, order_id, part_id, quantity, price):
    """
    Insert a new order detail into the OrderDetails table.
    """
    cursor.execute('''
    INSERT INTO OrderDetails (order_id, part_id, quantity, price)
    VALUES (?, ?, ?, ?)
    ''', (order_id, part_id, quantity, price))
    cursor.connection.commit()

def query_parts(cursor):
    """
    Query all data from the Parts table.
    """
    cursor.execute('SELECT * FROM Parts')
    return cursor.fetchall()

def query_suppliers(cursor):
    """
    Query all data from the Suppliers table.
    """
    cursor.execute('SELECT * FROM Suppliers')
    return cursor.fetchall()

def query_customers(cursor):
    """
    Query all data from the Customers table.
    """
    cursor.execute('SELECT * FROM Customers')
    return cursor.fetchall()

def query_orders(cursor):
    """
    Query all data from the Orders table.
    """
    cursor.execute('SELECT * FROM Orders')
    return cursor.fetchall()

def query_order_details(cursor):
    """
    Query all data from the OrderDetails table.
    """
    cursor.execute('SELECT * FROM OrderDetails')
    return cursor.fetchall()

def update_part(cursor, part_id, part_name, part_description, part_price, part_stock, supplier_id):
    """
    Update a part in the Parts table.
    """
    cursor.execute('''
    UPDATE Parts
    SET part_name = ?, part_description = ?, part_price = ?, part_stock = ?, supplier_id = ?
    WHERE part_id = ?
    ''', (part_name, part_description, part_price, part_stock, supplier_id, part_id))
    cursor.connection.commit()

def update_supplier(cursor, supplier_id, supplier_name, supplier_contact):
    """
    Update a supplier in the Suppliers table.
    """
    cursor.execute('''
    UPDATE Suppliers
    SET supplier_name = ?, supplier_contact = ?
    WHERE supplier_id = ?
    ''', (supplier_name, supplier_contact, supplier_id))
    cursor.connection.commit()

def update_customer(cursor, customer_id, customer_name, customer_contact, customer_vehicle):
    """
    Update a customer in the Customers table.
    """
    cursor.execute('''
    UPDATE Customers
    SET customer_name = ?, customer_contact = ?, customer_vehicle = ?
    WHERE customer_id = ?
    ''', (customer_name, customer_contact, customer_vehicle, customer_id))
    cursor.connection.commit()

def update_order(cursor, order_id, order_date, customer_id, total_amount):
    """
    Update an order in the Orders table.
    """
    cursor.execute('''
    UPDATE Orders
    SET order_date = ?, customer_id = ?, total_amount = ?
    WHERE order_id = ?
    ''', (order_date, customer_id, total_amount, order_id))
    cursor.connection.commit()

def update_order_detail(cursor, order_detail_id, order_id, part_id, quantity, price):
    """
    Update an order detail in the OrderDetails table.
    """
    cursor.execute('''
    UPDATE OrderDetails
    SET order_id = ?, part_id = ?, quantity = ?, price = ?
    WHERE order_detail_id = ?
    ''', (order_id, part_id, quantity, price, order_detail_id))
    cursor.connection.commit()

def delete_part(cursor, part_id):
    """
    Delete a part from the Parts table.
    """
    cursor.execute('''
    DELETE FROM Parts
    WHERE part_id = ?
    ''', (part_id,))
    cursor.connection.commit()

def delete_supplier(cursor, supplier_id):
    """
    Delete a supplier from the Suppliers table.
    """
    cursor.execute('''
    DELETE FROM Suppliers
    WHERE supplier_id = ?
    ''', (supplier_id,))
    cursor.connection.commit()

def delete_customer(cursor, customer_id):
    """
    Delete a customer from the Customers table.
    """
    cursor.execute('''
    DELETE FROM Customers
    WHERE customer_id = ?
    ''', (customer_id,))
    cursor.connection.commit()

def delete_order(cursor, order_id):
    """
    Delete an order from the Orders table.
    """
    cursor.execute('''
    DELETE FROM Orders
    WHERE order_id = ?
    ''', (order_id,))
    cursor.connection.commit()

def delete_order_detail(cursor, order_detail_id):
    """
    Delete an order detail from the OrderDetails table.
    """
    cursor.execute('''
    DELETE FROM OrderDetails
    WHERE order_detail_id = ?
    ''', (order_detail_id,))
    cursor.connection.commit()
