from View import View
from Model import Model


class Controller:
    flag_next = True
    flag_equals = False
    flag_state_equals = True

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def close(self):
        try:
            self.view.destroy()
            quit()
        except KeyboardInterrupt:
            pass

    def add_digit(self, digit):
        if self.flag_next:
            if self.flag_state_equals:
                if not self.model.get_number_input() or self.flag_equals:
                    self.view.set_entry_input("")
                    self.flag_equals = False
                value = self.view.get_entry_input() + str(digit)
                if value[0] != "0":
                    self.view.set_entry_input(value)
                    self.model.set_number_input(self.view.get_entry_input())
                else:
                    self.view.set_entry_input(digit)
                    self.model.set_number_input(str(digit))
            else:
                self.del_all()
                self.flag_state_equals = True
                self.add_digit(digit)

        else:
            self.del_all()
            self.flag_next = True
            self.add_digit(digit)

    def count_number(self, sign, x, y):
        value = self.model.perform_operation(sign, x, y)
        if value:
            return value
        else:
            self.flag_next = False
            self.view.set_entry_input(self.model.get_zero_error())
            return False

    def onValidate(self, digit):
        if digit.isdigit():
            return True
        else:
            self.view.bell()
            return False

    def del_digit(self):
        number = self.view.get_entry_input()
        if number:
            if not self.view.get_entry_two():
                self.view.set_entry_input(number[:len(number) - 1])
                self.model.set_number_input(self.view.get_entry_input())
                self.renewal_sign("")
            elif self.view.get_entry_input() and self.view.get_entry_two() and self.check_tem2(
                    self.view.get_entry_two()):
                self.view.set_entry_two("")
                self.model.set_number_input("")
                self.model.set_number_two("")

        else:
            self.view.bell()

    def del_all(self):
        if self.view.get_entry_input() or self.view.get_entry_two():
            self.view.set_entry_input("")
            self.view.set_entry_two("")
            self.model.set_number_two("")
            self.model.set_number_input("")
            self.renewal_sign("")
        else:
            self.view.bell()

    def del_down_number(self):
        if self.view.get_entry_input():
            self.view.set_entry_input("")
            self.model.set_number_input("")
        else:
            self.view.bell()

    def press_sign(self, sign: str):
        if not self.flag_next:
            self.del_all()
            self.flag_next = True

        if self.check_tem2(self.view.get_entry_two()):
            self.performing_operation_equals(sign)
        elif self.are_inputs_empty():
            self.first_execution_operation(sign)
        elif self.check_template1(self.view.get_entry_two()) and not self.model.get_number_input():
            self.change_sign_empty_line(sign)
        elif self.view.get_entry_input() and not self.view.get_entry_two():
            self.start_new_operation_with_input(sign)
        elif self.view.get_entry_input() and self.view.get_entry_two() and self.model.get_number_input() and not self.flag_equals:
            self.calculate_and_set_result(sign)

    def performing_operation_equals(self, sign):
        self.view.set_entry_two(f"{self.view.get_entry_input()} {sign}")
        self.model.set_number_input(self.view.get_entry_input())
        self.renewal_sign(sign)

    def first_execution_operation(self, sign):
        self.view.set_entry_two(f"0 {sign}")
        self.model.set_number_two(0)
        self.renewal_sign(sign)

    def change_sign_empty_line(self, sign):
        self.view.set_entry_two(f"{self.model.get_number_two()} {sign}")
        self.renewal_sign(sign)

    def start_new_operation_with_input(self, sign):
        self.model.set_number_two(self.model.get_number_input())
        self.view.set_entry_two(f"{str(self.model.get_number_two())} {sign}")
        self.model.set_number_input("")
        self.renewal_sign(sign)

    def calculate_and_set_result(self, sign):
        value = self.count_number(self.model.get_sign(), self.model.get_number_two(),
                                  self.model.get_number_input())
        if not value:
            return
        self.flag_equals = True
        self.model.set_number_two(value)
        self.view.set_entry_two(f"{value} {sign}")
        self.renewal_sign(sign)
        self.view.set_entry_input(value)
        self.model.set_number_input("")

    def renewal_sign(self, sign):
        self.model.set_sign(sign)
        #self.model.set_fun_sign(fun)

    def print_number(self):
        print(f"number_input = {self.model.get_number_input()}")
        print(f"number_two = {self.model.get_number_two()}")

    def are_inputs_empty(self):
        return not self.view.get_entry_input() and not self.view.get_entry_two()

    def equals(self):
        if not self.flag_next:
            self.del_all()
            self.flag_next = True

        if self.are_inputs_empty():
            self.view.set_entry_two(f"{0} =")
            self.model.set_number_two(0)
        elif (self.check_template1(self.view.get_entry_two()) and self.view.get_entry_input()
              and not self.model.get_sign() in self.model.get_sign_allowed()):
            self.view.set_entry_two(f"{self.view.get_entry_input()} =")
            self.model.set_number_two(self.view.get_entry_input())
            self.model.set_number_input("")
        elif not self.are_inputs_empty() and self.model.get_number_input() and not self.flag_equals:
            self.equals_count()
            self.flag_state_equals = False
        elif self.view.get_entry_input() and not self.view.get_entry_two():
            self.view.set_entry_two(f"{self.view.get_entry_input()} =")
            self.model.set_number_two(self.view.get_entry_input())
            self.model.set_number_input("")
        elif not self.model.get_number_input() and self.view.get_entry_input() and self.view.get_entry_two():
            self.model.set_number_input(self.model.get_number_two())
            self.equals_count()
            self.flag_state_equals = False


    def check_template1(self, value):
        try:
            if value:
                first, second = value.split()
                if self.is_valid(first) and second in self.model.get_sign_allowed() or "=":
                    return True
        except ValueError:
            return False
        return False

    def check_tem2(self, value):
        try:
            if value:
                first, second, third, fourth = value.split()
                if self.is_valid(first) and self.is_valid(
                        third) and second in self.model.get_sign_allowed() and fourth == "=":
                    return True
        except ValueError:
            return False
        return False

    def equals_count(self):
        value = self.count_number(self.model.get_sign(), self.model.get_number_two(), self.model.get_number_input())
        if not value:
            return
        self.view.set_entry_two(
            f"{self.model.get_number_two()} {self.model.get_sign()} {self.model.get_number_input()} =")
        self.view.set_entry_input(value)
        self.model.set_number_two(value)

    def is_valid(self, digit):
        if digit == self.model.get_zero_error():
            return True
        try:
            float(digit)
            return True
        except ValueError:
            return False

