"""
Essentially, the crate minigame is hangman
What this program aims to do is to not only predict the possible words,
but to also calculate the best choices for guesses, given the possible words
and weighted by the frequency of their appearance
"""

import math

dictionary = {}

with open("google-books-common-words.txt", 'r') as file:
    for line in file.readlines():
        args = line.split()
        dictionary[args[0].lower()] = int(args[1])

# for key in dictionary.keys():
#     print(key + " " + str(dictionary[key]))


while True:
    print("Enter the current word, and letters guessed:")
    args = input().split()
    revealed = args[0]
    wrong = ""
    if len(args) > 1:
        wrong = args[1]

    used = set()
    for i in revealed:
        used.add(i)
    for i in wrong:
        used.add(i)

    # print(used)

    possible_words = []
    failed = False

    for word in dictionary.keys():
        if len(revealed) != len(word):
            continue
        for i, j in zip(word, revealed):
            if i != j:
                if i in used or j != '?':
                    failed = True
                    break
        if not failed:
            possible_words.append((word, dictionary[word]))
        failed = False
    # print(possible_words)
    print("Top 20 words:")
    print(", ".join([possible_words[i][0] for i in range(20)]))

        # print(possible_words[i][0])

    best_guess = {}

    for word in possible_words:
        for char in word[0]:
            if char not in used:
                if char in best_guess.keys():
                    best_guess[char] += int(math.log(word[1]))
                else:
                    best_guess[char] = int(math.log(word[1]))

    best_guess = [(key, best_guess[key]) for key in best_guess.keys()]
    best_guess.sort(key=lambda x: x[1], reverse=True)
    print("Top 7 guess")
    # print(best_guess)
    print("; ".join([best_guess[i][0] + ", " + str(best_guess[i][1]) for i in range(7)]))

    print()

