import math
from src.utils.file_util import (
    read_file_lines,
)
from src.day import Day


class Day1(Day):
    def __init__(self, file_path):
        self.file_path = file_path

    def __calculate_fuel_for_module(self, module):
        return math.trunc(module / 3) - 2
       
    def part1(self):
        sum = 0
        for module in read_file_lines(self.file_path):
            sum += self.__calculate_fuel_for_module(module)
        return sum
   
    def part2(self):
        sum = 0
        for module in read_file_lines(self.file_path):
            sum += self.__calculate__fuel_for_module_including_fuel(module, 0)
        return sum

    def __calculate__fuel_for_module_including_fuel(self, module, sum):
        f = self.__calculate_fuel_for_module(module)
        if f <= 0:
            return sum
        else:
            sum += f
            return self.__calculate__fuel_for_module_including_fuel(f, sum)    