import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a simple sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sample_data = [
    ('Laptop', 2, 700.00),
    ('Laptop', 1, 700.00),
    ('Mouse', 5, 20.00),
    ('Mouse', 10, 18.00),
    ('Keyboard', 3, 45.00),
    ('Monitor', 2, 150.00),
    ('Monitor', 1, 155.00),
    ('USB Cable', 4, 5.00),
    ('USB Cable', 6, 4.50)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample sales_data.db created successfully!")
