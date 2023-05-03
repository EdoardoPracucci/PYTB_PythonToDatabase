from src.Database import sqlite_product_db
from src.Model import product


def main():
    print("Welcome to Product to Database in Python, this is a toy program to practise in the python db connection")
    my_product = product.Product(3, "tavolo", 40.20)
    #
    # SQLITE db
    # create product table
    # sqlite_product_db.create_table_product()
    #
    # insert product table
    # sqlite_product_db.insert_product(my_product)
    #
    # select all product
    sqlite_product_db.select_all_product()
    #
    # MYSQL db
    #
#


if __name__ == '__main__':
    main()
