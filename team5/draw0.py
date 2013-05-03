import turtle
import random

import maze


def draw_path(path, t):
    for s in path.steps:
        t.left(s.angle)
        t.forward(s.distance)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    p = maze.Path()
    p.steps = [maze.Segment(random.randrange(5, 100), random.randrange(-90, 90)) for i in range(100)]

    draw_path(p, t)
    raw_input()

if __name__ == '__main__':
    main()
