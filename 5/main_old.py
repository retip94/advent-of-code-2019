class DayFive:
    def __init__(self, input_value):
        self.__reset_input()
        self.input_value = input_value
        self.output_value = input_value

    def __reset_input(self):
        f = open("input.txt", "r")
        intcode_input = f.read()
        self.intcode = list(map(lambda x: int(x), intcode_input.split(',')))

    def __get_opcode_and_parameters(self, code):
        opcode = code % 100
        par1 = int((code / 100) % 10)
        par2 = int((code / 1000) % 10)
        par3 = int((code / 10000) % 10)
        return {'opcode': opcode, 'par1': par1, 'par2': par2, 'par3': par3}

    def calculate(self):
        outputs = []
        i = 0
        while i < len(self.intcode):
            instruction = self.__get_opcode_and_parameters(self.intcode[i])
            if instruction['opcode'] == 99:
                break

            elif instruction['opcode'] in [1, 2, 7, 8]:
                arg1 = self.intcode[i + 1] if instruction['par1'] else self.intcode[self.intcode[i + 1]]
                arg2 = self.intcode[i + 2] if instruction['par2'] else self.intcode[self.intcode[i + 2]]
                target = self.intcode[i + 3]
                i += 4
                if instruction['opcode'] == 1:
                    self.intcode[target] = arg1 + arg2
                elif instruction['opcode'] == 2:
                    self.intcode[target] = arg1 * arg2
                elif instruction['opcode'] == 7:
                    self.intcode[target] = 1 if arg1 < arg2 else 0
                elif instruction['opcode'] == 8:
                    self.intcode[target] = 1 if arg1 == arg2 else 0
            elif instruction['opcode'] in [3, 4]:
                target = self.intcode[i + 1]
                i += 2
                if instruction['opcode'] == 3:
                    self.intcode[target] = self.input_value
                else:
                    outputs.append(self.intcode[target])
            elif instruction['opcode'] in [5, 6]:
                arg1 = self.intcode[i + 1] if instruction['par1'] else self.intcode[self.intcode[i + 1]]
                target = self.intcode[i + 2] if instruction['par2'] else self.intcode[self.intcode[i + 2]]
                if instruction['opcode'] == 5:
                    if arg1 != 0:
                        i = target
                    else:
                        i += 3
                if instruction['opcode'] == 6:
                    if arg1 == 0:
                        i = target
                    else:
                        i += 3
            else:
                break
        return self.intcode, outputs


answers = DayFive(1)
print("answer for part1 is: ", answers.calculate()[1][-1])

answers = DayFive(5)
print("answer for part1 is: ", answers.calculate()[1][-1])
