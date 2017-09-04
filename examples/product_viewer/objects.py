class Product:
    def __init__(self, name="", price=0.0, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def getDiscountAmount(self):
        return self.price * self.discount / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

class Book(Product):
    def __init__(self, name="", price=0.0, discount=0, author=""):
        Product.__init__(self, name, price, discount)
        self.author = author

    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author


class Movie(Product):
    def __init__(self, name="", price=0.0, discount=0, year=0):
        Product.__init__(self, name, price, discount)
        self.year = year

    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"
