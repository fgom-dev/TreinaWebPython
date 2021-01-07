class No():

    def __init__(self, elem):
        self.elemento = elem
        self.prox = None


def remove_elemento(cabeca, n):
    tempCabeca = cabeca
    temp = cabeca

    if (n == 1):
        cabeca = temp.prox
    else:
        i = 1
        while (temp != None):
            if (i == n):
                tempCabeca.prox = temp.prox
                break

            tempCabeca = temp
            temp = temp.prox
            i += 1

    return cabeca

# Informe seu código aqui


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

    nova_lista = remove_elemento(cabeca, n)

    out = no_to_string(nova_lista)

    print(out)
