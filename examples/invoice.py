from decimal import Decimal
from decimal import ROUND_HALF_UP

choice = "y"
while choice == 'y':
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()

    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal("0.2")

    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount
    tax_percent = Decimal("0.05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    invoice_total = subtotal + sales_tax

    print("Order Total: {:10,}".format(order_total))
    print("Discount amount: {:10,}".format(discount))
    print("Subtotal: {:10,}".format(subtotal))
    print("Sales Tax: {:10,}".format(sales_tax))
    print("Invoice total: {:10,}".format(invoice_total))
    print()

    choice = input("Continue? (y/n): ")
    print()
print("Bye")
