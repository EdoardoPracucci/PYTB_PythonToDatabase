import sqlite3


path_db = "/home/edo/Documents/Repository/PYTDB_PythonToDatabase/src/Database/mysqlite"
conn = sqlite3.connect("mysqlite")
cur = conn.cursor()


def create_table_product():

    sql = """ CREATE TABLE IF NOT EXISTS product (
             id integer PRIMARY KEY NOT NULL,
             name text NOT NULL,
             price double NOT NULL
            ); """
    cur.execute(sql)
    conn.close()


def insert_product(product):
    sql = """INSERT INTO product(id, name, price) VALUES(1,'sedia',15.20)"""
    cur.execute(sql)
    conn.commit()
    conn.close()


def select_all_product():
    pass