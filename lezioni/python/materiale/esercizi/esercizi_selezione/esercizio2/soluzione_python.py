saldo = 500
pin_corretto = "1312"

pin = input("Inserisci il PIN: ")
importo = int(input("Quanto vuoi prelevare? "))

if pin != pin_corretto:
    print("PIN errato. Operazione annullata.")
elif importo <= 0:
    print("Importo non valido.")
elif importo % 10 != 0:
    print("Puoi prelevare solo multipli di 10 €.")
elif importo > saldo:
    print("Saldo insufficiente.")
else:
    saldo -= importo
    print(f"Prelievo effettuato! Saldo residuo: {saldo} €.")
    if saldo < 50:
        print("Attenzione: il tuo saldo è inferiore a 50 €.")