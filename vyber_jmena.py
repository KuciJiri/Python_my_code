import random

names= input("Napiš mi jména, oddělené čárkou\n:")

list_people = names.split(", ")

print(random.choice(list_people))