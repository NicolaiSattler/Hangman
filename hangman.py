import os
from getpass import getpass
import keyboard

from character import Character

class Hangman:

    def __init__(self):
        self.welcome_text = "Welcome to hangman.\nPlease enter a word to start the game...\nEnjoy!\n\n"
        self.enter_word_text = "Word of choice:"
        self.enter_word_error_text = "No word was supplied"
        self.enter_character_text = "Start guessing...\n\n"
        self.characters = []
        self.characterCount = 0
    
    def SubscribeKeyboard(self):
        keyboard.on_press(self.onKeyPress, False)
            
    def onKeyPress(self, name):
        print(name)
        
    def StartGame(self):
        print(self.welcome_text)

        result = self.UserSuppliesWord()

        self.characterCount = len(result)
        self.CreateResultCharacters(result)
        self.ClearText()
        self.SubscribeKeyboard()
        self.WriteAwnser()
    
    def WriteAwnser(self):
        wordLength = ''
        for i in range(0, self.characterCount):
            wordLength+="_ "
        
        print(wordLength + "\n\n")

    def ClearText(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

    def UserSuppliesWord(self):
        result = getpass(self.enter_word_text)
        
        if result:
            return result;
        else:
            print(self.enter_word_error_text)

            self.UserSuppliesWord()

    def AddCharacter(self, char: str, index: int):
        item = self.GetCharacter(char)
        if item is None:
            item = Character(char, index)
            self.characters.append(item)
        else:
            item.indexes.append(index)
            
    def GetCharacter(self, char: str):
        for item in self.characters:
            if item.character is char:
                return item
                
    def CreateResultCharacters(self, hangmanAnwser: str):
        index = 0
        for char in hangmanAnwser:
            self.AddCharacter(char, index)
            index = index + 1


