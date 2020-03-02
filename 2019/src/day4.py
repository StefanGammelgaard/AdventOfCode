from .day import Day
from collections import Counter
class Day4(Day):
    def __init__(self, file_name):
        self.input = '134792-675810'
        self.min = 134792
        self.max = 675810
        self.max_digits = 6
        self.other = set()

    def generate_sequence(self):
        for x in range(self.min, self.max + 1):
            yield x

    def part1(self):
        count = 0
        for x in self.generate_sequence():
            x = str(x)
            if any(x == y for x, y in zip(x, x[1:])) and \
               all(x <= y for x, y in zip(x, x[1:])): 
                count += 1
        return count

    def part2(self):
        # The gives the right answer but Im not sure its the right way to solve it
        count = 0
        for x in self.generate_sequence():
            x = str(x)
            if all(x <= y for x, y in zip(x, x[1:])) and \
                2 in Counter(x).values():
                count += 1
        return count

   

   