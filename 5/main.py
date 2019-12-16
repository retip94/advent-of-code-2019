import Common.computer as comp

input_path = '.\input.txt'
computer = comp.Computer(input_path)
computer.input(1)
print("answer for part1 is: ", computer.calculate()[1][-1])
# 16434972
computer = comp.Computer(input_path)
computer.input(5)
print("answer for part1 is: ", computer.calculate()[1][-1])
# 16694270