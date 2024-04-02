import math
print("Vítejte v programu kalkulačka...")
while True:
    cislo1 = float(input("Zadej první číslo:"))
    cislo2 = float(input("Zadej druhé číslo:"))
    operace = input("Zadej operaci: '+', '-', '*', '/', '^' (pro mocninu), 'sqrt' (pro odmocninu), nebo 'konec' pro ukončení: ")
    if operace == "+":
        print(cislo1 + cislo2)
    elif operace == "-":
        print(cislo1 - cislo2)
    elif operace == "*":
        print(cislo1 * cislo2)
    elif operace == "/":
        print(cislo1 / cislo2)
    elif operace == "^":
        print(cislo1 ** cislo2)
    elif operace == "sqrt":
        print(math.sqrt(cislo1))
    elif operace == "konec":
        print("Konec")
        break
    else:
        print("neplatna operace")
    volba = input("Chcete pokračovat? (ano/ne): ")
    if volba.lower() != 'ano':
        print("Konec")
        break