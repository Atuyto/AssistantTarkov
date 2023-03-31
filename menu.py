import tkinter as tk
from PIL import Image as img, ImageTk
import os, window, on_back_press, maps

class Menu :
    def __init__(self, root) -> None:
        self.textMenu = "Playing assistant"
        self.button_map = tk.Button(root, text="map")
        self.button_items = tk.Button(root, text="Items")

    def showButon(self):
        self.button_map.pack()
        self.button_items.pack()

    def getButton(self):
        return self.button_map

def mainMenu(root):
    fnt = window.Fenetre(root, False, "Menu")
    f = fnt.getRoot()

    menu = Menu(f)

    menu.showButon()

    f.mainloop()

