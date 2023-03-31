class Back_press :
    """
    Cette classe permet de vérifier si une touche est appuyer
    """
    def __init__(self) -> None: # j'initialise a rien
        self.keyPress = ""

    def call_back(self, event): # j'ajoute la touche de l'evenement
        self.keyPress = event.keysym


    def isPress(self, key, fenetre)-> bool:
        """
        je regarde si la touche est égale a celle qui est passé en paramètre et je renvoie vrai ou faux
        """
        fenetre.bind("<Key>", self.call_back )
        if self.keyPress == key:
            return True
        else :
            return False
    