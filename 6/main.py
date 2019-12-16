class Planet:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return "{} orbiting {}".format(self.name, self.parent)


class DaySix:
    def __init__(self):
        f = open("input.txt", "r")
        connections = f.read().split('\n')
        self.planets = {'COM': Planet('COM', '')}
        for connection in connections:
            parent_planet, child_planet = connection.split(')')
            self.planets[child_planet] = Planet(child_planet, parent_planet)
        orbits_number = self.__calculate_orbits()
        self.part_one_result = orbits_number
        self.part_two_result = self.find_path_between_planets(self.planets['YOU'], self.planets['SAN'])

    def __calculate_orbits(self):
        counter = 0
        for name, planet in self.planets.items():
            while planet.parent != '':
                counter += 1
                planet = self.planets[planet.parent]
        return counter

    def get_planet_chain_to_beginning(self, planet):
        chain = []
        while planet.parent != '':
            chain.append(planet.parent)
            planet = self.planets[planet.parent]
        return chain

    def find_path_between_planets(self, starting, destination):
        starting_chain = self.get_planet_chain_to_beginning(starting)
        destination_chain = self.get_planet_chain_to_beginning(destination)
        i = 0
        for planet in starting_chain:
            j = 0
            for planet2 in destination_chain:
                if planet == planet2:
                    return i + j
                j += 1
            i += 1


answers = DaySix()
print("answer for part1 is: ", answers.part_one_result)
print("answer for part2 is: ", answers.part_two_result)
