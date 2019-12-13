class DayOne:
    def __init__(self):
        f = open("input.txt", "r")
        input = f.read()
        self.modules_masses = set(map(lambda x: int(x), input.split('\n')))
        self.fuel = 0

    def part_one(self):
        for module_mass in self.modules_masses:
            # int() will round down the result
            self.fuel += int(module_mass / 3) - 2
        return self.fuel

    def part_two(self):
        for module_mass in self.modules_masses:
            additional_mass = int(module_mass / 3) - 2
            while additional_mass > 0:
                self.fuel += additional_mass
                additional_mass = int(additional_mass / 3) - 2
        return self.fuel


answers = DayOne()
print("answer to part1 is: ", answers.part_one())
answers = DayOne()
print("answer to part2 is: ", answers.part_two())
