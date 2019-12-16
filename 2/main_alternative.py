import Common.computer as comp

input_path = './input.txt'
computer = comp.Computer(input_path, 0)
computer.set_starting_values(12, 2)
print("answer for part1 is: ", computer.calculate()[0][0])
# 5098658
print("answer to part2 is: ", computer.find_starting_values_for_result(19690720))
# 5064
