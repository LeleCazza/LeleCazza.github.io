import math

distanza = float(input("Inserisci la distanza del viaggio (in km): "))
min = float(input("Inserisci il tempo di guida (in minuti): "))
consumo_medio = float(input("Inserisci il consumo medio (in kWh/100 km): "))

vel = distanza / (min / 60)
tempo_100km = (min / distanza) * 100
energia_totale = (distanza * consumo_medio) / 100
energia_ricarica = math.ceil((min /15) * 4)
sessioni_ricarica = math.ceil(energia_ricarica / 15)

print("\n--- REPORT VIAGGIO AUTO ELETTRICA ---")
print(f"Velocità media: {vel:.1f} km/h")
print(f"Tempo medio per 100 km: {tempo_100km:.1f} min/100 km")
print(f"Energia totale consumata: {energia_totale:.2f} kWh")
print(f"Energia raccomandata da ricaricare: {energia_ricarica} kWh")
print(f"Numero minimo di sessioni (15kWh) da effettuare: {sessioni_ricarica}")