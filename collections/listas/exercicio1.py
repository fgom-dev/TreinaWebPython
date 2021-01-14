if __name__ == "__main__":
    n = int(input())
    lista = []
    for i in range(0, n):
        linha = []
        dados = input().split(' ')
        d = int(dados[0])
        for j in range(0, d):
            linha.insert(j, int(dados[j + 1]))

        lista.insert(i, linha)

    q = int(input())
    for i in range(0, q):
        y, x = input().split(' ')

        try:
            linha = lista[int(y) - 1]
            print(linha[int(x) - 1])
        except:
            print("Erro!")