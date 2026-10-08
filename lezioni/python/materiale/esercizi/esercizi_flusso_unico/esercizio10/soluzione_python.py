from math import ceil

def n_lattine(resa, lunghezza, larghezza, altezza):
    superficie = ((lunghezza + larghezza) * 2) * altezza
    return ceil(superficie / resa)

def costo_stanza(prezzo_lattina, n_lattine, sconto_lattina):
    tot = n_lattine * prezzo_lattina * (100 - sconto_lattina) / 100
    tot += tot * 22 / 100
    return tot

# Inserimento dati
print("=== INSERIMENTO DATI TINTEGGIATURA ===")
resa = float(input("Inserisci la resa pittura per lattina (mq): "))
prezzo = float(input("Inserisci il prezzo per lattina: "))
sconto = int(input("Inserisci lo sconto per lattina (%): "))

# Calcolo per il Salotto
lunghezza, larghezza, altezza = map(float, input("Inserisci le dimensioni del Salotto (lunghezza, larghezza, altezza in metri): ").split())
lattine_salotto = n_lattine(resa, lunghezza, larghezza, altezza)
costo_salotto = costo_stanza(prezzo, lattine_salotto, sconto)

# Calcolo per la Camera da letto
lunghezza, larghezza, altezza = map(float, input("Inserisci le dimensioni della Camera da letto (lunghezza, larghezza, altezza in metri): ").split())
lattine_camera = n_lattine(resa, lunghezza, larghezza, altezza)
costo_camera = costo_stanza(prezzo, lattine_camera, sconto)

# Calcolo per la Cucina
lunghezza, larghezza, altezza = map(float, input("Inserisci le dimensioni della Cucina (lunghezza, larghezza, altezza in metri): ").split())
lattine_cucina = n_lattine(resa, lunghezza, larghezza, altezza)
costo_cucina = costo_stanza(prezzo, lattine_cucina, sconto)

totale = costo_salotto + costo_camera + costo_cucina

# stampa del preventivo
print("=== PREVENTIVO TINTEGGIATURA ===")
print(f"Salotto: {lattine_salotto} lattine necessarie - Costo: {costo_salotto:.2f} €")
print(f"Camera: {lattine_camera} lattine necessarie - Costo: {costo_camera:.2f} €")
print(f"Cucina: {lattine_cucina} lattine necessarie - Costo: {costo_cucina:.2f} €")
print("--------------------------------------------------")
print(f"Costo totale preventivo (IVA incl.): {totale:.2f} €")