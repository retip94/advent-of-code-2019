import time
import math


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible_asteroids = {}

    def __repr__(self):
        return "(x:{}, y:{})".format(self.x, self.y)

    def add_visible_asteroid(self, asteroid):
        angle = self.get_angle_between_asteroids(asteroid)
        self.visible_asteroids[asteroid] = angle

    def get_distance_to_asteroid(self, target_asteroid):
        return abs(target_asteroid.x - self.x) + abs(target_asteroid.y - self.y)

    def get_angle_between_asteroids(self, target_ateroid):
        delta_x = target_ateroid.x - self.x
        delta_y = self.y - target_ateroid.y
        angle = math.atan2(delta_x, delta_y)
        angle = (math.degrees(angle) + 360) % 360
        return angle

    def get_visible_asteroids_sorted_by_angle(self):
        return {k: v for k, v in sorted(self.visible_asteroids.items(), key=lambda item: item[1])}


class Space:
    def __init__(self, input_path):
        space_map = open(input_path, 'r').read()
        self.space_rows = space_map.split('\n')
        self.width = len(self.space_rows[0])
        self.height = len(self.space_rows)
        self.asteroids = self.__map_asteroids()

    def __map_asteroids(self):
        asteroids = []
        for y, row in enumerate(self.space_rows):
            for x, space_point in enumerate(row):
                if space_point == '#':
                    asteroids.append(Asteroid(x, y))
        return asteroids

    def check_for_clear_path(self, starting_asteroid, target_asteroid):
        distance = starting_asteroid.get_distance_to_asteroid(target_asteroid)
        line_params = self.__get_line_equation_parameters(starting_asteroid, target_asteroid)
        for asteroid in self.asteroids:
            # get next if it's starting or target
            if asteroid in [starting_asteroid, target_asteroid]:
                continue
            if line_params['a'] is None:
                if starting_asteroid.x == asteroid.x:
                    if starting_asteroid.get_distance_to_asteroid(asteroid) > distance:
                        continue
                    if line_params['go_right_or_up'] == (asteroid.y > starting_asteroid.y):
                        return False
            else:
                result = (line_params['a'] * asteroid.x + line_params['b'])
                if asteroid.y == round(result, 5):
                    if starting_asteroid.get_distance_to_asteroid(asteroid) > distance:
                        continue
                    if line_params['go_right_or_up'] == (asteroid.x > starting_asteroid.x):
                        return False
        return True

    def __get_line_equation_parameters(self, starting_asteroid, target_asteroid):
        try:
            a = (target_asteroid.y - starting_asteroid.y) / (target_asteroid.x - starting_asteroid.x)
            b = (target_asteroid.y - (a * target_asteroid.x))
            go_right_or_up = target_asteroid.x > starting_asteroid.x
        except ZeroDivisionError:
            a = None
            b = None
            go_right_or_up = target_asteroid.y > starting_asteroid.y
        return {'a': a, 'b': b, 'go_right_or_up': go_right_or_up}

    def __map_asteroids_to_visible_asteroids(self):
        for starting_asteroid in self.asteroids:
            self.__find_visible_asteroids(starting_asteroid)

    def __find_visible_asteroids(self, starting_asteroid):
        for asteroid in self.asteroids:
            if asteroid == starting_asteroid:
                continue
            if starting_asteroid in asteroid.visible_asteroids:
                starting_asteroid.add_visible_asteroid(asteroid)
            elif self.check_for_clear_path(starting_asteroid, asteroid):
                starting_asteroid.add_visible_asteroid(asteroid)

    def get_asteroid_with_max_number_of_visible_asteroids(self):
        self.__map_asteroids_to_visible_asteroids()
        max_visible_asteroids = 0
        max_asteroid = None
        for asteroid in self.asteroids:
            if len(asteroid.visible_asteroids) > max_visible_asteroids:
                max_visible_asteroids = len(asteroid.visible_asteroids)
                max_asteroid = asteroid
        return "{} with {} visible asteroids [index: {}]".format(max_asteroid, max_visible_asteroids,
                                                                 self.asteroids.index(max_asteroid))

    def part_two(self, asteroid_id):
        station = self.asteroids[asteroid_id]
        counter = 0
        while True:
            self.__find_visible_asteroids(station)
            sorted_visible_asteroids = station.get_visible_asteroids_sorted_by_angle()
            for visible_asteroid in sorted_visible_asteroids:
                counter += 1
                if (counter == 200):
                    result = visible_asteroid.x * 100 + visible_asteroid.y
                    return "The {}th asteroid to be vaporized is at {}. Result is={}".format(counter, visible_asteroid,
                                                                                             result)
                self.asteroids.remove(visible_asteroid)


time_now = time.time()
input_path = './input.txt'
space = Space(input_path)
print(space.asteroids)
# print(space.get_asteroid_with_max_number_of_visible_asteroids())

# we get id from part1
print(space.part_two(350))
print(time.time() - time_now)
