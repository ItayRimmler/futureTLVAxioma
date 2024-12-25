"""

Script name: "src\log.py"\n
Goal of the script: Contains the log and first_log function definition.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

def first_log(taxis):
    """
    Creates the first print.\n
    """
    print("Initial taxi locations:")
    for taxi in taxis:
        if taxi.state:
            print(f"Taxi-{taxi.id}: {taxi.x / 1000}Km, {taxi.y / 1000}Km (driving)")
        else:
            print(f"Taxi-{taxi.id}: {taxi.x/1000}Km, {taxi.y/1000}Km (standing)")

def log(taxis, j, kyu):
    """
    Prints into the log.\n
    """
    print(f"After {20*j} seconds:")
    print("Order Queue:")
    if kyu.i():
        print("Empty")
    else:
        for keeu in kyu.q:
            print(keeu)
    for taxi in taxis:
        if taxi.state:
            print(f"Taxi-{taxi.id}: {taxi.x / 1000}Km, {taxi.y / 1000}Km (driving)")
        else:
            print(f"Taxi-{taxi.id}: {taxi.x/1000}Km, {taxi.y/1000}Km (standing)")