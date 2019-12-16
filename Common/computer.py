class Computer:
    def __init__(self, input_path):
        self.input_path = input_path
        self.__reset_intcode(input_path)
        self.inputs = []

    def input(self, value):
        if isinstance(value, list):
            for v in value:
                self.inputs.append(v)
        else:
            self.inputs.append(value)

    def reset_input(self):
        self.inputs = []

    def __reset_intcode(self, input_path):
        f = open(input_path, "r")
        intcode_input = f.read()
        self.intcode = list(map(lambda x: int(x), intcode_input.split(',')))

    def __get_opcode_and_parameters(self, code):
        opcode = code % 100
        par1 = int((code / 100) % 10)
        par2 = int((code / 1000) % 10)
        par3 = int((code / 10000) % 10)
        return {'opcode': opcode, 'par1': par1, 'par2': par2, 'par3': par3}

    def set_starting_values(self, address1, address2):
        self.intcode[1] = address1
        self.intcode[2] = address2

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
                    try:
                        self.intcode[target] = self.inputs.pop(0)
                    except IndexError:
                        print("INDEX ERROR")
                        break
                else:
                    outputs.append(self.intcode[target])
                    # return self.intcode, [self.intcode[target]]

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

    def find_starting_values_for_result(self, result):
        for i in range(0, 100):
            for j in range(0, 100):
                self.__reset_intcode(self.input_path)
                self.set_starting_values(i, j)
                if result == self.calculate()[0][0]:
                    return 100 * i + j
