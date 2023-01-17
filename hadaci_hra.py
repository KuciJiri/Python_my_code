import random

print("Vítejte v hádací hře.\nMáte pět pokusů.")

characters = ["Hermiona", "Drako", "Ron", "Brumbál", "Hagrid", "Harry"]
character = characters [random.randint(0, len(characters)-1)]
guess = ""
guess_count = 3

while character != guess:
    if guess_count != 0:
        guess = input("Uhodněte jméno postavy z filmu Harry Potter.\nNa výběr máte z těchto postav\nHermiona, Drako, Ron, Brumbál, Hagrid, Harry:\n: ")
        guess_count -= 1
    else:
        print("Počet pokusů je vyčerpán.")
        break
    
    if character == guess:
        print(f"Uhádli jste správně {character}.")

 















