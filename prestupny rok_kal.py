def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Zadejte rok: "))
if is_leap_year(year):
    print("Rok je přestupný.")
else:
    print("Rok není přestupný.")