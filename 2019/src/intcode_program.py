import operator


class IntcodeProgram:
    def __init__(self, program):
        self.program = program
        self.pc = 0   

    def get_params(self, op):
        param1 = self.program[self.pc+1] if op[2] == '0' else self.pc+1
        param2 = self.program[self.pc+2] if op[1] == '0' else self.pc+2
        param3 = self.program[self.pc+3] if op[0] == '0' else self.pc+3       
 
        return param1, param2, param3

    def run_program(self, initial_override = { }):
        for k, v in initial_override.items():
            self.program[k] = v

        while True:
            op = str(self.program[self.pc])
            while len(op) < 5:
                op = '0' + op
            instruction = op[-1]
            p1, p2, p3 = self.get_params(op)

            if instruction == '1':
                self.program[p3] = self.program[p1] + self.program[p2]
                self.pc += 4
            if instruction == '2':
                self.program[p3] = self.program[p1] * self.program[p2]
                self.pc += 4
            if instruction == '3':
                print('Enter input...')
                inp = input()
                self.program[p1] = int(inp)
                self.pc += 2
            if instruction == '4':
                print('Output ->', self.program[p1])
                self.pc += 2         
            if instruction == '99':
                break
