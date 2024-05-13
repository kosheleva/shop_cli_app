CREATE DATABASE IF NOT EXISTS shop;

USE shop;

-- Create table "Categories"
CREATE TABLE IF NOT EXISTS shop.Categories (
	id INTEGER AUTO_INCREMENT,
    title CHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Fill in the table "Categories"
INSERT INTO shop.Categories
    (title)
VALUES
    ('Gold rings'),
    ('Gold earrings'),
    ('Gold bracelets'),
    ('Silver rings'),
    ('Silver earrings'),
    ('Silver bracelets'),
    ('Pendants'),
    ('Elite jewelry'),
    ('Watches'),
    ('Souvenirs and gifts');


-- Create table "Delivery Methods"
CREATE TABLE IF NOT EXISTS shop.DeliveryMethods (
	id INTEGER AUTO_INCREMENT,
    d_type CHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Fill in the table "Delivery Methods"
INSERT INTO shop.DeliveryMethods
    (d_type)
VALUES
    ('Pick up goods'),
    ('Post office'),
    ('Сourier'); 

-- Create table "Payment Methods"
CREATE TABLE IF NOT EXISTS shop.PaymentMethods (
	id INTEGER AUTO_INCREMENT,
    p_type CHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Fill in the table "Payment Methods"
INSERT INTO shop.PaymentMethods
    (p_type)
VALUES
    ('Cash'),
    ('Credit card'),
    ('Google Pay'),
    ('Apple Pay'); 

-- Create table "Customers"
CREATE TABLE IF NOT EXISTS shop.Customers (
	id INTEGER AUTO_INCREMENT,
	name CHAR(35) NOT NULL,
	surname CHAR(50) NOT NULL,
    password CHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Fill in the table "Customers"
INSERT INTO shop.Customers
    (name, surname, password)
VALUES
    ('Maria', 'Ko', 'Dj87#fD6sHHs0sywI');
        
-- Create table "Products"
CREATE TABLE IF NOT EXISTS shop.Products (
	id INTEGER AUTO_INCREMENT,
    code CHAR(20) NOT NULL,
	title CHAR(100) NOT NULL,
	price FLOAT NOT NULL,
    currency CHAR(10) NOT NULL,
    quantity SMALLINT NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES shop.Categories (id)
);

    
-- Fill in the table "Products"
INSERT INTO shop.Products
    (code, title, price, currency, quantity, category_id)
VALUES
    ('156399-547', 'Emerald-Cut Lab-Created Emerald and 1/4 CT. T.W. Diamond Frame Three Stone Ring in 10K Gold', 749, 'USD', 5, 1),
    ('1741356-547', '15.0mm Tube Hoop Earrings in 10K Gold', 349, 'USD', 2, 2),
    ('1683953-919', '1/10 CT. T.W. Diamond Channel-Set Huggie Hoop Earrings in 10K Gold', 420, 'USD', 1, 2),
    ('1770556-919', '1/4 CT. T.W. Diamond Station Bracelet in 10K Gold - 7', 2000, 'USD', 7, 3),
    ('1284225-919', '3.0mm Engravable Low Dome Comfort-Fit Wedding Band in 10K Rose Gold (1 Line)', 229, 'USD', 1, 4),
    ('143336-919', '6.0mm Diamond-Cut Swirl Milgrain Edge Comfort Fit Wedding Band in 10K Gold with White Rhodium', 400, 'USD', 2, 4),
    ('144277-919', '1/5 CT. T.W. Diamond Wishbone-Shaped Huggie Hoop Earrings in Sterling Silver', 469, 'USD', 9, 5),
    ('146711-919', '1/5 CT. T.W. Pear-Shaped Multi-Diamond Triple Frame Pendant in Sterling Silver', 539, 'USD', 1, 7),
    ('1773643-919', 'Vera Wang Men 3.0mm Black Spinel Tennis Bracelet in Sterling Silver with Black Ruthenium', 539, 'USD', 12, 8),
    ('1780749-919', 'Mens Citizen Tsuyosa Collection Automatic Watch with Blue Sunray Dial', 450, 'USD', 1, 9),
    ('1677609-919', 'Ladies Oval Birthstone and Diamond Accent Scroll Shank Class Ring in Sterling Silver and 18K Gold Plate (1 Stone)', 208, 'USD', 15, 10),
    ('1765780-919', 'Mens NHL Logo Cuff Links (Select Team)', 110, 'USD', 2, 10);

-- Create table "Discounts"
CREATE TABLE IF NOT EXISTS shop.Discounts (
	id INTEGER AUTO_INCREMENT,
	product_id INTEGER NOT NULL,
    discount SMALLINT NOT NULL,
    from_date DATE NOT NULL,
    due_date DATE NOT NULL,
    PRIMARY KEY (id),
	FOREIGN KEY (product_id) REFERENCES Products(id)
);

-- Fill in the table "Discounts"
INSERT INTO shop.Discounts 
    (product_id, discount, from_date, due_date)
VALUES
    (1, 5, CURDATE(), CURDATE() + INTERVAL 10 DAY),
    (2, 10, CURDATE(), CURDATE() + INTERVAL 10 DAY),
    (5, 8, CURDATE(), CURDATE() + INTERVAL 5 DAY),
    (7, 25, CURDATE(), CURDATE() + INTERVAL 3 DAY),
    (8, 35, CURDATE(), CURDATE() + INTERVAL 10 DAY),
    (9, 15, CURDATE(), CURDATE() + INTERVAL 5 DAY),
    (10, 15, CURDATE(), CURDATE() + INTERVAL 5 DAY),
    (12, 7, CURDATE(), CURDATE() + INTERVAL 10 DAY);

-- Create table "Orders"
CREATE TABLE IF NOT EXISTS shop.Orders (
	id INTEGER AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    payment_method_id INTEGER NOT NULL,
    delivery_method_id INTEGER NOT NULL,
    quantity SMALLINT NOT NULL,
    price FLOAT NOT NULL,
    currency CHAR(10) NOT NULL,
    payment_status ENUM('pending', 'done'),
    delivery_address TEXT NOT NULL,
    delivery_status ENUM('in_progress', 'delivered'),
    order_date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES Customers (id),
    FOREIGN KEY (product_id) REFERENCES Products (id),
    FOREIGN KEY (payment_method_id) REFERENCES PaymentMethods (id),
    FOREIGN KEY (delivery_method_id) REFERENCES DeliveryMethods (id)
);

-- Fill in the table "Orders"
INSERT INTO shop.Orders
    (customer_id, product_id, payment_method_id, delivery_method_id, quantity, price, currency, payment_status, delivery_address, delivery_status, order_date)
VALUES
    (1, 1, 1, 2, 1, 538.4, 'USD', 'pending', 'Post office 120', 'in_progress', CURDATE());



-- 1. login
SELECT * FROM Customers WHERE name='Maria' AND password='Dj87#fD6sHHs0sywI';

-- 2. list_products
SELECT * FROM Products;

-- 3. list_products_in:category
SELECT * FROM Products p
INNER JOIN Categories c ON c.id=p.category_id AND c.title='Gold rings';

-- 4. list_categories
SELECT * FROM Categories;

-- 5. list_products_with_discounts
SELECT p.code, p.title, p.price, d.discount, p.price - ((p.price * d.discount) / 100) 
as final_price, p.currency
FROM Products p INNER JOIN Discounts d ON p.id=d.product_id;

-- 6. list_payment_methods
SELECT p_type FROM PaymentMethods;

-- 7. list_delivery_types
SELECT d_type FROM DeliveryMethods;

-- 8. buy:product:payment_method:delivery_method:quantity
INSERT INTO shop.Orders
    (customer_id, product_id, payment_method_id, delivery_method_id, quantity, price, currency, payment_status, delivery_address, delivery_status, order_date)
VALUES
    (1, 1, 1, 2, 1, 538.4, 'USD', 'pending', 'Post office 120', 'in progress', CURDATE());

-- 9. cart
SELECT c.name, c.surname, o.order_date, p.title, p.price, p.currency, dm.d_type, o.delivery_address, o.delivery_status, pm.p_type, o.payment_status  FROM Orders o
INNER JOIN Products p ON p.id=o.product_id
INNER JOIN Customers c ON o.customer_id=c.id
INNER JOIN DeliveryMethods dm  ON o.delivery_method_id=dm.id
INNER JOIN PaymentMethods pm ON o.payment_method_id=pm.id
WHERE customer_id=1;


