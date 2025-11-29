
class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        valid = "0123456789()."
        for caract in self.number:
            if caract not in valid:
                return False
        return True

    def getId(self) -> str:
        return self.id

    def getNumber(self) -> str:
        return self.number

    def setId(self, id: str):
        self.id = id

    def setNumber(self, number: str):
        self.number = number

    def __str__(self):
        return f"{self.id}:{self.number}"


class Contact:
    def __init__(self, name: str = ""):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.fones.append(fone)
        else:
            print("fail: invalid number")
    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: index errado")
    def toogleFavorited(self):
        self.favorited = not self.favorited

    def isFavorited(self) -> bool:
        return self.favorited

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name

    def __str__(self):
        lista = ", ".join([str(f) for f in self.fones])
        if self.favorited:
            return f"@ {self.name} [{lista}]"
        else:
            return f"- {self.name} [{lista}]"


class Agenda:
    def __int__(self):
        self.contact: list[Contact] = []

    def FindPos(self, name: str) -> int:
        for i, c in enumerate(self.contact):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.FindPos(name)

        if pos != -1:
            contact = self.contact[pos]
            for f in fones:
                if f.isValid():
                    contact.fones.append(f)
                else:
                    print("fail: numero invalido")
        else:
            contact = Contact(name)
            for f in fones:
                if f.isValid():
                    contact.fones.append(f)
                else:
                    print("fail: numero invalido")
            self.contact.append(contact)

    def rmContact(self, name: str):
        pos = self.FindPos(name)
        if pos != -1:
            self.contact.pop(pos)
        else:
            print("fail: nao tem esse contato ai")


    def getContact(self, name: str):
        pos = self.FindPos(name)
        if pos != -1:
            return self.contact[pos]
        return None

    def search(self, pattern: str) -> list[Contact]:
        resultado = []
        pattern = pattern.lower()

        for contatos in self.contact:
            texto = contatos.getName().lower()

            for fones in contatos.fones:
                texto += " " + fones.id.lower()
                texto += " " + fones.number.lower()
            if pattern in texto:
                resultado.append(contatos)

        return resultado

    def getFavorited(self):
        return [contatos for contatos in self.contact if contatos.favorited]

    def getContacts(self):
        return self.contact

    def __str__(self):
        return "\n".join(str(contatos) for contatos in self.contact)







def main():
    agenda = Agenda()
    while True:
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

main()