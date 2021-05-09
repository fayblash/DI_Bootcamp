<!-- Exercise 1 : Items And Customers
Create a database called public.
<!--  -->

<!-- Add two tables:
items
customers. -->

CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 name_item VARCHAR (50) NOT NULL,
 price SMALLINT NOT NULL
)
CREATE TABLE customer(
 cust_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL
)
<!-- Follow the below instructions to determine which columns to add to the two tables:

Add the following items to the items table:
Small Desk – 100 (ie. price)
Large desk – 300
<!-- Fan – 80 -->
INSERT INTO items (name_item, price)
VALUES
('Small Desk',100),
('Large Desk',300),
('Fan',80);
<!-- Add 5 new customers to the customers table:
Greg Jones
Sandra Jones
Scott Scott
Trevor Green
Melanie Johnson -->
INSERT INTO customer (first_name, last_name)
VALUES
('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');

<!-- Use SQL to fetch the following data from the database:
<!-- All the items. -->
SELECT * FROM items
<!-- All the items with a price above 80 (80 not included). -->
SELECT * FROM items WHERE price > 80
<!-- All the items with a price below 300. (300 included) -->
SELECT * FROM items WHERE price < 300
<!-- All customers whose last name is ‘Smith’ (What will be your outcome?). -->
SELECT * FROM customer WHERE last_name ='Smith'
<!-- All customers whose last name is ‘Jones’. -->
SELECT * FROM customer WHERE last_name ='Jones'
<!-- All customers whose firstname is not ‘Scott’. --> --> --> -->
SELECT * FROM customer WHERE first_name !='Scott'