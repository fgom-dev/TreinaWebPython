from vetores import vetor
from listas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from filas import fila
from conjuntos import conjunto


print(30 * '-', 'MENU', 30 * '-')
print('1. Vetores')
print('2.Listas Ligadas')
print('3.Listas Duplamente Ligadas')
print('4.Pilhas')
print('5.Filas')
print('6.Conjuntos')

menu = int(input('Digite a opção desejada: '))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_final(1)
    vetor_teste.inserir_elemento_final(2)
    vetor_teste.inserir_elemento_final(3)
    vetor_teste.inserir_elemento_final(4)
    vetor_teste.inserir_elemento_final(5)

    print(vetor_teste.tamanho_vetor())
    print(vetor_teste.contem(7))
    print(vetor_teste.indice(6))
    print(vetor_teste)
    vetor_teste.remover_elemento_indice(3)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)
elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    lista_teste.inserir_posicao(1, 0)
    print(lista_teste)
    lista_teste.remover_elemento(0)
    print(lista_teste)
    # print(lista_teste.contem(15))
    # print(lista_teste.indice(0))
    # print(lista_teste.recuperar_elemento_no(0))
elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    lista_teste.inserir_posicao(1, 0)
    print(lista_teste)
    lista_teste.remover_elemento(0)
    print(lista_teste)
    print(lista_teste.contem(15))
    print(lista_teste.indice(0))
    print(lista_teste.recuperar_elemento_no(0))
elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    # pilha_teste.empilhar(6)
    # pilha_teste.empilhar(7)
    print(pilha_teste)
    print(pilha_teste.desempilhar())
elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
elif menu == 6:
    conjunto_teste = conjunto.Conjunto()
    conjunto_teste.inserir(1)
    conjunto_teste.inserir(2)
    conjunto_teste.inserir(3)
    print(conjunto_teste.inserir(3))
    # print(conjunto_teste.inserir_posicao(1, 3))
    print(conjunto_teste)
