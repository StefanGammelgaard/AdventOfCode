#from src.day1 import Day1
from src.day1 import Day1
from src.day2 import Day2
from src.day3 import Day3
from src.day4 import Day4
from src.day5 import Day5
from src.day6 import Day6
from src.utils.file_util import (
    get_file_path
)

answer_dict = {
    1: (3520097, 5277255),
    2: (3101878, 8444),
    3: (1285, 14228),
    4: (1955, 1319),
    5: (13346482, 12111395),
    6: (0, 0)
}
1
day_dict = {
    1: Day1,
    2: Day2,
    3: Day3,
    4: Day4,
    5: Day5,
    6: Day6,
}

def run_all_days():
    for x in range(25):
        d = get_day(x)
        if d:
            ans_part1, ans_part2 = answer_dict.get(x)
            try:
                assert d.part1() == ans_part1 
                assert d.part2() == ans_part2
                print(f'Day {x} success!') 
            except AssertionError as err:
                print(f'Day {x} failed!')
                print(repr(err))
            


def get_day(day):
    file_path = get_file_path(day)
    d = day_dict.get(day, None)
    if d:
        return d(file_path)


def main():
    run_all_days()
    return
    day = 2 # read input
    d = get_day(day)
    print(f'Part1: {d.part1()}') 
    print(d.part1())
    print(f'part2: {d.part2()}')



if __name__ == "__main__":
    main()



