import tkinter as tk
from tkinter import ttk
import mcschematic
from functools import partial

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.buttons = {}
        self.frames = []
        self.schematic = mcschematic.MCSchematic()
        self.title("bxRedstoneDesigner")
        self.blockListbox = ttk.Combobox(self)
        self.blockListbox['values'] = ["none", "wool", "redstone"]
        self.blockListbox['state'] = 'readonly'
        self.blockListbox.current(2)
        self.blockListbox.grid(row=0, column=0, padx=5, pady=5, columnspan=10, sticky="WENS")
        self.layerListbox = ttk.Combobox(self)
        self.layerListbox['values'] = [i+1 for i in range(10)]
        self.layerListbox.current(0)
        self.layerListbox['state'] = 'readonly'
        self.layerListbox.bind('<<ComboboxSelected>>', self.changeLayer)
        self.layerListbox.grid(row=1, column=0, padx=5, pady=5, columnspan=10, sticky="WENS")
        self.fileName = ttk.Entry(self)
        self.fileName.insert(0, "example")
        self.fileName.grid(row=11, column=0, columnspan=10, padx=5, pady=5, sticky="WENS")
        ttk.Button(self, text="Save", command=self.saveSchematic).grid(row=12, column=0, columnspan=10, padx=5, pady=5, sticky="WENS")
        for i in range(10):
            self.frames.append(ttk.Frame(self))
            self.frames[i].grid(row=2, column=0, padx=5, pady=5, columnspan=10, sticky="WENS")
        for y in range(10):
            for x in range(10):
                for z in range(10):
                    button = tk.Button(self.frames[y], text="", height=1, width=2, bd=0, bg='black', activebackground='black', padx=0, pady=0, command=partial(self.setBlock, x, y, z))
                    button.grid(row=x, column=z, pady=1, padx=1)
                    self.buttons["x" + str(x) + "y" + str(y) + "z" + str(z)] = button
        self.frames[0].tkraise()
        
    def setBlock(self, x, y, z):
        self.block = self.blockListbox.get()
        if self.block == "none":
            self.color = "black"
            self.itemId = "minecraft:air"
        elif self.block == "wool":
            self.color = "white"
            self.itemId = "minecraft:white_wool"
        elif self.block == "redstone":
            self.color = "red"
            self.itemId = "minecraft:redstone_wire"
        self.buttons["x" + str(x) + "y" + str(y) + "z" + str(z)].configure(bg=self.color, activebackground=self.color)
        self.schematic.setBlock((x, y, z), self.itemId)

    def changeLayer(self, event):
        layer_num = int(self.layerListbox.get()) - 1
        self.frames[layer_num].tkraise()

    def saveSchematic(self):
        self.schematic.save("schematics", self.fileName.get(), mcschematic.Version.JE_1_16_5) #minecraft version (example: 1.16.5 - "JE_1_16_5", 1.19.2 - "JE_1_19_2")

if __name__ == "__main__":
    App().mainloop()