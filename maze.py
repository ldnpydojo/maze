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

    def generate_path(self, start, stop):
        pass

    def generate_paths(self, n_paths=10):
        for i in range(n_paths):
            start = random()
            stop = random()
            self.paths.append(self.generate_path(start, stop))
