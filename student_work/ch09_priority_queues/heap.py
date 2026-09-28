%run heap.py
class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo = len(self.arreglo) -1
        hijo = self.arreglo[indice_hijo]
        indice_padre = indice_hijo // 2
        padre = self.arreglo[indice_padre]

        while hijo < padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = self.arreglo[indice_padre], self.arreglo[indice_hijo]
            indice_hijo = indice_padre
            indice_padre = indice_hijo // 2
            hijo = self.arreglo[indice_hijo]
            padre = self.arreglo[indice_padre]

    def remove_smallest(self):
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

                if (
                    hijo_der <= n
                    and self.arreglo[hijo_der] < self.arreglo[hijo_izq]
                ):
                    menor = hijo_der

                if self.arreglo[i] > self.arreglo[menor]:
                    self.arreglo[i], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[i],
                    )
                    i = menor
                else:
                    break

        return minimo

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)

        n = len(self.arreglo) - 1

        # 2. Recorremos desde el último nodo interno (n // 2) hasta la raíz (1)
        for inicio in range(n // 2, 0, -1):
            i = inicio
            while 2 * i <= n:
                hijo_izq = 2 * i
                hijo_der = 2 * i + 1
                menor = hijo_izq

                if (
                    hijo_der <= n
                    and self.arreglo[hijo_der] < self.arreglo[hijo_izq]
                ):
                    menor = hijo_der

                if self.arreglo[i] > self.arreglo[menor]:
                    self.arreglo[i], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[i],
                    )
                    i = menor
                else:
                    break
