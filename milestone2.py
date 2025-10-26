import random
Word_List = ["apple", "pineapple", "banana", "kiwi", "mango"]
print(Word_List)

def random_choice(Word_List):
    return random.choice(Word_List)

word = random_choice(Word_List)
print(word)

def Guess_func():
    guess = str(input("Guess a letter: "))
    if len(guess) == 1:
        print("Good Guess")
        return True
    else:
        print("Oops! That is not a valid input.")
        return False
    
Guess_func()