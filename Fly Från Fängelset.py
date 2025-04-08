# Start
# Färg
import colorama
from colorama import Fore, Back, Style
import random
colorama.init()

print(Fore.BLUE + "Fly från fängelset")
print(Fore.GREEN + "1. Starta spelet")
print(Fore.RED + "2. Avsluta spelet")

spelet_körs = True
försök = 5
nyckel_hittad = False  # Variabel för att spåra om spelaren har nyckeln
vakt_eliminerad = False  # Variabel för att spåra om vakten är eliminerad

for i in range(försök):
    gör_ett_val = input(Style.RESET_ALL + "Gör ett val: ")
    
    if gör_ett_val == "1":
        print(Fore.GREEN + "Startar spelet")
        spelet_körs = False  # Spelet har redan startat, så while-loopen ska inte köras
        break  # Avslutar loopen och startar spelet
    elif gör_ett_val == "2":
        print(Fore.RED + "Avslutar spelet")
        exit()
    else:
        print(Style.RESET_ALL + "Ogiltigt val, skriv 1 eller 2")
else:
    print(Fore.RED + "Är du dum i huvudet du ska skriva 1 eller 2..." + Style.RESET_ALL)

# Fortsätt med while-loop efter att for-loopen har avslutats, om spelet inte startades
while spelet_körs == True:
    gör_ett_val = input("Gör ett val: ")
    
    if gör_ett_val == "1":
        print(Fore.GREEN + "Startar spelet")
        spelet_körs = False
    elif gör_ett_val == "2":
        print(Fore.RED + "Avslutar spelet")
        exit()
    else:
        print(Style.RESET_ALL + "Ogiltigt val, skriv 1 eller 2")

# Rumfunktioner
def cell():
    print(Fore.BLUE + "Du är nu i en cell")
    spelarens_val = input(Fore.RESET + "Vill du gå till vaktrummet eller korridoren? (vaktrum/korridor): ").lower()
    if spelarens_val == "vaktrum":
        return "vaktrum"
    elif spelarens_val == "korridor":
        if not nyckel_hittad:
            print(Fore.RED + "Dörren till korridoren är låst. Försök hitta!")
            return "cell"
        return "korridor"
    else:
        print(Fore.RESET + "Ogiltigt val, du stannar i cellen.")
        return "cell"

def vaktrum():
    global nyckel_hittad, vakt_eliminerad
    print(Fore.BLUE + "Du är nu i vaktrummet")
    if not nyckel_hittad and not vakt_eliminerad:
        spelarens_val = input(Fore.RESET + "Du ser en nyckel på bordet. Vill du försöka ta den osedd eller attackera vakten? (ta/attackera/nej): ").lower()
        if spelarens_val == "ta":
            if random.random() < 0.8:  # 80% chans att lyckas
                print(Fore.GREEN + "Du tog nyckeln utan att vakten såg!")
                nyckel_hittad = True
            else:
                print(Fore.RED + "Vakten såg dig och kastade ut dig ur vaktrummet!")
                return "cell"
        elif spelarens_val == "attackera":
            if random.random() < 0.5:  # 50% chans att lyckas
                print(Fore.GREEN + "Du övermannade vakten och tog nyckeln!")
                nyckel_hittad = True
                vakt_eliminerad = True
            else:
                print(Fore.RED + "Vakten besegrade dig och du blev inspärrad igen!")
                return "cell"

    spelarens_val = input("Vill du gå till korridoren eller tillbaka till cellen? (korridor/cell): ").lower()
    if spelarens_val == "korridor":
        return "korridor"
    elif spelarens_val == "cell":
        return "cell"
    else:
        print("Ogiltigt val, du stannar i vaktrummet.")
        return "vaktrum"

def korridor():
    print(Fore.BLUE + "Du är nu i korridoren")
    if not nyckel_hittad:
        print(Fore.RED + "Dörren till avloppsrummet är låst. Försök hitta nyckeln i vaktrummet!")
        return "cell"
    spelarens_val = input("Vill du gå till avloppsrummet eller vaktrummet? (avloppsrum/vaktrum): ").lower()
    if spelarens_val == "avloppsrum":
        return "avloppsrum"
    elif spelarens_val == "vaktrum":
        return "vaktrum"
    else:
        print("Ogiltigt val, du stannar i korridoren.")
        return "korridor"

def avloppsrum():
    print(Fore.GREEN + "Du är nu i avloppsrummet")
    spelarens_val = input("Vill du gå tillbaka till korridoren eller fly? (korridor/fly): ").lower()
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
        aktuellt_rum = korridor()
    elif aktuellt_rum == "avloppsrum":
        aktuellt_rum = avloppsrum()

# Färgstädning
colorama.deinit()
