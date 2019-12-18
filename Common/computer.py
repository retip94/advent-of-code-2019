class Computer:
    def __init__(self, input_path):
        self.input_path = input_path
        self.__reset_intcode(input_path)
        for _ in range(0, 10000):
            self.intcode.append(0)
        self.inputs = []
        self.i = 0
        self.relative_base = 0

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

    def calculate(self, debug=False, painting=False):
        outputs = []
        while self.i < len(self.intcode):
            instruction = self.__get_opcode_and_parameters(self.intcode[self.i])
            if debug:
                print(self.i, self.intcode[self.i:self.i+4])
            try:
                arg1 = self.intcode[self.i + 1] if instruction['par1'] == 1 \
                    else self.intcode[self.intcode[self.i + 1]] if instruction['par1'] == 0 \
                    else self.intcode[self.relative_base + self.intcode[self.i + 1]]
                arg2 = self.intcode[self.i + 2] if instruction['par2'] == 1 \
                    else self.intcode[self.intcode[self.i + 2]] if instruction['par2'] == 0 \
                    else self.intcode[self.relative_base + self.intcode[self.i + 2]]
                arg3 = self.intcode[self.i + 3] if instruction['par3'] == 0 \
                    else self.relative_base + self.intcode[self.i + 3]
            except IndexError:
                pass
            if instruction['opcode'] == 99:
                if painting:
                    return None
                return self.intcode, outputs
            elif instruction['opcode'] in [1, 2, 7, 8]:
                self.i += 4
                if instruction['opcode'] == 1:
                    self.intcode[arg3] = arg1 + arg2
                    if debug:
                        print('Changing {} address to {}+{}'.format(arg3, arg1, arg2))
                elif instruction['opcode'] == 2:
                    self.intcode[arg3] = arg1 * arg2
                    if debug:
                        print('Changing {} address to {}*{}'.format(arg3, arg1, arg2))
                elif instruction['opcode'] == 7:
                    self.intcode[arg3] = 1 if arg1 < arg2 else 0
                    if debug:
                        print('Changing {} address to 1 if {}<{} else to 0'.format(arg3, arg1, arg2))
                elif instruction['opcode'] == 8:
                    self.intcode[arg3] = 1 if arg1 == arg2 else 0
                    if debug:
                        print('Changing {} address to 1 if {}=={} else to 0'.format(arg3, arg1, arg2))
            elif instruction['opcode'] == 3:
                arg1 = self.intcode[self.i + 1] if instruction['par1'] == 0 \
                    else self.relative_base + self.intcode[self.i + 1]
                self.i += 2
                try:
                    self.intcode[arg1] = self.inputs.pop(0)
                    if debug:
                        print('Changing {} address to input'.format(arg1))
                except IndexError:
                    print("INDEX ERROR")
                    break
            elif instruction['opcode'] == 4:
                self.i += 2
                outputs.append(arg1)
                # return self.intcode, arg1
                if len(outputs) == 2 and painting:
                    return outputs
            elif instruction['opcode'] in [5, 6]:
                if instruction['opcode'] == 5:
                    if arg1 != 0:
                        self.i = arg2
                        if debug:
                            print('Changing position to {}'.format(arg2))
                    else:
                        if debug:
                            print('Changing position to {}'.format(self.i))
                        self.i += 3
                if instruction['opcode'] == 6:
                    if arg1 == 0:
                        self.i = arg2
                        if debug:
                            print('Changing position to {}'.format(arg2))
                    else:
                        if debug:
                            print('Changing position to {}'.format(self.i))
                        self.i += 3
            elif instruction['opcode'] == 9:
                self.i += 2
                self.relative_base += arg1
                if debug:
                    print('Changing relative_base to {}'.format(self.relative_base))
            else:
                print("WRONG opcode")
                return None

    def find_starting_values_for_result(self, result):
        for i in range(0, 100):
            for j in range(0, 100):
                self.__reset_intcode(self.input_path)
                self.set_starting_values(i, j)
                if result == self.calculate()[0][0]:
                    return 100 * i + j
