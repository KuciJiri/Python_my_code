
vyska = input("Zadejte random výšku lidí v cm a hodnoty oddělte čárkou a mezerníkem.\nAplikace vypočítá průměrnou výšku.\n:")
list_vyska = vyska.split(", ")
soucet = 0

for i in list_vyska:
    soucet = soucet + int(i)

vysledek = soucet / len(list_vyska)
print (f"Průměrná výška je:{vysledek}cm")

