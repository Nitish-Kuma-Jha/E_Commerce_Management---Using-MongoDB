📦 E_Commerce_Management – Using MongoDB

📌 Project Overview

E_Commerce_Management – Using MongoDB is a Python-based database project that demonstrates how MongoDB can be used to manage core e-commerce operations. The project uses PyMongo to perform CRUD operations, aggregation pipelines, and data relationships across multiple collections such as Products, Customers, and Orders through a menu-driven command-line interface.

🛠 Technologies Used

Python

MongoDB

PyMongo

MongoDB Aggregation Framework

Command Line Interface (CLI)

🗂 Database Structure

Products – Stores product details such as name, price, and quantity

Customers – Stores customer information like name, email, and city

Orders – Stores order details including product, quantity, total price, order date, and status

✨ Key Features

Admin-secured product management

Add, view, and manage products and customers

Place, modify, and delete orders

Automatic order status updates (Processing → Packed → Shipped → Delivered)

Inventory management with quantity updates

Revenue calculation and total sales reports

Top-selling product analysis using aggregation

Customer-wise order history and billing

MongoDB $lookup for joining customer and product data

Advanced queries (sorting, filtering, counting, grouping)

▶️ How to Run the Project

Make sure MongoDB is running on your system

Install required library:

pip install pymongo


Run the Python file:

python ecommerce_management.py


Use the menu options to interact with the system

🔐 Admin Access

Some operations require admin authentication:

Username: Nitish Kumar Jha

Password: Nitish898k@

📊 Learning Outcomes

MongoDB schema design for real-world applications

Hands-on experience with CRUD operations

Aggregation pipelines for analytics

Inventory and order management logic

Data relationship handling using $lookup

📌 Conclusion

This project showcases the practical use of MongoDB as a standalone database solution for managing e-commerce data, focusing on performance, scalability, and efficient data handling through Python.
