from src.utils.file_util import read_file_delimited
from .intcode_program import IntcodeProgram
from .day import Day

class Day2(Day):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_intcode_input(self, delimeters = [',']):
        return read_file_delimited(self.file_path, delimeters)


    def part1(self):
        initial_overrides = { 1: 12,
                             2: 2 }
        intcode_program_input = self.get_intcode_input()
        # NOTE the input file is only 1 line, hence only 1 p
        for values in intcode_program_input:
            p = IntcodeProgram(values)
            return p.run_program(initial_overrides)
    
    def part2(self):
        for noun in range(100):
            for verb in range(100):
                initial_overrides = {
                    1: noun,
                    2: verb
                }
                intcode_program_input = self.get_intcode_input()
                for values in intcode_program_input:
                    p = IntcodeProgram(values)
                    if p.run_program(initial_overrides) == 19690720:
                        return 100 * noun + verb