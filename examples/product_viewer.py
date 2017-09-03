from objects import Product

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". " + product.name)
    print()

def show_product(product):
    print("PRODUCT DATA")
    print("Name: {:s}".format(product.name))
    print("Price: {:.2f}".format(product.price))
    print("Discount percent: {:d}%".format(product.discount))
    print("Discount amount: {:.2f}".format(product.getDiscountAmount()))
    print("Discount Price: {:.2f}".format(product.getDiscountPrice()))
    print()

def main():
    print("The Product Viewer")
    print()

    products = (Product("Rubber", 0.99, 5),
                Product("Pencil", 0.85, 2),
                Product("Eraser", 0.30, 0))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("view another product? (y/n): ")
        print()
        if choice != 'y':
            print("Bye!")
            break


if __name__ == "__main__":
    main()
