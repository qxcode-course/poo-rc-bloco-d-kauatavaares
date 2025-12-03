
class Fone:
    def __init__(self, id: str, number: str):
       self.__id = id
       self.__number = number

    def isValid(self) -> bool:
        valid = "0123456789()."
        for caract in self.__number:
            if caract not in valid:
                return False
        return True

    def getId(self) -> str:
        return self.__id

    def getNumber(self) -> str:
        return self.__number

    def setId(self, id: str):
       self.__id = id

    def setNumber(self, number: str):
       self.__number = number

    def __str__(self):
        return f"{self.__id}:{self.__number}"


class Contact:
    def __init__(self, name: str = ""):
        self.__name  = name
        self.__favorited = False
        self.__fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: invalid number")
    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: index errado")
    def toogleFavorited(self):
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited

    def getFones(self):
        return self.__fones

    def getName(self):
        return self.__name

    def setName(self, name: str):
       self.__name  = name

    def __str__(self):
        lista = ", ".join([str(f) for f in self.__fones])
        if self.__favorited:
            return f"@ {self.__name} [{lista}]"
        else:
            return f"- {self.__name} [{lista}]"





def main():
    contact = Contact
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            name = args[1] if len(args) > 1 else ""
            contact = Contact(name)
        elif args[0] == "show":
            print(contact)
        elif args[0] == "add":
            id = args[1]
            number = args[2]
            contact.addFone(id, number)
        elif args[0] == "rm":
            index = int(args[1])
            contact.rmFone(index)
        elif args[0] == "tfav":
            contact.toogleFavorited()
        else:
            print("fail: comando invalido")


main()
