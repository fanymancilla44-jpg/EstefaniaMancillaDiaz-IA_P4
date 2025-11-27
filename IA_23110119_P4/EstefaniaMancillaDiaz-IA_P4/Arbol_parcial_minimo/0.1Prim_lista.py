# prim con lista y heap
# construye un arbol parcial minimo sumando aristas baratas sin ciclos

import heapq  # uso heapq para una cola de prioridad minima

def prim_heap(adj, inicio=0):
    # adj es lista de adyacencia
    # adj u es una lista de pares v y w que significa arista u a v con costo w
    n = len(adj)                 # numero de nodos en el grafo
    visitado = [False] * n       # marca si el nodo ya esta dentro del arbol
    mst = []                     # aqui guardo las aristas elegidas del arbol
    costo_total = 0              # acumulador del costo del arbol

    # frontera de aristas con un heap de tuplas w u v
    frontera = []                # cola de prioridad de aristas que salen del conjunto actual

    # funcion local para agregar a la frontera todas las aristas que salen de un nodo u
    def empujar_aristas(u):
        # recorro vecinos v con peso w y los meto al heap si el vecino no esta visitado
        for v, w in adj[u]:
            if not visitado[v]:
                heapq.heappush(frontera, (w, u, v))  # meto la arista con su peso primero para ordenar por costo

    # inicio el arbol desde el nodo inicio
    visitado[inicio] = True      # marco el inicio como ya dentro del arbol
    empujar_aristas(inicio)      # cargo su frontera inicial

    # repetimos mientras haya frontera y aun falten nodos por conectar
    while frontera and len(mst) < n - 1:
        w, u, v = heapq.heappop(frontera)  # saco la arista mas barata disponible
        if visitado[v]:
            # si el destino ya esta dentro del arbol se ignora para evitar ciclo
            continue
        # acepto esta arista porque conecta el conjunto con un nodo nuevo
        visitado[v] = True
        mst.append((u, v, w))    # guardo la arista elegida
        costo_total += w         # sumo su costo
        empujar_aristas(v)       # agrego la nueva frontera que sale desde v

    # si no se lograron n menos uno aristas significa que el grafo era no conexo
    if len(mst) != n - 1:
        # regreso lo que se pudo y un aviso basico
        return mst, costo_total, False
    return mst, costo_total, True

def demo():
    # quiero tender cable barato para conectar puntos en mi cuarto
    # nodos
    # 0 router
    # 1 pc
    # 2 tv
    # 3 consola
    # 4 impresora
    # las distancias w simulan metros de cable entre puntos
    adj = [
        [(1, 4), (2, 6)],        # 0 router conectado cerca a pc y tv
        [(0, 4), (3, 3), (4, 5)],# 1 pc conecta a router consola e impresora
        [(0, 6), (3, 2)],        # 2 tv conecta a router y consola
        [(1, 3), (2, 2), (4, 4)],# 3 consola conecta a pc tv e impresora
        [(1, 5), (3, 4)],        # 4 impresora conecta a pc y consola
    ]

    # corro prim desde el router
    mst, costo, completo = prim_heap(adj, inicio=0)

    # muestro resultados en consola
    if completo:
        print("aristas del mst:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo total:", costo)
    else:
        print("no se puede conectar todo el grafo")
        print("aristas elegidas hasta ahora:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo parcial:", costo)

if __name__ == "__main__":
    demo()