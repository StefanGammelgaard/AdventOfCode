import math
from src.utils.file_util import read_file
from src.day import Day


class Day1(Day):
    def __init__(self):
        self.file_path = r'inputfiles\\day1.txt'

    def __calculate_fuel_for_module(self, module):
        return math.trunc(module / 3) - 2

    def calculate_fuel_requirement(self):
        sum = 0
        for module in read_file(self.file_path, is_generator=True):
            sum += self.__calculate_fuel_for_module(module)
        return sum

    def part1(self):
        print(self.calculate_fuel_requirement())


    def __calculate__fuel_for_module_including_fuel(self, module, sum):
        f = self.__calculate_fuel_for_module(module)
        if f <= 0:
            return sum
        else:
            sum += f
            return self.__calculate__fuel_for_module_including_fuel(f, sum)
       
    def part2(self):
        sum = 0
        for module in read_file(self.file_path, is_generator=True):
            sum += self.__calculate__fuel_for_module_including_fuel(module, 0)
        print(sum)


    