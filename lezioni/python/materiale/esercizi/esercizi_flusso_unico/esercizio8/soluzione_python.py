from math import sqrt
x = float(input("Lunghezza primo cateto: "))
y = float(input("Lunghezza secondo cateto: "))
print(f"La lunghezza dell'ipotenusa è: {sqrt(x**2 + y**2):.2f}")