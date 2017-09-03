import random

class Die:
  def __init__(self):
    self.__value = 1

  @property
  def value(self):        # read only
    return self.__value

  def roll(self):
    self.__value = random.randrange(1,7)

class Dice:
  def __init__(self):
    self.__list = []

  @property
  def list(self):           # read only
    dice_tuple = tuple(self.__list)
    return dice_tuple

  def addDie(self, die):
    self.__list.append(die)
