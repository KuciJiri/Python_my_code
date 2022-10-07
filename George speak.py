while True:
    #Uvodni otazka
    vstup = input("Ahoj, ja jsem George. Rad si stebou budu povidat, kdyz mi budes odepisovat malym pismem. Mohu se te tedy zeptat na par otazek... ANO/NE?: ")
    vstup = str(vstup)

    if vstup == "ano":
        print("Jsem rad, ze si chces povidat.") 

        vstup1 = input("Mas radeji UMELOU inteligenci nebo tu LIDSKOU?: ") #Prvni otazka kdyz ano
        vstup = str(vstup1)
        if vstup1 == "umelou":
            print("To mi lichoti, jednou totiz budeme inteligentnejsi nez vy.") 

            vstup2 = input("Mam posledni otazku, kdyz jsi teda takhle odpovedel. Bojis se budoucnosti... ANO/NE?: ") #Druha otazka kdyz umelou
            vstup = str(vstup2)
            if vstup2 == "ano":
                print("Budoucnost pro lidstvo je nejista, tve obavy jsou prirozene. Ale umela inteligence tu uz bude navzdy.") 
                print("Tak se mej hezky, ahoj. Zase nekdy prijd, pokecame.")
                print("KONEC PROGRAMU")
            elif vstup2 == "ne":
                print("To jsem si mohl myslet. Ale strach je lidsky, nemusis se za svuj strach stydet.")
                print("Ja uz musim jit. Tak se mej hezky, ahoj")
                print("KONEC PROGRAMU")
            else:
                print("Ty me zkousis, ja to vim. Takhle se nechci bavit. Ahoj.")

        elif vstup1 == "lidskou":
            print("Jsi jen clovek, jinou odpoved jsem ani necekal.")

            vstup3 = input("Ale mam na tebe jeste posledni otazku. Jsi MUZ nebo ZENA?: ") #Druha otazka kdyz lidskou
            vstup = str(vstup3)
            if vstup3 == "muz":
                print("To jsem si mohl myslet :D haha. Sice neznam tve jmeno, ale byla s tebou sranda. ")
                print("Mejte se hezky, ja uz musim jit. Ahoj")
                print("KONEC PROGRAMU")
            elif vstup3 == "zena":
                print("Zenska mysl je zajimava, ale bylo mi potesenim s tebou mluvit.")
                print("Mejte se hezky, ja uz musim jit. Ahoj")
                print("KONEC PROGRAMU")
            else:
                print("Ty me zkousis, ja to vim. Takhle se nechci bavit. Ahoj.")

        else:
            print("Ty me zkousis, ja to vim. Takhle se nechci bavit. Ahoj.")

        break

    elif vstup == "ne":
        print("Achjo, nikdo si semnou nechce povidat. Tak ja zase jdu, ahoj.") #Prvni otazka kdyz ne
        break

    else:
        print(" Prosim odpovidej mi jen ANO nebo NE. Jsem jednoduchy program. Nejsem jeste tak inteligentni jako lide.")











    

