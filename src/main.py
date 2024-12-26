"""

Script name: "src\main.py"\n
Goal of the script: Contains the main function that runs the whole program.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

# Libraries
import time
from classes.Taxi import Taxi
from classes.Queue import Queue
from log import *
from control import control
from customer_functions.customer_request import customer_request
taxis = []
for i in range(10):
    globals()[f'taxi{i+1}'] = Taxi(i+1)
    taxis.append(globals()[f'taxi{i+1}'])
first_log(taxis)
i = 1
kyu = Queue()
while True:
    kyu.e(customer_request())
    control(taxis, kyu)
    log(taxis, i, kyu)
    time.sleep(20)
    i += 1