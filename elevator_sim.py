# Simulation Algorithm:
# Initialize Simulation
#   1. Set time to 0
#   2. Initialize List of People
#   3. Generate elevators
#   4. Generate GUI
#   1. Load initial run time

# Execute Simulation
#   1. Generate people with requests
#   2. Update elevator-queues with requests
#   3. Update elevator-positions
#   4. Update elevator-occupancy
#   5. Update time

# Function Definitions
from Simulate import *


# Simulation Settings
num_of_elevators = 5
max_people = 2
max_floor = 20


# Initialization Sequence
# 1. Initialize time to 0
t = 0

# 2. Initialize List of People
people_wait = []
people_pend = []

# 3. Generate elevators
bank = []       # initialize list of elevators
for i in range(0,num_of_elevators):                     # Append randomized
    bank.append(Elevator(randint(0, max_floor - 1)))    # elevators to 'bank'

# 4. Generate GUI
print_title()
print("t = 0 (Initial Status)")
print_bank(bank)
print_people_wait(people_wait)
print_people_pend(people_pend)

# 5. Load Initial Run Time
run = int(input("Enter run time (Terminate with '-1'): "))
gen = input("Generate person per instant? ('y'/'n'): ")

# Execution Sequence
while run != -1:                    # Execute Simulation of user inputs != '-1'
    for time in range(0, run):      # Run Simulation for 'run' time instants

        # 1 Generate people with requests
        #---------------------------------MODIFY FOR CUSTOMIZED STIMULUS---------------------------#
        if  gen == "y":
            people_wait += gen_people(1, max_floor)     # extend list of people
        # -----------------------------------------------------------------------------------------#

        # 2. Update elevator-queues with requests
        for i, person in enumerate(people_wait):        # For each person:
            closest = get_closest(person, bank)         # find closest elevator

            if closest != -1:                           # If elevator was found.
                bank[closest].add_floor(person.start)   # add person's location to its queue
                people_pend.append(person)              # add person to pending list
                people_wait.pop(i)                      # remove person from waiting list

        # 3. Update elevator-positions
        for elevator in bank:                                   # For each elevator:
            elevator.update_position()                          # update its position

            # 4. Update elevator-occupancy
            if elevator.isOpen:                                 # If the elevator opens up:
                for j, person in enumerate(people_pend):        # For each pending person:

                    if elevator.curr_floor == person.start:     # If elevator reaches person
                        person.isInside = True                  # Load person onto elevator,
                        elevator.add_floor(person.dest)         # and queue person's destination

                    elif elevator.curr_floor == person.dest:    # Else if elevator reaches 'dest'
                        people_pend.pop(j)                      # Kick person out of elevator

        # 5. Update Time
        t += 1

    # Print Status and Load new run time
    print("\n\n\nt =", t)
    print_bank(bank)
    print_people_wait(people_wait)
    print_people_pend(people_pend)
    run = int(input("Enter run time (Terminate with '-1'): "))
    gen = input("Generate person per instant? ('y'/'n'): ")