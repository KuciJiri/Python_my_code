print("Vítejte v kalkulačce")
a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))
print("Vyberte jednu z požadovaných operací: ")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
operace = int(input(""))

if (operace == 1):
    vysledek = a + b
elif (operace == 2):
    vysledek = a - b
elif (operace == 3):
    vysledek = a * b
elif (operace == 4):
    vysledek = a / b
if operace > 0 and operace < 5:
    print("výsledek: %f" % (vysledek))
else:
    print("Chybná volba")
print("Děkuji za použití kalkulačky!")