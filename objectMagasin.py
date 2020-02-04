import sys
import time


def delay_print(s):
    # Affiche petit à petit un élément
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class ObjectMagasin():

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def vente(self):
        print("")

if __name__ == '__main__':
    #Objets
    Pokeball = ObjectMagasin("Pokeball",250)
    Superball = ObjectMagasin("Superball",600)
    Hyperball = ObjectMagasin("Hyperball",1000)

    ObjectList = [Pokeball,Superball,Hyperball] # Insert à Rendre automatique
    print("[================================= MAGASIN =================================]")

    for element in range(len(ObjectList)):
        i = 1 # A modifier en str
        ObjectList.append(element)
        # Ajout de ligne dynamique
        print(f"                             {str(i)}) {ObjectList[element].name} : {ObjectList[element].price} $                           ")
        i=int(i)+1
    print("                                                                                       ")
    print("                               ESC pour quitter ")
    print("[===========================================================================]")

    choix = int(input("                           Que voulez-vous acheter ?"))
    # Si ESC, quitter
    # Gérer inventaire