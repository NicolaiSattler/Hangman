class Character:
    def __init__(self, char: str, index: int):
        self.character = char.lower()
        self.hidden = True
        self.indexes = []
        self.indexes.append(index)
    
