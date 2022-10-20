def concatenaLista(l: list[int], target, listaResultante: list[int]):
    for num in l:
        if num > target:
            listaResultante.append(num)


def concatenaListas(l1: list[int], l2: list[int], target: int) -> list[int]:
    lista = []
    concatenaLista(l1, target, lista)
    concatenaLista(l2, target, lista)

    return lista


print(concatenaListas([1, 2, 3, 4], [5, 6, 7, 8, 9, 10], 9))
