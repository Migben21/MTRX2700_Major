# Dimensions in centimetres
# dm types can be placed anywhere
# f types require their own padded box
# t types require to be placed on the topmost layers

class Apples:
    def __init__(self):
        self.length = 5
        self.width = 5
        self.depth = 5
        self.volume = self.length * self.width * self.depth
        self.type = "dm"


class Bottles:
    def __init__(self):
        self.length = 5
        self.width = 5
        self.depth = 15
        self.volume = self.length * self.width * self.depth
        self.type = "f"


class Eggs:
    def __init__(self):
        self.length = 10
        self.width = 5
        self.depth = 5
        self.volume = self.length * self.width * self.depth
        self.type = "t"
