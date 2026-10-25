from math import sqrt, fabs, ceil, floor
from time import sleep
from random import randint

print("=== SISTEMA PRENOTAZIONI PARCO AVVENTURA ===")
x1, y1, x2, y2 = map(float, input("Inserisci le coordinate x1 y1 x2 y2 della mappa: ").split())
g, m, a = map(int, input("Inserisci la data odierna nel formato (gg/mm/aaaa): ").split("/"))
budget_utente = float(input("Inserisci il tuo budget a disposizione (€): "))
numero_partecipanti = int(input("Inserisci il numero di partecipanti: "))

dx = fabs(x2 - x1)
dy = fabs(y2 - y1)
distanza = sqrt(dx**2 + dy**2)
tempo_stimato = ceil(distanza * 2.5)
punti_bonus = floor(distanza / 3)
sconto_promozionale = randint(5, 20)
prezzo_biglietto = 18.50
costo_lordo = numero_partecipanti * prezzo_biglietto
costo_scontato = costo_lordo * (1 - sconto_promozionale / 100)
gruppi_completi, partecipanti_sfusi = divmod(numero_partecipanti, 4)
spesa_minima = min(budget_utente, costo_scontato)
spesa_massima = max(budget_utente, costo_scontato)
costo_finale = round(costo_scontato, 2)

print("\nCalcolo del percorso e verifica disponibilità in corso...", end=" ", flush=True)
sleep(2)
print("Completato!\n")
print("--- RIEPILOGO BIGLIETTO E TICKET ---")
print(f"Data di emissione: {g}", m, a, sep="-")
print(f"Distanza percorso calcolata: {distanza:.2f} km")
print(f"Tempo stimato per il percorso: {tempo_stimato} minuti")
print(f"Punti bonus accumulati: {punti_bonus}")
print(f"Sconto casuale applicato: {sconto_promozionale}%")
print(f"Gruppi da 4 completi: {gruppi_completi} (Partecipanti singoli: {partecipanti_sfusi})")
print(f"Costo totale calcolato: {costo_finale:.2f} €")
print(f"Confronto tra Budget e Spesa (Min / Max): {spesa_minima:.2f} € / {spesa_massima:.2f} €")