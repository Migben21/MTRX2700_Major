# Dimensions in centimetres
# dm types can be placed anywhere
# f types require their own padded box
# t types require to be placed on the topmost layers

class Apples:
    length = 5
    width = 5
    depth = 5
    type = "dm"

    def getvolume(self):
        volume = self.length * self.width * self.depth
        return volume


class Bottles:
    length = 5
    width = 5
    height = 15
    type = "f"

    def getvolume(self):
        volume = self.length * self.width * self.depth
        return volume


class Eggs:
    length = 10
    width = 5
    height = 5
    type = "t"

    def getvolume(self):
        volume = self.length * self.width * self.depth
        return volume

