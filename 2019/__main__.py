#from src.day1 import Day1
from src.day1 import Day1



day_dict = {
    1: Day1()
}

def main():
    # Parse the input somewhere
    d = day_dict.get(1)
    d.part1()
    d.part2()
    #d1 = Day1()
    #d1.part1()
    #d1.part2()

if __name__ == "__main__":
    main()



