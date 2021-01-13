import re
import inspect


class No():
    def __init__(self, val):
        self.val = val
        self.prox = None


class ListaLigada():

    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def remover(self, valor):
        if (self.cabeca != None and self.cabeca.prox != None):
            aux = self.cabeca

            while (aux.prox != None):
                if (aux.prox.val == valor):
                    val = aux.prox.val
                    aux.prox = aux.prox.prox
                    self.tamanho -= 1
                    return val

                aux = aux.prox

            return None
        elif (self.cabeca != None):
            valor = self.cabeca.val
            self.cabeca = None
            self.tamanho -= 1
            return valor
        else:
            return None

    def inserir(self, valor):
        if (self.cabeca == None):
            self.cabeca = No(valor)
            self.tamanho += 1
        else:
            aux = self.cabeca

            while (aux.prox != None):
                aux = aux.prox

            aux.prox = No(valor)
            self.tamanho += 1

    def recuperar(self, index):
        if (index > self.tamanho):
            return None
        else:
            aux = self.cabeca
            i = 0
            while (i < index and aux.prox != None):
                aux = aux.prox
                i += 1

            return aux.val

    def contem(self, valor):
        aux = self.cabeca
        while (aux != None):
            if (aux.val == valor):
                return True

            aux = aux.prox

        return False

    def exibir(self):
        aux = self.cabeca

        while (aux != None):
            print(aux.val)
            aux = aux.prox

    def get_tamanho(self):
        return self.tamanho


class Mapa():

    def __init__(self):
        self.__elementos = ListaLigada()
        self.__quantidade_categorias = 16

        for i in range(0, self.__quantidade_categorias):
            self.__elementos.inserir(ListaLigada())

    def contem_chave(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                return True

        return False

    def remover(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                categoria.remover(associacao)
                return

        raise Exception("A chave {} não existe".format(chave))

    def adicionar(self, chave, valor):
        if (self.contem_chave(chave)):
            self.remover(chave)

        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)
        categoria.inserir(Associacao(chave, valor))

    def recuperar(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                return associacao.valor

        raise Exception("A chave {} não existe".format(chave))

    def __str__(self):
        return "Mapa [elementos={}]".format(self.__elementos)

    def __gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__quantidade_categorias


class Associacao():

    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return "Associacao: {} - {}".format(self.__chave, self.__valor)


def processa_mapa():
    t = int(input())

    mapa = Mapa()
    for i in range(0, t):
        nome = input()
        telefone = input()

        mapa.adicionar(nome, telefone)

    t = int(input())
    for i in range(0, t):
        nome = input()
        if (mapa.contem_chave(nome)):
            print("{}={}".format(nome, mapa.recuperar(nome)))
        else:
            print("Não achado")


if __name__ == "__main__":

    filtro = {k: v for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k)}

    if not "Mapa" in filtro:
        print("É necessário declarar uma classe Mapa")
        quit()

    obj = Mapa()

    membro = [member for _name, member in inspect.getmembers(obj) if isinstance(member, ListaLigada)]

    if (len(membro) < 1):
        print("A classe deve implementar uma tabela de espalhamento com lista ligada")

    processa_mapa()