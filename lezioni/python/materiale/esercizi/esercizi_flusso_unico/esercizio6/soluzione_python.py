from time import sleep
giorno = int(input("Inserisci il giorno di emissione: "))
mese = int(input("Inserisci il mese di emissione: "))
anno = int(input("Inserisci l'anno di emissione: "))
print(f"Data di emissione: {giorno}", mese, anno, sep='-')
print("Verifica biglietto in corso...", end=" ", flush=True)
sleep(3)
print("Confermato!")