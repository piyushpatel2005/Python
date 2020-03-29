class Product:
    def __init__(self, name="", price=0.0, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def getDiscountAmount(self):
        discountAmount = self.price * self.discount / 100
        return round(discountAmount, 2)

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        return round(discountPrice, 2)

class LineItem:
    def __init__(self, product=None, quantity=1):
        self.product = product
        self.quantity = quantity

    def getTotal(self):
        if self.quantity > 1:
            total = self.product.getDiscountPrice() * self.quantity * 0.95
        else:
            total = self.product.getDiscountPrice() * self.quantity
        return total

class Cart:
    def __init__(self):
        self.__lineItems = []

    def addItem(self, item):
        self.__lineItems.append(item)

    def removeItem(self, index):
        self.__lineItems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineItems:
            if item.quantity > 1:
                total = total + item.getTotal()
            else:
                total += item.getTotal()
        return total

    def getItemCount(self):
        return len(self.__lineItems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineItems) - 1:
            raise StopIteration
        self.__index += 1
        lineItem = self.__lineItems[self.__index]
        return lineItem
