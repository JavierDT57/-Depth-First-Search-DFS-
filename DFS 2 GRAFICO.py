# Función DFS para un grafo de enteros
def dfs(grafo, inicio):
    visitados = set()
    pila = [(inicio, 0)]  # Agregar el nivel del nodo al recorrido
    while pila:
        vertice, nivel = pila.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            print("Nodo: {} (nivel {})".format(vertice, nivel))  # Imprimir el nivel del nodo
            for adyacente in reversed(grafo.get(vertice, [])):
                pila.append((adyacente, nivel+1))  # Agregar el nivel del adyacente al recorrido
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

# Función para calcular las distancias del nodo inicial a los demás nodos del grafo
def calcular_distancias(grafo, inicio):
    distancias = {inicio: 0}  # Inicializar la distancia del nodo inicial como 0
    cola = [inicio]  # Inicializar la cola con el nodo inicial
    while cola:
        nodo = cola.pop(0)
        for adyacente in grafo.get(nodo, []):
            if adyacente not in distancias:
                distancias[adyacente] = distancias[nodo] + 1
                cola.append(adyacente)
    return distancias

# Impresion de DFS y la distancia del nodo inicial
if __name__ == '__main__':
    grafo, inicio = leer_grafo_enteros()
    print("\nRecorrido DFS:")
    dfs(grafo, inicio)
    print("\nDistancia del nodo inicial:")
    distancias = calcular_distancias(grafo, inicio)
    for nodo, distancia in distancias.items():
        print("Nodo: {} - Distancia: {}".format(nodo, distancia))