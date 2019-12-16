import Common.computer as comp
import itertools

input_path = '.\input.txt'
max_amplified_signal = 0
max_phases_settings = []
for phases_settings in itertools.permutations(range(0,5)):
    computer = comp.Computer(input_path)
    signal = 0
    for phase in phases_settings:
        computer.input(phase)
        computer.input(signal)
        signal = computer.calculate()[1][-1]
    if signal>max_amplified_signal:
        max_amplified_signal = signal
        max_phases_settings = phases_settings
print("answer for part1 is: ", max_amplified_signal, max_phases_settings)


# computer = comp.Computer(input_path, 5)
# # print("answer for part1 is: ", computer.calculate()[1][-1])
