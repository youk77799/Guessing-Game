secret_word = "giraffe"
guess = ""
attempt = 0
guess_limit = 3
lose = False

while guess != secret_word and not lose:
    if attempt < guess_limit:
        guess = input("Enter guess: ")
        attempt += 1
    else:
        lose = True

if lose:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
