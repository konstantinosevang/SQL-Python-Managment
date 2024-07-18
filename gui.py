import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from db_setup import connect_to_db

def execute_predefined_query(query):
    """
    Execute a predefined SQL query and display the results.
    """
    conn = connect_to_db('car_parts.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Clear previous data in treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Insert new data
        for record in results:
            tree.insert("", "end", values=record)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

def insert_data(table, data):
    """
    Insert data into the specified table.
    """
    conn = connect_to_db('car_parts.db')
    cursor = conn.cursor()
    
    placeholders = ', '.join(['?'] * len(data))
    query = f"INSERT INTO {table} VALUES ({placeholders})"
    
    try:
        cursor.execute(query, data)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

def view_parts():
    """
    View all parts in the database.
    """
    query = "SELECT * FROM Parts"
    execute_predefined_query(query)

def view_suppliers():
    """
    View all suppliers in the database.
    """
    query = "SELECT * FROM Suppliers"
    execute_predefined_query(query)

def view_customers():
    """
    View all customers in the database.
    """
    query = "SELECT * FROM Customers"
    execute_predefined_query(query)

def view_orders():
    """
    View all orders in the database.
    """
    query = "SELECT * FROM Orders"
    execute_predefined_query(query)

def get_columns(table):
    """
    Retrieve the column names for the specified table.
    """
    conn = connect_to_db('car_parts.db')
    cursor = conn.cursor()
    
    query = f"PRAGMA table_info({table})"
    
    try:
        cursor.execute(query)
        columns = [info[1] for info in cursor.fetchall()]
        return columns
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []
    finally:
        conn.close()

def show_insert_window():
    """
    Show a new window for inserting data.
    """
    insert_window = tk.Toplevel()
    insert_window.title("Insert Data")

    tk.Label(insert_window, text="Table:").pack(pady=5)
    table_entry = ttk.Combobox(insert_window, values=["Parts", "Suppliers", "Customers", "Orders"])
    table_entry.pack(pady=5)

    fields_frame = tk.Frame(insert_window)
    fields_frame.pack(pady=10)

    def on_table_select(event):
        for widget in fields_frame.winfo_children():
            widget.destroy()
        
        table = table_entry.get()
        columns = get_columns(table)
        
        entries = []
        for col in columns:
            tk.Label(fields_frame, text=col).pack()
            entry = tk.Entry(fields_frame)
            entry.pack()
            entries.append(entry)
        
        def on_insert():
            data = tuple(entry.get() for entry in entries)
            insert_data(table, data)
        
        insert_button = tk.Button(insert_window, text="Insert", command=on_insert)
        insert_button.pack(pady=10)

    table_entry.bind("<<ComboboxSelected>>", on_table_select)

def main():
    """
    Main function to create a Tkinter GUI for querying the database.
    """
    global tree

    root = tk.Tk()
    root.title("Car Parts Database GUI")

    parts_button = tk.Button(root, text="View Parts", command=view_parts)
    parts_button.pack(pady=10)

    suppliers_button = tk.Button(root, text="View Suppliers", command=view_suppliers)
    suppliers_button.pack(pady=10)

    customers_button = tk.Button(root, text="View Customers", command=view_customers)
    customers_button.pack(pady=10)

    orders_button = tk.Button(root, text="View Orders", command=view_orders)
    orders_button.pack(pady=10)

    insert_button = tk.Button(root, text="Insert Data", command=show_insert_window)
    insert_button.pack(pady=10)

    columns = ("ID", "Name/Description", "Additional Info", "Price/Date", "Stock/Contact", "Supplier/Customer ID")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
