import math
from src.utils.file_util import (
    read_file_delimited
)
from .day import Day

class Point():
    def __init__(self, x = 0, y = 0, steps = 0):
        self.x = x
        self.y = y
        self.steps = steps
    
    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)

    #https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes
    # See the first answer
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Day3(Day):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_wire_input(self):
        return read_file_delimited(self.file_path, [','], convert_int=False)

    def get_points(self, wire_input):
        points = set()
        cur_pos = Point()
        s = 0
        for dir in wire_input:                
            d = dir[0]
            steps = int(dir[1:])
            for _ in range(steps):
                if d == 'R':
                    cur_pos.x += 1
                if d == 'L':
                    cur_pos.x -= 1
                if d == 'D':
                    cur_pos.y -= 1
                if d == 'U':
                    cur_pos.y += 1
                s += 1
                points.add(Point(cur_pos.x, cur_pos.y, s))
        return points
    
    def get_intersections(self):
        wire_input = self.get_wire_input()
        sets = []
        for input in wire_input:
            sets.append(self.get_points(input))
        return sets[0], sets[1], sets[0].intersection(sets[1])

    # Result should be 1285
    def part1(self):
        set1, set2, intersection = self.get_intersections()
        return min(intersection, key=lambda point: point.manhatten_distance()).manhatten_distance()

    def part2(self):
        set1, set2, intersections = self.get_intersections()
        # Check which point from set1 is in the intersection
        p1 = []
        for p in set1:
            if p in intersections:
                p1.append(p)
        # Check which points from set2 in the intersection
        p2 = []
        for p in set2:
            if p in intersections:
                p2.append(p)
        tups = []
        for p in p1:
            for pp in p2:
                if p == pp:
                    tups.append((p, pp))

        # Answer should be 14228
        m = min(tups, key=lambda tup: tup[0].steps + tup[1].steps)
        return m[0].steps + m[1].steps
        
            