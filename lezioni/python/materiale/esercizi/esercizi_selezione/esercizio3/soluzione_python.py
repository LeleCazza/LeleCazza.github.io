a = float(input("Inserisci il primo lato: "))
b = float(input("Inserisci il secondo lato: "))
c = float(input("Inserisci il terzo lato: "))

if a <= 0 or b <= 0 or c <= 0:
    print("I lati devono essere maggiori di zero.")
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("I lati inseriti non possono formare un triangolo.")
else:
    if a == b == c:
        print("Triangolo equilatero")
    elif a == b or b == c or a == c:
        print("Triangolo isoscele")
    else:
        print("Triangolo scaleno")