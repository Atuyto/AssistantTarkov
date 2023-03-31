import tkinter as tk
from PIL import Image as img, ImageTk
import os

class Fenetre:
    def __init__(self, root,  fullscreen:bool, fenetreName:str = "Assistant EFT" ) -> None:
        self.fenetre = root
        self.fenetre.lift()
        self.opacity = 1.0
        self.fenetre.geometry("500x500")
        self.name = fenetreName
        self.fenetre.title(self.name)
        self.fenetre.attributes("-topmost", True)
        self.fenetre.attributes("-fullscreen", fullscreen)
        
    
    def getRoot(self):
        return self.fenetre

    def change_opacity(self):
        if self.opacity == 1.0 :
            self.fenetre.attributes("-alpha", 0.0,)
            self.opacity = 0.0
        else:
            self.fenetre.attributes("-alpha", 1.0)
            self.opacity = 1.0

    def closeWindow(self):
        self.fenetre.destroy()

        
        


    def event(self, event):
        match event.keysym :
            case "Up" :
                self.change_opacity()
            case "Down":
                self.closeWindow()


