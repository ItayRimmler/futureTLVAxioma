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
    !!!! MISTAKE IN 1.b.1. {REDUNDANCY}!!!!\n
    !!!! MISTAKE IN 1.b.2. {REDUNDANCY}!!!!\n
    !!!! GENERAL MISTAKE: Could've set state to false in the Taxi's method. Redundantly did it in the control function. !!!!\n
    !!!! MISTAKE IN 2.c. {FUNCTIONALITY, BUT NOT THAT CRITICAL}!!!!\n
    Controls the taxi fleet >:):\n

    1. Going over each taxi and:

        a. Resetting remaining.\n

        b. Completing their previous track:
            1. If we haven't passed the start point, we set ex and wai to be the starting point.
                The taxi.start_x is redundant because we drive to it first, and the taxi's calc method can handle an x that's None.
                You COULD argue though, and say that it covers the case where there is an x to  travel and no y to travel,
                and just to be on the safe side, we handle the y being None in that case.
                It is executed perfectly in 2.c., with one exception that's mentioned there.\n

            2. We check whether the point is a start or end point. This addition is redundant and could've been merged with 1.b.1.
             You could argue though, that if it weren't for the mistake in 1.b.1. we could've avoided that mistake as well,
             and also that it was crucial to explicitly decide if we're sending start=True or end=True, just to be tidy.\n

            3. After we had travelled, or maybe not, we check whether we reached the endpoint, and if so, we set the taxi to not driving.\n

            4. We repeat 1.b.1. to 1.b.3. in case we made it to the starting point, but we still have remaining fuel for the endpoint as well (or part of the endpoint).
             This will happen only if we haven't changed the state, which is happening only when we reach an endpoint. This could be implemented in the method of Taxi.\n


    2. While the customer queue is not empty:

        a. We check if the previous rides have consumed all the fuel for this iteration of control. If so, we break.\n

        b. We check who is the closest vacant taxi. If all are taken then we break.\n

        c. Had we not broken, we update the queue and attempt to ride to the starting point, then the ending point.
         The mistake here is added as a comment in the end of the control function.\n

    """
    # 1.
    for taxi in taxis: # Continuing the existing rides
        # a.
        taxi.remaining = constant.RIDE_TIME * constant.VELOCITY
        # b.
        if taxi.state:
            # 1.b.1
            if not taxi.start_x is None or not taxi.start_y is None:
                ex = taxi.start_x
                wai = taxi.start_y
            else:
                ex = taxi.end_x
                wai = taxi.end_y
            # 1.b.2.
            s_or_e = taxi.start_x is None and taxi.start_y is None
            if s_or_e:
                taxi.calc_location(ex, wai, end=True)
            else:
                taxi.calc_location(ex, wai, start=True)
            # 1.b.3.
            if taxi.end_y is None:
                taxi.state = False
            # 4.
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
    # 2.
    while not kyu.i(): # Begins new ride(s)
        # a.
        total_remain = 0
        for taxi in taxis:
            total_remain += taxi.remaining
        if total_remain == 0:
            break
        # b.
        customer = kyu.p()
        distances = [3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE, 3*constant.GRID_SIZE]
        for taxi in taxis:
            if not taxi.state:
                distances[taxi.id - 1] = calc_distance(taxi, customer)
        if sum(distances) == 30 * constant.GRID_SIZE:
            break
        # c.
        kyu.d()
        closest_id = argmin(distances)
        closest = taxis[closest_id]
        closest.start_x, closest.start_y, closest.end_x, closest.end_y = customer[0], customer[1], customer[2], customer[3]
        closest.calc_location(closest.start_x, closest.start_y, start=True)
        closest.calc_location(closest.end_x, closest.end_y, end=True)
        if closest.end_y is None:
            closest.state = False

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