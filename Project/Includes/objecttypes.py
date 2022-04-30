# Dimensions in centimetres
# dm(doesn't matter) types can be placed anywhere
# f(fragile) types require their own padded box
# t(top layers) types require to be placed on the topmost layers
# h(heavy) types require to be placed on the bottommost layers

class Apples:
    def __init__(self):
        self.name = "apple"
        self.length = 5
        self.width = 5
        self.depth = 5
        self.volume = self.length * self.width * self.depth
        self.type = "dm"


class Bottles:
    def __init__(self):
        self.name = "bottle"
        self.length = 5
        self.width = 5
        self.depth = 15
        self.volume = self.length * self.width * self.depth
        self.type = "f"


class Eggs:
    def __init__(self):
        self.name = "egg"
        self.length = 10
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


# Dictionary to store all possible item names
allItems = {'apples': Apples, 'bottles': Bottles, 'eggs': Eggs, 'waterbottlepack': WaterBottlePack}
