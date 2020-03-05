from .day import Day
from src.utils.file_util import read_file_delimited
from .intcode_program import IntcodeProgram
from .ran import Lol


class Day5(Day):
    def __init__(self, file_path):
        self.file_path = file_path
        print(self.file_path)
        self.input_program = read_file_delimited(self.file_path, [','])

    def part1(self):
        
        for program in self.input_program:
            program = IntcodeProgram(program)
            program.run_program()
        # The whole program is stored in index 0 in input_program

    
    def part2(self):
        return
        print('part2')
    
    
