# Box dimensions in centimetres

class LargeBox:
    def __init__(self):
        self.length = 100
        self.width = 100
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.type = 'l'


class MediumBox:
    def __init__(self):
        self.length = 75
        self.width = 75
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.type = 'm'


class SmallBox:
    def __init__(self):
        self.length = 40
        self.width = 40
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.type = 's'


boxSizes = {'s': SmallBox, 'm': MediumBox, 'l': LargeBox}


class SortedBox:
    def __init__(self, size):
        self.contents = []
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
