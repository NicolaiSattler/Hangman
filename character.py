class Character:
    def __init__(self, char: str, index: int):
        self._character = char.lower()
        self._hidden = True
        self._indexes = []
        self._indexes.append(index)
    
    @property
    def character(self):
        return self._character
    
    @character.setter
    def character(self, value):
