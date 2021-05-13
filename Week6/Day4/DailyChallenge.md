<!-- Create a table orders and a table items. You decide which fields should be in each table, but each item should have a price. -->
create table orders(
    id serial primary key,
    order_id int,
    item_id int,
    date_sold date,
    buyer_id int,
    foreign key (item_id) references items(id),
    foreign key(buyer_id) references buyers(id)
)

create table items(
    id serial primary key,
    item_name varchar(100),
    price int
)

create table buyers(
    id serial primary key,
    name varchar(100),
    phone_number varchar(15)
)
insert into items(item_name,price)
values
('Table lamp',100),
('USB Charger',20),
('Fan',80),
('Curtains',75),
('Recliner',1000),
('Rug',250),
('Bookcase',550);

insert into buyers(name,phone_number)
values
('Fay Blashka','0549877253'),
('Ezra Gersten','0586523761'),
('Michelle Nagel','0583456778');

insert into orders(order_id,item_id,date_sold,buyer_id)
values
(1,3,'2020-01-05',2),
(1,5,'2020-01-05',2),
(2,7,'2021-05-01',1),
(2,6,'2021-05-01',1),
(2,1,'2021-05-01',1),
(3,2,'2021-05-12',3),
(4,4,'2021-05-12',2);




There is a relationship of one to many between the orders and the table items

Create a function that returns the total price for a given order

select sum(items.price) as total from orders
inner join items on orders.item_id=items.id
group by order_id

CREATE FUNCTION total_order(order_id int) RETURNS int AS $total$
BEGIN
   RETURN(SELECT sum(items.price) FROM orders inner join items on orders.item_id=items.id
group by orders.order_id);
END;
$total$ LANGUAGE plpgsql;

select * from total_order(4)

select sum(items.price) as total,buyers.name,orders.order_id from orders
inner join items on orders.item_id=items.id
inner join buyers on orders.buyer_id=buyers.id
group by buyer_id,buyers.name,orders.order_id
order by order_id


Bonus :
Create a table users
There is a relationship of one to many between the table user and the table orders
Create a function that returns the total price for a given order of a given user

