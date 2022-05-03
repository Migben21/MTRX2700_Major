# Dimensions in centimetres
# d(doesn't matter) types can be placed anywhere
# f(fragile) types require their own padded box
# t(top layers) types require placement on the topmost layers
# h(heavy) types require placement on the bottommost layers

class Apples:
    def __init__(self):
        self.name = "apple"
        self.length = 5
        self.width = 5
        self.depth = 5
        self.volume = self.length * self.width * self.depth
        self.type = "d"


class Bottles:
    def __init__(self):
        self.name = "bottle"
        self.length = 5
        self.width = 5
        self.depth = 20
        self.volume = self.length * self.width * self.depth
        self.type = "f"


class Eggs:
    def __init__(self):
        self.name = "egg"
        self.length = 30
        self.width = 5
        self.depth = 5
        self.volume = self.length * self.width * self.depth
        self.type = "t"


class WaterBottlePack:
    def __init__(self):
        self.name = "waterbottlepack"
        self.length = 30
        self.width = 25
        self.depth = 20
        self.volume = self.length * self.width * self.depth
        self.type = "h"


class JSOW:  # For testing
    def __init__(self):
        self.name = "agm154"
        self.length = 410
        self.width = 330
        self.depth = 150
        self.volume = self.length * self.width * self.depth
        self.type = "h"


class BoxFiller:  # For testing
    def __init__(self):
        self.name = "bigboi"
        self.length = 99
        self.width = 99
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.type = "h"


# Dictionary to store all possible item names
allItems = {'apples': Apples, 'bottles': Bottles, 'eggs': Eggs, 'waterbottlepack': WaterBottlePack, 'agm154': JSOW,
            'bigboi': BoxFiller}
