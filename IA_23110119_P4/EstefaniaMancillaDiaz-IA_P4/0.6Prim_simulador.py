# prim simulador paso a paso
# imprime cada arista que se agrega y el costo acumulado

import heapq  

def prim_simulador(adj, inicio=0):
    # adj es lista de adyacencia: adj[u] = [(v, w), ...]
    n = len(adj)                 # numero de nodos
    visitado = [False] * n       # marca de nodos dentro del arbol
    frontera = []                # heap de tuplas (w, u, v)
    mst = []                     # aristas elegidas
    costo_total = 0              # costo acumulado

    def empujar(u):
        # mete aristas de u hacia nodos fuera del arbol
        for v, w in adj[u]:
            if not visitado[v]:
                heapq.heappush(frontera, (w, u, v))

    # arranque
    print("inicio en nodo", inicio)
    visitado[inicio] = True
    empujar(inicio)

    paso = 0                     # contador de pasos
    while frontera and len(mst) < n - 1:
        w, u, v = heapq.heappop(frontera)
        if visitado[v]:
            # esta arista formaria ciclo, la salto
            continue

        # acepto la arista
        visitado[v] = True
        mst.append((u, v, w))
        costo_total += w
        paso += 1

        # prints del simulador
        print(f"paso {paso}: agrego {u}-{v} costo {w}  costo_acum {costo_total}")
        # muestro frontera actual resumida
        resumen = [(cw, cu, cv) for (cw, cu, cv) in frontera if not visitado[cv]]
        resumen = sorted(resumen)[:5]  # corto a 5 para que no truene
        if resumen:
            print("  frontera top:", resumen)
        else:
            print("  frontera vacia")

        # expando desde v
        empujar(v)

    completo = (len(mst) == n - 1)
    if completo:
        print("fin ok  costo_total:", costo_total)
    else:
        alcanzados = [i for i, f in enumerate(visitado) if f]
        faltantes = [i for i, f in enumerate(visitado) if not f]
        print("fin no conexo  alcanzados:", alcanzados, " faltantes:", faltantes)

    return mst, costo_total, completo

def demo():
    # conectar puntos de escritorio con tiras de cable
    # 0 regulador, 1 pc, 2 monitor, 3 router, 4 impresora
    adj = [
        [(1,2),(3,4)],          # 0
        [(0,2),(2,1),(4,5)],    # 1
        [(1,1),(3,3)],          # 2
        [(0,4),(2,3),(4,2)],    # 3
        [(1,5),(3,2)],          # 4
    ]

    prim_simulador(adj, inicio=0)

if __name__ == "__main__":
    demo()