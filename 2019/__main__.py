#from src.day1 import Day1
from src.day1 import Day1
from src.day2 import Day2
from src.utils.file_util import (
    get_file_path
)

day_dict = {
    1: Day1,
    2: Day2,
}

def get_day(day):
    file_path = get_file_path(day)
    d = day_dict.get(day)
    return d(file_path)


def main():
    day = 2 # read input
    d = get_day(day)
    print(f'Part1: {d.part1()}') 
    print(f'part2: {d.part2()}')

if __name__ == "__main__":
    main()



