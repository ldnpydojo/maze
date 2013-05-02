import os, sys
import random
import namedtuple

Segment = namedtuple("Segment", "angle distance")

class Path(object):

    def __init__(self):
        self.start = None
        self.stop = None
        self.steps = []

class Maze(object):

    w, h = 400, 400

    def __init__(self):
        self.paths = []
        self.entry = point_1
        self.exit = point_2

    def generate_path(self, start, stop):
        waypoints = []
        waypoints.append(start)
        for x in range(10):
            waypoints.append(
                (random.randint(self.w),
                random.randint(self.h))
            )
        waypoints.append(stop)

    def generate_paths(self, n_paths=10):
        for i in range(n_paths):
            start = 0, random.randint(self.h)
            stop = self.w, random.randint(self.h)
            self.paths.append(self.generate_path(start, stop))
