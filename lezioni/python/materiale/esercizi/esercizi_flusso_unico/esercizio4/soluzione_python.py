nome = str(input("Inserisci il nome del giocatore: "))
livello = int(input("Inserisci il livello: "))
punteggio = float(input("Inserisci il punteggio: "))
is_vip = bool(input("Sei VIP? (Premi Invio per No, digita un carattere qualsiasi per Si): "))

punteggio_finale = punteggio + (livello * 10)

print("\n--- SCHEDA GIOCATORE ---")
print(f"Nome: {nome} | Tipo: {type(nome)}")
print(f"Livello: {livello} | Tipo: {type(livello)}")
print(f"Punteggio: {punteggio} | Tipo: {type(punteggio)}")
print(f"Stato VIP: {is_vip} | Tipo: {type(is_vip)}")
print(f"Punteggio Finale Calcolato: {punteggio_finale}")