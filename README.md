# Management System Template

## Overview

This project provides a template for managing various entities using SQLite and Tkinter for the GUI. It allows users to insert, view, update, and delete data in the database, and offers a user-friendly interface for non-specialized users to query the database. The template can be customized for different use cases, such as inventory management, customer relations, or order tracking.

### Example: Car Parts Management System

In this example, the template is customized to manage car parts, suppliers, customers, and orders. The system includes features to manage car parts inventory, track suppliers, manage customer information, and handle orders.

## Features

- Database Setup: Create and initialize the database tables.
- Data Input: Insert data into parts, suppliers, customers, and orders tables.
- Query Execution: Execute predefined SQL queries to view parts, suppliers, customers, and orders.
- User-Friendly GUI: Simple and intuitive GUI for managing the database.

## Screenshots

### Main Interface

![Main Interface](path_to_image1.png)

The main interface of the Car Parts Database GUI provides buttons to view different types of data:

- View Parts
- View Suppliers
- View Customers
- View Orders
- Insert Data

It also displays a table showing sample data for car parts, including ID, Name/Description, Additional Info, Price/Date, Stock/Contact, and Supplier/Customer ID.

### Data Insertion Interface

![Data Insertion Interface](path_to_image2.png)

The data insertion interface allows users to add new entries to the database:

- A dropdown menu to select the table for data insertion (e.g., Orders)
- Input fields for relevant data (e.g., order_id, order_date, customer_id, total_amount)
- An "Insert" button to submit the new data

## Requirements

- Python 3.x
- SQLite
- Tkinter

## Installation

1. Clone the Repository:

   ```sh
   git clone https://github.com/konstantinosevang/SQL-Python-Managment.git
   cd car-parts-management
   ```

2. Create a Virtual Environment:

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install Dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script to set up the database and start the GUI:

```sh
python main.py
```

### GUI Operations

- View Parts: Displays all parts in the database.
- View Suppliers: Displays all suppliers in the database.
- View Customers: Displays all customers in the database.
- View Orders: Displays all orders in the database.
- Insert Data: Opens a new window to insert data into parts, suppliers, customers, or orders.

## Customization

To customize this template for different use cases, modify the database schema and GUI components as needed. Update the scripts in the `scripts` directory to match the new schema and functionalities.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, enhancements, or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- SQLite
- Tkinter

## Contact

For any inquiries, please contact konstantinosevang@gmail.com.
