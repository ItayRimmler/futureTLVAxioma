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
        Constructor:\n
        Id.\n
        x - current location.\n
        y - current location.\n
        state - true is driving, false is standing.\n
        start_x - start location for the allocated customer.\n
        start_y - start location for the allocated customer.\n
        end_x - end location for the allocated customer.\n
        end_y - end location for the allocated customer.\n
        remaining - how many meters can the taxi drive.\n
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
        !!!! MISTAKE IN 6 {REDUNDANCY}!!!!\n
        !!!! GENERAL MISTAKE: Could've set state to false in the Taxi's method. Redundantly did it in the control function. !!!!\n
        Calculates the location the taxi would be in, assuming it goes towards x and y, and the previously documented location is self.x and self.y:\n

        Priority is to go in the x axis first.\n

        1. Checking which axes are relevant, according to our priority.\n

        2. Driving = True, left_x* and left_y* are calculated.\n
        *the distances between the starting point and the destination.\n

        3. If we can cover both left_'s:
            a. We update remaining and location accordingly.\n
            b. We eliminate the start_'s and end_'s of the taxi.\n

        4. If we can cover only left_x AND it's greater than 0 (because 0 means this axis is irrelevant):
            a. We update remaining and location accordingly.\n
            b. We eliminate the start_x and end_x of the taxi.\n

        5. If we can't cover left_x AND it ain't 0 (because 0 means this axis is irrelevant), we update the location and remaining accordingly.\n

        6. Repeating 4 and 5 only for the y axis. Checking if left_y isn't 0 isn't necessary.\n

        :param x: The destination X coordinate.\n
        :param y: The destination Y coordinate.\n
        :param start: a boolean that determines if the destination the taxi rides towards is a start point.\n
        :param end: a boolean that determines if the destination the taxi rides towards is an end point.\n
        """
        # 1.
        if y is None:
            return
        if x is None:
            x = self.x
        # 2.
        left_x = abs(self.x - x)
        left_y = abs(self.y - y)
        self.state = True
        # 3.
        if self.remaining >= left_x + left_y:
            # a.
            self.remaining -= left_x + left_y
            self.x, self.y = x, y
            # b.
            if start:
                self.start_x, self.start_y = None, None
            elif end:
                self.end_x, self.end_y = None, None
            return

        # 4.
        elif self.remaining > left_x > 0:
            # a.
            self.remaining -= left_x
            self.x = x
            # b.
            if start:
                self.start_x = None
            elif end:
                self.end_x = None
        # 5.
        elif left_x > 0:
            self.x += self.remaining * int(self.x < x) - self.remaining * int(self.x > x)
            self.remaining = 0
        # 6.
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
