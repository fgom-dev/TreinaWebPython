from vetores import vetor
from listas import lista_ligada, lista_duplamente_ligada


print(30 * '-', 'MENU', 30 * '-')
print('1. Vetores')
print('2.Listas Ligadas')
print('3.Listas Duplamente Ligadas')

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
