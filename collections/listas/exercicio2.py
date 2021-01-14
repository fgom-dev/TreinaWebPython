if __name__ == "__main__":

    lista = input().split(' ')

    q = int(input())
    for i in range(0, q):
        acao = input()
        if (acao == "Inserir"):
            y, x = input().split(' ')
            lista.insert(int(y), x)
        else:
            y = int(input())
            lista.pop(y)

    for item in lista:
        print(item, end=' ')