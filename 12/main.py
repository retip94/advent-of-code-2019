from re import findall
import time
from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.starting_position = [x, y, z]
        # self.position_history = [self.position[:]]
        self.velocity = [0, 0, 0]
        self.energy = 0
        self.calculate_total_energy()
        self.was_here_in_past = False

    def __repr__(self):
        return "Moon{}({}) with {} energy".format(self.position, self.velocity, self.energy)

    def apply_gravity(self, other_moon):
        for i in range(0, 3):
            if self.position[i] > other_moon.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < other_moon.position[i]:
                self.velocity[i] += 1

    def move(self):
        for i in range(0, 3):
            self.position[i] += self.velocity[i]
        # self.was_here_in_past = (self.position in self.starting_position[:1])
        self.was_here_in_past = (self.position == self.starting_position)
        # self.position_history.append(self.position[:])

    def calculate_total_energy(self):
        potential_energy = self.calculate_potential_energy()
        kinetic_energy = self.calculate_kinetic_energy()
        self.energy = potential_energy * kinetic_energy

    def calculate_potential_energy(self):
        return sum([abs(x) for x in self.position])

    def calculate_kinetic_energy(self):
        return sum([abs(x) for x in self.velocity])


f = open('./input.txt', 'r')
moons_input = f.read().split('\n')
moons = []
for m in moons_input:
    x, y, z = [int(x) for x in findall(r'-?\d+', m)]
    moons.append(Moon(x, y, z))

# ---------------PART 1
for timestamp in range(0, 1000):
    # print(timestamp, moons)
    for moon in moons:
        for other_moon in moons:
            if other_moon == moon:
                continue
            moon.apply_gravity(other_moon)
    for moon in moons:
        moon.move()
for moon in moons:
    moon.calculate_total_energy()
moons_energy = sum([moon.energy for moon in moons])
print(moons_energy)
# 7928

# Explanation for part 2
'''
Solution 2
LCM works because each axis is cycling independently. Let's do a simple example:
3 series, each repeating at a different period. If the state is based on all 3 series, 
then how long until we see the same state again?
    0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
S1: 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3 0
S2: 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
S3; 0 1 2 3 4 5 0 1 2 3 4 5 0 1 2 3 4
S1 has a period of 4, S2 of 2, S3 of 6. And the combined series has a period of 12, 
which is the LCM of 2, 4, and 6. You'll get pairwise repetitions earlier than that.
S1 and S2 have a combined period of 4. S2 and S3 have a combined period of 6. 
But S1 and S3 have a combined period of 12.
There's a more mathematically rigorous way to describe this, but the 
above illustrates what's happening.
Explanation by u/rabuf (https://www.reddit.com/user/rabuf/) 
'''
'''
We will capture the orbital periods (https://en.wikipedia.org/wiki/Orbital_period) for each axis here:
{
  0: step at which all 4 moons are at their starting x-position and x-velocity
  1: step at which all 4 moons are at their starting y-position and y-velocity
  2: step at which all 4 moons are at their starting z-position and z-velocity
}
'''

def lcm(a, b):
  return (a * b) // gcd(a, b)

moons = []
for m in moons_input:
    x, y, z = [int(x) for x in findall(r'-?\d+', m)]
    moons.append(Moon(x, y, z))

starting_time = time.time()
timestamp = 0
axis_periods = {}
start = [[(m.position[axis], m.velocity[axis]) for m in moons] for axis in range(3)]
while len(axis_periods) < 3:
    # print(timestamp)
    timestamp += 1
    for moon in moons:
        for other_moon in moons:
            if other_moon == moon:
                continue
            moon.apply_gravity(other_moon)
    for moon in moons:
        moon.move()

    for axis in range(3):
        '''
        See if current (pos_axis, vel_axis) for all moons match their starting values:
        '''
        if axis not in axis_periods and start[axis] == [(m.position[axis], m.velocity[axis]) for m in moons]:
            axis_periods[axis] = timestamp

result = lcm(lcm(axis_periods[0],axis_periods[1]),axis_periods[2])
print('answer for part2 is: ',result)
