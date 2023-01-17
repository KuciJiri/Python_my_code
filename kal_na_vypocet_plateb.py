print("Vítejte v kalkulátoru na výpočet plateb")

cena = int(input("Kolik máte zplatit?: "))
dysko = int(input("Jak vysoké spropitné chcete nechat(v kč)?: "))
rozdelit = int(input("Mezi kolik lidí se má částka rozdělit?: "))

cenadysko = cena + dysko
vysledek = cenadysko / rozdelit

print(f"Každý zaplatíte {vysledek}kč.")
