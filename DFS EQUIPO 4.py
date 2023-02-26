def dfs(grafo, inicio):
    visitados = set()
    pila = [inicio]
    while pila:
        vertice = pila.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            print(vertice)
            pila.extend(reversed(grafo.get(vertice, [])))
    return visitados

# Función para leer un grafo con nodos enteros
def leer_grafo_enteros():
    grafo = {}
    n = int(input("Ingrese el número de nodos: "))
    for i in range(n):
        nodo = int(input("Ingrese el valor del nodo {}: ".format(i+1)))
        adyacentes = list(map(int, input("Ingrese los nodos adyacentes de {}: ".format(nodo)).strip().split()))
        grafo[nodo] = adyacentes
    nodo_inicial = int(input("Ingrese el nodo inicial: "))
    return grafo, nodo_inicial

# Ejemplo de uso
if __name__ == '__main__':
    grafo, inicio = leer_grafo_enteros()
    print("Recorrido DFS:")
    dfs(grafo, inicio) 