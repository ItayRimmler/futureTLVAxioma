"""

Script name: "classes\Taxi.py"\n
Goal of the script: Contains the Taxi class definition.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

# Imports
import src.constants as constant
import random

class Taxi:
    """
    Each Taxi object is an independent tracker of a taxi's location and state.\n
    """
    def __init__(self, id):
        """
        Constructor.\n
        """
        self.id = id
        self.x = random.randint(0, constant.GRID_SIZE)
        self.y = random.randint(0, constant.GRID_SIZE)
        self.state = False
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.remaining = constant.RIDE_TIME * constant.VELOCITY

    def calc_location(self, x, y, start=False, end=False):
        """
        Calculates the location the taxi would be in, assuming it goes towards x and y, and the previously documented location is self.x and self.y:\n
        :param x: The destination X coordinate.\n
        :param y: The destination Y coordinate.\n
        :param start: a boolean that determines if the destination the taxi rides towards is a start point.\n
        :param end: a boolean that determines if the destination the taxi rides towards is an end point.\n
        :param remainder: If it's true, then dist will be self.remaining. Else it will be calculated by the t*v formula.\n
        """
        if y is None:
            return
        if x is None:
            x = self.x
        left_x = abs(self.x - x)
        left_y = abs(self.y - y)
        self.state = True
        if self.remaining >= left_x + left_y:
            self.remaining -= left_x + left_y
            self.x, self.y = x, y
            if start:
                self.start_x, self.start_y = None, None
            elif end:
                self.end_x, self.end_y = None, None
            return
        elif self.remaining > left_x > 0:
            self.remaining -= left_x
            self.x = x
            if start:
                self.start_x = None
            elif end:
                self.end_x = None
        elif left_x > 0:
            self.x += self.remaining * int(self.x < x) - self.remaining * int(self.x > x)
            self.remaining = 0
        if self.remaining > left_y > 0:
            self.remaining -= left_y
            self.y = y
            if start:
                self.start_y = None
            elif end:
                self.end_y = None
        elif left_y > 0:
            self.y += self.remaining * int(self.y < y) - self.remaining * int(self.y > y)
            self.remaining = 0
