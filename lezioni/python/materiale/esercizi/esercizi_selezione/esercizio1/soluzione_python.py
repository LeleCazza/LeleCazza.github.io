eta = int(input("Inserisci la tua età: "))
giorno = input("Inserisci il giorno della settimana: ")

if eta < 0:
    print("Età non valida")
else:
    if eta < 12:
        prezzo = 5
    elif eta <= 25:
        prezzo = 7
    elif eta <= 64:
        prezzo = 10
    else:
        prezzo = 6

    if giorno == "mercoledì":
        prezzo -= 2
    print(f"Il costo totale del biglietto è di {prezzo} €.")