# prim en 2d con puntos
# genera un mst conectando puntos del plano con distancia euclidiana minima

import math
import heapq

def grafo_completo_desde_puntos(puntos):
    # convierte una lista de puntos 2d en un grafo completo
    # puntos[i] = (x, y)
    n = len(puntos)
    adj = [[] for _ in range(n)]
    for i in range(n):
        xi, yi = puntos[i]
        for j in range(i + 1, n):
            xj, yj = puntos[j]
            # distancia euclidiana
            d = math.hypot(xi - xj, yi - yj)
            # agrego arista en ambos sentidos porque es no dirigido
            adj[i].append((j, d))
            adj[j].append((i, d))
    return adj

def prim_heap(adj, inicio=0):
    # igual que el prim con heap, pero ahora los pesos son flotantes
    n = len(adj)
    visitado = [False] * n
    mst = []
    costo_total = 0.0
    frontera = []

    def empujar(u):
        for v, w in adj[u]:
            if not visitado[v]:
                heapq.heappush(frontera, (w, u, v))

    visitado[inicio] = True
    empujar(inicio)

    while frontera and len(mst) < n - 1:
        w, u, v = heapq.heappop(frontera)
        if visitado[v]:
            continue
        visitado[v] = True
        mst.append((u, v, w))
        costo_total += w
        empujar(v)

    completo = (len(mst) == n - 1)
    return mst, costo_total, completo

def demo():
    # quiero trazar cables entre puntos de una habitacion
    # coloco coordenadas aproximadas sobre un plano 2d
    # 0 router   1 pc   2 tv   3 consola   4 impresora
    puntos = [
        (0.0, 0.0),   # 0 router en esquina
        (2.0, 1.0),   # 1 pc sobre un escritorio
        (5.0, 0.5),   # 2 tv en otro muro
        (4.0, 2.5),   # 3 consola cerca de la tv
        (1.0, 3.0),   # 4 impresora en repisa
    ]

    # construyo el grafo completo a partir de puntos
    adj = grafo_completo_desde_puntos(puntos)

    # corro prim desde el router 0
    mst, costo, ok = prim_heap(adj, inicio=0)

    if ok:
        print("aristas del mst (u v dist):")
        for u, v, w in mst:
            print(u, v, round(w, 3))
        print("costo total:", round(costo, 3))
    else:
        print("no se pudo conectar todo")

if __name__ == "__main__":
    demo()