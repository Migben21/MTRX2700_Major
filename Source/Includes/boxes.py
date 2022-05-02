# Box dimensions in centimetres

class LargeBox:
    def __init__(self):
        self.length = 100
        self.width = 100
        self.depth = 40
        self.volume = self.length * self.width * self.depth


class MediumBox:
    def __init__(self):
        self.length = 75
        self.width = 75
        self.depth = 40
        self.volume = self.length * self.width * self.depth


class SmallBox:
    def __init__(self):
        self.length = 40
        self.width = 40
        self.depth = 40
        self.volume = self.length * self.width * self.depth