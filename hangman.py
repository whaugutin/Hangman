import random
import hangman_list as hl
import time

list_words = []
list_descrip =  []

for key in hl.dico.keys():
    list_words.append(key)
for val in hl.dico.values():
    list_descrip.append(val)


random_chosen_word = random.choice(list_words)
index = list_words.index(random_chosen_word)
description = list_descrip[index]


lives = 5
hide = []
for letter in random_chosen_word:
  hide.append("*")


print("\nBonjour\n")
name = input("Entrez votre nom, s'il vous plait: ")

try:
    people = open("players.txt", "r")
except FileNotFoundError:
    people = open("players.txt", "w")
    people.write(name + ",")
    people.close()
else:
    my_list = people.read().split(",")
    people.close()
    print("Nous avons déjà jouer avec:")
    for i in range(len(my_list)-1):
        print(f"{i+1}- {my_list[i]}")
    people = open("players.txt", "a")
    people.write(name + ",")
    people.close()
print(f"\nBonjour {name}, Nous allons jouer ensemble\n")


print(f"Vous allez déchiffrer un mot à {len(random_chosen_word)} charactère commencant par la lettre {random_chosen_word[0]}\n")
print(f"Définition du mot: {description}")
print(" ".join(hide))
print(f"Vous avez droit {lives} erreurs\n")


end_of_game = False
while not end_of_game:
    let_guess = input("Devinez une lettre qui est dans le mot caché: ").lower()
    num_of_letter = len(random_chosen_word)

    if let_guess in hide:
        print(f"Vous déja choisi la lettre {let_guess}")
    for position in range(num_of_letter):
        letter = random_chosen_word[position]
        if letter == let_guess:
            hide[position] = letter
    print(f"{' '.join(hide)}", end = "\n\n")

    if let_guess not in random_chosen_word:
        lives -= 1
        print("\nLa lettre que vous avez choisi n'est pas dans le mot")
        print(f"Il vous reste {lives} vie(s)")
        if lives == 0:
            end_of_game = True
            print(f"\nMalheureusement, {name} vous n'avez plus de vie")
            print(f"Le mot était '{random_chosen_word}'")
            time.sleep(3)

    if "*" not in hide:
        end_of_game = True
        print("\nVous avez gagnez  BRAVOO \U0001f44f \U0001f44f!!!!!")
        print(f"Bien joué {name}")
        time.sleep(3)
    