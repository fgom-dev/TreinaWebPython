import re


class NoArvore():

    def __init__(self, valor):
        self._valor = valor
        self.__no_esquerdo = None
        self.__no_direito = None

    @property
    def valor(self):
        return self._valor

    @property
    def no_esquerdo(self):
        return self.__no_esquerdo

    @property
    def no_direito(self):
        return self.__no_direito

    @no_direito.setter
    def no_direito(self, no_direito):
        self.__no_direito = no_direito

    @no_esquerdo.setter
    def no_esquerdo(self, no_esquerdo):
        self.__no_esquerdo = no_esquerdo

    def peso(self):
        return self.valor

    def __str__(self):
        return ("[(X)]" if self.__no_esquerdo == None else f'[({self.__no_esquerdo.__str__()})]') + \
               (f'[({self.valor.__str__()}') + \
               ("[(X)]" if self.__no_direito == None else f'[({self.__no_direito.__str__()})]')


class Arvore():
    def __init__(self):
        self.__raiz = None

    @property
    def raiz(self):
        return self.__raiz

    def inserir(self, no):
        no.no_direito = None
        no.no_esquerdo = None

        if (self.__raiz == None):
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)

    def __inserir(self, ref, novo_no):
        if (ref.peso() < novo_no.peso()):
            if (ref.no_direito == None):
                ref.no_direito = novo_no
            else:
                self.__inserir(ref.no_direito, novo_no)
        else:
            if (ref.no_esquerdo == None):
                ref.no_esquerdo = novo_no
            else:
                self.__inserir(ref.no_esquerdo, novo_no)

    def em_ordem(self):
        self.__em_ordem(self.__raiz)

    def __em_ordem(self, ref):
        if (ref.no_esquerdo != None):
            self.__em_ordem(ref.no_esquerdo)
            print(ref.valor)
            if (ref.no_direito != None):
                self.__em_ordem(ref.no_direito)
        else:
            print(ref.valor)
            if (ref.no_direito != None):
                self.__em_ordem(ref.no_direito)


def processa_arvore():
    arvore = Arvore()

    t = int(input())
    for i in range(0, t):
        valor = int(input())

        arvore.inserir(NoArvore(valor))

    arvore.em_ordem()


if __name__ == "__main__":

    filtro = {k: v for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k)}

    if (not "Arvore" in filtro) or (not "NoArvore" in filtro):
        print("É necessário declarar as classes Arvore e NoArvore")
        quit()

    processa_arvore()