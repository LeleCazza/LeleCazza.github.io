import random

peso_totale = float(input("Inserisci il peso totale della merce (in kg): "))
capacita_furgone = float(input("Inserisci la capacità massima del furgone (in kg): "))
costo_furgone = float(input("Inserisci il costo fisso per furgone (in €): "))
tariffa_al_kg = float(input("Inserisci la tariffa incassata al kg (in €): "))

supplemento = random.randint(5, 15)
furgoni_pieni, merce_rimasta = divmod(int(peso_totale), int(capacita_furgone))

peso_spedito = furgoni_pieni * capacita_furgone
costo_base = furgoni_pieni * costo_furgone
costo_totale = costo_base * (1 + supplemento / 100)
ricavo_lordo = peso_spedito * tariffa_al_kg
profitto_netto = ricavo_lordo - costo_totale
margine_percentuale = round((profitto_netto / costo_totale) * 100, 1)
spesa_minima = min(costo_base, costo_totale)
spesa_massima = max(costo_base, costo_totale)

print("\n--- REPORT LOGISTICA E SPEDIZIONI ---")
print(f"Supplemento carburante/traffico applicato: {supplemento}%")
print(f"Furgoni completi utilizzati: {furgoni_pieni}")
print(f"Merce rimasta in magazzino: {int(merce_rimasta)} kg")
print(f"Peso totale spedito: {int(peso_spedito)} kg")
print(f"Costo base furgoni: {costo_base:.2f} €")
print(f"Costo totale con supplemento: {costo_totale:.2f} €")
print(f"Ricavo lordo spedizioni: {ricavo_lordo:.2f} €")
print(f"Profitto netto: {profitto_netto:.2f} €")
print(f"Margine di profitto %: {margine_percentuale}%")
print(f"Spesa minima stimata (senza supplemento): {spesa_minima:.2f} €")
print(f"Spesa massima stimata (con supplemento): {spesa_massima:.2f} €")