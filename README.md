# 🧾 Task 7: Basic Sales Summary using SQLite & Python

## 📌 Objective
Extract and visualize basic sales insights from a SQLite database using Python.

## 🛠 Tools Used
- Python
- SQLite (via sqlite3)
- Pandas
- Matplotlib

## 📁 Dataset
A SQLite database named sales_data.db containing a single table called sales. The table includes:
- product (text)
- quantity (integer)
- price (real)

## 🚀 What the Script Does
- Connects to the sales_data.db database
- Runs a SQL query to compute total quantity sold and total revenue for each product
- Loads results into a pandas DataFrame
- Prints the summary table
- Plots a bar chart showing revenue by product
- Saves the chart as sales_chart.png
A simple summary table and a bar chart that visualize how much revenue each product generated.
