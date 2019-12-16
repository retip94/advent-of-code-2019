import Common.computer as comp

input_path = '.\input.txt'
computer = comp.Computer(input_path)
computer.input(1)
for _ in range(3000):
    computer.intcode.append(0)
print("answer for part1 is: ", computer.calculate()[1])
# 3512778005


computer = comp.Computer(input_path)
computer.input(2)
for _ in range(3000):
    computer.intcode.append(0)
print("answer for part2 is: ", computer.calculate()[1])
# 35920

