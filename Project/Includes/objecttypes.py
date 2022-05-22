# Dimensions in centimetres
# d(doesn't matter) types can be placed anywhere
# f(fragile) types require their own padded box
# t(top layers) types require placement on the topmost layers
# h(heavy) types require placement on the bottommost layers
# o(orientated) types cannot be rotated

class Apples:
    def __init__(self):
        self.name = "apple"
        self.height = 5
        self.width = 5
        self.length = 5
        self.volume = self.height * self.width * self.length
        self.type = "d"


class Bottles:
    def __init__(self):
        self.name = "bottle"
        self.height = 5
        self.width = 5
        self.length = 20
        self.volume = self.height * self.width * self.length
        self.type = "f"


class Eggs:
    def __init__(self):
        self.name = "egg"
        self.height = 30
        self.width = 5
        self.length = 5
        self.volume = self.height * self.width * self.length
        self.type = "t"


class WaterBottlePack:
    def __init__(self):
        self.name = "waterbottlepack"
        self.height = 30
        self.width = 25
        self.length = 20
        self.volume = self.height * self.width * self.length
        self.type = "h"


class JSOW:  # For testing
    def __init__(self):
        self.name = "agm154"
        self.height = 410
        self.width = 330
        self.length = 150
        self.volume = self.height * self.width * self.length
        self.type = "h"


class BoxFiller:  # For testing
    def __init__(self):
        self.name = "bigboi"
        self.height = 97
        self.width = 99
        self.length = 40
        self.volume = self.height * self.width * self.length
        self.type = "h"


class MilkCarton:
    def __init__(self):
        self.name = "milkcarton"
        self.height = 20
        self.width = 10
        self.length = 10
        self.volume = self.height * self.width * self.length
        self.type = "o"


class Plank:
    def __init__(self):
        self.name = "plank"
        self.height = 50
        self.width = 20
        self.length = 10
        self.volume = self.height * self.width * self.length
        self.type = "d"


# Dictionary to store all possible item names
allItems = {'apples': Apples, 'bottles': Bottles, 'eggs': Eggs, 'waterbottlepack': WaterBottlePack, 'agm154': JSOW,
            'bigboi': BoxFiller, 'milkcarton': MilkCarton, 'plank': Plank}