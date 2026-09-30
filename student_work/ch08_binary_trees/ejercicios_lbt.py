from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True 

    cola = [T.root()]
    encontro_hueco = False


    for p in cola:

        hijo_izq = T.left(p)
        if hijo_izq is not None:
            if encontro_hueco:
                return False  
            cola.append(hijo_izq)
        else:
            encontro_hueco = True


        hijo_der = T.right(p)
        if hijo_der is not None:
            if encontro_hueco:
                return False  
            cola.append(hijo_der)
        else:
            encontro_hueco = True

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    camino_p = []
    actual_p = p
    while actual_p is not None:
        camino_p.append(actual_p)
        actual_p = T.parent(actual_p)


    camino_q = []
    actual_q = q
    while actual_q is not None:
        camino_q.append(actual_q)
        actual_q = T.parent(actual_q)


    ancestro_comun = None
    for nodo in camino_p:
        if nodo in camino_q:
            ancestro_comun = nodo
            break


    indice_cruce_p = camino_p.index(ancestro_comun)
    ruta_subida = camino_p[:indice_cruce_p + 1]


    indice_cruce_q = camino_q.index(ancestro_comun)
    ruta_bajada = camino_q[:indice_cruce_q]
    ruta_bajada.reverse() 


    ruta_completa = ruta_subida + ruta_bajada


    elementos_str = [str(nodo.element()) for nodo in ruta_completa]
    return " -> ".join(elementos_str)
