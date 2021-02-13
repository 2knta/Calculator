import tkinter as tk

WIDTH = 400
HEIGHT = 500
GEOMETRY = "{}x{}".format(WIDTH, HEIGHT)
BACKGROUND_COLOR = "#181717"

class App(tk.Tk):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = App()
    app.title("Calculator")
    app.geometry(GEOMETRY)
    app.config(background=BACKGROUND_COLOR)
    app.resizable(False, False)
    app.mainloop()