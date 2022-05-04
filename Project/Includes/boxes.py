# Dimensions in centimetres

class LargeBox:
    def __init__(self, contents):
        self.length = 100
        self.width = 100
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 'l'
        if contents is None:
            contents = []
        self.contents = contents
        self.contentsVolume = 0
        for i in range(len(contents)):
            self.contentsVolume += contents[i].volume


class MediumBox:
    def __init__(self, contents):
        self.length = 75
        self.width = 75
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 'm'
        if contents is None:
            contents = []
        self.contents = contents
        self.contentsVolume = 0
        for i in range(len(contents)):
            self.contentsVolume += contents[i].volume


class SmallBox:
    def __init__(self, contents):
        self.length = 40
        self.width = 40
        self.depth = 40
        self.volume = self.length * self.width * self.depth
        self.size = 's'
        if contents is None:
            contents = []
        self.contents = contents
        self.contentsVolume = 0
        for i in range(len(contents)):
            self.contentsVolume += contents[i].volume


boxSizes = {'s': SmallBox, 'm': MediumBox, 'l': LargeBox}
