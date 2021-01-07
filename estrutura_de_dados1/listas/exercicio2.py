class No():

    def __init__(self, elem):
        self.elemento = elem
        self.prox = None


def remove_n_elemento_do_fim(cabeca, n):
    tempCabeca = cabeca
    temp = cabeca

    j = 1
    while (temp.prox != None):
        temp = temp.prox
        j += 1

    temp = cabeca

    n = j - n

    if (n == 0):
        cabeca = temp.prox
    else:
        i = 0
        while (temp != None):
            if (i == n):
                tempCabeca.prox = temp.prox
                break

            tempCabeca = temp
            temp = temp.prox
            i += 1

    return cabeca


# Coloque seu código aqui


def string_to_no(linha):
    node_values = linha.split(',')

    root = No(0)
    ptr = root
    for item in node_values:
        ptr.prox = No(item)
        ptr = ptr.prox

    return root.prox


def no_to_string(no):
    if (no == None):
        return "[]"

    result = "";
    while (no != None):
        result += no.elemento + ", "
        no = no.prox

    return "[" + result[:-2] + "]"


if __name__ == "__main__":
    line = input()
    cabeca = string_to_no(line)

    n = int(input())

    nova_lista = remove_n_elemento_do_fim(cabeca, n)

    out = no_to_string(nova_lista)

    print(out)