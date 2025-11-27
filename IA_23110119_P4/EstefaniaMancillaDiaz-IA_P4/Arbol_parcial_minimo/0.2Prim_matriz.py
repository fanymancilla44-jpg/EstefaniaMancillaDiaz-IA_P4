# prim con matriz O de V cuadrada
# construye un arbol parcial minimo sin ciclos usando matriz de pesos

INF = 10**9  # numero grande para simular infinito

def prim_matriz(mat, inicio=0):
    # mat es una matriz de pesos
    # mat[i][j] es el costo de i a j
    # cero significa que no hay arista excepto en la diagonal
    n = len(mat)                  # cantidad de nodos

    en_mst = [False] * n          # marca si el nodo ya esta dentro del arbol
    mejor = [INF] * n             # mejor costo para conectar cada nodo al arbol
    padre = [-1] * n              # desde que nodo se conecta el nodo i

    mejor[inicio] = 0             # el nodo de inicio entra primero
    costo_total = 0               # acumulador del costo del arbol
    aristas = []                  # lista de aristas del mst como tuplas u v w

    for _ in range(n):
        # elijo el nodo no incluido con menor costo de conexion
        u = -1
        m = INF
        for i in range(n):
            if not en_mst[i] and mejor[i] < m:
                m = mejor[i]
                u = i

        if u == -1:
            # no hay mas alcanzables, el grafo no es conexo
            break

        # agrego u al arbol
        en_mst[u] = True
        costo_total += mejor[u]   # suma cero para el primero

        # si u tiene padre valido, guardo la arista padre[u] - u
        if padre[u] != -1:
            aristas.append((padre[u], u, mejor[u]))

        # actualizo la frontera usando la fila u de la matriz
        for v in range(n):
            w = mat[u][v]         # peso de u a v
            # si hay arista y v no esta dentro y esta arista mejora su conexion
            if w > 0 and not en_mst[v] and w < mejor[v]:
                mejor[v] = w
                padre[v] = u

    completo = (len(aristas) == n - 1)  # si conecte todos
    return aristas, costo_total, completo

def demo():
    # puntos a conectar en un cuarto
    # 0 router, 1 pc, 2 tv, 3 consola, 4 impresora
    # matriz simetrica con ceros donde no hay conexion directa
    mat = [
        # 0  1  2  3  4
        [ 0, 4, 6, 0, 0],  # 0 router
        [ 4, 0, 0, 3, 5],  # 1 pc
        [ 6, 0, 0, 2, 0],  # 2 tv
        [ 0, 3, 2, 0, 4],  # 3 consola
        [ 0, 5, 0, 4, 0],  # 4 impresora
    ]

    aristas, costo, ok = prim_matriz(mat, inicio=0)

    if ok:
        print("aristas del mst:")
        for u, v, w in aristas:
            print(u, "-", v, "costo", w)
        print("costo total:", costo)
    else:
        print("grafo no conexo, no se pudo conectar todo")
        print("aristas obtenidas:")
        for u, v, w in aristas:
            print(u, "-", v, "costo", w)
        print("costo parcial:", costo)

if __name__ == "__main__":
    demo()