def fibonacci(ant: int, atual: int, n: int):
    resultado = ant + atual
    n += 1
    if n >= 50:
        return
    print(resultado)
    fibonacci(atual, resultado, n)

print(1)
print(1)
fibonacci(1, 1, 2)
