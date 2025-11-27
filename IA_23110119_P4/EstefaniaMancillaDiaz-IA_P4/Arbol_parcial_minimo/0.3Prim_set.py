# prim con set simple
# alternativa sin heap usando una lista como frontera

INF = 10**9  

def pop_min(frontera):
    # busca y saca la arista mas barata de la lista frontera
    # frontera guarda tuplas w u v
    if not frontera:
        return None
    idx = 0                      # guardo el indice del mejor
    for i in range(1, len(frontera)):
        if frontera[i][0] < frontera[idx][0]:
            idx = i
    return frontera.pop(idx)     # regreso y quito esa tupla

def prim_set(adj, inicio=0):
    # adj es lista de adyacencia
    # adj[u] tiene pares v y w que significan arista u v con peso w
    n = len(adj)                 # cantidad de nodos
    visitado = [False] * n       # marca si el nodo ya entro al arbol
    mst = []                     # aristas elegidas del arbol
    costo_total = 0              # suma de pesos del mst

    frontera = []                # lista que usaremos como set de aristas en la frontera

    def empujar(u):
        # mete a la frontera las aristas que salen de u hacia nodos no visitados
        for v, w in adj[u]:
            if not visitado[v]:
                frontera.append((w, u, v))  # guardo tupla peso origen destino

    # arranco desde el nodo inicio
    visitado[inicio] = True
    empujar(inicio)

    # repetimos hasta tener n menos uno aristas o se acabe la frontera
    while frontera and len(mst) < n - 1:
        mejor = pop_min(frontera)  # saco la arista mas barata de la lista
        if mejor is None:
            break
        w, u, v = mejor
        if visitado[v]:
            # si v ya esta adentro ignoro para evitar ciclo
            continue
        # acepto esta arista
        visitado[v] = True
        mst.append((u, v, w))
        costo_total += w
        empujar(v)                 # agrego nuevas aristas desde v

    completo = (len(mst) == n - 1) # si conecte todos los nodos
    return mst, costo_total, completo

def demo():
    # quiero conectar puntos de una mesa de trabajo con tiras de cable lo mas corto posible
    # 0 regulador
    # 1 soldador
    # 2 multimetro
    # 3 lampara
    # 4 extractor
    adj = [
        [(1,3),(2,5)],           # 0 regulador a soldador y multimetro
        [(0,3),(3,2),(4,6)],     # 1 soldador a regulador lampara extractor
        [(0,5),(3,4)],           # 2 multimetro a regulador lampara
        [(1,2),(2,4),(4,3)],     # 3 lampara a soldador multimetro extractor
        [(1,6),(3,3)],           # 4 extractor a soldador lampara
    ]

    mst, costo, ok = prim_set(adj, inicio=0)

    if ok:
        print("aristas del mst:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo total:", costo)
    else:
        print("grafo no conexo, no se pudo conectar todo")
        print("aristas obtenidas:")
        for u, v, w in mst:
            print(u, "-", v, "costo", w)
        print("costo parcial:", costo)

if __name__ == "__main__":
    demo()