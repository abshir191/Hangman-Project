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
        """
    Method that checks the guess(user input)
    
    
        takes in guess as an argument, which will represent the user input
        
        Method checks if the guessed letter is in the random word, and if it is replaces
        _ with the correctly guessed word
        
        else statement:
        takes a life away if the guessed letter isn't in the random word 
        and prints how many lives user has left
    
    """
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
        """
    This is Responsible for the user input, which we store in the guess variable.

    The method using a while loop which will keep running and is set to true.
    If the guessed lette rhas more than on alphanumerical character it'll be rejected
    and user is prompted to try again. 
    In this method i've also included a kill switch that's triggered if the num of lives = 0
    """
        while True:
           guess = input("Guess a letter")
           if len(guess) > 1 or not guess.isalpha():
               print(f"Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
           elif self.num_lives == 0:
               print("You're Dead")
               break
           else:
            self.check_guess(guess)
            self.list_of_guesses.append( guess)



word_list = ["apple", "pineapple", "banana", "kiwi", "mango"]
game1 = Hangman(word_list)            
game1.ask_for_input()
               





