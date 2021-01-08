class No():

    def __init__(self, elem):
        self.elemento = elem
        self.prox = None
        self.anterior = None


def remove_elemento(primeiro, n):
    temp = primeiro

    i = 1
    while (temp != None):
        if (i == n):
            aux = temp.anterior
            aux.prox = temp.prox
            aux.prox.anterior = temp.anterior
            break
        else:
            temp = temp.prox

        i += 1

    return primeiro

def string_to_no(linha):
    node_values = linha.split(',')

    root = No(node_values[0])
    ptr = root
    ptrA = None
    for item in node_values[1:]:
        ptr.anterior = ptrA
        ptr.prox = No(item)
        ptrA = ptr
        ptr = ptr.prox

    ptr.anterior = ptrA
    root.anterior = ptr

    return root


def no_to_string(no):
    if (no == None):
        return "[]"

    no2 = no

    i = 0
    result = "";
    while (no != None):
        result += no.elemento + ", "
        no = no.prox
        i += 1

    inverseResult = ""
    for j in range(0, i):
        inverseResult += no2.anterior.elemento + ", "
        no2 = no2.anterior

    return "[" + inverseResult[:-2] + "]\n[" + result[:-2] + "]"


if __name__ == "__main__":
    line = input()
    cabeca = string_to_no(line)

    n = int(input())

    nova_lista = remove_elemento(cabeca, n)

    out = no_to_string(nova_lista)

    print(out)