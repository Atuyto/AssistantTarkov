import tkinter as tk
from PIL import Image as img, ImageTk
import os, window, on_back_press


class Image:
    def __init__(self, collection:list, cur, fenetre ) -> None:
        self.imageList = collection
        self.curent = cur
        self.photoImage = ImageTk.PhotoImage(master = fenetre, file = self.imageList[self.curent][0])
        self.name = self.imageList[self.curent][1]
        self.limite = len(self.imageList)
        

    def showsImage(self, fenetre):
        """
        cette methode permet d'ajouter le label image sur la afenetre
        """
        self.label = tk.Label(fenetre, image = self.photoImage)
        self.label.pack()

    def event(self, even):
        """
        Cette methode permet de récupérer les evenement clavier flèche droite ou gauche pour changer d'image
        """
        if self.curent+1 > self.limite-1 or self.curent < -self.limite+1:
            self.curent = 0
        if even.keysym == "Right":
            self.curent += 1
        if even.keysym == "Left":
            self.curent -= 1
    
    def getCurent(self):
        """
        Je renvoie l'image qui est actuellement afficher
        """
        return self.curent
            
    def cancelLabel(self):
        """
        Je supprime le label sur le quel l'image est attaché
        """
        self.label.destroy()


def getMap(path:str):
    """
    Je viens récuper chacune des images qui ce trouve dans le répertoire MAP et je stocke le chemin et le nom du fichier sans l'extension
    """
    mapList = []
    image = os.listdir(path)
    for m in image :
        mapList.append((f"{path}/{m}", m.rsplit('.', 1)[0]))
    return mapList
    



def mapMain(root) :
    fnt = window.Fenetre(tk.Toplevel(root, takefocus=True), True, 'test')
    fenetre = fnt.getRoot()
    keyboard = on_back_press.Back_press()
    listMap = getMap("Content/MAP") 
    fenetre.focus_force()
    cur = 0   
    images = Image(listMap, cur, fenetre)
    images.showsImage(fenetre)
    quit = False
    while not quit: 
        fenetre.bind("<Up>", fnt.event)
        fenetre.bind("<Right>", images.event)
        fenetre.bind("<Left>", images.event)
        if (keyboard.isPress("Down", fenetre)):
            quit = True
            fenetre.destroy()
        if images.getCurent() != cur :
            images.cancelLabel()
            cur = images.getCurent()
            images = Image(listMap, cur, fenetre )
            images.showsImage(fenetre)

        fenetre.update()
    

    
    

