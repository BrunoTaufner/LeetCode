def testaFuncaoLoop(input_output: list[tuple]):
    erros = 0
    for tupla in input_output:
        result = testaFuncao(tupla[0], tupla[1])
        print(result)
        if result[0] == 'E':
            erros += 1
    print('----------- RESUMO -----------')
    print(f'Erros: {erros}\tAcertos: {len(input_output) - erros}')


def testaFuncao(input: list[int], output: int) -> str:
    result = greatestNumList(input)
    if result == output:
        return f'Acerto -> Valor esperado: {output} | Valor obtido: {result}'
    else:
        return f'**Erro -> Valor esperado: {output} | Valor obtido: {result}'


def greatestNumList(lista: list[int]) -> int:
    greatestNum = None
    if len(lista) > 0:
        greatestNum = lista[0]
    for num in lista:
        if greatestNum < num:
            greatestNum = num

    return greatestNum

testes = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
    ([2, 3, -2, -4, -5, -6, -7, -8, -9], 3),
    ([2, 3, -2, -4, -5, -6, -7, -8, -9], -1)
]
testaFuncaoLoop(testes)
