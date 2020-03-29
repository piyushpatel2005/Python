# import csv
from business import Product

# FILENAME = "products.csv"

# def get_products():
#     products = []
#     with open(FILENAME, newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             product = Product(row[0], float(row[1]), int(row[2]))
#             products.append(product)
#     return products
    


def get_products():
    products = [
        Product("The Holy Grail (DVD)", 4.75, 30),
        Product("Life of Brian (DVD)", 8.97, 20),
        Product("The Meaning of Life (DVD)", 6.50, 15),
        Product("Sofa", 99.99, 20),
        Product("28\" LCD TV", 129.99, 13),
        Product("XBox Games", 299.99, 18)
    ]
    return products