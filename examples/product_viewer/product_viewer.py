from objects import Product, Book, Movie

def show_products(products):
    print("Products")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + ". " + product.getDescription())
    print()

def show_product(product):
    print("PRODUCT DATA")
    print("Name:", product.name)
    if isinstance(product, Book):
        print("Author:", product.author)
    if isinstance(product, Movie):
        print("Year:", product.year)
    print("Discount Price: {:.2f}".format(product.getDiscountPrice()))
    print()

def main():
    print("The Product Viewer Program")
    print()
    products = (Product("Rubber", 0.88, 3),
              Book("A book of tomorrow", 3.23, 2, "Michael Bay"),
              Movie("Independence Day", 9.99, 5, 2016))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != 'y':
            break
if __name__ == "__main__":
    main()
