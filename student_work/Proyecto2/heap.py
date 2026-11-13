import graphviz
from IPython.display import display

class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        indice_hijo = len(self.arreglo) - 1
        hijo = self.arreglo[indice_hijo]
        indice_padre = indice_hijo // 2
        padre = self.arreglo[indice_padre]

        while hijo < padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = (
                self.arreglo[indice_padre],
                self.arreglo[indice_hijo],
            )
            indice_hijo = indice_padre
            indice_padre = indice_hijo // 2
            hijo = self.arreglo[indice_hijo]
            padre = self.arreglo[indice_padre]

        if imagen:
            display(self._dibujar())

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) <= 1:
            raise IndexError("remove_smallest de un Heap vacío")

        minimo = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            i = 1
            n = len(self.arreglo) - 1

            while 2 * i <= n:
                hijo_izq = 2 * i
                hijo_der = 2 * i + 1
                menor = hijo_izq

                if hijo_der <= n and self.arreglo[hijo_der] < self.arreglo[hijo_izq]:
                    menor = hijo_der

                if self.arreglo[i] > self.arreglo[menor]:
                    self.arreglo[i], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[i],
                    )
                    i = menor
                else:
                    break

        if imagen:
            display(self._dibujar())

        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1

        for inicio in range(n // 2, 0, -1):
            i = inicio
            while 2 * i <= n:
                hijo_izq = 2 * i
                hijo_der = 2 * i + 1
                menor = hijo_izq

                if hijo_der <= n and self.arreglo[hijo_der] < self.arreglo[hijo_izq]:
                    menor = hijo_der

                if self.arreglo[i] > self.arreglo[menor]:
                    self.arreglo[i], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[i],
                    )
                    i = menor
                else:
                    break

        if imagen:
            display(self._dibujar())

    def _dibujar(self):
        """Genera el árbol y retorna el objeto para poder guardarlo."""
        if len(self.arreglo) <= 1:
            return None

        dot = graphviz.Digraph()
        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

        n = len(self.arreglo)
        for i in range(1, n):
            dot.node(str(i), str(self.arreglo[i]))
            if i > 1:
                dot.edge(str(i // 2), str(i))

        return dot
