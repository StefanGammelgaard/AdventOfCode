#from src.day1 import Day1
from src.day1 import Day1
from src.day2 import Day2
from src.day3 import Day3
from src.day4 import Day4
from src.utils.file_util import (
    get_file_path
)

day_dict = {
    1: Day1,
    2: Day2,
    3: Day3,
    4: Day4,
}

def get_day(day):
    file_path = get_file_path(day)
    d = day_dict.get(day)
    return d(file_path)


def main():
    day = 4 # read input
    d = get_day(day)
    print(f'Part1: {d.part1()}') 
    print(f'part2: {d.part2()}')

        


if __name__ == "__main__":
    main()



