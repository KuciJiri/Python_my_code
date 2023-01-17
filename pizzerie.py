print("Vítejte v naší Pizzerii Rao")
size=input("Jakou velikost pizzy si dáte? s, m nebo l: ")
feferon=input("Chcete přidat feferonky? ano/ne?: ")
cheese=input("Chcete přidat cheese? ano/ne?: ")
bill=0

if size == "s":
    bill += 100
    if feferon == "ano":
        bill +=15
    if cheese == "ano":
        bill +=20
if size == "m":
    bill += 150
    if feferon == "ano":
        bill +=25
    if cheese == "ano":
        bill +=30    
if size == "l":
    bill += 200
    if feferon == "ano":
        bill +=25
    if cheese == "ano":
        bill +=30

print(f"Cena vaší pizzy je {bill} kč")

