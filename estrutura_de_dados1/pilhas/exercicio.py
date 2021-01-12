import re
import inspect


class No():
    def __init__(self, val):
        self.val = val
        self.prox = None


class Pilha():
    def __init__(self):
        self.cabeca = None

    def remove(self):
        aux = self.cabeca
        if (self.cabeca != None and self.cabeca.prox != None):
            self.cabeca = aux.prox
        else:
            self.cabeca = None;

        if (aux != None):
            return aux.val
        else:
            return None

    def inserir(self, valor):
        if (self.cabeca == None):
            self.cabeca = No(valor)
        else:
            aux = self.cabeca
            self.cabeca = No(valor)
            self.cabeca.prox = aux

    def exibir(self):
        aux = self.cabeca

        while (aux != None):
            print(aux.val)
            aux = aux.prox


def analisa_pilha(pilha):
    if (pilha != None):
        caractere = pilha.remove()
        parentese = 0
        chave = 0
        colchete = 0
        while (caractere != None):
            if (caractere == ")"):
                parentese += 1
            elif (caractere == "("):
                if (parentese == 0):
                    return False
                else:
                    parentese -= 1
            elif (caractere == "]"):
                colchete += 1
            elif (caractere == "["):
                if (colchete == 0):
                    return False
                else:
                    colchete -= 1
                break;
            elif (caractere == "}"):
                chave += 1
            elif (caractere == "{"):
                if (chave == 0):
                    return False
                else:
                    chave -= 1
            else:
                return False

            caractere = pilha.remove();

        if (chave == 0 and parentese == 0 and colchete == 0):
            return True;
        else:
            return False

    return False


def analisa_string():
    n = int(input())
    for i in range(0, n):
        pilha = Pilha()
        linha = input()
        for car in linha:

            if (car != "\n" and len(car) != 0):
                pilha.inserir(car);

        print("Balanceada" if analisa_pilha(pilha) else "Não balanceada")


def generate_call(obj):
    name = obj.__name__
    args = "( "
    for i in range(1, obj.__code__.co_argcount):
        args += "0,"

    args = args[:-1] + ")"
    return name.strip() + args


if __name__ == "__main__":

    filtro = {k: v for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k)}

    if not "Pilha" in filtro:
        print("É necessário declarar uma classe Pilha")

    for classe in filtro:
        if not inspect.ismodule(filtro[classe]) and inspect.isclass(filtro[classe]):
            args = "( "
            for i in range(1, vars(filtro[classe])["__init__"].__code__.co_argcount):
                args += "0,"

            args = args[:-1] + ")"

            obj = eval(filtro[classe].__name__ + args)

            metodos = {k: v for k, v in dict(inspect.getmembers(obj, inspect.ismethod)).copy().items() if
                       not re.search(r'\b__\w+__\b', k)}
            for nome in metodos:
                metodo = generate_call(metodos[nome])
                if metodo != None:
                    eval("obj." + metodo)

            membros = {k: v for k, v in dict(inspect.getmembers(obj)).copy().items() if
                       not re.search(r'\b__\w+__\b', k)}
            for nome in membros:

                if isinstance(membros[nome], (list, tuple)):
                    print("Um membro da classe não pode ser dos tipos list ou tuple")

    analisa_string()