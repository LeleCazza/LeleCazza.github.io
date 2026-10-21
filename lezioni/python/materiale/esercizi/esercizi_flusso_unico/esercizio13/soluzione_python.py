budget = float(input("Inserisci il budget totale (in €): "))
costo = float(input("Inserisci il costo di un pacchetto (in €): "))
ricavo = float(input("Inserisci il ricavo stimato per pacchetto (in €): "))

pacchetti, budget_residuo = divmod(budget, costo)
investimento = pacchetti * costo
totale = pacchetti * ricavo
profitto_netto = totale - investimento
roi = round((profitto_netto / investimento) * 100, 1)
minimo = min(investimento, totale)
massimo = max(investimento, totale)

print("\n--- REPORT ACQUISTO PACCHETTI E RENDIMENTO ---")
print(f"Pacchetti acquistabili: {pacchetti:.0f}")
print(f"Budget residuo non speso: {budget_residuo:.2f} €")
print(f"Investimento effettivo: {investimento:.2f} €")
print(f"Ricavo totale stimato: {totale:.2f} €")
print(f"Profitto netto: {profitto_netto:.2f} €")
print(f"ROI stimato: {roi}%")
print(f"Flusso monetario minimo (spesa): {minimo:.2f} €")
print(f"Flusso monetario massimo (ricavo): {massimo:.2f} €")