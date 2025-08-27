from collections import deque


def criarFila():
    return deque()


def inserirNaFila(fila, elemento):
    fila.append(elemento)


def removerNaFila(fila):
    return fila.popleft()


fila = criarFila()

inserirNaFila(fila, 8)
inserirNaFila(fila, 9)
inserirNaFila(fila, 10)
inserirNaFila(fila, 11)
inserirNaFila(fila, 12)
print(fila)
print(f'Removendo: {removerNaFila(fila)}')
print(f'Removendo: {removerNaFila(fila)}')
print(f'Removendo: {removerNaFila(fila)}')
print(fila)
