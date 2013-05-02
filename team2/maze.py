test = [[1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        ]

start = (0,0)
width = 5
height = 5
visited = []
current = start



visited.append(current)




def get_neighbours(maze, cell):
    neighbours = []
    # Try y
    try:
        coords = (cell[0] + 1, cell[1])
        maze[coords[0]][coords[1]]
        neighbours.append(coords)
    except IndexError:
        pass
    # try x
    try:
        coords = (cell[0], cell[1] + 1)
        maze[coords[0]][coords[1]]
        neighbours.append(coords)
    except IndexError:
        pass

    return neighbours
