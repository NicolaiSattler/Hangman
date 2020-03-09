import os
from getpass import getpass

from character import Character

class Hangman:

    def __init__(self):
        self.welcome_text = "Welcome to hangman.\nPlease enter a word to start the game...\nEnjoy!\n\n"
        self.enter_word_text = "Word of choice:"
        self.enter_word_error_text = "No word was supplied"
        self.enter_character_text = "Start guessing...\n\n"
        self.invalid_input = "Invalid input...\n"
        self.victory_text = "You have awnsered correctly!\n\nStart a new game? Yes (Y) or No (N)? "
        self.characterList = []
        self.lettersAttempted = 0
        self.maxAttempts = 10
        self.letterCount = 0
        self.awnser = ''
        self.invalidInput = False
       
    def StartGame(self):
        print(self.welcome_text)

        self.awnser = self.UserSuppliesWord()
        self.letterCount = len(self.awnser)
        self.CreateResultCharacters(self.awnser)
        self.ClearText()
        self.WriteInputInstructions()

    def EndGame(self):
        self.invalidInput = False
        self.ClearText()

        result = input(self.victory_text)

        if result.upper() == 'Y':
            self.ClearText()
            self.StartGame()
        elif result.upper() == 'N':
            return
        else:
            self.invalidInput = True

            print("Invalid Input..")
            self.EndGame()

    def ClearText(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

    def IncreaseAttemptCount(self):
        self.lettersAttempted  = self.lettersAttempted + 1

    def WriteInputInstructions(self):
        self.IncreaseAttemptCount()
        self.ClearText()
        self.WriteAwnser()

        result = input(f'Attempt {self.lettersAttempted} of {self.maxAttempts}:')
        length = len(result)

        if length == 0:
            print(self.invalid_input)
        elif length == 1:
            self.onKeyPress(result)
        elif length > 1:
            if result.lower() == self.awnser:
                self.EndGame()
            else:
                self.IncreaseAttemptCount()
                print("Wrong awnser, pentaly point...\n")

        self.WriteInputInstructions()

    def WriteAwnser(self):
        awnser = ''

        for i in range(0, self.letterCount):
            found = False

            for item in self.characterList:
                if not item.hidden and i in item.indexes:
                    awnser+=f'{item.character} '
                    found = True
                    break

            if not found:
               awnser+="_ "

        print(awnser + '\n')

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
