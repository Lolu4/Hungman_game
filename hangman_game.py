import random

word_list = ["python", "java", "kotlin", "javascript"]


def play():
    word = random.choice(word_list)
    hint = list("-" * len(word))
    lives = 8
    history = []
    while lives > 0 and list(hint) != word:
        print()
        print("".join(hint))
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should print a single letter")
            continue
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            print("It is not an ASCII lowercase letter")
            continue
        if letter in history:
            print("You already typed this letter")
            continue
        history.append(letter)
        if letter in word:
            for position in range(len(word)):
                if letter == word[position]:
                    hint[position] = letter
        else:
            print("No such letter in the word")
            lives -= 1
    if list(hint) == word:
        print()
        print("".join(hint))
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")


print("H A N G M A N")
choice = input('Type "play" to play the game, "exit" to quit:')
if choice == 'exit':
    exit()
elif choice == 'play':
    play()
