import random
class Hangman:
    def __init__(self, word_list, num_lives = 5 ):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list 
        self.list_of_guesses =  []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    index = self.word.index(letter)
                    self.word_guessed[index] = letter
                    self.num_letters -=1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left." )
    

    def ask_for_input(self):
        while True:
           guess = input("Guess a letter")
           if len(guess) > 1 or not guess.isalpha():
               print(f"Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
           #elif self.num_lives == 0:
            #   print("You're Dead")
             #  break
           else:
            self.check_guess(guess)
            self.list_of_guesses.append( guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives <=0:
            print("You Lost")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives > 0 and game.num_letters <=0:
            print(" Congratulations, You've won the game.")
            break

word_list = ["apple", "pineapple", "banana", "kiwi", "mango"]

#play_game(word_list)
game1 = Hangman(word_list)            
game1.ask_for_input()
               