# Dimensions in centimetres

class LargeBox:
    def __init__(self):
        self.length = 100
        self.width = 100
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 'l'


class MediumBox:
    def __init__(self):
        self.length = 75
        self.width = 75
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 'm'


class SmallBox:
    def __init__(self):
        self.length = 40
        self.width = 40
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 's'


boxSizes = {'s': SmallBox, 'm': MediumBox, 'l': LargeBox}


class SortedBox:
    def __init__(self, size, contents):
        if contents is None:
            contents = []
        self.contents = contents
        self.type = size
        match size:
            case 's':
                self.length = 40
                self.width = 40
                self.depth = 40
            case 'm':
                self.length = 75
                self.width = 75
                self.depth = 40
            case 'l':
                self.length = 100
                self.width = 100
                self.depth = 40
        self.volume = self.length * self.width * self.depth
