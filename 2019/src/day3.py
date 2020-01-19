import math
from src.utils.file_util import (
    read_file_delimited
)
from .day import Day

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = self.distance_to_central_port()

    def distance_to_central_port(self):
        return abs(abs(self.x) + abs(self.y))


class Day3(Day):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_wire_input(self):
        return read_file_delimited(self.file_path, [','], convert_int=False)

    def check_for_intersection(self, points, new_pos):
        for point in points:
            if point.x == new_pos.x and point.y == new_pos.y:
                return True
        return False
        
    def part1(self):
        
        wire_input = self.get_wire_input()
        for input in wire_input:
            points = []
            intersections = []
            # USE SET
            cur_pos = Point(0, 0)
            for dir in input:                
                d = dir[0]
                steps = int(dir[1:])
                for x in range(steps):
                    if d == 'R':
                        cur_pos.x += 1
                    if d == 'L':
                        cur_pos.x -= 1
                    if d == 'D':
                        cur_pos.y -= 1
                    if d == 'U':
                        cur_pos.y += 1
                    #print(f'Cur pos x {cur_pos.x}, y : {cur_pos.y}')
                    if self.check_for_intersection(points, cur_pos):
                        intersections.append(Point(cur_pos.x, cur_pos.y))
                    else:
                        points.append(Point(cur_pos.x, cur_pos.y))
                    #if not self.check_for_intersection(points, cur_pos):
                        #points.append(cur_pos)
                    #else:
                    #    intersections.append(cur_pos)
        #print(intersections)
            m = min(intersections, key=lambda x: x.distance)
            print(m.distance)
            #print(min(intersections, key=lambda x: x.distance).distance)
            #print(len(intersections))
        #for inter in intersections:

            #print(inter.distance_to_central_port())

                


    def part2(self):
        pass