from .no_duplamente_ligada import NoDuplamenteLigada


class ListaDuplamenteLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0

    def esta_vazia(self):
        return self.__tamanho == 0

    def inserir(self, elemento):
        novo_no = NoDuplamenteLigada(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            novo_no.anterior = self.__ultimo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1

    def inserir_posicao(self, posicao, elemento):
        if posicao == 0:
            novo_no = NoDuplamenteLigada(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no.anterior = novo_no
            self.__primeiro_no = novo_no
            self.__tamanho += 1
        elif posicao == self.__tamanho:
            self.inserir(elemento)
        else:
            no_atual = self.recuperar_no(posicao)
            no_anterior = no_atual.anterior
            novo_no = NoDuplamenteLigada(elemento)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
            no_atual.anterior = novo_no
            novo_no.anterior = no_anterior
            self.__tamanho += 1

    def __str__(self):
        temp = self.__primeiro_no
        elementos = ''
        while(temp):
            elementos = f'{elementos} {temp.elemento}'
            temp = temp.proximo
        return elementos

    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)
        if no != None:
            return no.elemento
        return None

    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao + 1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado

    def contem(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i
        return -1

    def remover_posicao(self, posicao):
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no.proximo = None
            proximo_no.anterior = None
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho - 1:
            penultimo_no = self.__ultimo_no.anterior
            penultimo_no.proximo = None
            self.__ultimo_no = None
            self.__ultimo_no = penultimo_no
        else:
            no_remover = self.recuperar_no(posicao)
            no_anterior = no_remover.anterior
            no_proximo = no_remover.proximo
            no_anterior.proximo = no_proximo
            no_proximo.anterior = no_anterior
            no_remover.proximo = None
            no_remover.anterior = None
        self.__tamanho -= 1

    def remover_elemento(self, elemento):
        indice = self.indice(elemento)
        self.remover_posicao(indice)

