from math import ceil

# VARIABILI GLOBALI
print("=== INSERIMENTO SPECIFICHE HOSTING ===")
RAM_VPS = float(input("Inserisci la RAM fornita da una singola VPS (GB): "))
DISK_VPS = float(input("Inserisci lo Spazio Disco fornito da una singola VPS (GB): "))
PREZZO = float(input("Inserisci il prezzo mensile per VPS (€): "))
LICENZA = float(input("Inserisci il costo licenza software per VPS (€): "))
SCONTO = float(input("Inserisci lo sconto hardware (%): "))

# FUNZIONI
def calcola_vps_necessarie(ram_richiesta: float, disk_richiesto: float):
    ''' Restituisce il numero di VPS necessarie'''
    vps_per_ram = ceil(ram_richiesta / RAM_VPS)
    vps_per_disk = ceil(disk_richiesto / DISK_VPS)
    return max(vps_per_ram, vps_per_disk)

def calcola_costo(num_vps: int):
    ''' Restituisce il costo totale delle VPS'''
    costo_hw_scontato = (num_vps * PREZZO) * (1 - SCONTO / 100)
    costo_licenze = num_vps * LICENZA
    return (costo_hw_scontato + costo_licenze) * 1.22

ram, disk = map(float, input("Inserisci RAM (GB) e Disco (GB) per E-commerce: ").split())
vps_e = calcola_vps_necessarie(ram, disk)
costo_e = calcola_costo(vps_e)

ram, disk = map(float, input("Inserisci RAM (GB) e Disco (GB) per App Mobile: ").split())
vps_a = calcola_vps_necessarie(ram, disk)
costo_a = calcola_costo(vps_a)

ram, disk = map(float, input("Inserisci RAM (GB) e Disco (GB) per Intranet: ").split())
vps_i = calcola_vps_necessarie(ram, disk)
costo_i = calcola_costo(vps_i)

# OUTPUT
print("\n=== PREVENTIVO CLOUD MULTI-RISORSA ===")
print(f"E-commerce: {vps_e} VPS necessarie - Costo mensile: {costo_e:.2f} €")
print(f"App Mobile: {vps_a} VPS necessarie - Costo mensile: {costo_a:.2f} €")
print(f"Intranet: {vps_i} VPS necessaria - Costo mensile: {costo_i:.2f} €")
print("-" * 50)
print(f"Costo totale mensile preventivo (IVA incl.): {costo_e+costo_a+costo_i:.2f} €")