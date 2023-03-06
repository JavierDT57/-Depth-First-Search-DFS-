import matplotlib.pyplot as plt
import networkx as nx

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
grafo, inicio = leer_grafo_enteros()

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

# Función para graficar el grafo
def graficar_nodos(grafo):
    plt.title("Grafo y sus distancias usando DFS")#Titulo al grafico de los NODOS
    G = nx.DiGraph()  # Crear un grafo dirigido y lo almacena en la variable G
    # Agregar nodos al grafo
    for nodo in grafo:#Agregamos los Nodos del grafo a la variable G
        G.add_node(nodo)
    # Agregar aristas al grafo
    for nodo, adyacentes in grafo.items():#Agrega las aristas del grafo mediante el diccionario de distancias (adyacentes)
        for adyacente in adyacentes:
            G.add_edge(nodo, adyacente)
    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    # Agregar etiquetas de distancia
    for nodo, distancia in distancias.items():
        pos_nodo = pos[nodo]
        plt.text(pos_nodo[0], pos_nodo[1]+0.1, str(distancia), horizontalalignment='center')
    plt.show()#Muestra el grafico



# Impresion de DFS, Distancia y grafico con la libreria Matplotlib
print("\nRecorrido DFS:")
dfs(grafo, inicio)
print("\nDistancia del nodo inicial:")
distancias = calcular_distancias(grafo, inicio)
for nodo, distancia in distancias.items():
   print("Nodo: {} - Distancia: {}".format(nodo, distancia))
print("\nGrafica del grafo:")
graficar_nodos(grafo)