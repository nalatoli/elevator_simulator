# Modules:
from random import *
from Elevator import Elevator
from Person import Person


# Print Script Title
def print_title():
    print("---------------------------")
    print("--ELEVATOR BANK SIMULATOR--")
    print("---------------------------\n")


# Print Bank Status
def print_bank(bank):
    print("--------------------------------------------------------")
    print ("ELEVATOR BANK STATUS")
    print("%-10s%-10s%-10s%-10s%-10s%-10s" %
          ("Number", "Curr.", "Dest.", "Motion", "Open?", "Queue"))
    for i, elevator in enumerate(bank):
        print("%-10s%-10s%-10s%-10s%-10s%-10s" %
              (str(i + 1),
              str(elevator.curr_floor),
              str(elevator.dest_floor),
              str(elevator.motion),
              str(elevator.isOpen),
              str(elevator.queue)))
    print("--------------------------------------------------------")


# Print People Status
def print_people_wait(people):
    print("--------------------------------------------------------")
    print("WAITING PEOPLE STATUS")
    print("%-10s%-10s%-10s" %
          ("Number", "Start.", "Dest."))
    for i, person in enumerate(people):
        print("%-10s%-10s%-10s" %
              (str(i + 1),
              str(person.start),
              str(person.dest)))
    print("--------------------------------------------------------")


def print_people_pend(people):
    print("--------------------------------------------------------")
    print("PENDING PEOPLE STATUS")
    print("%-10s%-10s%-10s%-10s" %
          ("Number", "Start.", "Dest.","Inside?"))
    for i, person in enumerate(people):
        print("%-10s%-10s%-10s%-10s" %
              (str(i + 1),
               str(person.start),
               str(person.dest),
               str(person.isInside)))
    print("--------------------------------------------------------")


# Generate List of Random People
def gen_people(num_of_people, max_floor):
    people = []                             # create empty list

    for i in range(0, num_of_people):       # iterate 'num_of_people' times
        while True:                         # do the following:
            start = randint(1, max_floor)   # get rand starting floor
            end = randint(1, max_floor)     # get rand destination floor
            if start != end:                # If the floors are not the same
                break                       # break out of infinite loop and
        people.append(Person(start, end))   # append person to list

    return people                           # return generated list


# Find closest Elevator
def get_closest(person, bank):
    curr_diff = 999                         # initialize distance between elevator and person
    closest = -1                            # set default elevator number to '-1'

    for num, elevator in enumerate(bank):   # for each elevator:
        if elevator.motion == "Stopped":    # If the elevator is stopped:

            pend_diff = abs(elevator.curr_floor - person.start)  # compute distance
            if pend_diff < curr_diff:       # If distance < previous distance
                curr_diff = pend_diff       # save value
                closest = num               # save elevator number

    if curr_diff != 999:                    # If initial value has changed:
        return closest                      # return elevator number

    for num, elevator in enumerate(bank):           # for each elevator(again):
        if elevator.motion == person.direction:     # If the elevator is traveling in person's direction:

            if ((elevator.motion == "Up" and person.start >= elevator.curr_floor) or    # And if the elevator does
            (elevator.motion == "Down" and person.start <= elevator.curr_floor)):       # not have to turn around

                pend_diff = abs(elevator.curr_floor - person.start)     # compute distance
                if pend_diff < curr_diff:                               # If distance < previous distance
                    curr_diff = pend_diff                               # save value
                    closest = num                                       # save elevator number

    return closest                          # return elevator number, even if invalid
