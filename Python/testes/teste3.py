
def proximosAnosBissextos(n: int) -> list[int]:
    lista = []
    i = 2024
    while i < (2024 + (n * 4)):
        if i % 100 != 0:
            lista.append(i)
        else:
            if i % 400 == 0:
                lista.append(i)
        i += 4

    return lista


print(proximosAnosBissextos(1000))
