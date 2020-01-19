import operator

class IntcodeProgram:
    def __init__(self, program):
        self.program = program
        self.operator_dict = {
            1: operator.add,
            2: operator.mul
        }
    
    def run_program(self, initial_override=  { }):
        for k, v in initial_override.items():
            self.program[k] = v

        for i in range(0, len(self.program), 4):
            opcode = self.program[i]
            if opcode == 99:
                break
            val1 = self.program[self.program[i+1]]
            val2 = self.program[self.program[i+2]]
            pos = self.program[i+3]
            self.program[pos] = self.shift(opcode, val1, val2)
        return self.program[0]
    
    def shift(self, opcode, val1, val2):
        op = self.operator_dict.get(opcode)
        return op(val1, val2) 
    
    