from .day import Day

class Day4(Day):
    def __init__(self, file_name):
        self.input = '134792-675810'
        self.min = 134792
        self.max = 675810
        self.max_digits = 6

    def part1(self):
        count = 0
        for x in range(self.min, self.max):
            if self.match_criteria(x):
                count += 1
        return count    
        
    def all_increasing(self, num):
        return all(x <= y for x, y in zip(num, num[1:]))
    
    def min_two_adjacent_equal_num(self, num):
        return any(x == y for x, y in zip(num, num[1:]))

    def match_criteria(self, num):
        return self.all_increasing(str(num)) and  \
               self.min_two_adjacent_equal_num(str(num)) and \
               len(str(num)) == self.max_digits
               

    def part2(self):
        pass    