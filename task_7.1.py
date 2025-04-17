import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Step 2: Write and run SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Step 3: Read SQL results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Print the summary
print("Sales Summary:")
print(df)

# Step 5: Plot a simple bar chart for revenue by product
plt.figure(figsize=(8, 5))
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save the chart as a PNG file
plt.show()

# Step 6: Close the database connection
conn.close()
