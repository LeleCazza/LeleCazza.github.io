import random, math

# VARIABILI GLOBALI
print("=== TELEMETRIA DRONI ===")
VELOCITA_BASE_KMH = 50
CONSUMO_PER_MINUTO = 0.8

#FUNZIONI
def calcola_velocità(vento: float):
    '''Restituisce la velocità effettiva del drone'''
    return VELOCITA_BASE_KMH - vento

def calcola_durata(distanza:float, velocità: float):
    '''Restituisce il tempo impiegato dal drone in minuti arrotondato per eccesso'''
    return math.ceil((distanza / velocità) * 60)

def calcola_batteria(batteria_iniziale: float, durata_viaggio: int):
    '''Restituisce la batteria consumata dal drone'''
    return batteria_iniziale - (durata_viaggio * CONSUMO_PER_MINUTO)

def stampa_report(distanza: float, velocità_vento: float, batteria_iniziale: float):
    velocità = calcola_velocità(velocità_vento)
    durata = calcola_durata(distanza, velocità)
    batteria = calcola_batteria(batteria_iniziale,durata)
    print("\n" + "=" * 45)
    print(" " * 6 + "REPORT TELEMETRIA DRONE")
    print("=" * 45)
    print(f"Vento contrario rilevato: {velocità_vento:.1f} km/h")
    print(f"Carica batteria iniziale: {batteria_iniziale:.1f}%")
    print(f"Velocità effettiva drone: {velocità:.1f} km/h")
    print(f"Tempo di volo stimato:    {durata} min")
    print(f"Batteria residua stimata: {batteria:.1f}%")
    print("=" * 45 + "\n")

distanza = float(input("Inserisci la distanza del cliente in km: "))
stampa_report(distanza, random.uniform(5.0, 15.0), random.uniform(85.0, 100.0))

distanza = float(input("Inserisci la distanza del cliente in km: "))
stampa_report(distanza, random.uniform(5.0, 15.0), random.uniform(85.0, 100.0))

distanza = float(input("Inserisci la distanza del cliente in km: "))
stampa_report(distanza, random.uniform(5.0, 15.0), random.uniform(85.0, 100.0))