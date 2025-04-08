import math

class Line:
    def __init__(self, beginning: tuple, end: tuple):
        self.x1, self.y1 = beginning
        self.x2, self.y2 = end
    
    def length(self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
