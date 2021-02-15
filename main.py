import tkinter as tk
import tkinter.font as tkFont
from functools import partial

WIDTH = 290
HEIGHT = 480
GEOMETRY = "{}x{}".format(WIDTH, HEIGHT)
BACKGROUND_COLOR = "#181717"
FRAME_OPTS = {"width": WIDTH, "height": HEIGHT, "bg": "black"}
DISPLAY_OPTS = {'ipadx': 20, 'ipady': 20, 'sticky': 'nswe', "padx": 5, "pady": 5}
BUTTONS = {"1": [5, 0], "2": [5, 1], "3": [5, 2],
           "4": [4, 0], "5": [4, 1], "6": [4, 2],
           "7": [3, 0], "8": [3, 1], "9": [3, 2],
           "0": [6, 1], "C": [2, 0], "%": [2, 1],
           "R": [2, 2], "/": [2, 3], "X": [3, 3],
           "-": [4, 3], "+": [5, 3], "00": [6, 0],
           ",": [6, 2], "=": [6, 3]}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator(self)


class Calculator(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.config(**FRAME_OPTS)
        self.pack(fill="both", expand="True")

        self.current_number = tk.StringVar()
        self.aux_number = ""
        self.op = ""

        self.create_ui()

    def create_ui(self):

        # Create Display
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.display = tk.Label(
        self, textvariable=self.current_number, font=fontStyle, anchor="e", bg="black", fg="white", padx=10)
        self.display.grid(row=0, column=0, columnspan=4, rowspan=2, **DISPLAY_OPTS)

        # Create Buttons
        for btn in BUTTONS:
            self.btn = self.create_button(
                BUTTONS[btn][0], BUTTONS[btn][1], btn)

    def create_button(self, row, column, content):
        opts = {'ipadx': 25, 'ipady': 25,
                'sticky': 'nswe', "padx": 2.5, "pady": 2.5}
        button = tk.Button(self, text=content)
        button.config(cursor="hand2", background=BACKGROUND_COLOR,
                      foreground="white", bd=0)
        if content in "00123456789":
            button.config(command=partial(self.btn_number, content))
        elif content == ",":
            button.config(command=self.btn_comma_action)
        elif content == "C":
            button.config(command=self.btn_reset)
        elif content == "R":
            button.config(command=self.btn_remove_one)
        elif content in "+-X/":
            button.config(command=partial(self.btn_action, content))
        elif content == "=":
            button.config(command=self.btn_equal_action)
        button.grid(row=row, column=column, **opts)
        return button

    def btn_number(self, number):
        self.check_error()
        self.current_number.set(self.current_number.get() + number)

    def btn_comma_action(self):
        self.check_error()            
        if "." not in self.current_number.get() and self.current_number.get() != "":
            self.current_number.set(self.current_number.get() + ".")

    def btn_reset(self):
        self.current_number.set("")
        self.aux_number = ""

    def btn_remove_one(self):
        self.check_error()
        if self.current_number != "":
            self.current_number.set(self.current_number.get()[:-1])

    def btn_plus_action(self):
        self.aux_number = self.current_number.get()
        self.current_number.set("")
        self.op = "+"

    def btn_action(self, option):
        self.check_error()
        if self.aux_number != "":
            self.btn_equal_action()
        if option == "+":
            self.aux_number = self.current_number.get()
            self.current_number.set("")
            self.op = "+"
        elif option == "-":
            self.aux_number = self.current_number.get()
            self.current_number.set("")
            self.op = "-"
        elif option == "X":
            self.aux_number = self.current_number.get()
            self.current_number.set("")
            self.op = "X"
        elif option == "/":
            self.aux_number = self.current_number.get()
            self.current_number.set("")
            self.op = "/"

    def btn_equal_action(self):
        if self.op == "+":
            self.current_number.set(
                float(self.current_number.get()) + float(self.aux_number))
        elif self.op == "-":
            self.current_number.set(
                float(self.aux_number) - float(self.current_number.get()))
        elif self.op == "X":
            self.current_number.set(
                float(self.current_number.get()) * float(self.aux_number))
        elif self.op == "/":
            try:
                self.current_number.set(float(self.aux_number) / float(self.current_number.get()))
            except:
                self.current_number.set("Error")

    def check_error(self):
        if self.current_number.get() == "Error":
            self.current_number.set("")


if __name__ == "__main__":
    app = App()
    app.title("Calculator")
    app.geometry(GEOMETRY)
    app.config(background=BACKGROUND_COLOR)
    app.resizable(False, False)
    app.mainloop()
