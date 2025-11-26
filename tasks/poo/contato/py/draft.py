class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def getId(self):
        return self.id
    def getNumber(self):
        return self.number
    def setId(self, id: str):
        self.id = id
    def setNumber(self, number: str):
        self.number = number
     def isValid(self) -> bool:
         if

    def __str__(self):
        return f"{self.id}, {self.number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited : bool
        self.fone: list[Fone] = []

    def addFone(self, id: str, number: str):
        if