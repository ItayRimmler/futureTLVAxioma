"""

Script name: "src\control.py"\n
Goal of the script: Contains the control function definition.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

# Imports
from math import sqrt
import constants as constant


def control(taxis, kyu):
    """
    Controls the taxi fleet >:).\n
    """
    customer = kyu.d()
    for taxi in taxis:
        taxi.calc_location(taxi.start_x, taxi.start_y, start=True, remainder=True)
        if taxi.remaining > 0:
            taxi.calc_location(taxi.end_x, taxi.end_y, end=True, remainder=True)
    distances = [3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE]
    while taxis[argmin(distances)].remaining > 0 or min(distances) == 3*constant.GRID_SIZE:
        for taxi in taxis:
            if taxi.state:
                continue
            if customer is None:
                break
            distances[taxi.id-1] = calc_distance(taxi, customer)
        if customer is None:
            break
        if not len(distances) == 0:
            taxis[argmin(distances)].start_x, taxis[argmin(distances)].start_y, taxis[argmin(distances)].end_x, taxis[argmin(distances)].end_y = customer[0], customer[1], customer[2], customer[3]
            if taxis[argmin(distances)].remaining > 0:
                taxis[argmin(distances)].calc_location(taxis[argmin(distances)].start_x, taxis[argmin(distances)].start_y, start=True, remainder=True)
                if taxis[argmin(distances)].remaining > 0:
                    taxis[argmin(distances)].calc_location(taxis[argmin(distances)].end_x, taxis[argmin(distances)].end_y, end=True, remainder=True)


# Helper functions

def calc_distance(taxi, customer):
    """
    Calculates the distance from the taxi's location
    """
    return sqrt((taxi.x - customer[0])**2 + (taxi.x - customer[1])**2)

def argmin(a):
    """
    Taken from Stackoverflow.\n
    """
    return min(range(len(a)), key=lambda x : a[x])