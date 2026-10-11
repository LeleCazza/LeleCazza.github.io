import math

importo = float(input("Inserisci l'importo puntato in euro: "))
quota1, quota2 = map(float,(input("Inserisci le quote dei due eventi: ").split()))

quota_finale = quota1 * quota2 * 1.05
vincita = math.floor(importo * quota_finale)
netto = vincita - importo

print("--- RIEPILOGO SCHEDINA ---")
print(f"Quota finale con bonus 5%: {quota_finale:.2f}")
print(f"Vincita arrotondata liquidata: {vincita:.2f}€")
print(f"Profitto netto: {netto:.2f}€")
print(f"Rendimento percentuale netto: {((netto / importo) * 100):.2f}%")