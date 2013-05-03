import random


class MazeGen(object):
    block_cell_icon = '#'
    end_cell_icon = '$'
    start_cell_icon = 'B'
    passage_cell_icon = ' '
    passage_wall_icon = '|'
    visited = []

    def __call__(
            self, x_range=30, y_range=30, x_start=0, y_start=0, routes=10):
        """
        create a maze using passed variables
        """
        #generate the blank maze
        self.maze = self.generate_blank_maze(x_range, y_range)
        #set the starting point
        self.start = (y_start, x_start)
        #create the various routes through the maze
        for route in range(routes):
            self.make_route(route)
        #print out the maze
        self.print_maze()

    def generate_blank_maze(self, x_range, y_range):
        return [
            [self.block_cell_icon for x in range(x_range)]
            for x in range(y_range)]

    def get_neighbours(self, cell):
        """
        Get the coordinates for the neighbouring cells
        """
        neighbours = []
        coords = (
            (cell[0] + 1, cell[1]),
            (cell[0], cell[1] + 1),
            (cell[0] - 1, cell[1]),
            (cell[0], cell[1] - 1),
        )

        for coord in coords:
            try:
                if coord[0] != -1 and coord[1] != -1:
                    self.maze[coord[0]][coord[1]]
                    neighbours.append(coord)
            except IndexError:
                continue

        return neighbours

    def valid_neighbours(self, x):
        """
        Check which neigbouring cells can be turned into passages
        """
        cell = self.maze[x[0]][x[1]]
        return cell == self.block_cell_icon

    def get_walls(self, x):
        """
        Check which neichbours are walls
        """
        cell = self.maze[x[0]][x[1]]
        return cell == self.passage_wall_icon

    def pick_neighbour(self, neighbours):
        """
        validates neighbours and picks one as next passage
        """
        neighbours = filter(self.valid_neighbours, neighbours)
        random_index = random.randint(0, len(neighbours) - 1)
        candidate = neighbours.pop(random_index)
        for neighbour in neighbours:
            #mark other neighbours as walls
            self.set_cell((neighbour), self.passage_wall_icon)
        return candidate

    def print_maze(self):
        for x, line in enumerate(self.maze):
            for y, cell in enumerate(line):
                # turn passage walls back into normal blocks
                if self.maze[x][y] == self.passage_wall_icon:
                    self.maze[x][y] = self.block_cell_icon
        for line in self.maze:
            print ''.join(line)

    def set_cell(self, coords, value):
        #set a cell to passed value
        self.maze[coords[0]][coords[1]] = value

    def make_route(self, route):
        if route == 0:
            #if this is the first route start at self.start
            current = self.start
            self.set_cell(current, self.start_cell_icon)
        else:
            #if additional route, start on previous route
            current = random.choice(self.visited)
            # check that we are on a pasage
            if self.maze[current[0]][current[1]] != self.passage_cell_icon:
                return
            #get neighbours
            neighbours = self.get_neighbours(current)
            #filter our non-walls
            walls = filter(self.get_walls, neighbours)
            #return if no walls among neighbours
            if not walls:
                return
            #turn one of the neighbouring walls to normal block
            #to unleash the new route
            self.set_cell(random.choice(walls), self.block_cell_icon)
        while True:
            #keep track of visited cells
            self.visited.append(current)
            #get neighbours
            neighbours = self.get_neighbours(current)
            try:
                #pick a neighbour to become the next passage
                next_cell = self.pick_neighbour(neighbours)
            except ValueError:
                if route == 0:
                    # mark end point if is original route
                    self.set_cell(current, self.end_cell_icon)
                break
            # mark new passage
            self.set_cell(next_cell, self.passage_cell_icon)
            current = next_cell


new_maze = MazeGen()
new_maze()
