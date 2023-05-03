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
    product_to_insert= (product.my_id, product.name, product.price)
    sql = """INSERT INTO product(id, name, price) VALUES(?,?,?)"""

    cur.execute(sql, product_to_insert)
    conn.commit()
    conn.close()


def select_all_product():
    data=cur.execute('''SELECT * from product''')
    print(data.fetchall())
    conn.close()