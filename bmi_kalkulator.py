kg = float(input("Zadejte svoji váhu v KG: "))
vyska = float(input("Zadejte svoji výšku v metrech: "))

bmi = (round(float(kg) / float(vyska)**2 ,1))

if bmi < 18.5:
    bmi_text="podváhu"
    

elif bmi < 25:
    bmi_text="normální váhu"
    

elif bmi < 30:
    bmi_text="nadváhu"
    

elif bmi < 35:
    bmi_text="obezitu"
    

elif bmi > 35:
    bmi_text="těžkou obezitu"  
    


print (f"Vaše BMI číslo je: {bmi} máte {bmi_text}")
