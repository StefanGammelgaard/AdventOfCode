from .day import Day

class Day4(Day):
    def __init__(self, file_name):
        self.input = '134792-675810'
        self.min = 134792
        self.max = 675810
        self.max_digits = 6
        self.other = set()

    def part1(self):
        count = 0
        for x in range(self.min, self.max + 1):
            if self.match_criteria(x, self.min_two_adjacent_equal_num):
                count += 1
        return count    

    def all_increasing(self, num):
        return all(x <= y for x, y in zip(num, num[1:]))
    
    def min_two_adjacent_equal_num(self, num):
        return any(x == y for x, y in zip(num, num[1:]))

    #  This doesnt work
    def max_two_adjacent_equal_num(self, num):
        pairs = zip(num, num[1:])
        print(list(pairs))


    def match_criteria(self, num, adjacent_fn):
        return self.all_increasing(str(num)) and  \
               adjacent_fn(str(num)) and \
               len(str(num)) == self.max_digits

    def check_for_odd_occurence(self, num):
        last_seen = ''
        counter = 1
        pair_found = False
        for c in num:
            if c == last_seen:
                counter += 1
            if c != last_seen:
                if counter >= 2 and counter % 2 != 0:
                    return False
                last_seen = c
                counter = 1
        return counter < 2 or (counter >= 2 and counter % 2 == 0)  

    def check(self, n):
        return list(n) == sorted(n) and 2 in map(n.count, n)

    def part2(self):
        y = '134889'
        #y = '3444'
        #r = self.check_for_odd_occurence(y)
        #return
        mine = set()
        #res = sum(self.criteria_match_LOL(str(pass_num), lambda x:x == 2) for pass_num in range(134792, 675810 + 1))
        # 1319
        count = 0
        other_res = []
        for x in range(self.min, self.max + 1):
            #if self.all_increasing(str(x)):

            #if self.check_for_odd_occurence(str(x)) and self.all_increasing(str(x)):
            #    mine.add(str(x))
            other_r = self.check(str(x))
            if other_r:
                other_res.append(x)
            #res = self.match_criteria(x, self.check_for_odd_occurence)
            #if res:
            #    count += 1
                #mine.add(str(x))
            #else:
                #print(x)
            #    mine.add(x)
        
       
        for x in mine:
            inc = self.all_increasing(str(x))
            adj = self.check_for_odd_occurence(str(x))
            if not adj and inc:
                adadad = 3
                print(x)
            if not self.all_increasing(str(x)):
                dadad = 3



        #print('MyCount:', len(mine))
        #print('OtherCount', len(self.other))
        #setMine = set(mine)
        #setOther = set(self.other)
        #dif = setOther.difference(mine)
        #d1 = mine.difference(setOther)
        #for s in d1:
        #    pass
            #print(s)
        #print(len(dif))
        #for x in mine:
        #    if x not in self.other:
        #        print(x)
        return count 