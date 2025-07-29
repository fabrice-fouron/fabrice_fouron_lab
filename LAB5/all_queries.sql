-- Simple Query --
SELECT customer_id, line1, city, state, zip_code, phone FROM addresses LIMIT 10;

-- Inner Join Query 1 --
SELECT first_name, last_name, email_address, order_date, ship_date
FROM customers 
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

-- Inner Join Query 2 --
SELECT category_name, product_name, products.description, date_added
FROM categories
INNER JOIN products
ON categories.category_id = products.category_id;

-- Inner Join Query 3 --
SELECT product_name, item_price, discount_amount, quantity, (item_price - discount_amount) AS Total
FROM order_items
INNER JOIN orders
INNER JOIN products
ON order_items.order_id = orders.order_id
AND order_items.item_id = products.product_id;

-- Inner Join Query 4 --
SELECT first_name, last_name, phone, card_number, line1, state, zip_code
FROM customers
INNER JOIN addresses
INNER JOIN orders
ON addresses.address_id = customers.shipping_address_id;

-- Inner Join Query 5 and with function --
SELECT order_id, SUM(list_price) AS TOTAL
FROM products
INNER JOIN order_items
ON products.product_id = order_items.item_id
GROUP BY order_id;

 -- Query with function 2 --
SELECT concat(first_name, " ", last_name) AS FULL_NAME, COUNT(orders.customer_id) AS num_of_orders
FROM orders
INNER JOIN customers
ON customers.customer_id = orders.customer_id
GROUP BY orders.customer_id;

-- Query with function 3 --
SELECT customer_id, SUM(tax_amount) AS TOTAL_TAX_AMOUNT
FROM orders
GROUP BY customer_id
LIMIT 10;

-- Query with function 4 --
SELECT product_name, SUM(quantity) AS amount_sold, SUM((item_price*quantity) - (discount_amount*quantity)) AS REVENUE
FROM order_items
INNER JOIN products
ON products.product_id = order_items.item_id
GROUP BY product_name;

-- Query with function 5 --
SELECT SUM((item_price*quantity) - (discount_amount*quantity)) AS  TOTAL_REVENUE
FROM order_items;