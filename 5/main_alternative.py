import Common.computer as comp

input_path = '.\input.txt'
computer = comp.Computer(input_path, 1)
print("answer for part1 is: ", computer.calculate()[1][-1])
computer = comp.Computer(input_path, 5)
print("answer for part1 is: ", computer.calculate()[1][-1])