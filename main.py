import os

print("                                                                                       ")
print("                                                                                       ")
print("[=================================JEU TEXTUEL POKEMON=================================]")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                  1) Combat Pokémon.                                 |")
print("|                                  2) Capture de Pokémon.                             |")
print("|                                  3) Magasin.                                        |")
print("|                                                                                     |")
print("[=====================================================================================]")
print("                                                                                       ")

while True:
    choix = int(input("                                       Que faire ?"))

    if (choix == 1):
        exec(open("combat.py").read())
    elif (choix == 2):
        exec(open("capture.py").read())
    elif (choix == 3):
        exec(open("objectMagasin.py").read())
    else:
        while (choix > 2):
            print("Veuillez selectionner un choix valide.")
            choix = int(input("                                       Que faire ?"))
            # Revenir au choix de fonctionnalité # A faire