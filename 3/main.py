import time
import numpy as np


class Wire:
    def __init__(self, path_str):
        path = path_str.split(',')
        path = list(map(lambda x: [x[0], int(x[1:])], path))
        self.path = path
        self.coordinates = []
        self.put_wire_on_grid()
        self.coordinates = np.array(self.coordinates)
        self.coordinates = self.coordinates.view(dtype='i,i').reshape((-1,))

    def put_wire_on_grid(self):
        x, y = 0, 0
        # move example R,75
        for move in self.path:
            direction, steps = move
            for i in range(0, steps):
                if direction == 'U':
                    y += 1
                elif direction == 'R':
                    x += 1
                elif direction == 'D':
                    y -= 1
                elif direction == 'L':
                    x -= 1
                self.coordinates.append((x, y))


class DayThree:
    def __init__(self):
        f = open("input.txt", "r")
        wires_paths = f.read()
        path1, path2 = wires_paths.split('\n')
        self.wire1 = Wire(path1)
        self.wire2 = Wire(path2)

    def find_crossings(self):
        crossings = np.intersect1d(self.wire1.coordinates, self.wire2.coordinates)

        return crossings

    def find_closest_crossing(self):
        crossings = self.find_crossings()
        shortest_distance = min(list(map(lambda coords: abs(coords[0]) + abs(coords[1]), crossings)))
        return shortest_distance

    def find_first_crossing(self):
        crossings = self.find_crossings()
        min_steps_sum = 9999999999999999999999999999999999999999
        for crossing in crossings:
            wire1_steps = np.where(self.wire1.coordinates == crossing)[0][0]
            wire2_steps = np.where(self.wire2.coordinates == crossing)[0][0]
            steps_sum = wire1_steps + 1 + wire2_steps + 1
            if steps_sum < min_steps_sum:
                min_steps_sum = steps_sum
        return min_steps_sum


time_now = time.time()
answers = DayThree()
print("answer for part1 is: ", answers.find_closest_crossing())
print("answer for part2 is: ", answers.find_first_crossing())

print(time.time() - time_now)
# 900 s -- traiditional way
# 1,66 s -- numpy
# answers for my input: 1064, 25676
