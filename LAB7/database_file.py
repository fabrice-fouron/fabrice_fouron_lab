import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root", # username
        password="helloworld", # password if needed
        database="my_guitar_shop"  # database name
    )

def simple_query():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, line1, city, state, zip_code, phone FROM addresses LIMIT 10;")
    result = cursor.fetchall()
    conn.close()
    output = ""
    for row in result:
        output += f"Customer ID: {row[0]} - Line 1: {row[1]} - City: {row[2]} - State: {row[3]} - ZIP code: {row[4]} - PHONE: {row[5]}\n"
    return output

# simple_query()
def inner_join_query_1():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, email_address, order_date, ship_date
        FROM customers 
        INNER JOIN orders ON customers.customer_id = orders.customer_id;
    """)
    result = cursor.fetchall()
    conn.close()
    output = ""

    for row in result:
        output += f"First Name: {row[0]} - Last Name: {row[1]} - Email Address: {row[2]} - Order Date: {row[3]} - Ship Date: {row[4]}"
    return output

def inner_join_query_2():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category_name, product_name, products.description, date_added
        FROM categories
        INNER JOIN products ON categories.category_id = products.category_id;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""
    for row in result:
        output += f"Category Name: {row[0]} - Product Name: {row[1]} - Description: {row[2]} - Date Added: {row[3]}"
    return output

def inner_join_query_3():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_name, item_price, discount_amount, quantity, (item_price - discount_amount) AS Total
        FROM order_items
        INNER JOIN orders ON order_items.order_id = orders.order_id
        INNER JOIN products ON order_items.item_id = products.product_id;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""
    for row in result:
        output += f"Product Name: {row[0]} - Price: ${row[1]} - Discount: {row[2]} - Quantity: {row[3]} - Total: {row[4]}"
    return result

def inner_join_query_4():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, phone, card_number, line1, state, zip_code
        FROM customers
        INNER JOIN addresses ON addresses.address_id = customers.shipping_address_id
        INNER JOIN orders ON customers.customer_id = orders.customer_id;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""
    for row in result:
        output += f"First Name: {row[0]} - Last Name: {row[1]} - PHONE: {row[2]} - Card Number: {row[3]} - Address: {row[4]}"
    return output

def inner_join_query_5_with_function():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT order_id, SUM(list_price) AS TOTAL
        FROM products
        INNER JOIN order_items ON products.product_id = order_items.item_id
        GROUP BY order_id;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""

    for row in result:
        output += f"Order ID: {row[0]} - Total amount: ${row[0]}"
    return output

def function_query_2():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT concat(first_name, " ", last_name) AS FULL_NAME, COUNT(orders.customer_id) AS num_of_orders
        FROM orders
        INNER JOIN customers ON customers.customer_id = orders.customer_id
        GROUP BY orders.customer_id;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""

    for row in result:
        output += f"Full Name: {row[0]} - Number of orders: {row[1]}"
    return output

def function_query_3():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT customer_id, SUM(tax_amount) AS TOTAL_TAX_AMOUNT
        FROM orders
        GROUP BY customer_id
        LIMIT 10;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""

    for row in result:
        output += f"Customer ID: {row[0]} - Total tax amount: ${row[1]}"
    return output

def function_query_4():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_name, SUM(quantity) AS amount_sold, 
               SUM((item_price*quantity) - (discount_amount*quantity)) AS REVENUE
        FROM order_items
        INNER JOIN products ON products.product_id = order_items.item_id
        GROUP BY product_name;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""

    for row in result:
        output += f"Product Name: {row[0]} - Amount Sold: {row[1]} - Revenue: {row[2]}"
    return output

def function_query_5():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM((item_price*quantity) - (discount_amount*quantity)) AS TOTAL_REVENUE
        FROM order_items;
    """)
    result = cursor.fetchall()
    conn.close()

    output = ""

    for row in result:
        output += f"Total Revenue: ${row[0]}"
    return output
