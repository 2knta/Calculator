import tkinter as tk
import tkinter.font as tkFont
from functools import partial

WIDTH = 265
HEIGHT = 450
GEOMETRY = "{}x{}".format(WIDTH, HEIGHT)
BACKGROUND_COLOR = "#181717"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator(self)

class Calculator(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config(width=WIDTH, height=HEIGHT, background=BACKGROUND_COLOR)
        self.pack(fill="both", expand="True")

        self.current_number = tk.StringVar()
        self.aux_number = ""
        self.op = ""

        self.create_ui()

    def create_ui(self):
        
        # Display
        opts = {'ipadx': 20, 'ipady': 20, 'sticky': 'nswe', "padx": 5, "pady": 5}
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.display = tk.Label(self, textvariable = self.current_number, font = fontStyle , anchor="e")
        self.display.grid(row=0, column=0, columnspan=4, rowspan=2, **opts)

        # Buttons
        self.btn_C = self.create_button(2, 0, "C")
        self.btn_percentage = self.create_button(2, 1, "%")
        self.btn_R = self.create_button(2, 2, "R")
        self.btn_dvision = self.create_button(2, 3, "/")

        self.btn_7 = self.create_button(3, 0, "7")
        self.btn_8 = self.create_button(3, 1, "8")
        self.btn_9 = self.create_button(3, 2, "9")
        self.btn_multiply = self.create_button(3, 3, "X")

        self.btn_4 = self.create_button(4, 0, "4")
        self.btn_5 = self.create_button(4, 1, "5")
        self.btn_6 = self.create_button(4, 2, "6")
        self.btn_subtract = self.create_button(4, 3, "-")

        self.btn_1 = self.create_button(5, 0, "1")
        self.btn_2 = self.create_button(5, 1, "2")
        self.btn_3 = self.create_button(5, 2, "3")
        self.btn_plus = self.create_button(5, 3, "+")

        self.btn_00 = self.create_button(6, 0, "00")
        self.btn_0 = self.create_button(6, 1, "0")
        self.btn_comma = self.create_button(6, 2, ",")
        self.btn_equal = self.create_button(6, 3, "=")

    def create_button(self, row, column, content):
        opts = {'ipadx': 20, 'ipady': 20, 'sticky': 'nswe', "padx": 5, "pady": 5}
        button = tk.Button(self, text=content)
        button.config(cursor="hand2", background="blue", foreground="white", bd=0)
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
        self.current_number.set(self.current_number.get() + number)
    
    def btn_comma_action(self):
        if "." not in self.current_number.get():
            self.current_number.set(self.current_number.get() + ".")

    def btn_reset(self):
        self.current_number.set("")
        self.aux_number = ""
    
    def btn_remove_one(self):
        if self.current_number != "":
            self.current_number.set(self.current_number.get()[:-1])

    def btn_plus_action(self):
        self.aux_number = self.current_number.get()
        self.current_number.set("")
        self.op = "+"
    
    def btn_action(self, option):
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
            self.current_number.set(float(self.current_number.get()) + float(self.aux_number))
        elif self.op == "-":
            self.current_number.set(float(self.aux_number) - float(self.current_number.get()))
        elif self.op == "X":
            self.current_number.set(float(self.current_number.get()) * float(self.aux_number))
        elif self.op == "/":
            self.current_number.set(float(self.aux_number) / float(self.current_number.get()))

if __name__ == "__main__":
    app = App()
    app.title("Calculator")
    app.geometry(GEOMETRY)
    app.config(background=BACKGROUND_COLOR)
    app.resizable(False, False)
    app.mainloop()