CREATE TABLE book( book_id SERIAL, name VARCHAR(60) NOT NULL DEFAULT '', genre VARCHAR(60) NOT NULL DEFAULT '', quantity_in_stock INT NOT NULL DEFAULT 0, PRIMARY KEY (book_id) ) WITH( OIDS=FALSE);
CREATE TABLE book_autor( book_id SERIAL, autor_id INT NOT NULL, PRIMARY KEY (autor_id), FOREIGN KEY (book_id) REFERENCES book(book_id) ) WITH( OIDS=FALSE);
CREATE TABLE CLIENT( client_id SERIAL, login VARCHAR(60) NOT NULL DEFAULT '', name VARCHAR(60) NOT NULL DEFAULT '', password VARCHAR(60) NOT NULL, PRIMARY KEY (client_id) ) WITH( OIDS=FALSE);
CREATE TABLE AUTOR( autor_id SERIAL, first_name VARCHAR(60) NOT NULL DEFAULT '', middle_name VARCHAR(60) NOT NULL DEFAULT '', full_name VARCHAR(60) NOT NULL DEFAULT '', short_name VARCHAR(60) NOT NULL DEFAULT '', FOREIGN KEY (autor_id) REFERENCES book_autor(autor_id) ) WITH( OIDS=FALSE);
CREATE TABLE rating( book_id SERIAL, rating NUMERIC NOT NULL DEFAULT 0.00, count_voted INT NOT NULL DEFAULT 0, FOREIGN KEY (book_id) REFERENCES book(book_id) ) WITH( OIDS=FALSE);
CREATE TABLE time_of_orders( order_id SERIAL, client_id SERIAL, open_date timestamp NOT NULL, close_date timestamp, FOREIGN KEY (client_id) REFERENCES client(client_id), PRIMARY KEY (order_id) ) WITH( OIDS=FALSE);
CREATE TABLE ORDER_ITEMS( order_id SERIAL, book_id SERIAL, FOREIGN KEY (order_id) REFERENCES time_of_orders(order_id), FOREIGN KEY (book_id) REFERENCES book(book_id) ) WITH( OIDS=FALSE);
