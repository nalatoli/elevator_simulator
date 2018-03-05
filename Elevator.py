#Elevator


class Elevator(object):
    #Motion Map for determing new elevator positions
    motion_map = {"Stopped": 0,
                  "Down": -1,
                  "Up": 1}

    # Constructor
    def __init__(self, start):
        self.curr_floor = start
        self.dest_floor = start
        self.motion = "Stopped"
        self.queue = []
        self.isOpen = True

    # Assign destination/motion
    def set_dest(self, floor):
        old_motion = self.motion                 # save old motion

        if self.curr_floor > self.queue[0]:      # If 'curr_floor' > top job,
            self.motion = "Down"                 # set motion to "Down"
            if self.motion != old_motion:        # If the direction has changed,
                self.queue.sort(reverse = True)  # order all jobs

        elif self.curr_floor < self.queue[0]:    # Else if 'curr_floor' < top job,
            self.motion = "Up"                   # set motion to "Up"
            if self.motion != old_motion:        # If the direction has changed,
                self.queue.sort()                # order all jobs

        self.dest_floor = self.queue[0]          # Set destination to top job

    # Queue Floor onto Elevator
    def add_floor(self, floor):

        for job in self.queue:
            if floor == job:                        # If floor is already in queue,
                break                               # terminate queuing
        else:                                       # Else,
            self.queue.append(floor)                # Add floor to end of queue and
            self.set_dest(floor)                    # reset destination floor/elevator motion

    # Move Elevator
    def update_position(self):
        if len(self.queue) > 0:                                 # Execute following if job is executing:

            self.isOpen = False                                 # CLOSE DOOR
            self.curr_floor += self.motion_map[self.motion]     # MOVE ELEVATOR

            if self.curr_floor == self.dest_floor:              # If elevator has reached its destination
                self.queue.pop(0)                               # JOB IS COMPLETE
                self.isOpen = True                              # OPEN DOOR

                if len(self.queue) != 0:                        # If there are pending jobs,
                    self.set_dest(self.queue[0])                # reset destination floor/mark elevator motion

                else:                                           # Else,
                    self.motion = "Stopped"                     # mark elevator as "Stationary"
