from itertools import permutations
from src.day import Day
from src.utils.file_util import read_file_delimited
from src.intcode_program import IntcodeProgram
from copy import deepcopy


class Day7(Day):
    def __init__(self, file_path):
        self.file_path = file_path
        self.program = None
        for p in read_file_delimited(self.file_path, [',']):
            self.program = p
            break


    def run_amplifier(self, phase_setting, input, program):
        intcode_program = IntcodeProgram(program)
        #print('intcode_program', intcode_program)
        return intcode_program.run_program(phase=phase_setting, inp=input)

    def part1(self):
        # phase_settings = [ [4,3,2,1,0] ]
        perms = permutations(range(5)) 
        #perms = [[4,3,2,1,0]]
        #print(list(perms))
        # run on each amplifier
        thruster_signal = []
        #pro = self.program[:]
        for perm in perms:
            # For each amplifier
            # output = 0
            output = 0
            for i in range(5):
                phase = perm[i]
                run_res = self.run_amplifier(phase, output, self.program[:])
                #print('run_res', run_res)
                output = run_res
                #break
            thruster_signal.append(run_res)
        return max(thruster_signal)   
        
        # for p in perms:
        #     output = 0
        #     pro = self.program[:]
        #     for phase in p:
        #         output += self.run_amplifier(phase, pro)
        #     thruster_signal.append(output)
        # 



    def part2(self):
        pass