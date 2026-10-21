# VARIABILI GLOBALI
print("=== TELEMETRIA FLOTTA LOGISTICA ===")
SECONDI = int(input("Inserisci i secondi trascorsi dalla mezzanotte: "))
SECONDI_IN_UN_GIORNO = 86400
CONSUMO_PER_SECONDO = 0.0025

#FUNZIONI
def converti_secondi(secondi: int):
    '''Converte i secondi in ore (h), minuti (m), secondi (s)'''
    h = secondi // (60*60)
    m = (secondi // 60) % 60
    s = secondi % 60
    return h, m, s

ore, minuti, secondi = converti_secondi(SECONDI)
percentuale = (SECONDI / SECONDI_IN_UN_GIORNO) * 100
sec_rim = SECONDI_IN_UN_GIORNO - SECONDI
ore_r, minuti_r, secondi_r = converti_secondi(sec_rim)
carburante = SECONDI * CONSUMO_PER_SECONDO

#OUTPUT
print("\n" + "=" * 40)
print(" " * 6 + "REPORT COMPUTER DI BORDO")
print("=" * 40)
print(f"Orario attuale:          {ore} h : {minuti} m : {secondi} s")
print(f"Avanzamento giornata:    {percentuale:.2f}%")
print(f"Tempo a fine turno:      {ore_r} h : {minuti_r} m : {secondi_r} s")
print(f"Carburante consumato:    {carburante:.2f} L")
print("=" * 40)