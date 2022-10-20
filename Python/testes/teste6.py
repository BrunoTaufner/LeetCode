listona: list[list] = []


def merge(lista: list[int], p: int, q: int, r: int):
    l1 = lista[p:q]
    l2 = lista[q:r]
    lista_ordenada = []
    i = 0
    j = 0
    while i < len(l1) or j < len(l2):
        if j >= len(l2):
            lista_ordenada.append(l1[i])
            i += 1
        elif i >= len(l1):
            lista_ordenada.append(l2[j])
            j += 1
        else:
            if l1[i] < l2[j]:
                lista_ordenada.append(l1[i])
                i += 1
            else:
                lista_ordenada.append(l2[j])
                j += 1
    return lista_ordenada


def mergeSort(lista: list[int], p: int = 0, r: int = -1):
    listinha = lista[p:r]
    if p <= r:
        listona.append(listinha)
    if len(listinha) >= 2:
        q = int((p + r) / 2)
        mergeSort(lista, p, q)
        mergeSort(lista, q, r)
        lista[p:r] = merge(lista, p, q, r)
    return listona


lista = [5, 3, 2, 1, 7, 10, 20, 12, -1, 100, 55]
mergeSort(lista, r=len(lista))
print(lista)
