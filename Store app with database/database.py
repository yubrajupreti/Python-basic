import sqlite3

conn = sqlite3.connect('stock.db')
c = conn.cursor()


def create_user_table():
    c.execute("""CREATE TABLE IF NOT EXISTS User( name TEXT, email TEXT, address TEXT, phone TEXT, password TEXT, silver TEXT, gold TEXT, bronze TEXT, normal TEXT )""")


def create_product_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Product( name TEXT, price INTEGER, quantity INTEGER, description TEXT)""")

def create_buying_table():

    c.execute("""CREATE TABLE IF NOT EXISTS Customer_buy( email TEXT, product TEXT,  quantity INTEGER,price INTEGER,dis_amount INTEGER ,amount INTEGER)""")
#
# create_user_table()
# create_product_table()
create_buying_table()