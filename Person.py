#Person


class Person(object):
    def __init__(self, start, dest):
        self.start = start
        self.dest = dest
        self.isInside = False

        if self.start > self.start:
            self.direction = "Down"
        else:
            self.direction = "Up"
