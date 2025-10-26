Word_List = ["apple", "pineapple", "banana", "kiwi", "mango"]

while True:
    guess = input("guess a letter").strip()
    if guess.isalpha() and len(guess) == 1:
        print("Good Guess")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

    if guess in word:
        print(f"Good guess{guess} in {word}")
    else:
        print(f"Sorry, {guess} is not in the word. Try again." )