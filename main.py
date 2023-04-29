from src.Database import sqlite_product_db
from src.Model import  product
def main():
    print("Welcome to Product to Database in Python, this is a toy program to practise in the python db connection")
    my_product = product.Product(1, "sedia", 15.20)
    sqlite_product_db.insert_product(my_product)

if __name__ == '__main__':
    main()
