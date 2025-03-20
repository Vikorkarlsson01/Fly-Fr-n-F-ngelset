# Start
# Färg
import colorama
from colorama import Fore, Back, Style
colorama.init()



print("fly från fängelset")
print("1. Starta spelet")
print("2. Avsluta spelet")

spelet_körs = True

while (spelet_körs == True):
    gör_ett_val = input("Gör ett val ")
    if (gör_ett_val == "1"):
        print("Statar spelet")
        spelet_körs = False
    elif (gör_ett_val == "2"):
        print("Avsluta spelet")
        exit()
    else:
        print("Ogiltigt val skriv 1 eller 2")


'''
elif (meny_val == "3"):
    print("\n")
    # Filens namn
    filnamn = "readme.txt"

    try:
        # Öppna filen i läsläge
        with open(filnamn, "r". encoding="utf-8") as fil:
        # Läs innehållet i konsolen
        print(innehåll)
        
'''