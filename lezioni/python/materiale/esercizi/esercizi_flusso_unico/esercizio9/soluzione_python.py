import math
x,y,z = map(float,input("Inserisci i tre numeri: ").split())
print(f"Gli opposti dei tre numeri sono: {x*-1} , {y*-1} , {z*-1}")
print(f"I valori assoluti dei tre numeri sono: {math.fabs(x)} , {math.fabs(y)} , {math.fabs(z)}")
print(f"La somma dei quadrati dei tre numeri è: {x**2 + y**2 + z**2}")