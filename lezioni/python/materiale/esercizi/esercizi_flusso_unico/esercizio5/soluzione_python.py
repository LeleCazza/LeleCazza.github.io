totale_conto = float(input("Inserisci il totale del conto (€): "))
num_persone = int(input("Inserisci il numero di persone: "))
quota = totale_conto / num_persone
print(f"Ogni persona deve pagare: {quota:.2f} €")