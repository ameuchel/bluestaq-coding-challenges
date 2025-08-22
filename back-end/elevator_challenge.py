import random
import time

### PARAMETERS FOR THE SIMULATION
NUM_FLOORS     = 4    # How many floors are in the elevator
STARTING_FLOOR = 1    # Which floor does the elevator start on in the simulation
ITER_PAUSE     = 0.01 # How long to pause between each iteration
ARRIVAL_RATE   = 0.1  # The chance that a person will press a button on a floor for each iteration
MAX_ITERS      = 100  # How many iterations to run the simulation

## PEFORM VALIDATION FOR SIMULATION PARAMS
if not (isinstance(NUM_FLOORS, int)) or (NUM_FLOORS < 2):
    raise Exception("'NUM_FLOORS' must be an integer greater than or equal to 2.")
elif not (isinstance(STARTING_FLOOR, int)) or (STARTING_FLOOR < 1) or (STARTING_FLOOR > NUM_FLOORS):
    raise Exception("'STARTING_FLOOR' must be an integer greater than 0 and less than or equal to 'NUM_FLOORS'.")
elif not ((isinstance(ITER_PAUSE, float)) or (isinstance(ITER_PAUSE, int))) or (ITER_PAUSE <= 0):
    raise Exception("'ITER_PAUSE' must be float value larger than 0.")
elif not (isinstance(ARRIVAL_RATE, float)) or (ARRIVAL_RATE <= 0) or (ARRIVAL_RATE >= 1):
    raise Exception("'ARRIVAL_RATE' must be float value larger than 0 and less than 1.")
elif not (isinstance(MAX_ITERS, int)) or (MAX_ITERS <= 0):
    raise Exception("'MAX_ITERS' must be an integer greater than 0.")

class Person:
    def __init__(self, starting_floor, request_number):
        """
        Object representing a person waiting for, riding, and exiting the elevator
        """
        self.floor_num = starting_floor
        self.floor_selection = None
        self.pick_direction()
        self.status = 'waiting'
        self.request_number = request_number
    
    def pick_direction(self):
        """
        Select the 'up' or 'down' button.
        Bottom floor can only select the 'up' button.
        Top floor can only select the 'down' button.
        Other floors have 50% chance of selecting up or down.
        """
        if self.floor_num == 1:
            self.direction = 'up'
        elif floor_num == elevator.num_floors:
            self.direction = 'down'
        elif random.random() < 0.5:
            self.direction = 'down'
        else:
            self.direction = 'up'

        print(f"Person on floor {self.floor_num} pressed the '{self.direction}' button.")

class Elevator:
    def __init__(self, num_floors: int = 4, starting_floor: int = 1):
        """
        Object simulating the elevator. Tracks the order in which buttons were selected on which
        floors as well as how many people are getting on and exiting the elevator.
        """
        self.num_floors = num_floors
        self.current_floor = starting_floor
        self.mode = 'idle'
        self.doors_opened = False
        self.direction_selected = None
        self.request_number = 0
        self.working_request_number = None
        self.pickup_floor = None
        self.dropoff_direction = None
        self.people = []

    def open_doors(self):
        if self.doors_opened is False:
            print("Doors opening...")
            self.doors_opened = True

    def close_doors(self):
        if self.doors_opened is True:
            print("Doors closing...")
            self.doors_opened = False
        
    def enter_elevator(self, person: Person):
        """
        Simulate person entering the elevator. They will make a floor selection based on their
        current floor and whether they pressed up or down.
        """
        self.open_doors()

        if person.direction == 'up':
            floor_selection = random.randint(person.floor_num+1, self.num_floors)
        else:
            floor_selection = random.randint(1, person.floor_num-1)

        person.floor_selection = floor_selection
        person.status = 'riding'

        print(f"Person selected floor {floor_selection}.")
    
    def check_floor(self):
        """
        Check which people should exit and/or enter the elevator on the current elevator floor
        """
        exit_count = 0                      # Track how many people are getting off the elevator
        enter_count = 0                     # Track how many people are getting on the elevator
        working_request_exited = False      # Whether the first person in the queue exited the elevator
        keep_people = []                    # Which people to keep track off

        # Loop through all people and determine if they are at a spot to get on or get off
        for person in self.people:
            if (person.status == 'riding') and (person.floor_selection == self.current_floor):
                self.open_doors()
                exit_count += 1
                if person.request_number == self.working_request_number:
                    working_request_exited = True
            else:
                keep_people.append(person)
                if (person.status == 'waiting') and (person.floor_num == self.current_floor) and (person.direction == self.dropoff_direction):
                    self.open_doors()
                    self.enter_elevator(person)
                    enter_count += 1
                    if person.request_number == self.working_request_number:
                        self.pickup_floor = person.floor_selection

        # Only keep people that didn't exit
        self.people = keep_people

        if exit_count:
            print(f"{exit_count} person(s) exited the elevator.")
        if enter_count:
            print(f"{enter_count} person(s) entered the elevator.")
        
        # If the primary person getting served just exited, check for next person in the queue
        if working_request_exited:
            smallest_request_number = 1e9
            found_next_person = False
            for person in self.people:
                if person.request_number < smallest_request_number:
                    next_person = person
                    found_next_person = True
                    smallest_request_number = person.request_number

            if found_next_person is True:
                # Reset the primary destination of the elevator
                self.working_request_number = smallest_request_number
                self.dropoff_direction =  next_person.direction
                if next_person.status == 'riding':
                    self.pickup_floor = next_person.floor_selection
                else:
                    self.pickup_floor = next_person.floor_num

                # Have someone hop on if they are going in the direction the elevator is heading anyways
                enter_count = 0
                for person in self.people:
                    if (person.status == 'waiting') and (person.floor_num == self.current_floor) and (person.direction == self.dropoff_direction):
                        self.open_doors()
                        self.enter_elevator(person)
                        enter_count += 1
                        if person.request_number == self.working_request_number:
                            self.pickup_floor = person.floor_selection

                if enter_count:
                    print(f"{enter_count} person(s) entered the elevator.")
            else:
                print("Elevator is now idle...")
                self.mode = 'idle'

        self.close_doors()

elevator = Elevator(num_floors=NUM_FLOORS, starting_floor=STARTING_FLOOR)
iteration = 0
while iteration < MAX_ITERS:
    ####### PRINT STATUS OF ELEVATOR GOING INTO CURRENT ITERATION #######
    print()
    print("STATUS:")
    print("Elevator floor:", elevator.current_floor)
    if elevator.pickup_floor is not None:
        print(f"Elevator travelling to floor {elevator.pickup_floor}")
    floor_status = {floor_num:{'waiting':{'up':0, 'down': 0}, 'travelling_to':0} for floor_num in range(1, elevator.num_floors+1)}
    for person in elevator.people:
        if person.status == 'riding':
            floor_status[person.floor_selection]['travelling_to'] += 1
        else:
            floor_status[person.floor_num]['waiting'][person.direction] += 1

    for floor_num, people_status in floor_status.items():
        print(f"FLOOR {floor_num}:")
        print(f"\t{people_status['waiting']['up']} person(s) waiting to go up.")
        print(f"\t{people_status['waiting']['down']} person(s) waiting to go down.")
        print(f"\t{people_status['travelling_to']} person(s) riding to.")
    print()
    ######################################################################

    # Check for new arrivals at each floor and if they're going up or down
    for floor_num in range(1, elevator.num_floors+1):
        if random.random() < ARRIVAL_RATE:
            person = Person(floor_num, elevator.request_number)
            elevator.people.append(person)

            if elevator.mode == 'idle':
                elevator.pickup_floor = person.floor_num
                elevator.dropoff_direction = person.direction
                elevator.mode = 'moving'
                elevator.working_request_number = elevator.request_number

            elevator.request_number += 1
            
    # Move elevator
    if elevator.mode == 'moving':
        if elevator.current_floor < elevator.pickup_floor:
            elevator.current_floor += 1
            print(f"Elevator moved to floor {elevator.current_floor}")
        elif elevator.current_floor > elevator.pickup_floor:
            elevator.current_floor -= 1
            print(f"Elevator moved to floor {elevator.current_floor}")
        
    # Check if people need to be picked up or dropped off
    elevator.check_floor()

    iteration += 1
    time.sleep(ITER_PAUSE)

    
