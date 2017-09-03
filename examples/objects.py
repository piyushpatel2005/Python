class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def getDiscountAmount(self):
        return self.price * self.discount / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
