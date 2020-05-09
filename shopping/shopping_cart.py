import db
from business import Product, LineItem, Cart
import uuid

def show_title():
    print("The Shopping Cart Program")
    print()

def show_menu():
    print("COMMAND MENU")
    print("cart - Show the cart")
    print("products - Show available products")
    print("buy - Place an order with items in cart")
    print("add - Add an item to the cart")
    print("del - Delete an item from cart")
    print("exit - Exit Program")
    print()

def show_products(products):
    print("PRODUCTS")
    line_format1 = "{:<5s} {:<25s} {:>10s} {:>10s} {:>12s}"
    line_format2 = "{:<5d} {:<25s} {:>10.2f} {:>10s} {:>12.2f}"
    print(line_format1.format("Item", "Name", "Price", "Discount", "Your Price"))

    for i in range(len(products)):
        product = products[i]
        print(line_format2.format(i+1, product.name, product.price, str(product.discount) + "%", product.getDiscountPrice()))
        print()
    print("We have promotions going on for combo purchases. If you buy multiple of any item, you qualify for additional 5% discount.")
    print()

def show_cart(cart):
    if cart.getItemCount() == 0:
        print("There are no items in your cart.\n")
    else:
        line_format1 = "{:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
        line_format2 = "{:<5d} {:<25s} {:>12.2f} {:>10d} {:>10.2f}"
        print(line_format1.format("Item", "Name", "Your Price", "Quantity", "Total"))

        i = 0
        for item in cart:
            print(line_format2.format(i+1, item.product.name, item.product.getDiscountPrice(), item.quantity, item.getTotal()))
        i += 1
    print("{:>66.2f}".format(cart.getTotal()))
    print()

def place_order(cart):
    if cart.getItemCount() == 0:
        print("There are no items in your cart.\n")
        print("You must add items to the cart before checking out.\n")
        return
    else:
        order_id = str(uuid.uuid4())
        print("Your order has been placed with order ID: " + order_id)
        print("Here is your receipt")
        print("=====================================================================================")
        print("XYZ Inc.")
        print("000 Fake St, Alexins")
        print("ON, Canada M43 G34")
        print("                      PURCHASE ORDER                        ")
        print("                      --------------                        ")
        print()
        print("Thank you very much for shopping with us. Following items will be delivered to your registered mail address within 5 days.")
        print("Order ID: " + order_id)
        line_format1 = "{:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
        line_format2 = "{:<5d} {:<25s} {:>12.2f} {:>10d} {:>10.2f}"
        print()
        print(line_format1.format("Item", "Name", "Your Price", "Quantity", "Total"))

        i = 0
        for item in cart:
            print(line_format2.format(i+1, item.product.name, item.product.getDiscountPrice(), item.quantity, item.getTotal()))
        i += 1
    print("{:>66.2f}".format(cart.getTotal()))
    print()

def add_item(cart, products):
    number = int(input("Item number: "))
    quantity = int(input("Quantity: "))
    if number < 1 or number > len(products):
        print("No product has that number.\n")
    else:
        product = products[number - 1]
        if quantity > 1:
            print("Congratulations, you are qualified for additional 5 percent discount on this product.")
            new_product = Product(product.name, float(product.price), int(product.discount + 5))
        item = LineItem(product, quantity)
        cart.addItem(item)
        print("Item " + str(cart.getItemCount()) + " was added.\n")

def remove_item(cart):
    number = int(input("Item number: "))
    if number < 1 or number > cart.getItemCount():
        print("The cart does not contain an item with that number.\n")
    else:
        cart.removeItem(number - 1)
        print("Item " + str(number) + " was deleted.\n")

def main():
    show_title()
    show_menu()

    products = db.get_products()
    show_products(products)

    cart = Cart()
    while True:
        command = input("Command: ")
        if command == "cart":
            show_cart(cart)
        elif command == "add":
            add_item(cart, products)
        elif command == "products":
            show_products(products)
        elif command == "del":
            remove_item(cart)
        elif command == "buy":
            place_order(cart)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
