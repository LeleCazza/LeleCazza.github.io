import random

numero_pc = random.randint(1, 3)

if numero_pc == 1:
    pc = "sasso"
elif numero_pc == 2:
    pc = "forbice"
else:
    pc = "carta"

utente = input("sasso, forbice o carta?: ")

if utente != "sasso" and utente != "carta" and utente != "forbice":
    print("Mossa non valida!")
else:
    print(f"Il PC ha scelto: {pc}")
    if utente == pc:
        print("Pareggio!")
    elif (utente == "sasso" and pc == "forbice") or (utente == "forbice" and pc == "carta") or (utente == "carta" and pc == "sasso"):
        print("Hai vinto!")
    else:
        print("Ha vinto il PC!")