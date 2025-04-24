# Start
import os
import random
# Färg
import colorama
from colorama import Fore, Back, Style
import random
colorama.init()

pinkod = str(random.randint(1000, 9999))  # Slumpmässig fyrsiffrig pinkod
filnamn = "Fly_Fron_Fengelset.txt"  # Filnamn på informationen - ("filnamn = r"C:\användare\ditt_namn\mapp\Fly_Fron_Fengelset.txt"")

spelet_körs = True
försök = 5
vakt_eliminerad = False  # Variabel för att spåra om vakten är eliminerad

def huvudmeny():
    global spelet_körs
    fel_försök = 0  # Räknare för felaktiga försök
    while True:
        print(Fore.MAGENTA + "Fly från fängelset")
        print(Fore.GREEN + "1. Starta spelet")
        print(Fore.RED + "2. Avsluta spelet")
        print(Fore.BLUE + "info" + Style.RESET_ALL)

        val = input("Gör ett val: ").lower()

        if val == "1":
            print(Fore.GREEN + "Startar spelet")
            spelet_körs = True
            break  # Gå vidare till spelet
        elif val == "2":
            print(Fore.RED + "Avslutar spelet")
            exit()
        elif val == "info":
            try:
                with open(filnamn, "r", encoding="utf-8") as fil:
                    innehåll = fil.read()
                    print("\n--- INFORMATION ---")
                    print(innehåll)
                    print("-------------------")
            except FileNotFoundError:
                print(Fore.RED + f"Filen '{filnamn}' hittades inte.")
        else:
            fel_försök += 1
            if fel_försök >= 5:
                print(Fore.YELLOW + "Japp, du lyckades skriva något som inte ens fanns som val. Imponerande! Testa 1, 2 eller info.")
                fel_försök = 0  # Återställ räknaren
            else:
                print(Style.RESET_ALL + f"Ogiltigt val, skriv 1, 2 eller info.")

# Anropa huvudmenyn i början av programmet
huvudmeny()
def cell():
    print(Fore.BLUE + "Du är nu i en cell")
    spelarens_val = input(Fore.RESET + "Vill du gå till vaktrummet eller korridoren? (vaktrum/korridor): ").lower()
    if spelarens_val == "vaktrum":
        return "vaktrum"
    elif spelarens_val == "korridor":
        kod_input = input(Fore.YELLOW + "Dörren är låst. Skriv in pinkoden för att låsa upp: ")
        if kod_input == pinkod:
            print(Fore.GREEN + "Koden var rätt! Dörren till korridoren är nu öppen.")
            return "korridor"
        else:
            print(Fore.RED + "Fel kod! Dörren förblir låst.")
            return "cell"
    else:
        print(Fore.RESET + "Ogiltigt val, du stannar i cellen.")
        return "cell"

def vaktrum():
    print(Fore.BLUE + "Du är nu i vaktrummet")
    spelarens_val = input(Fore.RESET + "Du ser en lapp på bordet. Vill du läsa den? (ja/nej): ").lower()
    if spelarens_val == "ja":
        print(Fore.GREEN + f"Du läser lappen och hittar pinkoden: {pinkod}")
    elif spelarens_val == "nej":
        print(Fore.YELLOW + "Du ignorerar lappen och går vidare.")
    else:
        print(Fore.RED + "Ogiltigt val, du stannar i vaktrummet.")
        return "vaktrum"

    spelarens_val = input(Fore.RESET + "Vill du gå till korridoren eller tillbaka till cellen? (korridor/cell): ").lower()
    if spelarens_val == "korridor":
        return "korridor"
    elif spelarens_val == "cell":
        return "cell"
    else:
        print("Ogiltigt val, du stannar i vaktrummet.")
        return "vaktrum"

def korridor(pinkod):
    print(Fore.BLUE + "Du är nu i korridoren")
    kod_input = str(input(Fore.YELLOW + "Dörren är låst. Skriv in pinkoden: "))
    if (kod_input == pinkod):
        print(Fore.GREEN + "Koden var rätt! Du kan fortsätta.")
    else:
        print(Fore.RED + "Fel kod. Du skickas tillbaka till cellen.")
        return "cell"
    spelarens_val = input(Fore.RESET + "Vill du gå till avloppsrummet eller vaktrummet? (avloppsrum/vaktrum): ").lower()
    if spelarens_val == "avloppsrum":
        return "avloppsrum"
    elif spelarens_val == "vaktrum":
        return "vaktrum"
    else:
        print("Ogiltigt val, du stannar i korridoren.")
        return "korridor"

def avloppsrum():
    print(Fore.GREEN + "Du är nu i avloppsrummet")
    spelarens_val = input(Fore.RESET + "Vill du gå tillbaka till korridoren eller fly? (korridor/fly): ").lower()
    if spelarens_val == "korridor":
        return "korridor"
    elif spelarens_val == "fly":
        print(Fore.MAGENTA + "Grattis! Du har flytt fängelset!")
        exit()
    else:
        print("Ogiltigt val, du stannar i avloppsrummet.")
        return "avloppsrum"

# Spelets huvudloop
aktuellt_rum = "cell"
while True:
    if aktuellt_rum == "cell":
        aktuellt_rum = cell()
    elif aktuellt_rum == "vaktrum":
        aktuellt_rum = vaktrum()
    elif aktuellt_rum == "korridor":
        aktuellt_rum = korridor(pinkod)
    elif aktuellt_rum == "avloppsrum":
        aktuellt_rum = avloppsrum()

# Färgstädning
colorama.deinit()
