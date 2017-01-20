class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def enter(self):
        print "You are in {}".format(self.name)
        print "Description: {}".format(self.description)
        print "Directions include: "
        print [key for key in self.paths.keys()]

        print "Which direction will you go next?"
        next_direction = raw_input(">")
        if next_direction in self.paths.keys():
            return self.go(next_direction)
