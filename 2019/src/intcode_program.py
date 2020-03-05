import operator


class IntcodeProgram:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.math_op_dict = {
            '1': operator.add,
            '2': operator.mul
        }

    def get_params(self, op):
        param1 = self.program[self.pc+1] if op[2] == '0' else self.pc+1
        param2 = self.program[self.pc+2] if op[1] == '0' else self.pc+2
        param3 = self.program[self.pc+3] if op[0] == '0' else self.pc+3       
 
        return param1, param2, param3

    def run_program(self, initial_override = { }, return_index_zero = False):
        for k, v in initial_override.items():
            self.program[k] = v
        output = 0
        try:
            while self.pc < len(self.program):
                #print(self.pc, '---', len(self.program))
                op = str(self.program[self.pc])
                while len(op) < 5:
                    op = '0' + op
                instruction = op[-1]
                p1, p2, p3 = self.get_params(op)

                if instruction == '1' or instruction == '2':
                    self.program[p3] = self.math_op_dict[instruction](self.program[p1], self.program[p2])
                    self.pc += 4
                    
                if instruction == '3':
                    print('Enter input...')
                    inp = input()
                    self.program[p1] = int(inp)
                    self.pc += 2

                if instruction == '4':
                    #print('Output ->', self.program[p1])
                    output = self.program[p1]
                    self.pc += 2         

                if instruction == '5':
                    if self.program[p1] != 0:
                        self.pc = self.program[p2]
                    else:
                        self.pc += 3
                        
                if instruction == '6':
                    if self.program[p1] == 0:
                        self.pc = self.program[p2]
                    else:
                        self.pc += 3

                if instruction == '7':
                    if self.program[p1] < self.program[p2]:
                        self.program[p3] = 1
                    else:
                        self.program[p3] = 0
                    self.pc += 4

                if instruction == '8':
                    if self.program[p1] == self.program[p2]:
                        self.program[p3] = 1
                    else:
                        self.program[p3] = 0
                    self.pc += 4

                if instruction == '9':
                    # Needed for day2
                    if return_index_zero:
                        return self.program[0]
                    return output
        # Part2 gives index of out bounds in at the last iteration...             
        except Exception as e:
            return output
        