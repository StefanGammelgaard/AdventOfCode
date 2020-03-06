from .day import Day
from src.utils.file_util import read_file_lines

class MapItem:
    def __init__(self, name):
        # List of other MapItems
        self.name = name
        self.orbitees = []

class Day6(Day):
    def __init__(self, file_path):
        self.file_path = file_path
        self.orbits = [line.strip('\n') for line in read_file_lines(self.file_path, False)]
        self.seen = set()
        self.total = 0

        #print(self.orbits)

    def get_hmm(self, o):
        s = o.split(')')
        # 0 = attractor, 1 = orbiter
        return s[0], s[1]

    def count(self, orbits):
        for o in orbits.orbitees:
            if o.name not in self.seen:
                #self.seen.add(o.name)
                self.total += 1
                self.count(o)


            

    def part1(self):
        # { MapItem.name: MapItem}
        orbit_dict = { }
        for orbit in self.orbits:
            a, o = self.get_hmm(orbit)
            #print(a, s)
            
            if a not in orbit_dict.keys():
                orbit_dict[a] = MapItem(a)
            if o not in orbit_dict.keys():
                orbit_dict[o] = MapItem(o)
            attractor = orbit_dict.get(a)
            orbitee = orbit_dict.get(o)
            attractor.orbitees.append(orbitee)

        #print(orbit_dict)
        for k, v in orbit_dict.items():
                self.count(v)
        
        print('TOTAL:', self.total)
        return self.total


    def part2(self):
        pass
