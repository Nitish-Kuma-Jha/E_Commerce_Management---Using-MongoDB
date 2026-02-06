from pymongo import MongoClient
from datetime import datetime, timedelta


client = MongoClient("mongodb://localhost:27017/")
db = client["E_Commerce_Database"]

products_collection = db["Products"]
customers_collection = db["Customers"]
orders_collection = db["Orders"]


def admin_access():
    ADMIN_USERNAME = "Nitish Kumar Jha"
    ADMIN_PASSWORD = "Nitish898k@"

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def add_product():
    if not admin_access():
        print("Access denied.")
        return

    product = {
        "name": input("Enter product name: "),
        "price": float(input("Enter product price: ")),
        "Quantity": int(input("Enter product quantity: "))
    }
    products_collection.insert_one(product)
    print("Product added successfully.")

def view_products():
    for p in products_collection.find():
        print(p)

def add_customer():
    customer = {
        "name": input("Enter customer name: "),
        "email": input("Enter customer email: "),
        "city": input("Enter customer city: ")
    }
    customers_collection.insert_one(customer)
    print("Customer added successfully.")

def view_customers():
    for c in customers_collection.find():
        print(c)

def place_order():
    customer_email = input("Enter customer email: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    customer = customers_collection.find_one({"email": customer_email})
    product = products_collection.find_one({"name": product_name})

    if not customer or not product:
        print("Customer or Product not found.")
        return

    if product["Quantity"] < quantity:
        print("Insufficient quantity.")
        return

    total_price = product["price"] * quantity

    order = {
        "customer_email": customer_email,
        "product_name": product_name,
        "quantity": quantity,
        "total_price": total_price,
        "order_date": datetime.now(),
        "order_status": "Processing"
    }

    orders_collection.insert_one(order)
    products_collection.update_one(
        {"name": product_name},
        {"$inc": {"Quantity": -quantity}}
    )
    print("Order placed successfully.")

def modify_order():
    customer_email = input("Enter customer email: ")
    new_quantity = int(input("Enter new quantity: "))

    order = orders_collection.find_one({"customer_email": customer_email})
    if not order:
        print("Order not found.")
        return

    product = products_collection.find_one({"name": order["product_name"]})
    available = product["Quantity"] + order["quantity"]

    if available < new_quantity:
        print("Insufficient quantity.")
        return

    new_total = product["price"] * new_quantity

    orders_collection.update_one(
        {"_id": order["_id"]},
        {"$set": {"quantity": new_quantity, "total_price": new_total}}
    )

    products_collection.update_one(
        {"name": order["product_name"]},
        {"$inc": {"Quantity": order["quantity"] - new_quantity}}
    )

    print("Order modified successfully.")

def view_orders():
    for o in orders_collection.find():
        print(o)

def delete_order():
    email = input("Enter customer email: ")
    result = orders_collection.delete_one({"customer_email": email})
    print("Order deleted." if result.deleted_count else "Order not found.")

def update_order_status():
    now = datetime.now()

    for order in orders_collection.find():
        hours = (now - order["order_date"]).total_seconds() / 3600

        if hours >= 72:
            status = "Delivered"
        elif hours >= 48:
            status = "Shipped"
        elif hours >= 24:
            status = "Packed"
        else:
            status = "Processing"

        orders_collection.update_one(
            {"_id": order["_id"]},
            {"$set": {"order_status": status}}
        )

def order_status():
    update_order_status()
    for o in orders_collection.find():
        print(
            f"Email: {o['customer_email']} | "
            f"Product: {o['product_name']} | "
            f"Status: {o['order_status']}"
        )

def customer_overall_orders_details():
    email = input("Enter customer email: ")
    customer = customers_collection.find_one({"email": email})
    if not customer:
        print("Customer not found.")
        return

    orders = list(orders_collection.find({"customer_email": email}))
    if not orders:
        print("No orders found.")
        return

    total_amount = sum(o["total_price"] for o in orders)

    print(customer)
    for o in orders:
        print(o)
    print("Total Amount:", total_amount)

def discount_calculation(total_amount):
    if total_amount > 5000:
        return total_amount * 0.10
    elif total_amount > 3000:
        return total_amount * 0.05
    return 0

def total_revenue():
    pipeline = [
        {
            "$group": {
                "_id": None,
                "Total_revenue": {"$sum": "$total_price"}
            }
        }
    ]
    print(list(orders_collection.aggregate(pipeline)))

def top_selling_product():
    pipeline = [{
            "$group": {
                "_id": "$product_name",
                "Total_revenue": {"$sum": "$quantity"}
            }},
            {"$sort":{"Total_sold":-1}},
            {"$limit":2}
    ]
    print(list(orders_collection.aggregate(pipeline)))

def order_detail_along_with_customer_info():
    pipeline = [
        {
            "$lookup": {
                "from": "Customers",
                "localField": "customer_email",
                "foreignField": "email",
                "as": "customer_details"
            }
        }
    ]
    for doc in orders_collection.aggregate(pipeline):
        print(doc)

def order_with_product_info():
    pipeline = [
        {
            "$lookup": {
                "from": "Products",
                "localField": "product_name",
                "foreignField": "name",
                "as": "product_details"}
            }
    ]
    for doc in orders_collection.aggregate(pipeline):
        print(doc)
    
def price_greater():
    for product in products_collection.find({"price": {"$gt": 2000}}):
        print(product)

def customers_from_city():
    city = input("Enter city name: ")
    for customer in customers_collection.find({"city": city}):
        print(customer)

def sort_products_by_price_desc():
    for product in products_collection.find().sort("price", -1):
        print(product)

def count_total_orders():
    total_orders = orders_collection.count_documents({})
    print(f"Total number of orders placed: {total_orders}")

def increase_product_quantity():
    result = products_collection.update_many(
        {},
        {"$inc": {"Quantity": 15}}
    )
    print(f"Updated {result.modified_count} products' quantities.")

def discount():
    result = db.Products.update_one(
        {"$set": {"discount": {"Laptop": 1000}}}
    )
    print(f"Added 'discount' field to {result.modified_count} products.")

def total_sales():
    pipeline = [
        {
            "$group":{
                "_id": "$product_name",
                "Total_sales": {"$sum": "$total_price"}
            }
        }
    ]
    print(list(orders_collection.aggregate(pipeline)))




def menu():
    while True:
        print("""
1. Add Product
2. View Products
3. Add Customer
4. View Customers
5. Place Order
6. Modify Order
7. View Orders
8. Customer Order Details
9. Delete Order
10. Order Status
11. Total Revenue
12. Top Selling Product
13. Order Details with Customer Info
14. Order Details with Product Info
15. Products with Price Greater than 2000
16. find all customers from a specific city
17. sort products by price in descending order
18. count total number of orders placed
19. increase the quantity of all products by 15
20. add a new field 'discount' with default value 0 to all products
21. wishlist in customer details
22. total sales for each product
23. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            place_order()
        elif choice == "6":
            modify_order()
        elif choice == "7":
            view_orders()
        elif choice == "8":
            customer_overall_orders_details()
        elif choice == "9":
            delete_order()
        elif choice == "10":
            order_status()
        elif choice == "11":
            total_revenue()
        elif choice == "12":
            top_selling_product()
        elif choice == "13":
            order_detail_along_with_customer_info()
        elif choice == "14":
            order_with_product_info()
        elif choice == "15":
            price_greater()
        elif choice == "16":
            customers_from_city()
        elif choice == "17":
            sort_products_by_price_desc()
        elif choice == "18":
            count_total_orders()
        elif choice == "19":
            increase_product_quantity()
        elif choice == "20":
            discount()
        elif choice == "21":
            wishlist_customers()
        elif choice == "22":
            total_sales()
        elif choice == "23":
            break
        else:
            print("Invalid choice.")

menu()
