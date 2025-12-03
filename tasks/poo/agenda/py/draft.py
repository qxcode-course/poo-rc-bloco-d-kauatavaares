
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
        self.__name = name
        self.__favorited = False
        self.__fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            raise Exception("fail: invalid number")
    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            raise Exception("fail: index errado")

    def toogleFavorited(self):
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited

    def getFones(self):
        return self.__fones

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def __str__(self):
        lista = ", ".join([str(f) for f in self.__fones])
        if self.__favorited:
            return f"@ {self.__name} [{lista}]"
        else:
            return f"- {self.__name} [{lista}]"


class Agenda:
    def __init__(self):
        self.__contact: list[Contact] = []

    def FindPos(self, name: str) -> int:
        for i, c in enumerate(self.__contact):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.FindPos(name)

        if pos != -1:
            for f in fones:
                self.__contact[pos].addFone(f.getId(), f.getNumber())
        else:
            contact = Contact(name)
            for f in fones:
                contact.addFone(f.getId(), f.getNumber())
            self.__contact.append(contact)
            self.__contact.sort(key=lambda x: x.getName().lower())

    def getContact(self, name: str):
        pos = self.FindPos(name)
        if pos == -1:
            raise Exception("fail: não encontrado")
        return self.__contact[pos]

    def rmContact(self, name: str):
        pos = self.FindPos(name)
        if pos == -1:
            raise Exception("fail: nao encontrando")
        else:
            self.__contact.pop(pos)



    def search(self, pattern: str):
        resultado = []
        pattern = pattern.lower()

        for contact in self.__contact:
            found = False

            if pattern in contact.getName().lower():
                found = True
            else:
                for fone in contact.getFones():
                    if pattern in fone.getId().lower() or pattern in fone.getNumber():
                        found = True
            if found:
                resultado.append(contact)

        return resultado

    def getFavorited(self):
        return [contatos for contatos in self.__contact if contatos.isFavorited()]

    def getContacts(self):
        return self.__contact

    def __str__(self):
        return "\n".join(str(contatos) for contatos in self.__contact) if self.__contact else "fail: sem contatos"


def main():
    agenda = Agenda()
    while True:
        try:
            line = input()
            print("$" + line)
            args = line.split()

            if args[0] == "end":
                break
            elif args[0] == "add":
                name = args[1]
                fones = []
                for itens in args[2:]:
                    id, number = itens.split(":")
                    fones.append(Fone(id, number))
                agenda.addContact(name, fones)
            elif args[0] == "show":
                print(agenda)
            elif args[0] == "rmFone":
                name = args[1]
                index = int(args[2])
                contact = agenda.getContact(name)
                contact.rmFone(index)
            elif args[0] == "rm":
                agenda.rmContact(args[1])
            elif args[0] == "tfav":
                 pos = agenda.FindPos(args[1])
                 if pos == -1:
                     print("fail: nao encontrado")
                 else:
                     agenda.getContacts()[pos].toogleFavorited()
            elif args[0] == "search":
                res = agenda.search(args[1])
                for c in res:
                    print(c)
            elif args[0] == "favs":
                for contact in agenda.getFavorited():
                    print(contact)
            else:
                print("fail: comando não encontrado")

        except Exception as e:
            print(e)





main()