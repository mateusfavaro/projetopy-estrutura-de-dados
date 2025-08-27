from heapq import *

fila_prioridade = []

heappush(fila_prioridade, (2, 'Atender cliente VIP'))
heappush(fila_prioridade, (1, 'Situação critica'))
heappush(fila_prioridade, (3, 'Responder emails'))
heappush(fila_prioridade, (1, 'Incendio'))

while fila_prioridade:
    prioridade, tarefa = heappop(fila_prioridade)
    print(f'Executando: {tarefa} - Prioridade: {prioridade}')
