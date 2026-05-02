import sqlite3

def init_db():
    connection = sqlite3.connect('grocery_store.db')
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uom (
            uom_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uom_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            uom_id INTEGER NOT NULL,
            price_per_unit REAL NOT NULL,
            FOREIGN KEY (uom_id) REFERENCES uom (uom_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total REAL NOT NULL,
            datetime TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_details (
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity REAL NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (order_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        )
    ''')

    # Seed data
    cursor.execute('DELETE FROM uom')
    cursor.executemany('INSERT INTO uom (uom_id, uom_name) VALUES (?, ?)', [
        (1, 'Each'),
        (2, 'Kg')
    ])

    cursor.execute('DELETE FROM products')
    cursor.executemany('INSERT INTO products (product_id, name, uom_id, price_per_unit) VALUES (?, ?, ?, ?)', [
        (1, 'Apple', 2, 2.5),
        (2, 'Banana', 2, 1.2),
        (3, 'Milk', 1, 3.0),
        (4, 'Bread', 1, 2.0)
    ])

    connection.commit()
    print("Database initialized successfully.")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    init_db()
