import mysql.connector

cnx = mysql.connector.connect(host="localhost",
                              user="root",
                              password="ciao1234",
                              database="PYTDB")
my_cursor = cnx.cursor()


def insert_product_mysql(product):
    values = (product.my_id, product.name, product.price)
    sql = "INSERT INTO product (id,name,price) VALUES (%s , %s , %s)"

    my_cursor.execute(sql, values)
    cnx.commit()

def delete_product_mysql():
    pass


def select_product_mysql():
    print("MYSQL data:")
    sql = "select * from product"
    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    print(my_result)
    my_cursor.close()
    cnx.close()
