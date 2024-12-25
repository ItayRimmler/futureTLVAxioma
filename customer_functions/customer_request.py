"""

Script name: "customer_functions\customer_request.py"\n
Goal of the script: Contains the customer requests simulation function.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

# Imports
import src.constants as constant
import random

def customer_request():
    """
    Generates a request for a ride:
    :return: A random coordinate on the grid (in meters)
    """
    start_x, start_y = random.randint(0, constant.GRID_SIZE), random.randint(0, constant.GRID_SIZE)
    end_x= random.randint(max(0, start_x - constant.MAX), min(constant.GRID_SIZE, start_x + constant.MAX))
    remain = abs(start_x - end_x)
    end_y = random.randint(max(0, start_y - remain), min(constant.GRID_SIZE, start_y + remain))
    return [start_x, start_y, end_x, end_y]