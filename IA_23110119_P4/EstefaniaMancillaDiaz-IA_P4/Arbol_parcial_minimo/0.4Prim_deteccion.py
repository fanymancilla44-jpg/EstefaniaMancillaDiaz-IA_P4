# prim con deteccion de no conexo
# intenta construir un arbol parcial minimo y avisa si el grafo no se puede conectar

import heapq  # cola de prioridad minima

INF = 10**9  # valor grande para infinito

def prim_con_deteccion(adj, inicio=0):
    # adj es lista de adyacencia
    # adj[u] contiene pares v y w que significan arista u a v con costo w
    n = len(adj)                 # cantidad de nodos
    visitado = [False] * n       # marca si el nodo ya entro al arbol
    mst = []                     # aristas elegidas del arbol
    costo_total = 0              # suma de pesos del arbol
    frontera = []                # heap de tuplas w u v

    def empujar(u):
        # mete a la frontera aristas que salen de u hacia nodos no visitados
        for v, w in adj[u]:
            if not visitado[v]:
                heapq.heappush(frontera, (w, u, v))

    # arranco desde el nodo inicio
    visitado[inicio] = True
    empujar(inicio)

    # cuantos nodos ya estan dentro del arbol
    dentro = 1

    # repito hasta formar n menos uno aristas o quedarme sin frontera
    while frontera and len(mst) < n - 1:
        w, u, v = heapq.heappop(frontera)  # saco la arista mas barata
        if visitado[v]:
            # si v ya esta adentro ignoro para evitar ciclo
            continue

        # acepto la arista porque conecta con un nodo nuevo
        visitado[v] = True
        dentro += 1
        mst.append((u, v, w))
        costo_total += w

        # agrego la nueva frontera desde v
        empujar(v)

    # si no logre conectar todos los nodos el grafo es no conexo
    completo = (dentro == n and len(mst) == n - 1)
    return mst, costo_total, completo, visitado

def demo():
    # ejemplo 1 conexo
    adj_ok = [
        [(1, 4), (2, 6)],          # 0
        [(0, 4), (3, 3)],          # 1
        [(0, 6), (3, 2)],          # 2
        [(1, 3), (2, 2)],          # 3
    ]
    mst, costo, ok, vis = prim_con_deteccion(adj_ok, inicio=0)
    print("ejemplo conexo:")
    if ok:
        print("mst:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo total:", costo)
    else:
        print("no conexo, nodos alcanzados:", [i for i, f in enumerate(vis) if f])

    print()

    # ejemplo 2 no conexo
    # componentes: {0,1} y {2,3}
    adj_bad = [
        [(1, 5)],       # 0 conectado solo con 1
        [(0, 5)],       # 1 conectado solo con 0
        [(3, 7)],       # 2 conectado solo con 3
        [(2, 7)],       # 3 conectado solo con 2
    ]
    mst, costo, ok, vis = prim_con_deteccion(adj_bad, inicio=0)
    print("ejemplo no conexo:")
    if ok:
        print("mst:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo total:", costo)
    else:
        alcanzados = [i for i, f in enumerate(vis) if f]
        faltantes = [i for i, f in enumerate(vis) if not f]
        print("no se puede conectar todo")
        print("alcanzados desde el inicio:", alcanzados)
        print("faltantes:", faltantes)
        print("aristas obtenidas:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo parcial:", costo)

if __name__ == "__main__":
    demo()