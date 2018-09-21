""""
This module contains Calculator class
"""

class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return  self.current

    def group_data(self,rawArray):
        marker1X = rawArray[:,0]
        marker1Y = rawArray[:,1]
        marker1Z = rawArray[:,2]
        self.GroupedData = {'marker1X':marker1X,
                    'marker1Y':marker1Y,
                    'marker1Z':marker1Z}
        return self.GroupedData



