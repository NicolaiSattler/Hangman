import os
import sys
import pyfiglet
from getpass import getpass

from character import Character

class Hangman:

    def __init__(self):
        self.hangman_ansii_text = "Hangman!"
        self.awesome_ansii_text = "Awesome!"
        self.game_over_ansii_text = "Game Over..."
        self.welcome_text = "Please enter a word to start the game...\n\nEnjoy!\n\n"
        self.enter_word_text = "Word of choice:"
        self.enter_word_error_text = "No word was supplied"
        self.enter_character_text = "Start guessing...\n\n"
        self.invalid_input = "Invalid input...\n"
        self.victory_text = "You have awnsered correctly!\n\nStart a new game? Yes (Y) or No (N)? "
        self.game_over_text = "You were not able to guess the correct awnser.\n\nWould you like to try again? Yes (Y) or No (N)?"
        self.characterList = []
        self.lettersAttempted = 0
        self.maxAttempts = 10
        self.letterCount = 0
        self.awnser = ''
        self.invalidInput = False
       
    def StartGame(self):
        title_ansii = pyfiglet.figlet_format(self.hangman_ansii_text)

        print(title_ansii + '\n')
        print(self.welcome_text)

        self.awnser = self.UserSuppliesWord()
        self.letterCount = len(self.awnser)
        self.CreateResultCharacters(self.awnser)
        self.ClearText()
        self.WriteInputInstructions()

    def EndGame(self, gameover: bool):
        self.invalidInput = False
        self.lettersAttempted = 0
        self.ClearText()
        
        title_text = self.awesome_ansii_text if gameover == False else self.game_over_ansii_text
        action_text = self.victory_text if gameover == False else self.game_over_text
        
        print(pyfiglet.figlet_format(title_text))
        
        result = input(action_text)

        if result.upper() == 'Y':
            self.ClearText()
            self.ClearCharacters()
            self.StartGame()
        elif result.upper() == 'N':
            self.ClearText()
            sys.exit("Game ended...")
        else:
            self.invalidInput = True

            print("Invalid Input..")
            self.EndGame(gameover)

    def ClearCharacters(self):
        self.characterList = [];

    def ClearText(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

    def IncreaseAttemptCount(self):
        self.lettersAttempted  = self.lettersAttempted + 1

    def WriteInputInstructions(self):
        self.IncreaseAttemptCount()
        self.ClearText()
        self.WriteAwnser()
        
        attemptString = "Attempt {0} of {1}:".format(self.lettersAttempted, self.maxAttempts)

        result = input(attemptString)
        length = len(result)

        if length == 0:
            print(self.invalid_input)
        elif length == 1:
            self.onKeyPress(result)
            wordFound = self.ValidateAwnser()

            if wordFound == True:
                self.EndGame(False)
        elif length > 1:
            if result.lower() == self.awnser:
                self.EndGame(False)
            else:
                self.IncreaseAttemptCount()
                print("Wrong awnser, pentaly point...\n")
        
        if self.lettersAttempted == self.maxAttempts:
            self.EndGame(True)

        self.WriteInputInstructions()

    def WriteAwnser(self):
        awnser = ''

        for i in range(0, self.letterCount):
            found = False

            for item in self.characterList:
                if not item.hidden and i in item.indexes:
                    awnser+= item.character + ' '
                    found = True
                    break

            if not found:
               awnser+="_ "

        print(awnser + '\n')

    def ValidateAwnser(self) -> bool:
        allCharactersFound = True

        for item in self.characterList:
            if item.hidden == True:
                allCharactersFound = False
                break
        return allCharactersFound

    def onKeyPress(self, letter: str):
        for item in self.characterList:
            if item.character == letter.lower():
                item.hidden = False
                break
     

    def UserSuppliesWord(self):
        result = getpass(self.enter_word_text)
        
        if result:
            return result.lower();
        else:
            print(self.enter_word_error_text)

            self.UserSuppliesWord()

    def AddCharacter(self, char: str, index: int):
        item = self.GetCharacter(char)
        if item is None:
            item = Character(char, index)
            self.characterList.append(item)
        else:
            item.indexes.append(index)
            
    def GetCharacter(self, char: str):
        for item in self.characterList:
            if item.character == char:
                return item
                
    def CreateResultCharacters(self, hangmanAnwser: str):
        index = 0
        for char in hangmanAnwser:
            self.AddCharacter(char, index)
            index = index + 1
