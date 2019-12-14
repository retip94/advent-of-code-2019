class Password:
    def __init__(self, password):
        self.password = str(password)

    def is_valid_for_part_one(self):
        if not self.__check_if_is_six_digits():
            return False
        if not self.__has_at_least_two_same_adjacent_digits():
            return False
        if not self.__never_decrease():
            return False
        return True

    def is_valid_for_part_two(self):
        if not self.__check_if_is_six_digits():
            return False
        if not self.__has_two_same_adjacent_digits():
            return False
        if not self.__never_decrease():
            return False
        return True

    def __check_if_is_six_digits(self):
        return len(self.password) == 6

    def __has_at_least_two_same_adjacent_digits(self):
        for i in range(0, len(self.password) - 1):
            if self.password[i] == self.password[i + 1]:
                return True
        return False

    def __never_decrease(self):
        for i in range(1, len(self.password)):
            if self.password[i] < self.password[i - 1]:
                return False
        return True

    def __has_two_same_adjacent_digits(self):
        for i in range(0, len(self.password) - 1):
            if self.password[i] == self.password[i + 1]:
                try:
                    if self.password[i] != self.password[i + 2]:
                        try:
                            if self.password[i] != self.password[i - 1]:
                                return True
                        except IndexError:
                            return True
                except IndexError:
                    try:
                        if self.password[i] != self.password[i - 1]:
                            return True
                    except IndexError:
                        return True
        return False


class DayFour:
    def __init__(self):
        f = open("input.txt", "r")
        self.starting, self.ending = f.read().split('-')

    def find_number_of_valid_passwords_for_part_one(self):
        count = 0
        for password in range(int(self.starting), int(self.ending)):
            password = Password(password)
            if password.is_valid_for_part_one():
                count += 1
        return count

    def find_number_of_valid_passwords_for_part_two(self):
        count = 0
        for password in range(int(self.starting), int(self.ending)):
            password = Password(password)
            if password.is_valid_for_part_two():
                count += 1
        return count


answers = DayFour()
print("answer for part1 is: ", answers.find_number_of_valid_passwords_for_part_one())
print("answer for part2 is: ", answers.find_number_of_valid_passwords_for_part_two())
