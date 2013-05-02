import os, sys
import math
import random
from collections import namedtuple

Segment = namedtuple("Segment", "angle distance")

class Path(object):

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.steps = []

class Maze(object):

    w, h = 400, 400

    def __init__(self):
        self.paths = []

    def generate_paths(self, x, w, n, result):
        if n == 0:
            return
        angle = random.randrange(0, 60)
        l  = math.cos(angle / 180 * math.pi) / w
        self.generate_paths(x + w / 2, w / 2, n - 1, result)
        self.generate_paths(x, w / 2, n - 1, result)
        result.append(Segment(angle, w))
        result.append(Segment(-2 * angle, w))

    def generate_path_1(self, start, stop):
        waypoints = []
        waypoints.append(start)
        waypoints.append(stop)

    def generate_paths_2(self, n_paths=10):
        for i in range(n_paths):
            start = 0, random.randint(self.h)
            stop = self.w, random.randint(self.h)
            self.paths.append(self.generate_path(start, stop))


m = Maze()
r = []
m.generate_paths(100, 100, 5, r)
import pprint
pprint.pprint(r)
print r