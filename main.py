import tkinter as tk
from functools import partial

WIDTH = 265
HEIGHT = 427
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
        self.create_ui()

    def create_ui(self):
        
        # Display
        opts = {'ipadx': 20, 'ipady': 20, 'sticky': 'nswe', "padx": 5, "pady": 5}
        self.display = tk.Label(self)
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
        button.grid(row=row, column=column, **opts)
        return button


    def btn_reset(self):
        pass

if __name__ == "__main__":
    app = App()
    app.title("Calculator")
    app.geometry(GEOMETRY)
    app.config(background=BACKGROUND_COLOR)
    app.resizable(False, False)
    app.mainloop()