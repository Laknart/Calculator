from tkinter import *
import Data_file


def sum_digit(x, y):
    return x + y


def multi_digit(x, y):
    return x * y


def division_digit(x, y):
    return x / y


def minus_digit(x, y):
    return x - y


def is_valid(digit):
    if digit == Data_file.zero_error:
        return True
    try:
        float(digit)
        return True
    except ValueError:
        return False


def equals(x, y, fun):
    return fun(x, y)


def is_float(x):
    if int(x) == float(x):
        return int(x)
    else:
        return float(x)


class View(Tk):
    size_W = Data_file.size_W  # 400
    size_H = Data_file.size_H  # 500
    flag_next = True
    flag_equals = False
    flag_state_equals = True
    number_input = ""
    number_two = ""
    number_free = ""
    fun_sign = ""
    sign = ""
    sign_allowed = ("+", "/", "x", "-")

    def __init__(self):
        super().__init__()
        self.title("Hell")
        self.config(width=self.size_W, height=self.size_H)
        self.resizable(width=False, height=False)
        self.geometry(f"{self.size_W}x{self.size_H}")
        self.protocol("WM_DELETE_WINDOW", self._close)

        self.entry_input = Entry(master=self, justify="right", font=("Arial", 15), validate="key",
                                 validatecommand=(self.register(is_valid), "%S"))

        self.entry_input.grid(row=1, column=0, columnspan=4, sticky="wens")

        self.entry_two = Entry(master=self, justify="right", font=("Arial", 15))
        self.entry_two.grid(row=0, column=0, columnspan=4, sticky="wens")

        self.button_plus = Button(master=self, text="+", bd=3,
                                  command=lambda: self.press_sign(sign="+", fun=sum_digit))
        self.button_plus.grid(row=2, column=3, stick="wens", padx=2, pady=2)
        self.button_CE = Button(master=self, text="CE", bd=3, command=self.del_down_number)
        self.button_CE.grid(row=2, column=0, stick="wens", padx=2, pady=2)
        self.button_C = Button(master=self, text="C", bd=3, command=self.del_all)
        self.button_C.grid(row=2, column=1, stick="wens", padx=2, pady=2)
        self.button_seven = Button(master=self, text="7", bd=3, command=lambda: self.add_digit(7))
        self.button_seven.grid(row=3, column=0, stick="wens", padx=2, pady=2)
        self.button_eight = Button(master=self, text="8", bd=3, command=lambda: self.add_digit(8))
        self.button_eight.grid(row=3, column=1, stick="wens", padx=2, pady=2)
        self.button_nine = Button(master=self, text="9", bd=3, command=lambda: self.add_digit(9))
        self.button_nine.grid(row=3, column=2, stick="wens", padx=2, pady=2)
        self.button_four = Button(master=self, text="4", bd=3, command=lambda: self.add_digit(4))
        self.button_four.grid(row=4, column=0, stick="wens", padx=2, pady=2)
        self.button_fife = Button(master=self, text="5", bd=3, command=lambda: self.add_digit(5))
        self.button_fife.grid(row=4, column=1, stick="wens", padx=2, pady=2)
        self.button_six = Button(master=self, text="6", bd=3, command=lambda: self.add_digit(6))
        self.button_six.grid(row=4, column=2, stick="wens", padx=2, pady=2)
        self.button_one = Button(master=self, text="1", bd=3, command=lambda: self.add_digit(1))
        self.button_one.grid(row=5, column=0, stick="wens", padx=2, pady=2)
        self.button_two = Button(master=self, text="2", bd=3, command=lambda: self.add_digit(2))
        self.button_two.grid(row=5, column=1, stick="wens", padx=2, pady=2)
        self.button_three = Button(master=self, text="3", bd=3, command=lambda: self.add_digit(3))
        self.button_three.grid(row=5, column=2, stick="wens", padx=2, pady=2)
        self.button_DEL = Button(master=self, text="DEL", bd=3, command=self.del_digit)
        self.button_DEL.grid(row=2, column=2, stick="wens", padx=2, pady=2)
        self.button_division = Button(master=self, text="/", bd=3,
                                      command=lambda: self.press_sign(sign="/", fun=division_digit))
        self.button_division.grid(row=3, column=3, stick="wens", padx=2, pady=2)
        self.button_multi = Button(master=self, text="X", bd=3,
                                   command=lambda: self.press_sign(sign="x", fun=multi_digit))
        self.button_multi.grid(row=4, column=3, stick="wens", padx=2, pady=2)
        self.button_minus = Button(master=self, text="-", bd=3,
                                   command=lambda: self.press_sign(sign="-", fun=minus_digit))
        self.button_minus.grid(row=5, column=3, stick="wens", padx=2, pady=2)
        self.button17 = Button(master=self, text="#", bd=3, command=self.print_number)
        self.button17.grid(row=6, column=0, stick="wens", padx=2, pady=2)
        self.button_zero = Button(master=self, text="0", bd=3, command=lambda: self.add_digit(0))
        self.button_zero.grid(row=6, column=1, stick="wens", padx=2, pady=2)
        self.button_comma = Button(master=self, text=",", bd=3)
        self.button_comma.grid(row=6, column=2, stick="wens", padx=2, pady=2)
        self.button_equals = Button(master=self, text="=", bd=3, command=self.equals)
        self.button_equals.grid(row=6, column=3, stick="wens", padx=2, pady=2)

        for i in range(0, 5):
            self.grid_columnconfigure(i, minsize=100)

        self.grid_rowconfigure(0, minsize=50)
        self.grid_rowconfigure(1, minsize=50)

        for i in range(2, 7):
            self.grid_rowconfigure(i, minsize=80)

    def add_digit(self, digit):
        if self.flag_next:
            if self.flag_state_equals:
                if not self.number_input or self.flag_equals:
                    self.entry_input.delete(0, "end")
                    self.flag_equals = False
                value = self.entry_input.get() + str(digit)
                if value[0] != "0":
                    self.entry_input.delete(0, "end")
                    self.entry_input.insert(0, value)
                    self.number_input = self.entry_input.get()
                else:
                    self.entry_input.delete(0, "end")
                    self.entry_input.insert(0, str(digit))
                    self.number_input = str(digit)
            else:
                self.del_all()
                self.flag_state_equals = True
                self.add_digit(digit)

        else:
            self.del_all()
            self.flag_next = True
            self.add_digit(digit)

    def count_number(self, fun, x, y):
        try:
            return str(is_float(fun(float(x), float(y))))
        except ZeroDivisionError:
            self.flag_next = False
            self.entry_input.delete(0, 'end')
            self.entry_input.insert(0, Data_file.zero_error)
            return False

    def _close(self):
        try:
            self.destroy()
            quit()
        except KeyboardInterrupt:
            pass

    def onValidate(self, digit):
        if digit.isdigit():
            return True
        else:
            self.bell()
            return False

    def del_digit(self):
        number = self.entry_input.get()
        if number:
            if not self.entry_two.get():
                self.entry_input.delete(0, "end")
                self.entry_input.insert(0, number[:len(number) - 1])
                self.number_input = self.entry_input.get()
                self.renewal_sign("", "")
            elif self.entry_input.get() and self.entry_two.get() and self.check_tem2(self.entry_two.get()):
                self.entry_two.delete(0, "end")
                self.number_input = ""
                self.number_two = ""

        else:
            self.bell()

    def del_all(self):
        if self.entry_input.get() or self.entry_two.get():
            self.entry_input.delete(0, "end")
            self.entry_two.delete(0, "end")
            self.number_two = ""
            self.number_input = ""
            self.renewal_sign("", "")
        else:
            self.bell()

    def del_down_number(self):
        if self.entry_input.get():
            self.entry_input.delete(0, "end")
            self.number_input = ""
        else:
            self.bell()

    def press_sign(self, sign: str, fun):
        if self.flag_next:
            if self.check_tem2(self.entry_two.get()):
                self.entry_two.delete(0, "end")
                self.entry_two.insert(0, f"{self.entry_input.get()} {sign}")
                self.number_input = self.entry_input.get()
                self.renewal_sign(sign, fun)
            elif not self.entry_input.get() and not self.entry_two.get():
                self.entry_two.insert(0, f"0 {sign}")
                self.number_two = 0
                self.renewal_sign(sign, fun)
            elif self.check_template1(self.entry_two.get()):
                self.entry_two.delete(0, "end")
                self.entry_two.insert(0, f"{self.number_two} {sign}")
                self.renewal_sign(sign, fun)
            elif self.entry_input.get() and not self.entry_two.get():
                self.number_two = self.number_input
                self.entry_two.insert(0, f"{str(self.number_two)} {sign}")
                self.number_input = ""
                self.renewal_sign(sign, fun)
            elif self.entry_input.get() and self.entry_two.get() and self.number_input and not self.flag_equals:
                value = self.count_number(self.fun_sign, self.number_two, self.number_input)
                if not value:
                    return
                self.flag_equals = True
                self.number_two = value
                self.entry_two.delete(0, "end")
                self.entry_two.insert(0, f"{value} {sign}")
                self.renewal_sign(sign, fun)
                self.entry_input.delete(0, "end")
                self.entry_input.insert(0, value)
                self.number_input = ""
        else:
            self.del_all()
            self.flag_next = True
            self.press_sign(sign, fun)

    def renewal_sign(self, sign, fun):
        self.sign = sign
        self.fun_sign = fun

    def print_number(self):
        print(f"number_input = {self.number_input}")
        print(f"number_two = {self.number_two}")

    def equals(self):
        if self.flag_next:
            if not self.entry_two.get() and not self.entry_input.get():
                self.entry_two.insert(0, f"{0} =")
                self.number_two = 0
            elif (self.check_template1(self.entry_two.get()) and self.entry_input.get()
                  and not self.sign in self.sign_allowed):
                self.entry_two.delete(0, "end")
                self.entry_two.insert(0, f"{self.entry_input.get()} =")
                self.number_two = self.entry_input.get()
                self.number_input = ""
            elif self.entry_input.get() and self.entry_two.get() and self.number_input and not self.flag_equals:
                self.equals_count()
                self.flag_state_equals = False
            elif self.entry_input.get() and not self.entry_two.get():
                self.entry_two.insert(0, f"{self.entry_input.get()} =")
                self.number_two = self.entry_input.get()
                self.number_input = ""
            elif not self.number_input and self.entry_input.get() and self.entry_two.get():
                self.number_input = self.number_two
                self.equals_count()
                self.flag_state_equals = False
        else:
            self.del_all()
            self.flag_next = True

    def check_template1(self, value):
        try:
            if value:
                first, second = value.split()
                if is_valid(first) and second in self.sign_allowed or "=":
                    return True
        except ValueError:
            return False
        return False

    def check_tem2(self, value):
        try:
            if value:
                first, second, third, fourth = value.split()
                if is_valid(first) and is_valid(third) and second in self.sign_allowed and fourth == "=":
                    return True
        except ValueError:
            return False
        return False

    def equals_count(self):
        value = self.count_number(self.fun_sign, self.number_two, self.number_input)
        if not value:
            return
        self.entry_two.delete(0, "end")
        self.entry_two.insert(0, f"{self.number_two} {self.sign} {self.number_input} =")

        self.entry_input.delete(0, "end")
        self.entry_input.insert(0, value)
        self.number_two = value

    def main(self):
        try:
            self.mainloop()
        except KeyboardInterrupt:
            pass


def main():
    azu = View()
    azu.main()


if __name__ == '__main__':
    main()
