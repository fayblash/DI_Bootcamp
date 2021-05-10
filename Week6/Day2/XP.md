<!-- Exercise 1 : Items And Customers
Instructions
<!-- We will work on the public database that we created yesterday. -->

<!-- Use SQL to get the following from the database:
All items, ordered by price (lowest to highest). -->
select * from items order by price asc
<!-- Items with a price above 80 (80 included), ordered by price (highest to lowest). -->
select * from items where price>=80 order by price asc 

<!-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results. -->
select first_name,last_name from customer order by last_name asc limit 3

<!-- All last names (no other columns!), in reverse alphabetical order (Z-A) -->
select last_name from customer order by last_name desc 

<!-- Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table: -->
CREATE TABLE purchases(
id SERIAL PRIMARY KEY,
cust_id  SMALLINT NOT NULL,
item_id  SMALLINT NOT NULL,
FOREIGN KEY (cust_id) REFERENCES customer (cust_id),
FOREIGN KEY (item_id) REFERENCES items (item_id)
)

<!-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not? -->

<!-- Add 5 rows which reference existing customers and items. -->
INSERT INTO purchases (cust_id,item_id) 
VALUES
    ( (SELECT cust_id from customer WHERE first_name='Greg'),(SELECT item_id from items WHERE item_id=1)),
    ( (SELECT cust_id from customer WHERE first_name='Trevor'),(SELECT item_id from items WHERE item_id=3)),
    ( (SELECT cust_id from customer WHERE first_name='Sandra'),(SELECT item_id from items WHERE item_id=2));

<!-- Use SQL to get the following from the database: -->
<!-- All purchases. Is this information useful to us? No -->

<!-- All purchases, joining with the customers table. -->
SELECT customer.first_name, customer.last_name, purchases.id
FROM customer
INNER JOIN purchases
ON customer.cust_id = purchases.cust_id;

<!-- Purchases of the customer with the ID equal to 4. -->
select * from purchases where cust_id=4

<!-- Purchases for a large desk AND a small desk -->
select items.name_item,purchases.id
from items
inner join purchases
on items.item_id=purchases.item_id
where items.name_item = 'Small Desk' or items.name_item='Large Desk';

<!-- Create a purchase for Scott Scott – he bought a hard drive. -->
INSERT INTO items (name_item, price)
VALUES
('Hard Drive',250);
INSERT INTO purchases (cust_id,item_id) 
VALUES
( (SELECT cust_id from customer WHERE first_name='Scott'),(SELECT item_id from items WHERE name_item='Hard Drive'));


<!-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
Customer first name
Customer last name
Item name -->
SELECT customer.first_name,customer.last_name,items.name_item 
FROM purchases 
INNER JOIN customer ON purchases.cust_id = customer.cust_id
INNER JOIN items ON purchases.item_id = items.item_id;


<!-- Exercise 2 : Dvdrental Database
We will use the newly installed dvdrental database.

<!-- In the dvdrental database write a query to select all the columns from the “customer” table. -->
select * from customer
<!-- Write a query to display the names (first_name, last_name) using an alias named “full_name”. -->
select concat(first_name,' ',last_name) as full_name from customer

<!-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates). -->
SELECT DISTINCT create_date FROM customer;

<!-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name. -->
select * from customer order by first_name desc

<!-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate. -->
select film_id,title,description,release_year,rental_rate from film order by rental_rate asc

<!-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table. -->
select address,phone,district from address where district = 'Texas';

<!-- Write a query to retrieve all movie details where the movie id is either 15 or 150. -->
select * from film where film_id = 15 or film_id=150

<!-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table. -->
select film_id,title,description,length,rental_rate from film where title = 'Baked Cleopatra';

<!-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie. -->
select film_id,title,description,length,rental_rate from film where title like 'Ba%';

<!-- Write a query which will find the 10 cheapest movies. -->
select title from film order by rental_rate asc limit 10 


<!-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
Bonus: Try to not use LIMIT. -->
select title from film order by rental_rate asc limit 10 offset 10

<!-- Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…). -->
SELECT concat(customer.first_name,' ',customer.last_name) as customer_name,payment.amount,payment.payment_date 
FROM payment
INNER JOIN customer ON payment.customer_id=customer.customer_id
order by payment.customer_id asc;

<!-- You need to check your inventory. Write a query to get all the movies which are not in inventory. -->
select film.title
from film
join inventory on film.film_id=inventory.film_id 
where film.film_id not in (inventory.film_id) 

<!-- Write a query to find which city is in which country. -->
select city.city,country.country
from city
join country on city.country_id=country.country_id

<!-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd. -->
