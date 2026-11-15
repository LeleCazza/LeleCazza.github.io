import random

scelta = input("Scegli pari o dispari: ")
numero_utente = int(input("Inserisci un numero intero da 1 a 5: "))

if scelta != "pari" and scelta != "dispari":
    print("Scelta non valida! Devi scrivere 'pari' o 'dispari'.")
elif numero_utente < 1 or numero_utente > 5:
    print("Numero non valido! Inserisci un numero da 1 a 5.")
else:
    numero_pc = random.randint(1, 5)
    somma = numero_utente + numero_pc

    print(f"Il PC ha scelto: {numero_pc}")
    print(f"La somma è {somma}.")

    if somma % 2 == 0 and scelta == "pari":
        print("È uscito pari: hai vinto!")
    elif somma % 2 != 0 and scelta == "dispari":
        print("È uscito dispari: hai vinto!")
    else:
        print("Ha vinto il PC!")