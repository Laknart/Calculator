from tkinter import Tk, Entry, Button


class View(Tk):
    size_W = 400
    size_H = 500

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Hell")
        self.geometry(f"{self.size_W}x{self.size_H}")
        self.protocol("WM_DELETE_WINDOW", self.controller.close)
        self.resizable(width=False, height=False)

        self.entry_input = Entry(master=self, justify="right", font=("Arial", 15), validate="key",
                                 validatecommand=(self.register(self.controller.is_valid), "%S"))
        self.entry_input.grid(row=1, column=0, columnspan=4, sticky="wens")
        self.entry_two = Entry(master=self, justify="right", font=("Arial", 15))
        self.entry_two.grid(row=0, column=0, columnspan=4, sticky="wens")
        self.button_plus = self.create_button("+", 2, 3,
                                              lambda: self.controller.press_sign(sign="+"))#,
                                                                                 # fun=self.controller.sum_digit))
        self.button_CE = self.create_button("CE", 2, 0, self.controller.del_down_number)
        self.button_C = self.create_button("C", 2, 1, self.controller.del_all)
        self.button_seven = self.create_button("7", 3, 0, lambda: self.controller.add_digit(7))
        self.button_eight = self.create_button("8", 3, 1, lambda: self.controller.add_digit(8))
        self.button_nine = self.create_button("9", 3, 2, lambda: self.controller.add_digit(9))
        self.button_four = self.create_button("4", 4, 0, lambda: self.controller.add_digit(4))
        self.button_five = self.create_button("5", 4, 1, lambda: self.controller.add_digit(5))
        self.button_six = self.create_button("6", 4, 2, lambda: self.controller.add_digit(6))
        self.button_one = self.create_button("1", 5, 0, lambda: self.controller.add_digit(1))
        self.button_two = self.create_button("2", 5, 1, lambda: self.controller.add_digit(2))
        self.button_three = self.create_button("3", 5, 2, lambda: self.controller.add_digit(3))
        self.button_DEL = self.create_button("DEL", 2, 2, self.controller.del_digit)
        self.button_division = self.create_button("/", 3, 3,
                                                  lambda: self.controller.press_sign(sign="/"))
        self.button_multi = self.create_button("X", 4, 3, lambda: self.controller.press_sign(sign="x"))
        self.button_minus = self.create_button("-", 5, 3, lambda: self.controller.press_sign(sign="-"))

        self.button17 = self.create_button("#", 6, 0, self.controller.print_number)
        self.button_zero = self.create_button("0", 6, 1, lambda: self.controller.add_digit(0))
        self.button_comma = self.create_button(",", 6, 2)
        self.button_equals = self.create_button("=", 6, 3, self.controller.equals)

        for i in range(0, 5):
            self.grid_columnconfigure(i, minsize=100)

        self.grid_rowconfigure(0, minsize=50)
        self.grid_rowconfigure(1, minsize=50)

        for i in range(2, 7):
            self.grid_rowconfigure(i, minsize=80)

    def create_button(self, text, row, column, command=None):
        button = Button(master=self, text=text, bd=3, command=command)
        button.grid(row=row, column=column, stick="wens", padx=2, pady=2)
        return button

    def get_entry_input(self):
        return self.entry_input.get()

    def get_entry_two(self):
        return self.entry_two.get()

    def set_entry_input(self, value):
        self.entry_input.delete(0, "end")
        self.entry_input.insert(0, value)

    def set_entry_two(self, value):
        self.entry_two.delete(0, "end")
        self.entry_two.insert(0, value)

    def main(self):
        self.mainloop()
