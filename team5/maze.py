import os, sys
import math
import random
from collections import namedtuple

Segment = namedtuple("Segment", "angle distance")

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


m = Maze()
r = []
m.generate_paths(100, 100, 5, r)
import pprint
pprint.pprint(r)
print r
