import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bxRedstoneDesigner")

if __name__ == "__main__":
    App().mainloop()