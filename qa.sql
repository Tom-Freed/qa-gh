CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(255) NOT NULL, 
    last_name varchar(255) NOT NULL, 
    email varchar(255), 
    post_address varchar(255),
    PRIMARY KEY (customer_id)
    );

CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT, 
    title VARCHAR(255) NOT NULL, 
    price FLOAT NOT NULL, 
    quantity INT NOT NULL, 
    PRIMARY KEY (product_id)
    );

CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    order_status VARCHAR(255) NOT NULL, 
    order_date DATE NOT NULL, 
    order_total FLOAT NOT NULL, 
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    );

INSERT INTO customers (first_name, last_name, email, post_address) VALUES ('bob', 'bobinson', 'bob@bobmail.com', 'bobville')
