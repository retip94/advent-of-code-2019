class DayTwo:
    def __init__(self):
        self.reset_input()
        self.set_starting_values(12, 2)

    def reset_input(self):
        f = open("input.txt", "r")
        intcode_input = f.read()
        self.intcode = list(map(lambda x: int(x), intcode_input.split(',')))

    def set_starting_values(self, address1, address2):
        self.intcode[1] = address1
        self.intcode[2] = address2

    def calculate(self):
        i = 0
        while i < len(self.intcode):
            opcode = self.intcode[i]
            if opcode == 99:
                break
            elif opcode == 1:
                self.intcode[self.intcode[i + 3]] = self.intcode[self.intcode[i + 1]] + self.intcode[
                    self.intcode[i + 2]]
            elif opcode == 2:
                self.intcode[self.intcode[i + 3]] = self.intcode[self.intcode[i + 1]] * self.intcode[
                    self.intcode[i + 2]]
            i += 4
        return self.intcode[0]

    def find_starting_values_for_result(self, result):
        for i in range(0, 100):
            for j in range(0, 100):
                self.reset_input()
                self.set_starting_values(i, j)
                if result == self.calculate():
                    print(i,j)
                    return 100*i+j


answers = DayTwo()
print("answer to part1 is: ", answers.calculate())
# 5098658
print("answer to part2 is: ", answers.find_starting_values_for_result(19690720))
# 5064
