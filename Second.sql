--Create a Table Product with columns product id, product name, price, category, units
create table Product(
ID integer,
Name text,
price real,
category text,
units integer
);

insert into Product(ID, Name, price, category, units)
VALUES
(1, 'Sonic Ultra', 1500.50, 'Monitor', 150),
(2, 'Gaming MousePad', 30, 'MousePad', 40),
(3, 'Click-Clack', 150.49, 'Keyboard', 300),
(4, 'Ventilation-Model', 10.99, 'Mouse', 100),
(5, 'Fitbit', 300.99, 'Watch', 30),
(6, 'iPhone', 1000.00, 'Phone', 500),
(7, 'Samsung S23', 700.00, 'Phone', 450),
(8, 'Beats223', 80, 'HeadPhones', 100),
(9, 'Dualsense-Wireless', 75, 'Controller', 150),
(10, 'Digi-Art', 40, 'i-Pad Pen', 35);
select * from Product;
select distinct category from product;
select sum(price) from Product;
select * from Product where price = (select max(price) from product);