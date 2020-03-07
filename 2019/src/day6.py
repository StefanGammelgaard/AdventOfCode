from .day import Day
from src.utils.file_util import read_file_lines

class MapItem:
    def __init__(self, name):
        # List of other MapItems
        self.name = name
        self.prev = None # Points to the previous node
        self.orbitees = []
        

class Day6(Day):
    def __init__(self, file_path):
        self.file_path = file_path
        self.orbits = [line.strip('\n') for line in read_file_lines(self.file_path, False)]
        #self.seen = set()
        self.total = 0

    def create_orbit_dict(self):
        orbit_dict = { }
        for orbit in self.orbits:
            a, o = self.get_hmm(orbit)
            if a not in orbit_dict.keys():
                orbit_dict[a] = MapItem(a)
            if o not in orbit_dict.keys():
                orbit_dict[o] = MapItem(o)
            attractor = orbit_dict.get(a)
            orbitee = orbit_dict.get(o)
            attractor.orbitees.append(orbitee)
            orbitee.prev = attractor
            b = 3
        return orbit_dict

    def get_hmm(self, o):
        s = o.split(')')
        # 0 = attractor, 1 = orbiter
        return s[0], s[1]

    def count(self, orbits):
        for o in orbits.orbitees:
            self.total += 1
            self.count(o)

    def part1(self):
        orbit_dict = self.create_orbit_dict()
        for k, v in orbit_dict.items():
                self.count(v)
        return self.total

    def check_orbitees(self, o, paths, cur_path, target):
        if len(o.orbitees) == 0 and o.name not in ['SAN', 'YOU']:
            return
        cur_path.add(o.name)
        #print('Checking orbits for:', o.name)
        if o.name == target:
            print('lol')
            print(cur_path)
            paths.add(''.join(cur_path))
            print(paths)
            #return cur_path
        for os in o.orbitees:
            cp = cur_path.copy()
            cp.add(os.name)
            self.check_orbitees(os, paths, cp, target)
            
    def check_node(self, o, target):
        for os in o.orbitees:
            cp = set()
            cp.add(o.name)
            self.check_orbitees(os, set(), cp, target)
#            valid, p = self.check_orbitees(os, set(), set())
    
    """
    This could done a lot easier without doing recursion backwards
    """
    def part2(self):
        orbit_dict = self.create_orbit_dict()

        start = orbit_dict.get('COM')
        self.check_node(start, 'SAN')
        self.check_node(start, 'YOU')

        # We start at our location
        #start = orbit_dict.get('YOU')
        #valid_paths = []
        #invalid = set()
        #self.check_node(start, set(), invalid)
        #print('Invalid', invalid)
        #for o in start.prev.orbitees:
        #    self.check_node(o, set())








        #ll = self.check_prev(start.prev, set(), set())
        #print(ll)
        # Start with prev of ourself.
        found = False
        #print(start.prev.orbitees)
        
        #for o in start.prev.orbitees:
            #self.check_orbitee(o.prev)
            #print('Check:', o.name)
            #self.check_orbitee(o)
            # self.check_orbitee(o.prev)
            #print(o)
        
        # Check if any orbitees contains our target:
        

        
        
        

