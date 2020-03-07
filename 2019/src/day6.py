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
        #self.seen = set()
        self.total = 0

    def create_orbit_dict(self):
        orbit_dict = { }
        for orbit in self.orbits:
            a, o = self.split_orbit(orbit)
            if a not in orbit_dict.keys():
                orbit_dict[a] = MapItem(a)
            if o not in orbit_dict.keys():
                orbit_dict[o] = MapItem(o)
            attractor = orbit_dict.get(a)
            orbitee = orbit_dict.get(o)
            attractor.orbitees.append(orbitee)
        return orbit_dict

    def split_orbit(self, o):
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

    def check_orbitee(self, o, cp, vp):
        if len(o.orbitees) == 0:
            # If its a dead end, we can just return
            if o.name not in ['YOU', 'SAN']:
                return
            # We have found a valid path
            else:
                cp.append(o.name)
                vp.append(cp)
                return
        else:
            # Check orbitees of planet
            cp.append(o.name)
            for os in o.orbitees:
                self.check_orbitee(os, cp[:], vp)

                
    def check_node(self, o, cp, vp):
        for os in o.orbitees:
            self.check_orbitee(os, cp, vp)

    def part2(self):
        """
        """
        orbit_dict = self.create_orbit_dict()
        # We start at node 'COM' and work our way from there towards our targets 'SAN' and 'YOU'
        start = orbit_dict.get('COM')
        current_path = []
        valid_paths = []
        self.check_node(start, current_path, valid_paths)

        y_p = None
        s_p = None
        # Valid_paths contains the paths to our targets
        # Valid paths could be made into a dict instead of this
        for p in valid_paths:
            if 'SAN' in p:
                s_p = p[:]
                s_p.remove('SAN')
            if 'YOU' in p:
                y_p = p[:]
                y_p.remove('YOU')
        # Not very memory efficient since we are copying the list at each loop            
        while y_p[0] == s_p[0]:
            y_p = y_p[1:]
            s_p = s_p[1:]

        """
        What could be done:
        return len(y_p) + len(s_p)
        But that is technically not correct!
        Because for each path, the number of 'jumps' is equal = #planets - 1
        Meaning is should be len(y_p) - 1 + len(s_p) - 1
        But since we are deleting the planet where the two paths diverse in the while loop, 
        we are actually deleting two jumps at that point.
        So...
        """
        return len(y_p) - 1 + len(s_p) - 1 + 2
        