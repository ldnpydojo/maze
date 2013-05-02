import random
import pprint

maze = [[1 for x in range(10)] for x in range(10)]

start = (0, 0)
visited = []
current = start

visited.append(current)


def get_neighbours(cell):
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
                maze[coord[0]][coord[1]]
                neighbours.append(coord)
        except IndexError:
            continue

    return neighbours

def valid_neighbours(x):
    cell= maze[x[0]][x[1]]
    return cell != 2 and cell != 0


def pick_neighbour(neighbours):
    neighbours = filter(valid_neighbours, neighbours)
    random_index = random.randint(0,len(neighbours) - 1)
    candidate =  neighbours.pop(random_index)
    for neighbour in neighbours:
        maze[neighbour[0]][neighbour[1]] = 2
    return candidate


def set_cell(coords, value):
    maze[coords[0]][coords[1]] = value

set_cell(current, 0)
while True:
    neighbours = get_neighbours(current)
    try:
        next_cell = pick_neighbour(neighbours)
    except ValueError:
        for x, line in enumerate(maze):
            for y, cell in enumerate(line):
                if maze[x][y] == 2:
                    maze[x][y] = 1
        pprint.pprint(maze)
        break
    maze[next_cell[0]][next_cell[1]] = 0
    current = next_cell


