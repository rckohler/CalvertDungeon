import random


class Map:

    def __init__(self, row_count, col_count):
        self.rowCount = row_count
        self.colCount = col_count
        self.grid = self.create_empty_map()

    def create_empty_map(self, empty='-'):
        grid = []
        for row in range(self.rowCount):
            row = []
            for col in range(self.colCount):
                row += empty
            grid.append(row)
        return grid

    def say_grid(self):
        for row in self.grid:
            m = ''
            for col in row:
                m += col
            print(m)


class Room:
    def __init__(self, location, grid, width=None, height=None, doors=[None, None, None, None], isHall=False,
                 placeDoors=True):

        if width is None:
            self.width = random.randint(6, 8)
            self.height = random.randint(6, 8)
        else:
            self.height = height
            self.width = width
        self.doors = doors
        self.add_walls(grid, location)
        self.choose_door_locations(location, placeDoors)
        self.add_doors(grid)
        if not isHall:
            self.create_halls(grid, self.doors)

    def choose_door_locations(self, location, placeDoors):
        # top, bottom, left, right

        top = self.doors[0]
        bottom = self.doors[1]
        left = self.doors[2]
        right = self.doors[3]
        if placeDoors:
            if top is None:
                top = (location[0], location[1] + int(self.width / 2))  # modify to move door from center of wall.
            if bottom is None:
                bottom = (location[0] + self.height - 1,
                          location[1] + int(self.width / 2))  # modify to move door from center of wall.
            if left is None:
                left = (location[0] + int(self.height / 2), location[1])  # modify to move door from center of wall.
            if right is None:
                right = (location[0] + int(self.height / 2),
                         location[1] + self.width - 1)  # modify to move door from center of wall.
        self.doors = [top, bottom, left, right]

    def add_walls(self, grid, location):
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or col == 0 or row == self.height - 1 or col == self.width - 1:
                    grid[row + location[0]][col + location[1]] = 'X'
                else:
                    grid[row + location[0]][col + location[1]] = ' '

    def add_doors(self, grid):
        for door in self.doors:
            if door is not None:
                grid[door[0]][door[1]] = '!'

    def create_halls(self, grid, doors):
        try:
            top = doors[0]
            bottom = doors[1]
            left = doors[2]
            right = doors[3]

            # bottom
            height = random.randint(5, 10)
            startRow = top[0] + self.height - 1
            startCol = top[1] - 1
            location = (startRow, startCol)
            width = 3
            exitDoor = (startRow + height - 1, top[1])
            doors = (exitDoor, bottom, None, None)
            Room(location, grid, width, height, doors, True, False)

            # top
            height = random.randint(3, 5)
            startRow = top[0] - height + 1
            startCol = top[1] - 1
            location = (startRow, startCol)
            width = 3
            exitDoor = (startRow, bottom[1])
            doors = [exitDoor, top, None, None]
            Room(location, grid, width, height, doors, True, False)

            # left
            height = 3
            startRow = left[0] - int(height / 2)
            width = random.randint(3, 5)
            startCol = left[1] - width + 1
            location = (startRow, startCol)
            exitDoor = (startRow + 1, left[1] - width + 1)
            doors = [None, None, exitDoor, left]
            if startCol > 0 and startRow > 0 and startCol < 50 and startRow < 50:
                Room(location, grid, width, height, doors, True, False)

            # right
            height = 3
            startRow = right[0] - int(height / 2)
            width = random.randint(3, 5)
            startCol = right[1]
            location = (startRow, startCol)
            exitDoor = (startRow + 1, right[1] + width - 1)
            doors = [None, None, right, exitDoor]
            if startCol > 0 and startRow > 0 and startCol < 50 and startRow < 50:
                Room(location, grid, width, height, doors, True, False)

            return True
        except:
            return False


m = Map(50, 50)
r = Room((20, 20), m.grid)

m.say_grid()
