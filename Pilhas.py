from collections import deque


def criarPilha():
    return deque()


def inserirNaPilha(pilha, elemento):
    pilha.append(elemento)


def removerDaPilha(pilha):
    return pilha.pop()


pilha = criarPilha()

inserirNaPilha(pilha, 8)
inserirNaPilha(pilha, 9)
inserirNaPilha(pilha, 10)
inserirNaPilha(pilha, 11)
inserirNaPilha(pilha, 12)
print(pilha)
print(f'Removendo: {removerDaPilha(pilha)}')
print(f'Removendo: {removerDaPilha(pilha)}')
print(f'Removendo: {removerDaPilha(pilha)}')
print(pilha)
