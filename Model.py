class Model:
    def __init__(self):
        self.number_input = ""
        self.number_two = ""
        self.sign = ""
        self.sign_allowed = ("+", "/", "x", "-")
        self.zero_error = "Деление на ноль невозможно"

    def set_number_input(self, value):
        self.number_input = value

    def set_number_two(self, value):
        self.number_two = value

    def set_sign(self, value):
        self.sign = value

    def get_number_input(self):
        return self.number_input

    def get_number_two(self):
        return self.number_two

    def get_sign(self):
        return self.sign

    def get_sign_allowed(self):
        return self.sign_allowed

    def get_zero_error(self):
        return self.zero_error

    @staticmethod
    def sum_digit(x, y):
        return x + y

    @staticmethod
    def multi_digit(x, y):
        return x * y

    @staticmethod
    def division_digit(x, y):
        return x / y

    @staticmethod
    def minus_digit(x, y):
        return x - y

    def perform_operation(self, sign, x, y):
        x = float(x)
        y = float(y)
        if sign == "+":
            return self.conversion_float(self.sum_digit(x, y))
        elif sign == "-":
            return self.conversion_float(self.minus_digit(x, y))
        elif sign == "x":
            return self.conversion_float(self.multi_digit(x, y))
        elif sign == "/":
            if float(y) == 0:
                return None
            return self.conversion_float(self.division_digit(x,y))
        return None


    @staticmethod
    def conversion_float(x):
        if int(x) == float(x):
            return int(x)
        else:
            return float(x)
