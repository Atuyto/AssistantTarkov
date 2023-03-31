import tkinter as tk
import maps, window, menu




def mainProg():
    fnt = window.Fenetre(tk.Tk(), False)
    fenetre = fnt.getRoot()
    #print(getItems("Content/Items.bin"))
    #fenetre.bind("<Down>", lambda e: fenetre.destroy())
    #maps.mapMain(fenetre)
    #maps.test(fenetre)

    menu.mainMenu(fenetre)

    fenetre.mainloop()
    

if __name__ == "__main__":
    mainProg()