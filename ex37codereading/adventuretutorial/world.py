__author__ = 'Phillip Johnson'

_world = {}
starting_position = (0, 0)

def tile_exists(x, y): #used by roominstance.adjacenttiles to return move options
        """Returns the tile at the given coordinates or None if there is no tile.

        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y)) #get returns a value for a given key in the _world dictionary


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines() # reads every line to a list. list rows
    x_max = len(rows[0].split('\t')) # splits values at the tab on top row and returns the # of values as x max
    #actual file has 4 tabs, so 5 different x values including the start position
    for y in range(len(rows)): #returns number of rows as 'y'. There are 8 rows
    # not including a blank end one. testing reveals readlines() doesn't care about 
    # a blank, final, endline (but does count any other blank line)
        cols = rows[y].split('\t') #starting at row zero, it splits each row by tabs and stores value in cols list
        for x in range(x_max): #goes through each column number. Unsure why range was used and not cols.
        # possibly this was decided to restrict to the tabs in the first line only
            tile_name = cols[x].replace('\n', '') #replaces any newlines in the column with nothing
            # and populated the tile name variable with the result. This is because the last column
            # in every row contains a \n character. Essentially does two things in one line.
            if tile_name == 'StartingRoom': #a place on the map needs to be named StartingRoom
                global starting_position #declare this a global name
                starting_position = (x, y) # populates the starting position as a tuple
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            # Creates a dictionary key of (x, y), with value None if the tile_name is blank,
            # otherwise, imports the tile_name object(method) from the 'tiles' module. This populates
            # the room name from tiles.py module into the _world dictionary. The arguments (x, y) are
            # passed to this method in the _world dictionary
            # Ultimately, _world has been populated with methods from 'tiles' that have x, y position
            # arguments for each tile. Each (x, y) position is also a dictionary key for each item


