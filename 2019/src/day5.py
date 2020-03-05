from .day import Day
from src.utils.file_util import read_file_delimited
from .intcode_program import IntcodeProgram
from .ran import Lol
from copy import deepcopy


class Day5(Day):
    def __init__(self, file_path):
        self.file_path = file_path
        print(self.file_path)
    """
    Because read_file_delimited is a generator it needs to be called twich if it is to used in both part1 and part2
    """

    def part1(self):
        for program in read_file_delimited(self.file_path, [',']):
            p = IntcodeProgram(program)
            return p.run_program()

    
    def part2(self):
        for program in read_file_delimited(self.file_path, [',']):
            p = IntcodeProgram(program)
            return p.run_program()


    
