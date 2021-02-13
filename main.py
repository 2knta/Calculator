import tkinter as tk
from functools import partial

WIDTH = 265
HEIGHT = 427
GEOMETRY = "{}x{}".format(WIDTH, HEIGHT)
BACKGROUND_COLOR = "#181717"
BUTTONS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


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
        opts = {'ipadx': 20, 'ipady': 20, 'sticky': 'nswe', "padx": 5, "pady": 5}

        self.display = tk.Label(self)
        self.display.grid(row=0, column=0, columnspan=4, rowspan=2, **opts)

        self.button = tk.Button(self, text="C", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=2, column=0, **opts)

        self.button = tk.Button(self, text="%", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=2, column=1, **opts)

        self.button = tk.Button(self, text="R", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=2, column=2, **opts)

        self.button = tk.Button(self, text="/", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=2, column=3, **opts)
        # ----------------------------
        self.button = tk.Button(self, text="7", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=3, column=0, **opts)

        self.button = tk.Button(self, text="8", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=3, column=1, **opts)

        self.button = tk.Button(self, text="9", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=3, column=2, **opts)

        self.button = tk.Button(self, text="X", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=3, column=3, **opts)
        # ----------------------------
        self.button = tk.Button(self, text="4", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=4, column=0, **opts)

        self.button = tk.Button(self, text="5", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=4, column=1, **opts)

        self.button = tk.Button(self, text="6", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=4, column=2, **opts)

        self.button = tk.Button(self, text="-", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=4, column=3, **opts)
        # ----------------------------
        self.button = tk.Button(self, text="1", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=5, column=0, **opts)

        self.button = tk.Button(self, text="2", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=5, column=1, **opts)

        self.button = tk.Button(self, text="3", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=5, column=2, **opts)

        self.button = tk.Button(self, text="+", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=5, column=3, **opts)
        #----------------------------------
        self.button = tk.Button(self, text="00", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=6, column=0, **opts)

        self.button = tk.Button(self, text="0", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=6, column=1, **opts)

        self.button = tk.Button(self, text=",", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=6, column=2, **opts)

        self.button = tk.Button(self, text="=", command=self.btn_reset)
        self.button.config(cursor="hand2", background="blue", foreground="white", bd=0)
        self.button.grid(row=6, column=3, **opts)

    def btn_reset(self):
        pass

if __name__ == "__main__":
    app = App()
    app.title("Calculator")
    app.geometry(GEOMETRY)
    app.config(background=BACKGROUND_COLOR)
    app.resizable(False, False)
    app.mainloop()