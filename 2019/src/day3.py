import math
from src.utils.file_util import (
    read_file_delimited
)
from .day import Day

class Point():
    def __init__(self, x, y, steps):
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
        cur_pos = Point(0, 0, 0)
        for dir in wire_input:                
            d = dir[0]
            steps = int(dir[1:])
            s = 0
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
        return sets[0].intersection(sets[1])


    # Result should be 1285
    def part1(self):
        return min(self.get_intersections(), key=lambda point: point.manhatten_distance()).manhatten_distance()

    def part2(self):
        intersections = self.get_intersections()
        # cant index in sets!
        limit = len(intersections)
        cur_best = 99999
        for i, intersection in enumerate(intersections):
            if limit - 1 == i:
                break
            if steps := intersection.steps + intersection[i + 1].steps < cur_best:
                cur_best = steps
        return cur_best
            