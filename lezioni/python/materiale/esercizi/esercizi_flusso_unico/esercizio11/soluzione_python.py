import math

distanza = float(input("Inserisci la distanza percorsa (in km): "))
tempo = float(input("Inserisci il tempo impiegato (in minuti): "))
peso = float(input("Inserisci il tuo peso corporeo (in kg): "))

velocita = distanza / (tempo / 60)
passo = tempo / distanza
calorie = 1.03 * peso * distanza
acqua = (tempo / 15) * 150

print("--- REPORT SESSIONE DI CORSA ---")
print(f"Velocità media: {velocita:.1f} km/h")
print(f"Passo medio: {passo:.1f} min/km")
print(f"Calorie stimate bruciate: {calorie:.2f} kcal")
print(f"Acqua raccomandata per il recupero: {math.ceil(acqua)} ml")
print("Numero minimo di bicchieri (200ml) da bere:", math.ceil(acqua / 200))