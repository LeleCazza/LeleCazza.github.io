a = 17  # Grammi totali / Fattore di crescita
b = 5   # Numero provette / Cicli di crescita

grammi_esatti = a / b
grammi_interi = a // b
resto_avanzato = a % b
popolazione_batteri = a ** b

print("Grammi esatti per provetta:", grammi_esatti, "g")
print("Grammi interi per provetta:", grammi_interi, "g")
print("Resto rimasto nella provetta madre:", resto_avanzato, "g")
print("Popolazione batteri dopo 5 cicli:", popolazione_batteri)