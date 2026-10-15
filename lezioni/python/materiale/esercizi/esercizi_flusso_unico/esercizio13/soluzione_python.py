import math

# 1. Prima funzione: 4 parametri, doppio ceil e scelta del massimo tra RAM e Disco
def calcola_vps_necessarie(ram_richiesta, disk_richiesto, ram_singola_vps, disk_singola_vps):
    vps_per_ram = math.ceil(ram_richiesta / ram_singola_vps)
    vps_per_disk = math.ceil(disk_richiesto / disk_singola_vps)
    # Si prende il massimo per garantire che entrambe le risorse siano sufficienti
    return max(vps_per_ram, vps_per_disk)

# 2. Seconda funzione: 4 parametri, sconto solo su hardware + costo licenza + IVA
def calcola_costo_progetto(num_vps, prezzo_vps, costo_licenza_vps, percentuale_sconto):
    costo_hardware_scontato = (num_vps * prezzo_vps) * (1 - percentuale_sconto / 100)
    costo_licenze_totale = num_vps * costo_licenza_vps  
    imponibile_totale = costo_hardware_scontato + costo_licenze_totale
    costo_ivato = imponibile_totale * 1.22
    return costo_ivato

# === PROGRAMMA PRINCIPALE ===
print("=== INSERIMENTO SPECIFICHE HOSTING ===")
ram_vps = float(input("Inserisci la RAM fornita da una singola VPS (GB): "))
disk_vps = float(input("Inserisci lo Spazio Disco fornito da una singola VPS (GB): "))
prezzo_vps = float(input("Inserisci il prezzo mensile per VPS (€): "))
licenza_vps = float(input("Inserisci il costo licenza software per VPS (€): "))
sconto_hw = float(input("Inserisci lo sconto hardware (%): "))
ram_ecom, disk_ecom = map(float, input("Inserisci RAM (GB) e Disco (GB) per E-commerce: ").split())
ram_app, disk_app = map(float, input("Inserisci RAM (GB) e Disco (GB) per App Mobile: ").split())
ram_intra, disk_intra = map(float, input("Inserisci RAM (GB) e Disco (GB) per Intranet: ").split())

# Calcolo VPS necessarie
vps_ecom = calcola_vps_necessarie(ram_ecom, disk_ecom, ram_vps, disk_vps)
vps_app = calcola_vps_necessarie(ram_app, disk_app, ram_vps, disk_vps)
vps_intra = calcola_vps_necessarie(ram_intra, disk_intra, ram_vps, disk_vps)

# Calcolo costi
costo_ecom = calcola_costo_progetto(vps_ecom, prezzo_vps, licenza_vps, sconto_hw)
costo_app = calcola_costo_progetto(vps_app, prezzo_vps, licenza_vps, sconto_hw)
costo_intra = calcola_costo_progetto(vps_intra, prezzo_vps, licenza_vps, sconto_hw)

costo_totale = costo_ecom + costo_app + costo_intra

# Stampa Output
print("\n=== PREVENTIVO CLOUD MULTI-RISORSA ===")
print(f"E-commerce: {vps_ecom} VPS necessarie - Costo mensile: {costo_ecom:.2f} €")
print(f"App Mobile: {vps_app} VPS necessarie - Costo mensile: {costo_app:.2f} €")
print(f"Intranet: {vps_intra} VPS necessaria - Costo mensile: {costo_intra:.2f} €")
print("-" * 50)
print(f"Costo totale mensile preventivo (IVA incl.): {costo_totale:.2f} €")