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
    for taxi in taxis: # Continuing the existing rides
        taxi.remaining = constant.RIDE_TIME * constant.VELOCITY
        if taxi.state:
            if taxi.start_x or taxi.start_y:
                ex = taxi.start_x
                wai = taxi.start_y
            else:
                ex = taxi.end_x
                wai = taxi.end_y
            s_or_e = taxi.start_x is None and taxi.start_y is None
            if s_or_e:
                taxi.calc_location(ex, wai, end=True)
            else:
                taxi.calc_location(ex, wai, start=True)
            if taxi.end_y is None:
                taxi.state = False
            if taxi.state:
                if taxi.start_x or taxi.start_y:
                    ex = taxi.start_x
                    wai = taxi.start_y
                else:
                    ex = taxi.end_x
                    wai = taxi.end_y
                s_or_e = taxi.start_x is None and taxi.start_y is None
                if s_or_e:
                    taxi.calc_location(ex, wai, end=True)
                else:
                    taxi.calc_location(ex, wai, start=True)
                if taxi.end_y is None:
                    taxi.state = False
    while not kyu.i(): # Begins new ride(s)
        total_remain = 0
        for taxi in taxis:
            total_remain += taxi.remaining
        if total_remain == 0:
            break
        customer = kyu.p()
        distances = [3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE]
        for taxi in taxis:
            if not taxi.state:
                distances[taxi.id - 1] = calc_distance(taxi, customer)
        if sum(distances) == 30 * constant.GRID_SIZE:
            break
        kyu.d()
        closest_id = argmin(distances)
        closest = taxis[closest_id]
        closest.start_x, closest.start_y, closest.end_x, closest.end_y = customer[0], customer[1], customer[2], customer[3]
        closest.calc_location(closest.start_x, closest.start_y, start=True)
        closest.calc_location(closest.end_x, closest.end_y, end=True)



# Helper functions

def calc_distance(taxi, customer):
    """
    Calculates the distance from the taxi's location
    """
    return sqrt((taxi.x - customer[0])**2 + (taxi.y - customer[1])**2)

def argmin(a):
    """
    Taken from Stackoverflow.\n
    """
    return min(range(len(a)), key=lambda x : a[x])