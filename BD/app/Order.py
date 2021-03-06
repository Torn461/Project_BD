#!/usr/bin/python

import psycopg2
import psycopg2.extras
import string
import datetime
path = "/home/andrey/Project_BD-master/BD/app/"

def open_order(book_id, first_name, second_name, email, phone_number, delivery_address):
    open_date = datetime.datetime.now()
    list_args = ['book0book_id', 'client0client_id', 'time_of_orders0open_date']#, 'book0quantity_in_stock', 'autor0first_name','autor0middle_name', 'autor0short_name', 'rating0rating', 'rating0count_voted']
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    print(book_id, first_name, second_name, email, phone_number, delivery_address)
    print(type(book_id))
    #print("\n")
    book_id0 = int(book_id)
    book_id = book_id0
    print(book_id)
    #print("\n")
    c = (first_name, second_name, email, phone_number, delivery_address,)
    cur.execute("SELECT client_id FROM client WHERE first_name = %s AND second_name = %s AND email = %s AND phone_number = %s AND delivery_address = %s;", c)
    client_id = cur.fetchall()
    if client_id == []:
        try:
            cur.execute("INSERT INTO client (first_name, second_name, email, phone_number, delivery_address) VALUES (%s, %s, %s, %s, %s);", c)
            conn.commit()
        except psycopg2.Error as e:
            print(e)
            conn.rollback()
        cur.execute("SELECT client_id FROM client WHERE first_name = %s AND second_name = %s AND email = %s AND phone_number = %s AND delivery_address = %s;",c)
        client_id = cur.fetchall()
    client_id = client_id[0][0]
    #print(open_date.timestamp())
    open_date = str(open_date)
    open_date = open_date[:open_date.rfind(".")]
    print(open_date)
    command="INSERT INTO time_of_orders (client_id, open_date) VALUES (%s, TIMESTAMP %s);"
    try:
        cur.execute(command, (client_id, open_date,))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
        conn.rollback()
        return ('Error1: New order not add')

    cur.execute("SELECT order_id FROM time_of_orders WHERE client_id = %s AND open_date = %s;", (client_id, open_date,))
    order_id = cur.fetchall()[0][0]
    command = "INSERT INTO order_items (book_id, order_id) VALUES (%s, %s);"
    try:
        cur.execute(command, (book_id, order_id,))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
        conn.rollback()
        return ('Error2: New order not add')
    return ('New order add')


def View_current_orders():
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    command = "SELECT * FROM ((time_of_orders LEFT JOIN (book LEFT JOIN order_items ON book.book_id = order_items.book_id) ON order_items.order_id = time_of_orders.order_id)) WHERE time_of_orders.close_date = '2000-01-01 00:00:00' ORDER BY time_of_orders.open_date ;"
    #print(command)
    #print(tuple(args))
    try:
        cur.execute(command)
        return cur.fetchall()
    except psycopg2.Error as e:
        print(e)
        conn.rollback()
    return []


def close_order(order_id):
    close_date = datetime.datetime.now()
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    command = "UPDATE time_of_orders SET close_date = %s WHERE order_id = %s;"
    try:
        cur.execute(command, (close_date, order_id))
        return "Order " + order_id + " update"
    except psycopg2.Error as e:
        print(e)
        conn.rollback()
        return "Error: Order " + order_id + " not update"


#open_order('13', 'ebrb', 'AWBA', 'btetbeb', '816618716', 'ebrberberbe')